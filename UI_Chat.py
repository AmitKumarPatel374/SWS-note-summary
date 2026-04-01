import streamlit as st
import os
from dotenv import load_dotenv
from chatbot import summarize_notes   # ✅ import from backend

# -------------------- CONFIG --------------------
st.set_page_config(page_title="✨ Notes Summarizer", page_icon="🧠", layout="centered")

# -------------------- STYLING --------------------
st.markdown("""
<style>
.big-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    color: #4CAF50;
}
.sub-text {
    text-align: center;
    color: gray;
    margin-bottom: 20px;
}
.stTextArea textarea {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- LOAD ENV --------------------
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# -------------------- HEADER --------------------
st.markdown('<div class="big-title">🧠 Smart Notes Summarizer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Turn your messy notes into exam-ready gold 🚀</div>', unsafe_allow_html=True)

# -------------------- INPUT --------------------
notes = st.text_area(
    "📘 Paste your notes here:",
    height=250,
    placeholder="Type or paste your notes..."
)

# -------------------- BUTTON --------------------
if st.button("✨ Generate Summary"):
    if not API_KEY:
        st.error("❌ API Key not found. Please check your .env file.")
    elif notes.strip() == "":
        st.warning("⚠️ Please enter some notes first.")
    else:
        with st.spinner("⏳ Summarizing your notes..."):
            try:
                result = summarize_notes(notes)

                st.success("✅ Summary Generated Successfully!")
                st.balloons()

                st.markdown("---")
                st.markdown("### 📄 Your Summary")
                st.write(result)

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown("<center>Made with ❤️ using Streamlit</center>", unsafe_allow_html=True)