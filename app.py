import streamlit as st
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }

    h1, h2, h3 {
        color: #00ADB5;
    }

    .stButton>button {
        background-color: #00ADB5;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 15em;
    }

    </style>
""", unsafe_allow_html=True)

# Page Config
st.set_page_config(
    page_title="Anshika Portfolio",
    page_icon="💻",
    layout="wide"
)

# Header
st.title("Anshika Saxena")
st.subheader("CSE-AI Student | Python & AI Enthusiast")
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("assets/profile.jpg", width=250)
st.write("""
Welcome to my portfolio website.
I am a B.Tech CSE-AI student passionate about
Artificial Intelligence, Machine Learning,
Python Development, and solving real-world problems.
""")

# About Section
st.header("About Me")

st.write("""
I am currently pursuing B.Tech in Computer Science Engineering
with specialization in Artificial Intelligence.
I enjoy building AI-based applications and learning new technologies.
""")

# Skills Section
st.header("Skills")

skills = [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "DSA",
    "DBMS",
    "C Programming",
    "Streamlit",
    "Git & GitHub"
]

cols = st.columns(4)

for index, skill in enumerate(skills):
    cols[index % 4].success(skill)

# Projects Section
st.header("Projects")

projects = {
    "AI Study Planner":
    "An AI-powered study planner that helps students organize subjects, schedules, and study goals efficiently.",

    "AI Resume Analyzer":
    "A Streamlit-based AI resume analyzer that evaluates resumes, extracts skills, and provides insights for improvement."
}
col1, col2 = st.columns(2)

with col1:
    st.container(border=True)
    st.subheader("📚 AI Study Planner")
    st.write(
        "An AI-powered study planner that helps students organize subjects, schedules, and study goals efficiently."
    )

with col2:
    st.container(border=True)
    st.subheader("📄 AI Resume Analyzer")
    st.write(
        "A Streamlit-based AI resume analyzer that evaluates resumes, extracts skills, and provides insights for improvement."
    )
# Resume Section
st.header("Resume")

with open("assets/resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="📄 Download Resume",
    data=PDFbyte,
    file_name="Anshika_Resume.pdf",
    mime='application/octet-stream'
)

# Contact Section
st.header("Contact")

st.write("📧 Email: anshi.saxena2004@gmail.com")
st.write("💼 LinkedIn: https://www.linkedin.com/in/anshika-saxena-14502b311?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")
st.write("🐙 GitHub: https://github.com/anshi544")

# Footer
st.write("---")
st.caption("Made with ❤️ using Streamlit")