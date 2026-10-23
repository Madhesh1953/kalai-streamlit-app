import html

import streamlit as st

st.set_page_config(
    page_title="Kalai-oda Azhaagana Payanam",
    page_icon="💗",
    layout="wide"
)

# ---------------- CSS DESIGN ----------------
st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(
        135deg,
        #fff4fa,
        #f4f0ff,
        #fff9ef
    );
    color: #30243d !important;
}

/* Main text */
.stApp p,
.stApp label,
.stApp li,
.stApp span {
    color: #30243d;
}

/* Main title */
.hero {
    text-align: center;
    padding: 20px;
}

.hero h1 {
    color: #a51d65 !important;
    font-size: 38px;
    font-weight: bold;
}

.hero p {
    color: #604078 !important;
    font-size: 21px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #fff0f7;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] h2 {
    color: #482641 !important;
}

/* Input box */
.stTextInput input {
    color: #30243d !important;
    background-color: #ffffff !important;
    border: 1px solid #d99cbd !important;
    border-radius: 10px;
}

/* Input placeholder */
.stTextInput input::placeholder {
    color: #76677c !important;
    opacity: 1;
}

/* Story card */
.story-card {
    background-color: #ffffff;
    border: 1px solid #edc5dd;
    border-radius: 18px;
    padding: 18px;
    text-align: center;
    min-height: 390px;
    box-shadow: 0 5px 18px #874c8218;
}

/* Emoji */
.emoji {
    font-size: 42px;
    margin-bottom: 10px;
}

/* Story title */
.pill {
    display: inline-block;
    padding: 8px 10px;
    border-radius: 20px;
    background-color: #ffe0ef;
    color: #842052 !important;
    font-weight: bold;
    margin: 10px 0;
    font-size: 14px;
}

/* Story content */
.story-text {
    font-size: 16px;
    line-height: 1.8;
    color: #40334f !important;
}

/* Story ending */
.story-end {
    color: #b32370 !important;
    font-weight: bold;
    line-height: 1.7;
    margin-top: 16px;
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

.stButton button p,
.stButton button span {
    color: #7b174c !important;
}

.stButton button:hover {
    background-color: #f2bfdc !important;
    border-color: #b94f8a !important;
}

/* Footer */
.footer {
    background: linear-gradient(
        90deg,
        #ffe0ef,
        #eee3ff
    );
    border: 1px solid #e7c3e0;
    border-radius: 20px;
    padding: 22px;
    margin-top: 25px;
    text-align: center;
}

.footer h2 {
    color: #8f205c !important;
    font-size: 25px;
}

.footer p {
    color: #49334f !important;
    font-size: 17px;
    line-height: 1.8;
}

/* Small screen adjustment */
@media (max-width: 768px) {
    .hero h1 {
        font-size: 27px;
    }

    .hero p {
        font-size: 17px;
    }

    .story-card {
        min-height: auto;
    }
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 💗 Oru Chinna Surprise")

    name = st.text_input(
        "Peru enter pannu",
        value="Kalai"
    ).strip()

    if not name:
        name = "Kalai"

    show_story = st.button(
        "✨ En Payanathai Kaattu",
        width="stretch"
    )

    st.write("🌷 Eppovum nambikkaiyoda iru!")
    st.caption("Anbudan, Madhesh 💗")

# Peru-la < > maadhiri characters irundha HTML udaiyaama irukka
safe_name = html.escape(name)


# ---------------- TITLE ----------------
# NOTE: HTML-kulla blank line, 4-space indent irukka koodaadhu.
# Irundha Streamlit adhai code block-a maathidum.
st.markdown(
    '<div class="hero">'
    f'<h1>💗 {safe_name.upper()}-ODA AZHAAGANA PAYANAM 💗</h1>'
    '<p>Kashtathula irundhu santhosham varaikkum...</p>'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<p style="text-align:center; font-size:18px; '
    'color:#40334f; line-height:1.8;">'
    'Oru ponnu thannoda kashtangala thaandi, '
    'kanavugalai niraivethura azhaagana kathai. 🌸'
    '</p>',
    unsafe_allow_html=True
)


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

for column, stage in zip(columns, stages):
    with column:
        card_html = (
            '<div class="story-card">'
            f'<div class="emoji">{stage["emoji"]}</div>'
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

    st.success(
        f"{name}, un vaazhkaiyila azhaagana naalgal "
        "vara vaazhthukkal! 💗"
    )


# ---------------- BOTTOM MESSAGE ----------------
st.markdown(
    '<p style="text-align:center; color:#604078; '
    'margin-top:20px; font-size:16px;">'
    'Oru chinna surprise... un mugathula oru smile vara! 🌷'
    '</p>',
    unsafe_allow_html=True
)
