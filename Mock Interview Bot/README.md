# 🧑‍💻 Mock Interview Bot

An AI-powered mock interview application built with Streamlit that provides real-time feedback on interview performance.

## Features

- **Multiple Interview Types**: Technical, HR, and Behavioral interviews
- **AI Feedback**: Structured evaluation using Groq's LLaMA model
- **PDF Reports**: Download detailed feedback reports
- **Interactive UI**: Clean, user-friendly Streamlit interface

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install streamlit fpdf2 requests python-dotenv
   ```
3. Create a `.env` file with your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

Run the application:
```bash
streamlit run main.py
```

## File Structure

- `main.py` - Main Streamlit application with UI and interview logic
- `groq_handler.py` - Handles API communication with Groq LLaMA model
- `report_generator.py` - Generates PDF reports from interview feedback

## How It Works

1. Select interview type (Technical/HR/Behavioral)
2. Answer predefined questions
3. Receive AI-generated feedback with scores for clarity, confidence, and technical accuracy
4. Download complete feedback as PDF report

## Requirements

- Python 3.7+
- Groq API key
- Internet connection for AI feedback
