import streamlit as st
import pdfplumber
import google.generativeai as genai

# Configure Streamlit page
st.set_page_config(page_title="Resume Feedback AI (Gemini)", layout="centered")
st.title("📄 Resume Feedback Agent using Google Gemini")

# Input Gemini API key
gemini_api_key = st.text_input("🔑 Enter your Gemini API Key:", type="password")

# Upload resume
uploaded_file = st.file_uploader("📁 Upload your resume (PDF)", type="pdf")

# Optional job description
job_description = st.text_area("🧾 Paste job description (optional)", height=150)

resume_text = ""

# Extract text from uploaded PDF
if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            resume_text += page.extract_text()

    st.subheader("📄 Extracted Resume Text")
    st.text_area("Resume Preview", resume_text, height=250)

# When API key and resume are available
if uploaded_file and gemini_api_key:
    if st.button("🧠 Get Feedback"):
        with st.spinner("Analyzing with Gemini..."):

            try:
                # Configure Gemini API
                genai.configure(api_key=gemini_api_key)

                # Use supported model for content generation
                model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")  # or gemini-1.5-pro

                # Prompt to Gemini
                prompt = f"""
You are an expert resume reviewer.
Please review the resume below and provide detailed feedback on:
- Formatting
- Grammar
- Relevance of experience and skills
- Strength of bullet points
- Suggestions for improvement

Resume:
\"\"\"
{resume_text}
\"\"\"
"""

                if job_description.strip():
                    prompt += f"""

Also compare it to this job description:
\"\"\"
{job_description}
\"\"\"
Offer specific suggestions to improve the resume for this role.
"""

                # Generate content
                response = model.generate_content(prompt)

                # Display response
                st.subheader("✅ Gemini Feedback")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"❌ Gemini API Error: {str(e)}")

else:
    if not gemini_api_key:
        st.info("Please enter your Gemini API key.")
