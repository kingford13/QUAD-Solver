import streamlit as st

st.set_page_config(page_title="QUAD Solver", page_icon="📚")

st.title("📚 QUAD SOLVER")
st.subheader("Ghana WASSCE - All Subjects")

# ===== FULL SHS QUESTION BANK =====
questions = {
    "Core Maths": [
        {"q": "Solve: 2x + 3 = 11, find x", "a": "4", "exp": "2x=8, x=4"},
        {"q": "What is 25% of 200?", "a": "50", "exp": "25/100 * 200 = 50"},
        {"q": "Factorize: x² - 9", "a": "(x-3)(x+3)", "exp": "Difference of two squares"},
    ],
    "English": [
        {"q": "Past tense of 'go'?", "a": "went", "exp": "go - went - gone"},
        {"q": "Plural of 'child'?", "a": "children", "exp": "Irregular plural"},
    ],
    "Integrated Science": [
        {"q": "Chemical symbol for water?", "a": "H2O", "exp": "2 Hydrogen, 1 Oxygen"},
        {"q": "Powerhouse of the cell?", "a": "mitochondria", "exp": "Produces energy"},
        {"q": "Atomic number of Carbon?", "a": "6", "exp": "6 protons"},
    ],
    "Social Studies": [
        {"q": "How many regions in Ghana?", "a": "16", "exp": "16 regions since 2019"},
        {"q": "First President of Ghana?", "a": "Kwame Nkrumah", "exp": "Dr. Kwame Nkrumah"},
    ],
    "Physics": [
        {"q": "SI unit of force?", "a": "Newton", "exp": "Force measured in Newtons (N)"},
        {"q": "Speed of light?", "a": "3x10^8", "exp": "3 x 10^8 m/s in vacuum"},
    ],
    "Chemistry": [
        {"q": "pH of pure water?", "a": "7", "exp": "Neutral pH"},
    ],
    "Biology": [
        {"q": "How many chromosomes in humans?", "a": "46", "exp": "23 pairs"},
    ],
    "Elective Maths": [
        {"q": "What is sin 90°?", "a": "1", "exp": "sin 90 = 1"},
    ],
    "Economics": [
        {"q": "What does GDP stand for?", "a": "Gross Domestic Product", "exp": "Total value of goods/services"},
    ],
    "Government": [
        {"q": "How many arms of government?", "a": "3", "exp": "Executive, Legislature, Judiciary"},
    ]
}

# ===== APP LOGIC =====
subject = st.selectbox("Choose Your SHS Subject:", list(questions.keys()))

st.divider()
st.write(f"### {subject} Questions")

score = 0
for i, item in enumerate(questions[subject]):
    st.write(f"**Q{i+1}: {item['q']}**")
    user_ans = st.text_input(f"Your answer for Q{i+1}", key=f"{subject}_{i}")

    if user_ans:
        if user_ans.lower().strip() in item['a'].lower() or item['a'].lower() in user_ans.lower().strip():
            st.success(f"✅ Correct! {item['exp']}")
            score += 1
        else:
            st.error(f"❌ Wrong. Answer: {item['a']}")
            st.info(f"Explanation: {item['exp']}")

st.divider()
st.write(f"Made by KINGSFORD for Ghana SHS students 🇬🇭")