# 📄 Resume Feedback AI (Google Gemini + Streamlit)

A simple **AI-powered Resume Feedback Agent** built with **Streamlit** and **Google Gemini API**.  
It extracts text from resumes (PDF format), analyzes them, and provides **detailed feedback** on formatting, grammar, skills relevance, and bullet point strength.  
Optionally, you can also paste a **job description** to get tailored suggestions on how to improve your resume for that specific role.  

---

## 🚀 Features
- Upload resume in **PDF** format  
- Extracts text using **pdfplumber**  
- Uses **Google Gemini AI** to analyze the resume  
- Provides feedback on:
  - ✅ Formatting  
  - ✅ Grammar & readability  
  - ✅ Relevance of skills/experience  
  - ✅ Strength of bullet points  
- Job description matching for **role-specific feedback**  
- Clean & interactive UI with **Streamlit**  

---

## 🛠️ Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/resumeFeedback-ai.git
   cd resumeFeedback-ai
   ```

2. (Optional) Create & activate virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```
   or if `streamlit` is not recognized:
   ```bash
   python -m streamlit run app.py
   ```

---

## 📦 Requirements

Create a `requirements.txt` file with:
```
streamlit
pdfplumber
google-generativeai
```

---

## 🔑 API Key Setup
- You need a **Google Gemini API key** to use this app.  
- Get it from [Google AI Studio](https://aistudio.google.com/app/apikey).  
- Enter the key in the app when prompted.  

---

## 📸 Demo
*(Add screenshots or GIF of your app running here)*  

---

## 📌 Future Improvements
- Add resume ATS score checker  
- Export feedback as PDF  
- Support for DOCX resumes  
- Advanced comparison with multiple job postings  

---

## 👨‍💻 Author
**Shubham Modi**  
💼 Engineering Student | 💻 Web Developer | 🤖 AI Enthusiast  
