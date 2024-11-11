

# Kalvi Chat - AI Model for Teaching Tamil Content

**Kalvi Chat** is an AI-powered chatbot designed to teach Tamil content using the **Gemini API** and **Python**. The chatbot is built using **Streamlit** to provide an interactive, web-based interface where users can learn Tamil through conversations, lessons, translations, and explanations.

## Features

- **AI-Powered Conversations**: Utilizes the Gemini API to generate contextual responses and educational content.
- **Tamil Language Support**: Provides lessons, translations, and explanations in Tamil.
- **Interactive Learning**: Engage with the bot to ask questions and learn Tamil in a conversational manner.
- **Streamlit Web Interface**: Built using Streamlit to create an interactive and easy-to-use web app.

- 
## Technologies Used

- **Gemini API**: The core AI service for generating responses and content. Users need to purchase access to the Gemini API to use it.
- **Python**: The backend programming language used to handle user inputs and interact with the Gemini API.
- **Streamlit**: A Python framework to build the web interface for the chatbot.
- **Natural Language Processing (NLP)**: For processing and understanding user input in Tamil.

## Getting Started

### Prerequisites

Before using Kalvi Chat, ensure you have the following:

- **Python 3.8+** installed on your machine.
- A **Gemini API** key, which you can obtain by purchasing access to the Gemini API.

### Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd kalvi-chat
   ```

2. **Install Dependencies**
   Install the required Python libraries using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Gemini API Key**
   - Purchase the Gemini API from [Gemini API website](https://geminiapi.com) (or the respective platform).
   - After obtaining the API key, add it to your environment variables:
   ```bash
   export GEMINI_API_KEY="your_api_key"
   ```
   Alternatively, you can store the API key in a configuration file (e.g., `config.py`) and load it into your project.

4. **Run the Streamlit Application**
   After installing dependencies and setting up the API key, you can launch the app using the following command:
   ```bash
   streamlit run app.py
   ```

   This will start the Streamlit server and open the web interface in your browser.
