# 📄 Resume Whisperer – AI Resume Analyzer

An intelligent resume analysis tool powered by Google's Gemini AI that helps job seekers optimize their resumes for specific job descriptions. Get professional insights, improvement suggestions, and tailored resume summaries in seconds.

## ✨ Features

- **📋 Resume Analysis**: Upload PDF resumes and get comprehensive analysis
- **🎯 Job Matching**: Compare your resume against specific job descriptions
- **🤖 AI-Powered Insights**: Leverages Google Gemini 2.0 Flash for intelligent analysis
- **📊 Match Scoring**: Get a quantified job match score out of 100
- **📝 Professional Summary**: AI-generated professional summary of your resume
- **🔧 Improvement Suggestions**: Receive 5 targeted improvements to enhance job relevance
- **✍️ Resume Rewriting**: Get a rewritten resume summary tailored to the job

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google API Key for Gemini AI

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SaiShankar93/Resume-Review-AI
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv env
   # On Windows
   .\env\Scripts\activate
   # On macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```
   
   Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

5. **Run the application**
   ```bash
   streamlit run streamlit.py
   ```

## 🛠️ Dependencies

- **streamlit** - Web app framework
- **PyMuPDF (fitz)** - PDF text extraction
- **langchain** - LLM application framework
- **langchain-google-genai** - Google Gemini integration
- **python-dotenv** - Environment variable management

## 📱 How to Use

1. **Launch the app** - Run `streamlit run streamlit.py` and open the provided URL
2. **Upload Resume** - Upload your resume in PDF format
3. **Add Job Description** - Paste the job description you're targeting
4. **Analyze** - Click the "Analyze" button to get AI insights
5. **Review Results** - Get your analysis including:
   - Professional resume summary
   - 5 improvement suggestions
   - Job match score (0-100)
   - Rewritten resume summary

## 🏗️ Project Structure

```
LLMs/
├── .env                           # Environment variables (not tracked)
├── .gitignore                     # Git ignore rules
├── README.md                      # Project documentation
├── streamlit.py                   # Main Streamlit application
├── resume_review.py               # Additional resume review functionality
├── restaurant_name_pred.ipynb    # Jupyter notebook (separate project)
└── env/                           # Virtual environment (not tracked)
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Your Google Gemini AI API key | Yes |

### Model Configuration

The app uses Google Gemini 2.0 Flash with the following settings:
- **Temperature**: 0.5 (balanced creativity/consistency)
- **Model**: gemini-2.0-flash

## 🎯 Use Cases

- **Job Seekers** - Optimize resumes for specific positions
- **Career Coaches** - Provide data-driven resume feedback
- **HR Professionals** - Understand how resumes match job requirements
- **Students** - Learn resume best practices and improvement areas

## 🔒 Privacy & Security

- Resumes are processed in memory and not stored permanently
- API communications are encrypted
- Environment variables keep API keys secure
- No personal data is logged or retained

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

### Common Issues

**Error: "GOOGLE_API_KEY environment variable is not set"**
- Ensure your `.env` file contains the correct API key
- Verify the API key is valid and active

**PDF Upload Issues**
- Ensure the file is a valid PDF
- Check file size (very large PDFs may take longer to process)

**Module Import Errors**
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Ensure you're using the correct virtual environment

## 🔮 Future Enhancements

- [ ] Support for multiple file formats (DOCX, TXT)
- [ ] Batch resume processing
- [ ] Resume template suggestions
- [ ] Industry-specific analysis
- [ ] ATS (Applicant Tracking System) compatibility scoring
- [ ] Resume formatting recommendations

## 📞 Support

For support, questions, or feature requests, please open an issue in the GitHub repository.

---

**Made with ❤️ and AI** - Helping job seekers land their dream jobs, one resume at a time.
