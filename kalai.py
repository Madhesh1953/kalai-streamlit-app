import base64
import html
import mimetypes
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Kalai-oda Azhaagana Payanam",
    page_icon="💗",
    layout="wide"
)

# ---------------- CSS DESIGN ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;1,9..144,500&family=Nunito:wght@400;600;700&display=swap');

.stApp {
    background: linear-gradient(135deg, #fff4fa, #f4f0ff, #fff9ef);
    color: #30243d !important;
    font-family: 'Nunito', sans-serif;
}

.stApp p, .stApp label, .stApp li, .stApp span { color: #30243d; }

/* Hero */
.hero {
    position: relative;
    overflow: hidden;
    text-align: center;
    padding: 34px 20px 22px;
    border-radius: 26px;
    background: linear-gradient(160deg, #ffe3f1, #ece2ff 60%, #fff3e0);
    border: 1px solid #efcde2;
    margin-bottom: 18px;
}

.hero h1 {
    font-family: 'Fraunces', serif;
    color: #a51d65 !important;
    font-size: 42px;
    font-weight: 600;
    line-height: 1.2;
    margin: 0 0 8px 0;
    padding: 0;
    position: relative;
    z-index: 2;
}

.hero p {
    color: #604078 !important;
    font-size: 21px;
    font-style: italic;
    margin: 0;
    position: relative;
    z-index: 2;
}

/* Falling petals (hero only) */
.petal {
    position: absolute;
    top: -30px;
    font-size: 20px;
    opacity: 0.85;
    animation: fall 9s linear infinite;
    z-index: 1;
}
.petal:nth-child(1) { left: 6%;  animation-delay: 0s;   }
.petal:nth-child(2) { left: 22%; animation-delay: 2.5s; font-size: 16px; }
.petal:nth-child(3) { left: 41%; animation-delay: 5s;   }
.petal:nth-child(4) { left: 63%; animation-delay: 1.5s; font-size: 17px; }
.petal:nth-child(5) { left: 80%; animation-delay: 4s;   }
.petal:nth-child(6) { left: 93%; animation-delay: 6.5s; font-size: 15px; }

@keyframes fall {
    0%   { transform: translateY(0) rotate(0deg); opacity: 0; }
    10%  { opacity: 0.85; }
    100% { transform: translateY(260px) rotate(300deg); opacity: 0; }
}

@media (prefers-reduced-motion: reduce) {
    .petal { animation: none; display: none; }
}

/* Sidebar */
[data-testid="stSidebar"] { background-color: #fff0f7; }
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] h2 { color: #482641 !important; }

/* Input */
.stTextInput input {
    color: #30243d !important;
    background-color: #ffffff !important;
    border: 1px solid #d99cbd !important;
    border-radius: 10px;
}
.stTextInput input::placeholder { color: #76677c !important; opacity: 1; }

/* Intro line */
.intro {
    text-align: center;
    font-size: 18px;
    color: #40334f;
    line-height: 1.8;
    margin: 6px 0 20px;
}

/* Story card */
.story-card {
    background-color: #ffffff;
    border: 1px solid #edc5dd;
    border-radius: 20px;
    padding: 14px 14px 20px;
    text-align: center;
    min-height: 480px;
    box-shadow: 0 6px 20px #874c8218;
    transition: transform .2s ease, box-shadow .2s ease;
}
.story-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 28px #874c8228;
}

.emoji { font-size: 42px; margin-bottom: 10px; }

.card-img {
    display: block;
    width: 100%;
    height: 180px;
    object-fit: cover;
    border-radius: 14px;
    margin-bottom: 10px;
}

.banner-img {
    display: block;
    width: 100%;
    max-height: 260px;
    object-fit: cover;
    border-radius: 22px;
    margin-bottom: 18px;
    box-shadow: 0 6px 20px #874c8230;
}

.pill {
    display: inline-block;
    padding: 8px 14px;
    border-radius: 20px;
    background-color: #ffe0ef;
    color: #842052 !important;
    font-family: 'Fraunces', serif;
    font-weight: 600;
    margin: 8px 0 6px;
    font-size: 16px;
}

.story-text {
    font-size: 15.5px;
    line-height: 1.75;
    color: #40334f !important;
    padding: 0 4px;
}

.story-end {
    font-family: 'Fraunces', serif;
    font-style: italic;
    color: #b32370 !important;
    font-weight: 500;
    line-height: 1.6;
    margin-top: 14px;
    font-size: 17px;
}

/* Button */
.stButton button {
    background-color: #f7d7e9 !important;
    color: #7b174c !important;
    border: 1px solid #d98ab7 !important;
    border-radius: 12px;
    font-weight: bold;
    min-height: 45px;
}
.stButton button p, .stButton button span { color: #7b174c !important; }
.stButton button:hover {
    background-color: #f2bfdc !important;
    border-color: #b94f8a !important;
}

/* Footer */
.footer {
    background: linear-gradient(90deg, #ffe0ef, #eee3ff);
    border: 1px solid #e7c3e0;
    border-radius: 22px;
    padding: 26px;
    margin-top: 26px;
    text-align: center;
}
.footer h2 {
    font-family: 'Fraunces', serif;
    color: #8f205c !important;
    font-size: 27px;
}
.footer p { color: #49334f !important; font-size: 17px; line-height: 1.8; }

@media (max-width: 768px) {
    .hero h1 { font-size: 27px; }
    .hero p { font-size: 17px; }
    .story-card { min-height: auto; margin-bottom: 14px; }
}
</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 💗 Oru Chinna Surprise")

    name = st.text_input("Peru enter pannu", value="Kalai").strip()
    if not name:
        name = "Kalai"

    show_story = st.button("✨ En Payanathai Kaattu", width="stretch")

    st.write("🌷 Eppovum nambikkaiyoda iru!")
    st.caption("Anbudan, Madhesh 💗")

safe_name = html.escape(name)


# ---------------- IMAGE HELPERS ----------------
# Unga own photos use panna: script pakkathula "images" folder create panni
# banner.jpg, stage1.jpg ... stage4.jpg podunga (.jpg/.jpeg/.png/.webp).
# Photo irundha adhu varum; illa-na keezha irukkura illustrations varum.
IMG_DIR = Path(__file__).parent / "images"


@st.cache_data
def find_image(stem):
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        path = IMG_DIR / (stem + ext)
        if path.exists():
            mime = mimetypes.guess_type(path.name)[0] or "image/jpeg"
            data = base64.b64encode(path.read_bytes()).decode()
            return f"data:{mime};base64,{data}"
    return None


# ---------------- BUILT-IN ILLUSTRATIONS (SVG) ----------------
def sparkle(x, y, c="#fff6c7", s=8):
    return (
        f'<path d="M{x} {y-s} L{x+s/4} {y-s/4} L{x+s} {y} L{x+s/4} {y+s/4} '
        f'L{x} {y+s} L{x-s/4} {y+s/4} L{x-s} {y} L{x-s/4} {y-s/4}Z" fill="{c}"/>'
    )


def wrap(inner, top, bottom, gid, w=300, h=180):
    return (
        f'<svg class="card-img" viewBox="0 0 {w} {h}" '
        'preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">'
        f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/>'
        '</linearGradient></defs>'
        f'<rect width="{w}" height="{h}" fill="url(#{gid})"/>{inner}</svg>'
    )


def flower(x, y, petal="#ff8fc0", r=7):
    petals = "".join(
        f'<circle cx="{x + dx}" cy="{y + dy}" r="{r*0.7}" fill="{petal}"/>'
        for dx, dy in [(0, -r), (r, 0), (0, r), (-r, 0)]
    )
    return (
        f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+34}" stroke="#4f9a63" stroke-width="3"/>'
        f'{petals}<circle cx="{x}" cy="{y}" r="{r*0.6}" fill="#ffd966"/>'
    )


def butterfly(x, y, c1="#c78bff", c2="#ff8fc0"):
    return (
        f'<ellipse cx="{x-7}" cy="{y-4}" rx="8" ry="6" fill="{c1}" transform="rotate(-20 {x-7} {y-4})"/>'
        f'<ellipse cx="{x+7}" cy="{y-4}" rx="8" ry="6" fill="{c1}" transform="rotate(20 {x+7} {y-4})"/>'
        f'<ellipse cx="{x-6}" cy="{y+5}" rx="6" ry="5" fill="{c2}"/>'
        f'<ellipse cx="{x+6}" cy="{y+5}" rx="6" ry="5" fill="{c2}"/>'
        f'<rect x="{x-1}" y="{y-8}" width="2" height="18" rx="1" fill="#5a3a68"/>'
    )


def scene_rain():
    rain = "".join(
        f'<line x1="{x}" y1="{y}" x2="{x-6}" y2="{y+16}" stroke="#9db0e4" '
        'stroke-width="2" stroke-linecap="round"/>'
        for x, y in [(55, 92), (85, 108), (115, 90), (200, 96), (230, 112),
                     (255, 94), (70, 140), (130, 150), (190, 146), (245, 140)]
    )
    cloud = (
        '<g fill="#b9b3d6"><ellipse cx="110" cy="62" rx="42" ry="24"/>'
        '<ellipse cx="150" cy="48" rx="40" ry="28"/>'
        '<ellipse cx="195" cy="64" rx="42" ry="24"/>'
        '<rect x="80" y="62" width="150" height="24" rx="12"/></g>'
        '<g fill="#a29cc6"><ellipse cx="60" cy="38" rx="26" ry="14"/>'
        '<ellipse cx="255" cy="34" rx="24" ry="13"/></g>'
    )
    umbrella = (
        '<path d="M128 128 a24 24 0 0 1 48 0 z" fill="#ff8fc0"/>'
        '<path d="M128 128 q6 7 12 0 q6 7 12 0 q6 7 12 0 q6 7 12 0" fill="#ff8fc0"/>'
        '<line x1="152" y1="128" x2="152" y2="156" stroke="#7b4a6b" stroke-width="3" stroke-linecap="round"/>'
        '<path d="M152 156 q-1 7 -8 6" fill="none" stroke="#7b4a6b" stroke-width="3" stroke-linecap="round"/>'
        '<path d="M152 140 c-5-5-9-1-5 3 l5 5 l5-5 c4-4 0-8-5-3z" fill="#ffd6ea" transform="translate(0,-2) scale(1)"/>'
    )
    ground = '<ellipse cx="150" cy="182" rx="170" ry="16" fill="#8f8bb5"/>'
    return wrap(cloud + rain + ground + umbrella, "#8d86b8", "#c9c3e6", "g1")


def scene_sprout():
    rays = "".join(
        f'<line x1="238" y1="52" x2="{238 + 30*__import__("math").cos(a)}" '
        f'y2="{52 + 30*__import__("math").sin(a)}" stroke="#ffd37a" stroke-width="3" stroke-linecap="round"/>'
        for a in [i * 0.52 for i in range(12)]
    )
    sun = '<circle cx="238" cy="52" r="20" fill="#ffd37a"/>'
    hills = (
        '<ellipse cx="70" cy="190" rx="130" ry="46" fill="#a5d6a7"/>'
        '<ellipse cx="240" cy="196" rx="140" ry="50" fill="#81c784"/>'
    )
    plant = (
        '<path d="M150 170 Q148 140 150 112" stroke="#3f8f55" stroke-width="5" fill="none" stroke-linecap="round"/>'
        '<ellipse cx="128" cy="112" rx="24" ry="12" fill="#4caf6a" transform="rotate(-28 128 112)"/>'
        '<ellipse cx="174" cy="102" rx="24" ry="12" fill="#66bb7a" transform="rotate(28 174 102)"/>'
        '<ellipse cx="150" cy="170" rx="22" ry="7" fill="#8d6e63"/>'
    )
    return wrap(rays + sun + hills + plant + sparkle(80, 60) + sparkle(110, 34, s=6),
                "#ffe6d0", "#ffd0e4", "g2")


def scene_crown():
    crown = (
        '<defs><linearGradient id="gold" x1="0" y1="0" x2="0" y2="1">'
        '<stop offset="0" stop-color="#ffe27a"/><stop offset="1" stop-color="#f2a93b"/>'
        '</linearGradient></defs>'
        '<path d="M96 128 L104 72 L130 102 L150 62 L170 102 L196 72 L204 128 Z" '
        'fill="url(#gold)" stroke="#d9942c" stroke-width="2" stroke-linejoin="round"/>'
        '<rect x="94" y="126" width="112" height="16" rx="6" fill="url(#gold)" stroke="#d9942c" stroke-width="2"/>'
        '<circle cx="104" cy="70" r="6" fill="#ff6fa8"/><circle cx="150" cy="60" r="7" fill="#7fd1ff"/>'
        '<circle cx="196" cy="70" r="6" fill="#ff6fa8"/>'
        '<circle cx="124" cy="134" r="4" fill="#fff"/><circle cx="150" cy="134" r="4" fill="#ff6fa8"/>'
        '<circle cx="176" cy="134" r="4" fill="#fff"/>'
    )
    stars = (sparkle(52, 50, s=10) + sparkle(250, 44, s=9) + sparkle(70, 130, s=7)
             + sparkle(240, 128, s=8) + sparkle(205, 28, s=6) + sparkle(98, 26, s=6))
    return wrap(crown + stars, "#e9d5ff", "#ffc9e2", "g3")


def scene_garden():
    rainbow = "".join(
        f'<path d="M{40+i*8} 150 A{110-i*8} {110-i*8} 0 0 1 {260-i*8} 150" fill="none" '
        f'stroke="{c}" stroke-width="8" opacity="0.75"/>'
        for i, c in enumerate(["#ff9aa2", "#ffd6a5", "#fdffb6", "#b5ead7", "#a0c4ff"])
    )
    sun = '<circle cx="262" cy="30" r="16" fill="#ffd37a"/>'
    ground = '<ellipse cx="150" cy="190" rx="190" ry="44" fill="#9ad9a5"/>'
    flowers = (flower(60, 130, "#ff8fc0") + flower(105, 138, "#c78bff", 6)
               + flower(200, 134, "#ffb3d1", 7) + flower(246, 128, "#ffd966", 7))
    bugs = butterfly(130, 60) + butterfly(190, 82, "#ffb36b", "#ff8fc0")
    return wrap(sun + rainbow + ground + flowers + bugs + sparkle(40, 40, s=7),
                "#cfeaff", "#fff1d6", "g4")


def banner_svg():
    petals = "".join(
        f'<ellipse cx="{x}" cy="{y}" rx="7" ry="4" fill="#ff9ccb" opacity="0.8" '
        f'transform="rotate({r} {x} {y})"/>'
        for x, y, r in [(120, 60, 30), (300, 110, 70), (520, 50, -20), (760, 95, 40),
                        (980, 55, 10), (1100, 120, -40), (640, 140, 60), (210, 150, -10)]
    )
    inner = (
        '<circle cx="960" cy="90" r="44" fill="#ffe08a" opacity="0.9"/>'
        '<path d="M0 190 Q200 120 420 170 T840 160 T1200 150 V240 H0Z" fill="#e8c6f5"/>'
        '<path d="M0 215 Q260 160 520 200 T1200 190 V240 H0Z" fill="#f7b6d6"/>'
        + petals + butterfly(420, 90) + butterfly(820, 70, "#ffb36b", "#ff8fc0")
        + sparkle(180, 90, s=9) + sparkle(700, 40, s=8) + sparkle(1060, 40, s=7)
    )
    svg = wrap(inner, "#ffe9f4", "#e9deff", "gb", w=1200, h=240)
    return svg.replace('class="card-img"', 'class="banner-img"')


SCENES = [scene_rain, scene_sprout, scene_crown, scene_garden]


# ---------------- TITLE ----------------
# NOTE: HTML-kulla blank line, 4-space indent irukka koodaadhu.
st.markdown(
    '<div class="hero">'
    '<span class="petal">🌸</span><span class="petal">🌷</span>'
    '<span class="petal">🌸</span><span class="petal">🌷</span>'
    '<span class="petal">🌸</span><span class="petal">🌷</span>'
    f'<h1>💗 {safe_name.upper()}-ODA AZHAAGANA PAYANAM 💗</h1>'
    '<p>Kashtathula irundhu santhosham varaikkum...</p>'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="intro">'
    'Oru ponnu thannoda kashtangala thaandi, '
    'kanavugalai niraivethura azhaagana kathai. 🌸'
    '</p>',
    unsafe_allow_html=True
)


# ---------------- BANNER ----------------
banner = find_image("banner")
if banner:
    st.markdown(f'<img class="banner-img" src="{banner}" alt="banner">',
                unsafe_allow_html=True)
else:
    st.markdown(banner_svg(), unsafe_allow_html=True)


# ---------------- STORY STAGES ----------------
stages = [
    {
        "emoji": "🌧️",
        "title": "1. Kashtamaana Naalgal",
        "text": (
            f"{safe_name}, sila naal unakku kashtama irukkalaam. "
            "Manasu kashtapadalaam, edhirkaalam pathi bayam varalaam. "
            "Aana indha kashtam un vaazhkai mothamum illa. "
            "Konjam konjama nee munnera mudiyum."
        ),
        "end": "Nee ninaikkiradha vida strong! 💗"
    },
    {
        "emoji": "🌱",
        "title": "2. Valarchi",
        "text": (
            "Naal pogapoga pudhu vishayangal kathukko. "
            "Un kanavugalukkaaga muyarchi pannu. "
            "Thappu nadandhaalum adhulendhu kathukko. "
            "Chinna munnetram kooda mukkiyam dhaan."
        ),
        "end": "Un muyarchi mukkiyam! ✨"
    },
    {
        "emoji": "👑",
        "title": "3. Princess Life",
        "text": (
            "Sila varushangal kazhichu, nee un kaalula ninnu, "
            "unakku pidicha vaazhkaiyai uruvaakkalaam. "
            "Thannambikkaiyoda un mudivugalai neeye eduthu, "
            "un kanavugalai nokki munneru."
        ),
        "end": "Un vaazhkaiyin raani nee dhaan! 👑"
    },
    {
        "emoji": "🌸",
        "title": "4. Happy Life",
        "text": (
            "Innum sila varushangal pogum. Unakku pidicha "
            "vishayangalai senju, azhaagana ninaivugalai "
            "uruvakki, mananimmadhiyoda sirichu vaazhra "
            "naalgal varanum. Un kanavugal niraiveranum."
        ),
        "end": "Un future azhaaga irukkattum! 🦋"
    }
]


# ---------------- DISPLAY CARDS ----------------
columns = st.columns(4, gap="medium")

for i, (column, stage) in enumerate(zip(columns, stages), start=1):
    with column:
        img = find_image(f"stage{i}")
        if img:
            top = f'<img class="card-img" src="{img}" alt="stage {i}">'
        else:
            top = SCENES[i - 1]()

        card_html = (
            '<div class="story-card">'
            f'{top}'
            f'<div class="pill">{stage["title"]}</div>'
            f'<div class="story-text">{stage["text"]}</div>'
            f'<div class="story-end">{stage["end"]}</div>'
            '</div>'
        )
        st.markdown(card_html, unsafe_allow_html=True)


# ---------------- FINAL MESSAGE ----------------
footer_html = (
    '<div class="footer">'
    f'<h2>💖 Eppovum Sirichitte Iru, {html.escape(name.title())}! 💖</h2>'
    '<p>'
    'Un vaazhkaila innum azhaagana pakkangal vara pogudhu. '
    'Un kanavugalai nambu, un mela nambikkai vai. '
    'Unakku santhoshamum mananimmadhiyum kidaikkanum.'
    '</p>'
    '<p><b>Anbudan, Madhesh 💗</b></p>'
    '</div>'
)
st.markdown(footer_html, unsafe_allow_html=True)


# ---------------- BUTTON ACTION ----------------
if show_story:
    st.balloons()
    st.success(f"{name}, un vaazhkaiyila azhaagana naalgal vara vaazhthukkal! 💗")


# ---------------- BOTTOM MESSAGE ----------------
st.markdown(
    '<p style="text-align:center; color:#604078; margin-top:20px; font-size:16px;">'
    'Oru chinna surprise... un mugathula oru smile vara! 🌷'
    '</p>',
    unsafe_allow_html=True
)
