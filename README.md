# AI Interview Chatbot

## Overview
The AI Interview Chatbot is a web application built using Streamlit and OpenAI's GPT API. It allows users to submit their details and engage in an interactive AI-powered interview simulation. The chatbot provides dynamic responses to candidate inputs, making it a useful tool for interview preparation.

## Features
- **Candidate Form Submission**: Users enter their name, email, and resume before starting the interview.
- **AI-Powered Interview**: The chatbot interacts with the candidate in real time using OpenAI's API.
- **Session Logging**: Tracks user interactions and maintains session state.
- **Streamlit UI**: Simple and intuitive interface for seamless user experience.

## Technologies Used
- **Python**: Backend logic and API calls
- **Streamlit**: Web interface
- **OpenAI API**: AI-powered interview responses

## Installation
### Prerequisites
- Python 3.8+
- OpenAI API Key
- Required dependencies in `requirements.txt`

### Steps to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/Abhijit1102/interview_ai.git
   cd interview_ai
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the OpenAI API key:
   ```bash
   export OPENAI_API_KEY='your-api-key'
   ```
   (For Windows: `set OPENAI_API_KEY=your-api-key`)
4. Run the Streamlit app:
   ```bash
   streamlit run src/app.py
   ```
5. Open the browser and navigate to the displayed URL.

## Usage
1. Enter your name, email, and upload your resume.
2. Click on the "Start Interview" button.
3. Engage with the AI interviewer by typing responses.
4. The AI will guide you through the interview dynamically.

## Future Improvements
- Resume parsing and AI-based question customization.
- User authentication and saved interview sessions.
- Integration with other AI models for enhanced feedback.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to fork the repository and submit pull requests for improvements.

## Contact
For any queries or suggestions, reach out to `abhijitrajkumar2@gmail.com`.

