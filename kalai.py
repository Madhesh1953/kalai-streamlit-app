
import streamlit as st

st.set_page_config(
    page_title="Kalai-oda Azhaagana Payanam",
    page_icon="💗",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff4fa, #f4f0ff, #fff9ef);
}
.hero {
    text-align: center;
    padding: 20px;
}
.hero h1 {
    color: #b83276;
    font-size: 42px;
}
.hero p {
    color: #77558f;
    font-size: 22px;
}
.story-card {
    background: white;
    border: 1px solid #f3cde2;
    border-radius: 20px;
    padding: 20px;
    text-align: center;
    min-height: 340px;
    box-shadow: 0 7px 22px #874c8215;
}
.emoji {
    font-size: 48px;
}
.pill {
    display: inline-block;
    padding: 7px 12px;
    border-radius: 25px;
    background: #ffe0ef;
    color: #9b3269;
    font-weight: bold;
    margin: 10px 0;
}
.story-text {
    font-size: 16px;
    line-height: 1.8;
    color: #4d456c;
}
.footer {
    background: linear-gradient(90deg, #ffe0ef, #eee3ff);
    border-radius: 22px;
    padding: 22px;
    margin-top: 22px;
    text-align: center;
}
.footer h2 {
    color: #a52c6b;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 💗 Oru Chinna Surprise")

    name = st.text_input(
        "Peru",
        value="Kalai"
    ).strip()

    if not name:
        name = "Kalai"

    show_story = st.button("✨ En Payanathai Kaattu")

    st.write("🌷 Eppovum nambikkaiyoda iru!")
    st.caption("Anbudan, Madhesh 💗")

# Title
st.markdown(f"""
<div class="hero">
    <h1>💗 {name.upper()}-ODA AZHAAGANA PAYANAM 💗</h1>
    <p>Kashtathula irundhu santhosham varaikkum...</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<p style="text-align:center;font-size:18px;">
Oru ponnu thannoda kashtangala thaandi,
kanavugalai niraivethura azhaagana kathai. 🌸
</p>
""", unsafe_allow_html=True)

# Story stages
stages = [
    {
        "emoji": "🌧️",
        "title": "1. Kashtamaana Naalgal",
        "text": (
            f"{name}, sila naal unakku kashtama irukkalaam. "
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

columns = st.columns(4, gap="medium")

for column, stage in zip(columns, stages):
    with column:
        st.markdown(f"""
        <div class="story-card">
            <div class="emoji">{stage["emoji"]}</div>
            <div class="pill">{stage["title"]}</div>
            <div class="story-text">{stage["text"]}</div>
            <br>
            <b style="color:#d94691;">{stage["end"]}</b>
        </div>
        """, unsafe_allow_html=True)

# Final message
st.markdown(f"""
<div class="footer">
    <h2>💖 Eppovum Sirichitte Iru, {name.title()}! 💖</h2>
    <p style="font-size:17px;line-height:1.8;">
    Un vaazhkaila innum azhaagana pakkangal vara pogudhu.
    Un kanavugalai nambu, un mela nambikkai vai.
    Unakku santhoshamum mananimmadhiyum kidaikkanum.
    </p>
    <p><b>Anbudan, Madhesh 💗</b></p>
</div>
""", unsafe_allow_html=True)

# Button action
if show_story:
    st.balloons()
    st.success(
        f"{name}, un vaazhkaiyila azhaagana naalgal vara vaazhthukkal! 💗"
    )

st.markdown("""
<p style="text-align:center;color:#8b719e;margin-top:18px;">
Oru chinna Python surprise... un mugathula oru smile vara! 🌷
</p>
""", unsafe_allow_html=True)
