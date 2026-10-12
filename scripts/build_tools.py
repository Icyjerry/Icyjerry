"""Build themed tool cards with a compact desktop rail and readable mobile rows."""
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET

ASSETS = Path(__file__).resolve().parents[1] / 'assets'
ET.register_namespace('', 'http://www.w3.org/2000/svg')
GROUPS = [
    ('Languages', ['Python-Dark', 'C', 'CPP', 'Java-Dark', 'Bash-Dark'],
     ['Python · C / C++ · Java · Shell']),
    ('Models & experiments', ['PyTorch-Dark', 'Anaconda-Dark'],
     ['PyTorch · Hugging Face · Jupyter', 'Conda / uv']),
    ('Systems workbench', ['Linux-Dark', 'Bash-Dark'],
     ['Linux · Shell', 'computer systems coursework']),
    ('Everyday tools', ['Git', 'VSCode-Dark', 'Idea-Dark'],
     ['Git · VS Code · JetBrains']),
]
THEMES = {
    'dark': ('#161b22', '#e6edf3', '#929da9', '#30363d', '#dca65b'),
    'light': ('#f6f8fa', '#24292f', '#59636e', '#d0d7de', '#966017'),
}


def icon(filename, x, y, size, prefix):
    root = ET.parse(ASSETS / 'icons' / (filename + '.svg')).getroot()
    ids = {n.get('id'): prefix + n.get('id') for n in root.iter() if n.get('id')}
    for n in root.iter():
        for attr, value in list(n.attrib.items()):
            if attr == 'id':
                n.set(attr, ids[value])
            else:
                for old, new in ids.items():
                    value = value.replace('url(#' + old + ')', 'url(#' + new + ')')
                    if value == '#' + old:
                        value = '#' + new
                n.set(attr, value)
    root.attrib.update(x=str(x), y=str(y), width=str(size), height=str(size))
    return ET.tostring(root, encoding='unicode')


for theme, (panel, fg, muted, border, accent) in THEMES.items():
    for layout in ['desktop', 'mobile']:
        mobile = layout == 'mobile'
        width, height, step, row_h = (360, 564, 144, 132) if mobile else (960, 388, 100, 88)
        content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">Tools I reach for</title>
<desc id="desc">{escape('; '.join(name + ': ' + ', '.join(lines) for name, _, lines in GROUPS))}</desc>
<style>.name,.note,.index {{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}} .name {{fill:{fg};font-size:17px;font-weight:600}} .note {{fill:{muted};font-size:{'11.5' if mobile else '13'}px}} .index {{fill:{accent};font-size:12px}}</style>
'''
        for i, (name, icons, lines) in enumerate(GROUPS):
            y = i * step
            content += f'<rect x=".5" y="{y+.5}" width="{width-1}" height="{row_h-1}" rx="8" fill="{panel}" stroke="{border}"/>'
            if mobile:
                content += f'<text x="20" y="{y+27}" class="name">{escape(name)}</text><text x="340" y="{y+26}" text-anchor="end" class="index">0{i+1}</text>'
                icon_x, icon_y, size, gap = 20, y+42, 40, 48
                text_x, text_y = 20, y+103
                notes = lines
            else:
                content += f'<text x="26" y="{y+49}" class="index">0{i+1}</text><text x="62" y="{y+50}" class="name">{escape(name)}</text><path d="M280 {y+20}V{y+68}" stroke="{border}"/>'
                icon_x, icon_y, size, gap = 306, y+20, 48, 58
                text_x, text_y = 626, y+(49 if len(lines)==1 else 39)
                notes = ['Python · C / C++', 'Java · Shell'] if i==0 else lines
                if i==0:
                    text_y = y+39
            for j, filename in enumerate(icons):
                content += icon(filename, icon_x+j*gap, icon_y, size, f'g{i}-i{j}-')
            for j, line in enumerate(notes):
                content += f'<text x="{text_x}" y="{text_y+j*(16 if mobile else 22)}" class="note">{escape(line)}</text>'
        (ASSETS / f'tools-{layout}-{theme}.svg').write_text(content + '</svg>\n')
