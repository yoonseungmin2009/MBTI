import streamlit as st
import random

# ──────────────────────────────────────────────
# 페이지 설정
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="🎮 MBTI 포켓몬 매칭",
    page_icon="⚡",
    layout="centered",
)

# ──────────────────────────────────────────────
# CSS 스타일
# ──────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Nanum+Gothic:wght@400;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Nanum Gothic', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #fef9c3 0%, #fce7f3 40%, #e0f2fe 100%);
    min-height: 100vh;
}

h1, h2, h3 {
    font-family: 'Jua', sans-serif !important;
}

/* 타이틀 */
.main-title {
    font-family: 'Jua', sans-serif;
    font-size: 2.8rem;
    text-align: center;
    background: linear-gradient(90deg, #f59e0b, #ef4444, #8b5cf6, #3b82f6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.2rem;
    line-height: 1.2;
}

.subtitle {
    text-align: center;
    color: #6b7280;
    font-size: 1.05rem;
    margin-bottom: 2rem;
}

/* MBTI 버튼 그리드 */
.mbti-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    margin: 1rem 0 2rem 0;
}

.mbti-btn {
    background: white;
    border: 2.5px solid #e5e7eb;
    border-radius: 16px;
    padding: 14px 8px;
    text-align: center;
    cursor: pointer;
    transition: all 0.2s ease;
    font-family: 'Jua', sans-serif;
    font-size: 1rem;
    color: #374151;
    box-shadow: 3px 3px 0px #e5e7eb;
}

.mbti-btn:hover {
    transform: translateY(-3px);
    box-shadow: 3px 6px 0px #d1d5db;
}

.mbti-btn.selected {
    border-color: #f59e0b;
    background: #fffbeb;
    box-shadow: 3px 3px 0px #fbbf24;
    color: #d97706;
}

/* 결과 카드 */
.result-card {
    background: white;
    border-radius: 24px;
    padding: 2rem;
    box-shadow: 6px 6px 0px #d1d5db;
    border: 2.5px solid #e5e7eb;
    margin-top: 1.5rem;
    animation: popIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

@keyframes popIn {
    from { transform: scale(0.8); opacity: 0; }
    to   { transform: scale(1);   opacity: 1; }
}

.pokemon-name {
    font-family: 'Jua', sans-serif;
    font-size: 2rem;
    color: #1f2937;
    margin: 0.5rem 0 0.2rem 0;
}

.pokemon-type-badge {
    display: inline-block;
    padding: 4px 14px;
    border-radius: 99px;
    font-size: 0.85rem;
    font-weight: 800;
    margin: 2px;
}

.reason-box {
    background: #fef9c3;
    border-left: 4px solid #f59e0b;
    border-radius: 0 12px 12px 0;
    padding: 1rem 1.2rem;
    margin: 1rem 0;
    font-size: 0.97rem;
    color: #374151;
    line-height: 1.7;
}

.trait-pill {
    display: inline-block;
    background: #ede9fe;
    color: #5b21b6;
    border-radius: 99px;
    padding: 3px 12px;
    font-size: 0.82rem;
    margin: 3px;
    font-weight: 700;
}

.section-label {
    font-family: 'Jua', sans-serif;
    font-size: 1.1rem;
    color: #6b7280;
    margin: 1.2rem 0 0.4rem 0;
}

.footer-note {
    text-align: center;
    color: #9ca3af;
    font-size: 0.8rem;
    margin-top: 2.5rem;
}

/* selectbox 스타일 */
div[data-baseweb="select"] > div {
    border-radius: 16px !important;
    border: 2.5px solid #e5e7eb !important;
    font-family: 'Jua', sans-serif !important;
    font-size: 1.1rem !important;
    box-shadow: 3px 3px 0px #e5e7eb !important;
    background: white !important;
}

/* 버튼 */
.stButton > button {
    font-family: 'Jua', sans-serif !important;
    font-size: 1.1rem !important;
    border-radius: 16px !important;
    border: 2.5px solid #f59e0b !important;
    background: linear-gradient(135deg, #fbbf24, #f59e0b) !important;
    color: white !important;
    box-shadow: 3px 3px 0px #d97706 !important;
    transition: all 0.15s !important;
    padding: 0.6rem 2rem !important;
    width: 100% !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 3px 5px 0px #b45309 !important;
}
.stButton > button:active {
    transform: translateY(1px) !important;
    box-shadow: 1px 1px 0px #b45309 !important;
}
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────
# 데이터: MBTI별 포켓몬 추천
# ──────────────────────────────────────────────
MBTI_POKEMON = {
    "INTJ": {
        "emoji": "🧠",
        "label": "전략가",
        "pokemon": "리자몽",
        "pokemon_en": "Charizard",
        "number": 6,
        "types": [("🔥 불꽃", "#ef4444", "#fee2e2"), ("🦅 비행", "#60a5fa", "#dbeafe")],
        "traits": ["완벽주의자", "독립적", "전략적 사고", "카리스마"],
        "reason": "리자몽은 자신만의 방식으로 강해지는 포켓몬이에요. 강한 자존심과 독립심, 그리고 한 번 목표를 정하면 끝까지 밀어붙이는 추진력이 INTJ와 딱 맞아요! 🐉\n아무나 따르지 않고 오직 진정한 강자만 인정하는 모습이 당신과 닮았어요.",
        "color": "#ef4444",
        "bg": "#fff1f2",
    },
    "INTP": {
        "emoji": "🔬",
        "label": "논리술사",
        "pokemon": "폴리곤Z",
        "pokemon_en": "Porygon-Z",
        "number": 474,
        "types": [("💻 노말", "#6b7280", "#f3f4f6")],
        "traits": ["분석적", "창의적", "호기심 왕", "비선형적 사고"],
        "reason": "폴리곤Z는 업그레이드를 거듭해 예측 불가능한 행동을 하는 포켓몬이에요. 끊임없이 이론을 탐구하고, 남들이 이해 못 하는 생각의 흐름을 가진 INTP와 완벽 매칭! 🤖\n논리 속에서 창의성을 폭발시키는 당신, 멋져요.",
        "color": "#6b7280",
        "bg": "#f9fafb",
    },
    "ENTJ": {
        "emoji": "👑",
        "label": "통솔자",
        "pokemon": "루카리오",
        "pokemon_en": "Lucario",
        "number": 448,
        "types": [("⚔️ 격투", "#f97316", "#fff7ed"), ("🔮 강철", "#64748b", "#f1f5f9")],
        "traits": ["리더십", "카리스마", "목표지향", "강한 의지"],
        "reason": "루카리오는 무리를 이끄는 리더이자 파동을 통해 멀리까지 꿰뚫어 보는 통찰력의 포켓몬이에요. ENTJ의 타고난 리더십과 날카로운 판단력이 꼭 닮았어요! ✨\n어디서든 존재감을 뿜뿜 발산하는 당신과 찰떡!",
        "color": "#3b82f6",
        "bg": "#eff6ff",
    },
    "ENTP": {
        "emoji": "💡",
        "label": "발명가",
        "pokemon": "게노세크트",
        "pokemon_en": "Genesect",
        "number": 649,
        "types": [("🐛 벌레", "#84cc16", "#f7fee7"), ("🔮 강철", "#64748b", "#f1f5f9")],
        "traits": ["논쟁 즐김", "혁신적", "재치 넘침", "빠른 적응"],
        "reason": "게노세크트는 고대 생물을 최첨단으로 개조한 포켓몬! 기존 것을 뒤집고 새롭게 만드는 ENTP의 혁신 DNA와 완전 일치해요 ⚙️\n토론에서 항상 상대를 당황시키는 당신, 게노세크트처럼 최강이에요!",
        "color": "#84cc16",
        "bg": "#f7fee7",
    },
    "INFJ": {
        "emoji": "🌙",
        "label": "선지자",
        "pokemon": "루기아",
        "pokemon_en": "Lugia",
        "number": 249,
        "types": [("🌊 물", "#38bdf8", "#e0f2fe"), ("🦅 비행", "#60a5fa", "#dbeafe")],
        "traits": ["깊은 공감", "이상주의", "직관력", "평화 추구"],
        "reason": "루기아는 바다 깊숙이 홀로 살며 강한 힘을 품속에 감추고 있어요. 세상을 더 좋게 만들고 싶지만 조용히 뒤에서 이끄는 INFJ의 모습 그 자체예요 🕊️\n당신의 깊은 공감 능력과 신비로운 직관력, 정말 특별해요.",
        "color": "#38bdf8",
        "bg": "#f0f9ff",
    },
    "INFP": {
        "emoji": "🌸",
        "label": "중재자",
        "pokemon": "이브이",
        "pokemon_en": "Eevee",
        "number": 133,
        "types": [("⭐ 노말", "#fbbf24", "#fffbeb")],
        "traits": ["감수성 풍부", "이상적", "창의적", "공감 능력"],
        "reason": "이브이는 어떤 타입으로도 진화할 수 있는 가능성의 포켓몬! 무한한 잠재력과 깊은 감수성을 가진 INFP와 찰떡이에요 🌈\n자신만의 세계관이 뚜렷하고 진심을 다해 관계를 소중히 여기는 당신, 이브이처럼 빛나요.",
        "color": "#f59e0b",
        "bg": "#fffbeb",
    },
    "ENFJ": {
        "emoji": "🌟",
        "label": "선도자",
        "pokemon": "세레비",
        "pokemon_en": "Celebi",
        "number": 251,
        "types": [("🌿 풀", "#22c55e", "#f0fdf4"), ("🔮 에스퍼", "#a855f7", "#faf5ff")],
        "traits": ["따뜻한 리더십", "타인 중심", "영감을 줌", "카리스마"],
        "reason": "세레비는 숲을 지키고 모두를 이끄는 시간여행 포켓몬이에요. 주변 사람들에게 영감을 주고 함께 성장하길 원하는 ENFJ의 따뜻한 리더십과 딱 맞아요 💚\n당신이 있는 곳에는 항상 따뜻함이 가득!",
        "color": "#22c55e",
        "bg": "#f0fdf4",
    },
    "ENFP": {
        "emoji": "🎪",
        "label": "활동가",
        "pokemon": "피카츄",
        "pokemon_en": "Pikachu",
        "number": 25,
        "types": [("⚡ 전기", "#facc15", "#fefce8")],
        "traits": ["열정 넘침", "사교적", "자유로운 영혼", "창의적"],
        "reason": "피카츄는 어디서든 에너지를 발산하고 모두를 밝게 만드는 포켓몬이에요! 넘치는 열정과 긍정 에너지로 주변을 들뜨게 만드는 ENFP와 찰떡이에요 ⚡\n당신의 빛나는 존재감, 정말 최고예요!",
        "color": "#facc15",
        "bg": "#fefce8",
    },
    "ISTJ": {
        "emoji": "📋",
        "label": "현실주의자",
        "pokemon": "동탁군",
        "pokemon_en": "Aegislash",
        "number": 681,
        "types": [("👻 고스트", "#8b5cf6", "#f5f3ff"), ("🔮 강철", "#64748b", "#f1f5f9")],
        "traits": ["책임감", "신뢰할 수 있음", "원칙주의", "꼼꼼함"],
        "reason": "동탁군은 왕실의 검사이자 충직한 수호자예요. 자신의 임무에 절대 흔들리지 않는 강한 책임감이 ISTJ와 딱 맞아요 🗡️\n묵묵히 신뢰를 쌓고 언제나 든든하게 곁에 있는 당신, 정말 소중한 사람이에요.",
        "color": "#8b5cf6",
        "bg": "#f5f3ff",
    },
    "ISFJ": {
        "emoji": "🤗",
        "label": "수호자",
        "pokemon": "토게피",
        "pokemon_en": "Togepi",
        "number": 175,
        "types": [("✨ 페어리", "#ec4899", "#fdf2f8")],
        "traits": ["헌신적", "다정함", "세심함", "전통 중시"],
        "reason": "토게피는 행복 에너지를 나눠주는 포켓몬이에요! 주변 사람들의 행복을 위해 조용히 헌신하는 ISFJ의 따뜻한 마음과 완전 같아요 💕\n당신 곁에 있으면 마음이 따뜻해지는 이유가 있었네요!",
        "color": "#ec4899",
        "bg": "#fdf2f8",
    },
    "ESTJ": {
        "emoji": "⚖️",
        "label": "경영자",
        "pokemon": "강철톤",
        "pokemon_en": "Aggron",
        "number": 306,
        "types": [("🔮 강철", "#64748b", "#f1f5f9"), ("🪨 바위", "#a3a3a3", "#f5f5f5")],
        "traits": ["규칙 중시", "조직적", "리더십", "실용적"],
        "reason": "강철톤은 자신의 영역을 철저히 지키는 규율과 질서의 포켓몬이에요. 체계를 세우고 목표를 향해 효율적으로 나아가는 ESTJ와 완벽 매칭 🏔️\n당신이 있으면 어떤 조직이든 제대로 돌아가요!",
        "color": "#64748b",
        "bg": "#f8fafc",
    },
    "ESFJ": {
        "emoji": "💝",
        "label": "집정관",
        "pokemon": "클레페어리",
        "pokemon_en": "Clefable",
        "number": 36,
        "types": [("✨ 페어리", "#ec4899", "#fdf2f8")],
        "traits": ["사교적", "배려심 깊음", "조화 추구", "충직함"],
        "reason": "클레페어리는 달빛 아래서 춤추며 주변을 행복하게 만드는 포켓몬이에요! 모두가 잘 지내길 바라며 관계를 소중히 여기는 ESFJ와 닮았어요 🌙\n당신이 있는 자리는 언제나 화목하고 따뜻해요.",
        "color": "#f472b6",
        "bg": "#fdf2f8",
    },
    "ISTP": {
        "emoji": "🔧",
        "label": "장인",
        "pokemon": "메타그로스",
        "pokemon_en": "Metagross",
        "number": 376,
        "types": [("🔮 강철", "#64748b", "#f1f5f9"), ("🧠 에스퍼", "#a855f7", "#faf5ff")],
        "traits": ["냉철함", "실용적", "손재주 뛰어남", "독립적"],
        "reason": "메타그로스는 4개의 뇌로 슈퍼컴퓨터보다 빠른 계산을 하는 포켓몬이에요. 감정보다 논리와 분석으로 상황을 해결하는 ISTP의 냉철함과 찰떡이에요 🤖\n조용하지만 실력으로 증명하는 당신, 멋져요!",
        "color": "#64748b",
        "bg": "#f8fafc",
    },
    "ISFP": {
        "emoji": "🎨",
        "label": "예술가",
        "pokemon": "뮤",
        "pokemon_en": "Mew",
        "number": 151,
        "types": [("🔮 에스퍼", "#a855f7", "#faf5ff")],
        "traits": ["자유로운 영혼", "감수성", "친절함", "현재에 충실"],
        "reason": "뮤는 모든 포켓몬의 기원이자 자유롭게 날아다니는 신비로운 존재예요. 순수하고 창의적이며 자신만의 감성으로 세상을 바라보는 ISFP와 완전 닮았어요 🌈\n당신의 순수한 감수성이 세상을 더 아름답게 만들어요.",
        "color": "#a855f7",
        "bg": "#faf5ff",
    },
    "ESTP": {
        "emoji": "⚡",
        "label": "사업가",
        "pokemon": "전룡",
        "pokemon_en": "Dragonite",
        "number": 149,
        "types": [("🐉 드래곤", "#7c3aed", "#f5f3ff"), ("🦅 비행", "#60a5fa", "#dbeafe")],
        "traits": ["행동파", "대담함", "현실적", "사교적"],
        "reason": "전룡은 빠른 비행으로 세계를 누비며 위기에 처한 이들을 도와주는 행동파 포켓몬이에요! 생각보다 행동이 앞서고 어떤 상황에서도 적응하는 ESTP와 완벽 매칭 🚀\n당신이 있으면 지루할 틈이 없어요!",
        "color": "#f97316",
        "bg": "#fff7ed",
    },
    "ESFP": {
        "emoji": "🎉",
        "label": "엔터테이너",
        "pokemon": "파이리",
        "pokemon_en": "Charmander",
        "number": 4,
        "types": [("🔥 불꽃", "#ef4444", "#fee2e2")],
        "traits": ["밝고 활기참", "즉흥적", "애교 만점", "존재감 폭발"],
        "reason": "파이리는 귀엽고 애교 넘치지만 진화하면 엄청난 강함을 보여주는 포켓몬이에요! 밝은 에너지로 주변을 빛내고 분위기를 이끄는 ESFP와 딱 맞아요 🔥\n당신이 있는 곳은 언제나 파티예요!",
        "color": "#ef4444",
        "bg": "#fff1f2",
    },
}

MBTI_TYPES = list(MBTI_POKEMON.keys())

TYPE_GROUPS = {
    "분석가 🧠": ["INTJ", "INTP", "ENTJ", "ENTP"],
    "외교관 🌿": ["INFJ", "INFP", "ENFJ", "ENFP"],
    "관리자 📋": ["ISTJ", "ISFJ", "ESTJ", "ESFJ"],
    "탐험가 🎯": ["ISTP", "ISFP", "ESTP", "ESFP"],
}

# ──────────────────────────────────────────────
# 타이틀
# ──────────────────────────────────────────────
st.markdown('<div class="main-title">⚡ MBTI 포켓몬 매칭 🎮</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">나의 MBTI에 딱 맞는 포켓몬을 찾아봐요! 🔍✨</div>', unsafe_allow_html=True)

# 귀여운 장식
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<p style='text-align:center; font-size:2rem;'>🌟</p>", unsafe_allow_html=True)
with col2:
    st.markdown("<p style='text-align:center; font-size:2rem;'>🎮</p>", unsafe_allow_html=True)
with col3:
    st.markdown("<p style='text-align:center; font-size:2rem;'>✨</p>", unsafe_allow_html=True)

st.divider()

# ──────────────────────────────────────────────
# MBTI 선택
# ──────────────────────────────────────────────
st.markdown("### 🙋 내 MBTI를 선택해줘요!")

# 그룹별 탭
tabs = st.tabs(list(TYPE_GROUPS.keys()))

selected_mbti = None

# session_state 초기화
if "chosen_mbti" not in st.session_state:
    st.session_state.chosen_mbti = None

for tab, (group_name, members) in zip(tabs, TYPE_GROUPS.items()):
    with tab:
        cols = st.columns(4)
        for i, mbti in enumerate(members):
            info = MBTI_POKEMON[mbti]
            with cols[i]:
                is_selected = st.session_state.chosen_mbti == mbti
                btn_label = f"{info['emoji']}\n**{mbti}**\n{info['label']}"
                if st.button(
                    f"{info['emoji']} {mbti}\n{info['label']}",
                    key=f"btn_{mbti}",
                    use_container_width=True,
                    type="primary" if is_selected else "secondary",
                ):
                    st.session_state.chosen_mbti = mbti
                    st.rerun()

# ──────────────────────────────────────────────
# 결과 표시
# ──────────────────────────────────────────────
if st.session_state.chosen_mbti:
    mbti = st.session_state.chosen_mbti
    data = MBTI_POKEMON[mbti]

    st.markdown("---")
    st.markdown(f"### 🎊 **{mbti}** 유형에게 어울리는 포켓몬은...")

    # 포켓몬 스프라이트 URL (PokeAPI 공식 스프라이트) - 정수 번호 사용
    num = data['number']
    sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{num}.png"
    fallback_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{num}.png"
    num_display = str(num).zfill(3)  # 표시용만 0 패딩

    # 결과 레이아웃
    col_img, col_info = st.columns([1, 2])

    with col_img:
        st.markdown(
            f"""
            <div style="
                background: {data['bg']};
                border-radius: 20px;
                padding: 1.5rem;
                text-align: center;
                border: 2.5px solid {data['color']}33;
                box-shadow: 4px 4px 0px {data['color']}33;
            ">
                <img src="{sprite_url}"
                     style="width:100%; max-width:180px;"
                     onerror="this.onerror=null; this.src='{fallback_url}'"
                />
                <div style="font-size:0.8rem; color:#9ca3af; margin-top:0.3rem;">No.{num_display}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_info:
        # 이름
        st.markdown(
            f'<div class="pokemon-name">🎯 {data["pokemon"]}</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div style="color:#6b7280; font-size:0.9rem; margin-bottom:0.8rem;">{data["pokemon_en"]}</div>',
            unsafe_allow_html=True,
        )

        # 타입 뱃지
        type_html = ""
        for type_name, text_color, bg_color in data["types"]:
            type_html += f'<span class="pokemon-type-badge" style="background:{bg_color}; color:{text_color};">{type_name}</span> '
        st.markdown(type_html, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # 공통 특성
        st.markdown('<div class="section-label">💎 공통 특성</div>', unsafe_allow_html=True)
        traits_html = "".join(
            [f'<span class="trait-pill">{t}</span>' for t in data["traits"]]
        )
        st.markdown(traits_html, unsafe_allow_html=True)

    # 매칭 이유
    st.markdown('<div class="section-label">💬 매칭 이유</div>', unsafe_allow_html=True)
    reason_html = data["reason"].replace("\n", "<br>")
    st.markdown(
        f'<div class="reason-box">{reason_html}</div>',
        unsafe_allow_html=True,
    )

    # 궁합 포켓몬 (랜덤 다른 MBTI)
    other_mbtis = [m for m in MBTI_TYPES if m != mbti]
    partner_mbti = random.choice(other_mbtis)
    partner = MBTI_POKEMON[partner_mbti]

    st.markdown('<div class="section-label">🤝 포켓몬 궁합 파트너</div>', unsafe_allow_html=True)
    partner_sprite = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{partner['number']}.png"
    partner_fallback = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{partner['number']}.png"
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, {data['bg']}, {partner['bg']});
            border-radius: 16px;
            padding: 1rem 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            border: 2px dashed #e5e7eb;
        ">
            <img src="{partner_sprite}" style="width:60px;" onerror="this.onerror=null; this.src='{partner_fallback}'" />
            <div>
                <strong style="font-size:1.05rem;">{partner_mbti} · {partner['pokemon']}</strong>
                <div style="color:#6b7280; font-size:0.85rem; margin-top:0.2rem;">
                    {partner['emoji']} {partner['label']} 유형과 함께라면 무적이에요! ✨
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 다시 하기
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 다른 MBTI도 확인해보기", use_container_width=True):
        st.session_state.chosen_mbti = None
        st.rerun()

    # 공유 문구
    st.markdown(
        f"""
        <div style="
            text-align:center;
            background: white;
            border-radius: 16px;
            padding: 1rem;
            margin-top: 1rem;
            border: 2px solid #fde68a;
            color: #92400e;
            font-size: 0.9rem;
        ">
            🎮 나의 MBTI <strong>{mbti}</strong>에 어울리는 포켓몬은 <strong>{data['pokemon']}</strong>이에요!<br>
            친구에게도 공유해보세요 👀✨
        </div>
        """,
        unsafe_allow_html=True,
    )

else:
    # 아직 선택 전
    st.markdown(
        """
        <div style="
            text-align: center;
            padding: 3rem 1rem;
            color: #9ca3af;
        ">
            <div style="font-size: 4rem;">👆</div>
            <div style="font-size: 1.1rem; margin-top: 0.5rem;">
                위에서 MBTI를 선택하면<br>어울리는 포켓몬을 알려드려요!
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ──────────────────────────────────────────────
# 푸터
# ──────────────────────────────────────────────
st.markdown(
    """
    <div class="footer-note">
        Made with ❤️ + ⚡ · 포켓몬 이미지 출처: PokéAPI<br>
        이 매칭은 재미를 위한 것이에요! 실제 MBTI와 다를 수 있어요 😄
    </div>
    """,
    unsafe_allow_html=True,
)
