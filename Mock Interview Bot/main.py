import streamlit as st
from groq_handler import ask_groq
from report_generator import generate_pdf
import base64

st.set_page_config(page_title="🧑‍💼 Mock Interview Bot", layout="centered")
st.title("🧑‍💻 AI Mock Interview Bot")

# Session init
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
    st.session_state.answers = []
    st.session_state.feedback = []

interview_type = st.selectbox("📋 Choose interview type", ["Technical", "HR", "Behavioral"])

questions = {
    "Technical": [
        "Explain the concept of OOP with examples.",
        "What happens when you type a URL in your browser?",
        "How do you handle performance issues in backend services?"
    ],
    "HR": [
        "Tell me about yourself.",
        "Why should we hire you?",
        "What are your biggest strengths and weaknesses?"
    ],
    "Behavioral": [
        "Describe a time you faced a challenge at work.",
        "How do you handle conflict in a team?",
        "Tell me about a time you took initiative."
    ]
}

current_qs = questions[interview_type]

if st.session_state.q_index < len(current_qs):
    st.markdown(f"### ❓ {current_qs[st.session_state.q_index]}")
    answer = st.text_area("💬 Your Answer", key=f"answer_{st.session_state.q_index}")
    
    if st.button("Submit Answer"):
        prompt = f"""
        Interview Type: {interview_type}
        Question: {current_qs[st.session_state.q_index]}
        Candidate Answer: {answer}

        Evaluate the answer and give structured feedback:
        - Clarity (1-10):
        - Confidence (1-10):
        - Technical Accuracy (1-10):
        - Communication:
        - Suggestions for improvement:
        - Overall Score (1-10):
        """
        feedback = ask_groq(prompt)
        st.session_state.answers.append(answer)
        st.session_state.feedback.append(feedback)
        st.session_state.q_index += 1
        st.experimental_rerun()
else:
    st.markdown("### 🎓 Interview Complete! Here's your feedback:")
    full_report = ""

    for i, fb in enumerate(st.session_state.feedback):
        st.markdown(f"#### Q{i+1}: {current_qs[i]}")
        st.markdown(fb)
        full_report += f"Q{i+1}: {current_qs[i]}\n{fb}\n\n"

    # PDF Download
    pdf_base64 = generate_pdf(full_report)
    st.markdown(f'<a href="data:application/pdf;base64,{pdf_base64}" download="MockInterviewFeedback.pdf">📄 Download Feedback as PDF</a>', unsafe_allow_html=True)

    if st.button("🔄 Restart Interview"):
        st.session_state.q_index = 0
        st.session_state.answers.clear()
        st.session_state.feedback.clear()
        st.experimental_rerun()
