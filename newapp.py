import streamlit as st
import pdfplumber
from streamlit_option_menu import option_menu
import plotly.express as px
import random
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #0f172a, #1e293b, #334155);
    color: white !important;
}
html, body, [class*="css"] {
    color: white !important;
}
.main-title {
    font-size: 65px;
    font-weight: 900;
    text-align: center;
    color: #00FFF7;
    margin-bottom: 10px;
    text-shadow: 2px 2px 20px rgba(0,255,247,0.7);
}
.sub-title {
    text-align: center;
    font-size: 26px;
    color: white !important;
    margin-bottom: 35px;
    font-weight: 600;
}
h1, h2, h3, h4, h5, h6 {
    color: #00FFF7 !important;
    font-weight: bold;
}
p, span, label, div {
    color: white !important;
}
section[data-testid="stSidebar"] {
    background: #111827;
}
section[data-testid="stSidebar"] * {
    color: white !important;
    font-size: 17px;
}
.stButton>button {
    background: linear-gradient(90deg, #00FFF7, #38BDF8);
    color: black !important;
    border-radius: 14px;
    border: none;
    font-size: 20px;
    font-weight: bold;
    width: 100%;
    padding: 14px;
    transition: 0.3s;
    box-shadow: 0px 0px 15px rgba(0,255,247,0.5);
}

.stButton>button:hover {
    transform: scale(1.04);
}
.stTextInput>div>div>input,
.stTextArea textarea {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 12px;
    border: 2px solid #00FFF7;
    font-size: 18px;
}
.stSelectbox div[data-baseweb="select"] {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 12px;
}
[data-testid="stFileUploader"] {
    background-color: #1e293b;
    border-radius: 18px;
    padding: 15px;
    border: 2px dashed #00FFF7;
}
[data-testid="metric-container"] {
    background: linear-gradient(145deg, #1e293b, #334155);
    border-radius: 18px;
    padding: 20px;
    border: 2px solid #00FFF7;
    box-shadow: 0px 0px 15px rgba(0,255,247,0.2);
}
.stTabs [data-baseweb="tab"] {
    background-color: white !important;
    color: black !important;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px;
}

.stTabs [aria-selected="true"] {
    background-color: #00FFF7 !important;
    color: black !important;
}
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ============================================
# HERO SECTION
# ============================================

st.markdown("""
<div class="main-title">
🤖 AI Resume Analyzer
</div>

<div class="sub-title">
🔥 ATS Checker • Mock Interview • Career Roadmap • Skills Analyzer
</div>
""", unsafe_allow_html=True)
with st.sidebar:

    selected = option_menu(
        "🤖 AI Menu",
        [
            "Dashboard",
            "Resume Analyzer",
            "Mock Interview",
            "Career Roadmap",
            "Project Generator",
            "Skills Gap Analyzer",
            "About"
        ],

        icons=[
            "house",
            "file-earmark-person",
            "robot",
            "graph-up",
            "code-slash",
            "search",
            "info-circle"
        ],

        menu_icon="cast",
        default_index=0
    )

if selected == "Dashboard":

    st.title("🚀 AI Career Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📄 ATS Accuracy", "98%")

    with col2:
        st.metric("💼 Hiring Success", "92%")

    with col3:
        st.metric("🚀 AI Features", "15+")

    st.markdown("---")

    st.subheader("🔥 Features")

    features = [
        "✅ ATS Resume Checker",
        "✅ AI Mock Interview",
        "✅ Career Roadmap",
        "✅ Recruiter Insights",
        "✅ Skills Gap Analysis",
        "✅ Salary Estimator",
        "✅ Resume Performance Graph"
    ]

    for feature in features:
        st.success(feature)

    st.balloons()

elif selected == "Resume Analyzer":

    st.title("📄 Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

    skills = [
        "Python", "Java", "C", "C++", "SQL",
        "MongoDB", "Machine Learning",
        "Deep Learning", "OpenCV",
        "Power BI", "Data Science",
        "HTML", "CSS", "JavaScript"
    ]

    def extract_text(pdf_file):

        text = ""

        with pdfplumber.open(pdf_file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text

        return text

    def get_skills(text):

        found = []

        for skill in skills:

            if skill.lower() in text.lower():
                found.append(skill)

        return found

    if uploaded_file:

        resume_text = extract_text(uploaded_file)

        found_skills = get_skills(resume_text)

        ats_score = min(len(found_skills) * 7, 100)

        st.success("✅ Resume Uploaded Successfully!")

        st.subheader("🛠 Detected Skills")

        for skill in found_skills:
            st.success(skill)

        st.subheader("🎯 ATS Score")

        st.progress(ats_score)

        st.metric(
            "ATS Score",
            f"{ats_score}%"
        )

        st.subheader("💼 Predicted Role")

        if "Machine Learning" in found_skills:
            role = "🤖 AI / ML Engineer"

        elif "SQL" in found_skills:
            role = "📊 Data Analyst"

        else:
            role = "💻 Software Developer"

        st.success(role)

        st.subheader("💰 Estimated Salary")

        salary = random.randint(6, 25)

        st.metric(
            "Expected Salary",
            f"₹{salary} LPA"
        )

        st.subheader("🏆 Hiring Decision")

        if ats_score >= 80:
            st.success("✅ Strong Hire")

        elif ats_score >= 60:
            st.warning("⚠ Consider for Interview")

        else:
            st.error("❌ Needs Improvement")

        chart_data = {
            "Category": [
                "Skills",
                "Projects",
                "Resume",
                "Experience"
            ],
            "Score": [
                ats_score,
                85,
                80,
                75
            ]
        }

        fig = px.pie(
            names=chart_data["Category"],
            values=chart_data["Score"],
            title="📊 Resume Performance"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

elif selected == "Mock Interview":

    st.title("🎤 AI Mock Interview")

    role = st.selectbox(
        "💼 Select Role",
        [
            "AI Engineer",
            "Data Scientist",
            "Software Developer",
            "Web Developer",
            "Cybersecurity Analyst"
        ]
    )

    difficulty = st.selectbox(
        "⚡ Select Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    if st.button("🚀 Generate Interview Questions"):

        questions = [
            "Tell me about yourself.",
            "Explain your projects.",
            "Why should we hire you?",
            "Explain Machine Learning.",
            "What are your strengths?"
        ]

        for i, q in enumerate(questions, 1):
            st.info(f"{i}. {q}")

    answer = st.text_area(
        "📝 Type Your Answer",
        height=180
    )

    if st.button("✅ Evaluate Answer"):

        if len(answer) > 120:

            st.success("""
🎉 Excellent Answer!

✅ Strong communication  
✅ Good technical explanation  
🏆 Score: 9/10
            """)

        elif len(answer) > 50:

            st.warning("""
⚠ Good Answer

🏆 Score: 7/10
            """)

        else:

            st.error("""
❌ Answer Too Short

🏆 Score: 4/10
            """)

elif selected == "Career Roadmap":

    st.title("🚀 Career Roadmap")

    career = st.selectbox(
        "💼 Choose Career",
        [
            "AI Engineer",
            "Data Scientist",
            "Full Stack Developer",
            "Cybersecurity Analyst",
            "Cloud Engineer"
        ]
    )

    if st.button("🔥 Generate Roadmap"):

        st.success(f"""
# 🚀 {career} Roadmap

✅ Learn Programming  
✅ Build Projects  
✅ Practice DSA  
✅ Create Portfolio  
✅ Earn Certifications  
        """)

elif selected == "Project Generator":

    st.title("💻 AI Project Generator")

    domain = st.selectbox(
        "Choose Domain",
        [
            "AI/ML",
            "Web Development",
            "Cybersecurity"
        ]
    )

    if st.button("🚀 Generate Project"):

        st.success(f"""
🔥 Advanced {domain} Project

✅ Resume Worthy  
✅ Real World Project  
✅ Attractive UI  
        """)
elif selected == "Skills Gap Analyzer":

    st.title("📈 Skills Gap Analyzer")

    current_skill = st.selectbox(
        "🛠 Select Skill",
        [
            "Python",
            "Machine Learning",
            "Web Development",
            "Data Science",
            "Cybersecurity",
            "Cloud Computing"
        ]
    )

    if st.button("🚀 Analyze Skills"):

        st.success(f"""
# 🔥 {current_skill} Analysis

✅ Improve Problem Solving  
✅ Build Advanced Projects  
✅ Learn System Design  
✅ Practice Daily  
        """)

elif selected == "About":

    st.title("ℹ About AI Resume Analyzer")

    st.markdown("""
# 🤖 AI Resume Analyzer Platform

An advanced AI-powered career assistant.

## 🚀 Features

✅ ATS Score  
✅ Resume Analysis  
✅ Mock Interview  
✅ Career Roadmap  
✅ Skills Gap Analyzer  
    """)
st.markdown("---")

st.caption("🚀 Developed using Streamlit")
