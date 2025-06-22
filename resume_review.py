import streamlit as st
import fitz
import os
from dotenv import load_dotenv

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI



load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.5)

# Prompt template
prompt = PromptTemplate(
    input_variables=["resume_text", "job_description"],
    template="""
You are a professional resume coach.

Given the resume and job description below:
- Give a professional summary of the resume.
- List 5 improvements to make it more job-relevant.
- Calculate a job match score out of 100.
- Rewrite the resume summary to better fit the job.

Resume:
{resume_text}

Job Description:
{job_description}
"""
)

# Create LangChain pipeline
chain = LLMChain(llm=llm, prompt=prompt)

# Streamlit UI
st.title("📄 Resume Whisperer – AI Resume Analyzer")

resume_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste the Job Description")

if st.button("Analyze", key="analyze_button"):
    if resume_file and job_description:
        with st.spinner("Analyzing your resume with Gemini..."):
            # Extract text from PDF
            doc = fitz.open(stream=resume_file.read(), filetype="pdf")
            resume_text = ""
            for page in doc:
                resume_text += page.get_text()

            # Run through LLM
            response = chain.run({
                "resume_text": resume_text,
                "job_description": job_description
            })

        st.subheader("🔍 AI Analysis")
        st.markdown(response)
    else:
        st.warning("Please upload a resume and paste a job description.")
