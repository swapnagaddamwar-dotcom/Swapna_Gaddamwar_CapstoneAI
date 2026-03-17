# Medical Prior-Auth AI Assistant
This capstone project automates the comparison of clinical notes against insurance requirements using local LLMs.

## 🚀 Setup Instructions
1. **Install Ollama:** Download from [ollama.com](https://ollama.com).
2. **Pull Model:** Run `ollama pull mistral` in your terminal.
3. **Install Python Libraries:** `pip install -r requirements.txt`.
4. **Run App:** `streamlit run app.py`.

## 🛠️ Technical Stack
- **LLM:** Mistral-7B (via Ollama)
- **UI:** Streamlit
- **Processing:** pypdf for clinical note extraction

## 📝 Features
- **Privacy-First:** Processes data locally on your machine.
- **Evidence-Based:** Quotes clinical notes to justify authorization status.
