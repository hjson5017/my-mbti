import streamlit as st
import random

# -------------------------------------------------
# MBTI 유형별 추천 포켓몬 데이터
# -------------------------------------------------
MBTI_POKEMON = {
    "INTJ": [
        {"name": "메타그로스", "type": "강철/에스퍼", "desc": "뛰어난 연산 능력을 지닌 전략가 포켓몬으로, 치밀한 계획을 세우는 INTJ와 잘 어울려요."},
        {"name": "게노세크트", "type": "벌레/강철", "desc": "냉철하고 지적인 이미지로 INTJ의 분석적인 성향과 닮았어요."},
    ],
    "INTP": [
        {"name": "무장조", "type": "강철/비행", "desc": "복잡한 구조와 논리적인 매력을 지닌 포켓몬, 호기심 많은 INTP에게 딱이에요."},
        {"name": "슈바르고", "type": "벌레/강철", "desc": "독창적이고 분석적인 사고를 가진 INTP와 잘 맞아요."},
    ],
    "ENTJ": [
        {"name": "펜드라", "type": "드래곤/비행", "desc": "타고난 리더십과 카리스마를 지닌 포켓몬으로 ENTJ의 통솔력과 닮았어요."},
        {"name": "루카리오", "type": "격투/강철", "desc": "강한 의지와 목표 지향적인 성격이 ENTJ와 잘 어울려요."},
    ],
    "ENTP": [
        {"name": "조로아크", "type": "악", "desc": "재치있고 임기응변에 능한 포켓몬, 아이디어가 넘치는 ENTP와 잘 맞아요."},
        {"name": "또가스", "type": "독", "desc": "예측불가능하고 재미있는 매력이 ENTP와 닮았어요."},
    ],
    "INFJ": [
        {"name": "라티아스", "type": "드래곤/에스퍼", "desc": "신비롭고 통찰력 있는 포켓몬으로, 깊은 내면을 가진 INFJ와 어울려요."},
        {"name": "세레비", "type": "풀/에스퍼", "desc": "이상주의적이고 따뜻한 INFJ의 성향과 닮았어요."},
    ],
    "INFP": [
        {"name": "뮤", "type": "에스퍼", "desc": "순수하고 자유로운 영혼을 가진 포켓몬으로, 몽상가 기질의 INFP와 잘 맞아요."},
        {"name": "피오네", "type": "물", "desc": "따뜻하고 감성적인 매력이 INFP와 닮았어요."},
    ],
    "ENFJ": [
        {"name": "가디안", "type": "격투/에스퍼", "desc": "동료를 이끌고 보호하는 성향이 ENFJ의 헌신적인 리더십과 잘 어울려요."},
        {"name": "라프라스", "type": "물/얼음", "desc": "다정하고 남을 잘 챙기는 성격이 ENFJ와 닮았어요."},
    ],
    "ENFP": [
        {"name": "블레이범", "type": "불꽃/격투", "desc": "밝고 에너지 넘치는 포켓몬으로, 열정적인 ENFP와 완벽하게 어울려요."},
        {"name": "피카츄", "type": "전기", "desc": "사교적이고 발랄한 매력이 ENFP를 닮았어요."},
    ],
    "ISTJ": [
        {"name": "메탕구", "type": "강철/에스퍼", "desc": "원칙과 책임감을 중시하는 성실한 포켓몬으로 ISTJ와 잘 맞아요."},
        {"name": "코바르온", "type": "강철/격투", "desc": "묵묵하고 신뢰감 있는 이미지가 ISTJ와 닮았어요."},
    ],
    "ISFJ": [
        {"name": "픽시", "type": "페어리", "desc": "따뜻하고 헌신적인 성격이 배려심 많은 ISFJ와 잘 어울려요."},
        {"name": "라프라스", "type": "물/얼음", "desc": "보살핌을 잘 하는 다정한 성향이 ISFJ와 닮았어요."},
    ],
    "ESTJ": [
        {"name": "번치코", "type": "격투", "desc": "규율과 체계를 중시하는 포켓몬으로 ESTJ의 리더십과 잘 맞아요."},
        {"name": "핫삼", "type": "벌레/강철", "desc": "강인하고 실용적인 성격이 ESTJ와 닮았어요."},
    ],
    "ESFJ": [
        {"name": "이브이", "type": "노말", "desc": "사교적이고 다정한 포켓몬으로, 사람들과 잘 어울리는 ESFJ와 잘 맞아요."},
        {"name": "밀로틱", "type": "물", "desc": "우아하고 배려심 넘치는 매력이 ESFJ와 닮았어요."},
    ],
    "ISTP": [
        {"name": "겐가", "type": "고스트/독", "desc": "독립적이고 실용적인 문제 해결 능력이 ISTP와 잘 어울려요."},
        {"name": "쥬피썬더", "type": "전기", "desc": "냉철하고 순발력 있는 매력이 ISTP와 닮았어요."},
    ],
    "ISFP": [
        {"name": "라티오스", "type": "드래곤/에스퍼", "desc": "감수성이 풍부하고 예술적인 포켓몬으로 ISFP와 잘 어울려요."},
        {"name": "글레이시아", "type": "얼음", "desc": "부드럽고 온화한 매력이 ISFP를 닮았어요."},
    ],
    "ESTP": [
        {"name": "간부짱", "type": "불꽃/격투", "desc": "행동력이 강하고 열정적인 포켓몬으로 ESTP와 잘 맞아요."},
        {"name": "저리더프", "type": "전기", "desc": "빠르고 대담한 성격이 ESTP와 닮았어요."},
    ],
    "ESFP": [
        {"name": "치코리타", "type": "풀", "desc": "밝고 사랑스러운 매력이 사교적인 ESFP와 잘 어울려요."},
        {"name": "고라파덕", "type": "물", "desc": "유쾌하고 자유분방한 매력이 ESFP를 닮았어요."},
    ],
}

# -------------------------------------------------
# 페이지 설정
# -------------------------------------------------
st.set_page_config(page_title="MBTI 포켓몬 추천", page_icon="⚡", layout="centered")

st.title("⚡ MBTI 포켓몬 추천기")
st.write("당신의 MBTI를 선택하면, 딱 어울리는 포켓몬을 추천해드려요!")

mbti_list = list(MBTI_POKEMON.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_list)

if st.button("포켓몬 추천받기"):
    candidates = MBTI_POKEMON[selected_mbti]
    pokemon = random.choice(candidates)

    st.subheader(f"🎉 {selected_mbti} 유형에게 어울리는 포켓몬은...")
    st.markdown(f"### 🐾 {pokemon['name']}")
    st.write(f"**타입:** {pokemon['type']}")
    st.write(f"**설명:** {pokemon['desc']}")

    st.divider()
    st.caption("버튼을 다시 누르면 같은 MBTI 안에서 다른 포켓몬이 나올 수도 있어요!")
else:
    st.info("MBTI를 선택하고 버튼을 눌러주세요.")

st.divider()
st.caption("Made with Streamlit • 별도 라이브러리 없이 순수 Python + Streamlit만 사용")
