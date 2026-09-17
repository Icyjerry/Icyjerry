"""Refresh repository-local GitHub cards. Requires GH_TOKEN; no third-party packages."""
import datetime as dt
from html import escape
import json
import os
from pathlib import Path
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'github'
USER = 'Icyjerry'
THEMES = {
    'dark': ('0d1117', 'e6edf3', '929da9', '30363d', 'dca65b'),
    'light': ('ffffff', '24292f', '59636e', 'd0d7de', '966017'),
}


def streaks(counts):
    """Today may still be empty; a streak ending yesterday remains current."""
    longest = run = 0
    for count in counts:
        run = run + 1 if count else 0
        longest = max(longest, run)
    active = counts[:-1] if counts and not counts[-1] else counts
    current = 0
    for count in reversed(active):
        if not count:
            break
        current += 1
    return current, longest


def request(url, payload=None):
    headers = {'User-Agent': 'Icyjerry-profile'}
    if payload is not None:
        headers.update(Authorization='Bearer ' + os.environ['GH_TOKEN'],
                       **{'Content-Type': 'application/json'})
    req = urllib.request.Request(url, data=json.dumps(payload).encode() if payload else None, headers=headers)
    with urllib.request.urlopen(req, timeout=45) as response:
        return response.read()


def svg(width, height, title, colors):
    bg, fg, muted, border, accent = colors
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title">
<title id="title">{escape(title)}</title>
<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="8" fill="#{bg}" stroke="#{border}"/>
<style>text {{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;fill:#{fg}}} .muted {{fill:#{muted};font-size:12px}} .accent {{fill:#{accent}}}</style>'''


def refresh():
    OUT.mkdir(parents=True, exist_ok=True)
    query = '''query($login:String!) { user(login:$login) { contributionsCollection {
      contributionCalendar { totalContributions weeks { contributionDays { date contributionCount } } }
    } } }'''
    data = json.loads(request('https://api.github.com/graphql', {'query': query, 'variables': {'login': USER}}))
    if data.get('errors'):
        raise RuntimeError(data['errors'])
    calendar = data['data']['user']['contributionsCollection']['contributionCalendar']
    days = [d for w in calendar['weeks'] for d in w['contributionDays']]
    # GitHub's calendar dates, including today, define the calculation window.
    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    days = [d for d in days if d['date'] <= today]
    current, longest = streaks([d['contributionCount'] for d in days])
    recent = days[-31:]
    end = days[-1]['date']
    for theme, colors in THEMES.items():
        bg, fg, muted, border, accent = colors
        card = svg(960, 144, 'Contribution streaks in the past-year GitHub calendar', colors)
        card += f'<text x="24" y="27" class="muted">CONTRIBUTION STREAK · PAST YEAR</text><text x="936" y="27" text-anchor="end" class="muted">{days[0]["date"]} / {end}</text>'
        for i, (value, label) in enumerate([(current, 'current streak · days'), (longest, 'longest in window · days'), (calendar['totalContributions'], 'contributions in window')]):
            x = 26 + i * 320
            if i:
                card += f'<path d="M{x-18} 51V120" stroke="#{border}"/>'
            card += f'<text x="{x}" y="88" font-size="36" class="accent">{value}</text><text x="{x}" y="116" class="muted">{label}</text>'
        (OUT / f'streak-{theme}.svg').write_text(card + '</svg>\n')
        graph = svg(960, 240, f'Daily GitHub contributions: {recent[0]["date"]} to {end}', colors)
        graph += '<text x="24" y="28" class="muted">ACTIVITY · LAST 31 DAYS</text>'
        peak = max(1, max(d['contributionCount'] for d in recent))
        for tick in sorted({0, peak // 2, peak}):
            y = 185 - tick / peak * 125
            graph += f'<path d="M48 {y}H932" stroke="#{border}"/><text x="36" y="{y+4}" text-anchor="end" class="muted">{tick}</text>'
        for i, day in enumerate(recent):
            value = day['contributionCount']
            h = value / peak * 125
            x = 53 + i * 28.3
            graph += f'<rect x="{x:.1f}" y="{185-max(h,2):.1f}" width="16" height="{max(h,2):.1f}" rx="2" fill="#{accent if value else border}"><title>{day["date"]}: {value} contributions</title></rect>'
            if i in [0, 10, 20, 30]:
                graph += f'<text x="{x+8:.1f}" y="207" text-anchor="middle" class="muted">{day["date"][5:]}</text>'
        graph += f'<text x="932" y="228" text-anchor="end" class="muted">GitHub API · updated {today} UTC</text></svg>\n'
        (OUT / f'activity-{theme}.svg').write_text(graph)
        # Keep the last valid card if a public widget service is unavailable.
        for name, endpoint, options in [
            ('stats', 'api', {'show_icons': 'true', 'hide_rank': 'true', 'custom_title': 'On GitHub', 'card_width': 460}),
            ('languages', 'api/top-langs/', {'layout': 'compact', 'langs_count': 8, 'exclude_repo': USER, 'card_width': 460, 'custom_title': 'Public code / languages'}),
        ]:
            params = dict(username=USER, bg_color=bg, title_color=accent, text_color=fg,
                          icon_color=accent, border_color=border, border_radius=8, **options)
            url = 'https://github-stats-extended.vercel.app/' + endpoint + '?' + urllib.parse.urlencode(params)
            path = OUT / f'{name}-{theme}.svg'
            try:
                content = request(url)
                root = ET.fromstring(content)
                if root.tag != '{http://www.w3.org/2000/svg}svg':
                    raise ValueError('Response is not an SVG')
                text = ' '.join(root.itertext()).lower()
                if any(message in text for message in ['something went wrong', 'rate limit', 'could not fetch', 'deployment has been']):
                    raise ValueError('Service returned an error card')
                path.write_bytes(content)
            except Exception as exc:
                if not path.exists():
                    raise
                print(f'::warning::{name}/{theme}: keeping previous valid image ({exc})')
    print(f'Updated through {end}: streak {current}, longest {longest}; {len(days)} calendar days')


if __name__ == '__main__':
    refresh()
