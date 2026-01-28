# 🤖 AdPortal - AI Copy Generator

A powerful, Streamlit-powered AI application designed to generate high-conversion ad copy variations using Large Language Models (LLMs). This tool helps digital marketers and agency owners optimize their campaigns by providing creative, tone-specific headlines, primary text, and CTAs in seconds.

---

## ✨ Key Features

- **Multi-Tone Generation** - Choose from Professional, Friendly, Persuasive, Bold, or Minimalist tones
- **Targeted Content** - Generates copy specific to your product, audience, and unique benefits
- **Structured Output** - Specialized logic to ensure "Primary Text" remains concise (one paragraph, 2-3 sentences)
- **Custom UI** - A modern, centered dashboard built with a branded AdPortal interface
- **Session Management** - Keeps track of your generated variations and previous inputs for easy regeneration

---

## 🛠️ Project Structure

```
AI_COPY_GENERATOR/
├── .streamlit/
│   ├── config.toml           # Streamlit theme configuration
│   └── style.css             # Custom UI styling
├── backend/
│   └── ai_service.py         # LLM integration logic (Gemini/OpenAI)
├── streamlit_app/
│   └── ui_components.py      # Reusable UI cards and headers
├── app.py                    # Main application entry point
├── .env                      # API keys (ignored by git)
├── .gitignore                # Security rules for GitHub
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 🚀 Getting Started

Follow these steps to set up the project locally on your machine.

### 1. Clone the Repository

First, clone the repository and navigate into the project folder:

```bash
git clone https://github.com/sbshihab24/AI-Copy-Generator.git
cd AI-Copy-Generator
```

### 2. Set Up the Environment

Create a virtual environment to keep your dependencies organized, then activate it and install the required packages:

```bash
# Create the virtual environment
python -m venv venv

# Activate the environment
# On Windows:
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Add Your API Key

The app requires an API key to communicate with the AI model. Create a `.env` file in the root directory and add your key:

```plaintext
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 4. Run the App

Once everything is set up, you can launch the Streamlit application with the following command:

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

---

## 📝 Usage

1. **Input Details** - Enter your Product/Service name, Target Audience, and Key Benefits
2. **Select Style** - Choose the desired Tone and Copy Type (Headlines, CTAs, etc.)
3. **Generate** - Click the ✨ **Generate Copy** button
4. **Refine** - Use the 🔄 **Regenerate** button to get new variations based on the same inputs

---

## 📋 Requirements

- Python 3.8+
- Streamlit
- Google Generative AI API (or OpenAI API)
- Other dependencies listed in `requirements.txt`

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or suggestions.

---

## ⚖️ License

Distributed under the MIT License. See `LICENSE` file for more information.

---

## 👨‍💻 Author

**Mehedi Hasan Shihab**

---

**Last Updated:** December 2025



