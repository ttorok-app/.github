#!/usr/bin/env python3
"""조직 프로필 배너(라이트·다크) 생성기.

    python3 profile/assets/make_banner.py

문구·색을 바꾸려면 아래 상수만 고치고 다시 실행한다.
색은 ttorok-docs `09` 4절 디자인 토큰(oklch)을 sRGB hex로 옮긴 값이다.
"""
import math
import os

TITLE = "또록사주"
SUBTITLE = "사주로 1년에 한 편, 나만의 웹툰"
LABEL = "TTOROK SAJU · 2027"

PAPER, INK = "#f4f0e8", "#1c1b19"
# 상생 순서(木→火→土→金→水)로 시계 방향 배치. (글자, 오행색, 글자색)
ELEMENTS = [
    ("木", "#428252", PAPER),
    ("火", "#c74d38", PAPER),
    ("土", "#b99056", INK),
    ("金", "#c9ced4", INK),
    ("水", "#0a345a", PAPER),
]

THEMES = {
    "light": {"bg": PAPER, "ink": INK, "soft": "#6b665d", "ring": "#d9d1c1"},
    "dark": {"bg": INK, "ink": PAPER, "soft": "#a8a196", "ring": "#3a3833"},
}


def banner(theme: str) -> str:
    t = THEMES[theme]
    cx, cy, R, r = 1030, 160, 108, 40
    circles = []
    for i, (ch, color, text) in enumerate(ELEMENTS):
        a = math.radians(-90 + i * 72)
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        if theme == "light" and ch == "金":
            stroke = f' stroke="{INK}" stroke-width="2"'  # 밝은 배경에서 金 원 윤곽
        elif theme == "dark":
            stroke = f' stroke="{PAPER}" stroke-opacity="0.35" stroke-width="2"'
        else:
            stroke = ""
        circles.append(
            f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}"{stroke}/>\n'
            f'  <text x="{x:.1f}" y="{y + 14:.1f}" text-anchor="middle" font-size="40" fill="{text}" class="serif">{ch}</text>'
        )
    body = "\n".join(circles)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="320" viewBox="0 0 1280 320" role="img" aria-label="{TITLE}: {SUBTITLE}">
  <style>
    .serif {{ font-family: 'Noto Serif KR', 'Nanum Myeongjo', 'AppleMyungjo', 'Batang', serif; font-weight: 700; }}
    .sans {{ font-family: 'IBM Plex Sans KR', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif; }}
    .mono {{ font-family: 'IBM Plex Mono', 'SFMono-Regular', Menlo, Consolas, monospace; }}
  </style>
  <rect width="1280" height="320" rx="24" fill="{t['bg']}"/>
  <text x="96" y="104" font-size="18" letter-spacing="6" fill="{t['soft']}" class="mono">{LABEL}</text>
  <text x="90" y="196" font-size="92" fill="{t['ink']}" class="serif">{TITLE}</text>
  <text x="96" y="248" font-size="28" fill="{t['soft']}" class="sans">{SUBTITLE}</text>
  <circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{t['ring']}" stroke-width="2" stroke-dasharray="4 8"/>
{body}
</svg>
"""


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    for theme in THEMES:
        path = os.path.join(here, f"banner-{theme}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(banner(theme))
        print("wrote", os.path.relpath(path))
