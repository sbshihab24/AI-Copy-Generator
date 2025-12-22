# 🤖 AdPortal - AI Copy Generator

A powerful, Streamlit-powered AI application designed to generate high-conversion ad copy variations using Large Language Models (LLMs). This tool helps digital marketers and agency owners optimize their campaigns by providing creative, tone-specific headlines, primary text, and CTAs in seconds.

## ✨ Key Features

* **Multi-Tone Generation**: Choose from Professional, Friendly, Persuasive, Bold, or Minimalist tones.
* **Targeted Content**: Generates copy specific to your product, audience, and unique benefits.
* **Structured Output**: Specialized logic to ensure "Primary Text" remains concise (one paragraph, 2-3 sentences).
* **Custom UI**: A modern, centered dashboard built with a branded AdPortal interface.
* **Session Management**: Keeps track of your generated variations and previous inputs for easy regeneration.

## 🛠️ Project Structure

```text
AI_COPY_GENERATOR/
├── .streamlit/
│   ├── config.toml       # Streamlit theme configuration
│   └── style.css         # Custom UI styling
├── backend/
│   └── ai_service.py     # LLM integration logic (Gemini/OpenAI)
├── streamlit_app/
│   └── ui_components.py  # Reusable UI cards and headers
├── app.py                # Main application entry point
├── .env                  # API keys (ignored by git)
├── .gitignore            # Security rules for GitHub
└── requirements.txt      # Python dependencies
🚀 Getting Started
Follow these steps to set up the project locally on your machine.

1. Clone the repository
First, clone the repository and navigate into the project folder:

Bash

git clone [https://github.com/sbshihab24/AI-Copy-Generator.git](https://github.com/sbshihab24/AI-Copy-Generator.git)
cd AI-Copy-Generator
2. Set up the environment
Create a virtual environment to keep your dependencies organized, then activate it and install the required packages:

Bash

# Create the virtual environment
python -m venv venv

# Activate the environment
# On Windows:
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
3. Add your API Key
The app requires an API key to communicate with the AI model. Create a .env file in the root directory and add your key:

Plaintext

GOOGLE_API_KEY=your_gemini_api_key_here
4. Run the App
Once everything is set up, you can launch the Streamlit application with the following command:

Bash

streamlit run app.py
📝 Usage
Input Details: Enter your Product/Service name, Target Audience, and Key Benefits.

Select Style: Choose the desired Tone and Copy Type (Headlines, CTAs, etc.).

Generate: Click the ✨ Generate Copy button.

Refine: Use the 🔄 Regenerate button to get new variations based on the same inputs.

⚖️ License
Distributed under the MIT License. See LICENSE for more information.

Developed by Mehedi Hasan Shihab


Would you like me to generate the **requirements.txt** content so that the installation s
