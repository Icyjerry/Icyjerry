"""Generate the two theme variants of the original profile illustrations."""
from pathlib import Path
from html import escape

ASSETS = Path(__file__).resolve().parents[1] / 'assets'
THEMES = {
    'dark': ('#0d1117', '#161b22', '#e6edf3', '#929da9', '#30363d', '#dca65b'),
    'light': ('#ffffff', '#f6f8fa', '#24292f', '#59636e', '#d0d7de', '#966017'),
}

for theme, (bg, panel, fg, muted, border, accent) in THEMES.items():
    def start(height, title):
        return f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height}" viewBox="0 0 960 {height}" role="img" aria-labelledby="title">
<title id="title">{escape(title)}</title>
<style>
text {{font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; fill:{fg}}}
.small {{font-size:13px;fill:{muted}}} .label {{font-size:15px}} .accent {{fill:{accent}}}
.flow {{stroke-dasharray:3 13;animation:flow 5s linear infinite}}
.cursor {{animation:blink 1.4s steps(2,end) infinite}}
@keyframes flow {{to {{stroke-dashoffset:-64}}}}
@keyframes blink {{50% {{opacity:0}}}}
@media (prefers-reduced-motion:reduce) {{.flow,.cursor {{animation:none}}}}
</style>
<rect x=".5" y=".5" width="959" height="{height-1}" rx="10" fill="{bg}" stroke="{border}"/>
'''
    header = start(298, 'Jerry Hu / Icyjerry — Fudan Software Engineering. Learning how models work, and what runs underneath.')
    header += f'''<path d="M1 42H959" stroke="{border}"/>
<circle cx="24" cy="22" r="4" fill="{accent}"/><text x="39" y="27" class="small">icyjerry / ~/learning</text>
<text x="928" y="27" text-anchor="end" class="small">models &amp; systems</text>
<text x="32" y="109" font-size="52" font-weight="700" letter-spacing="-3">Jerry Hu<tspan class="accent">_</tspan></text>
<text x="34" y="142" class="label" fill="{muted}">Software Engineering · Fudan University</text>
<text x="34" y="203" class="label"><tspan class="accent">$</tspan> follow the tensor</text>
<text x="34" y="230" class="small">from the model to the machine.</text>
<text x="34" y="267" class="small">learning / building / taking things apart</text>
<rect x="410" y="255" width="8" height="15" fill="{accent}" class="cursor"/>
<path d="M563 72V265" stroke="{border}"/>
'''
    for i,(name,detail) in enumerate([('tokens','language'),('tensors','computation'),('memory','execution'),('hardware','the next question')]):
        y=85+i*53
        if i<3:
            header+=f'<path d="M603 {y+9}V{y+45}" stroke="{border}" stroke-width="2"/><path class="flow" d="M603 {y+9}V{y+45}" stroke="{accent}" stroke-width="2"/>'
        header+=f'<circle cx="603" cy="{y}" r="4" fill="{accent if i<2 else bg}" stroke="{accent if i<2 else muted}"/><text x="624" y="{y+5}" font-size="18">{name}</text><text x="914" y="{y+5}" class="small" text-anchor="end">{detail}</text>'
    (ASSETS/f'header-{theme}.svg').write_text(header+'</svg>\n')
    roadmap=start(420,'Learning map: systems foundations → neural networks → Transformers → training → post-training → AI systems. A direction of study, not a completion chart.')
    roadmap+=f'<text x="28" y="33" class="small">LEARNING MAP</text><text x="932" y="33" class="small" text-anchor="end">keep asking what happens underneath</text>'
    stages=[
        ('01','Foundations','CS61A / B / C · CS170 · CSAPP','programs, algorithms, memory'),
        ('02','Neural networks','micrograd · makemore','gradients, one operation at a time'),
        ('03','Transformers','GPT / nanoGPT · BPE','tokens → attention → logits'),
        ('04','LLM training','GPT-2 reproduction · PyTorch','data, loss, optimization'),
        ('05','Post-training','fine-tuning · Hugging Face','adapt a model; inspect its mistakes'),
        ('06','AI systems','CS336 → inference / runtimes / infra','next: how does it run efficiently?'),
    ]
    for i,(n,name,topics,question) in enumerate(stages):
        y=75+i*56
        roadmap+=f'<path d="M28 {y+28}H932" stroke="{border}" opacity=".65"/>'
        if i<5:
            roadmap+=f'<path d="M43 {y+8}V{y+48}" stroke="{border}"/><path d="M43 {y+8}V{y+48}" class="flow" stroke="{accent}"/>'
        roadmap+=f'<circle cx="43" cy="{y}" r="13" fill="{panel}" stroke="{border}"/><text x="43" y="{y+4}" text-anchor="middle" font-size="11" class="accent">{n}</text><text x="72" y="{y+5}" font-size="17" font-weight="600">{escape(name)}</text><text x="298" y="{y-2}" class="label">{escape(topics)}</text><text x="298" y="{y+18}" class="small">{escape(question)}</text>'
    roadmap+='<text x="28" y="405" class="small">A direction of study — not a checklist of completed courses.</text></svg>\n'
    (ASSETS/f'learning-path-{theme}.svg').write_text(roadmap)
