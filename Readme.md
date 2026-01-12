# 📱 SMS Spam Classifier

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/your-username/sms-spam-classifier/main/app.py)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful and user-friendly SMS Spam Classifier built with Streamlit and machine learning. This application helps you identify whether an SMS message is spam or legitimate (ham) in real-time.

## 🚀 Features

- **Real-time Classification**: Instantly classify SMS messages as spam or ham.
- **Advanced Preprocessing**: Utilizes NLTK for text preprocessing including tokenization, stopword removal, and stemming.
- **Machine Learning Powered**: Employs TF-IDF vectorization and a trained model for accurate predictions.
- **Simple UI**: Clean and intuitive Streamlit interface for easy interaction.
- **Fast and Efficient**: Lightweight and optimized for quick predictions.

## 📋 Requirements

- Python 3.8 or higher
- Streamlit
- NLTK
- scikit-learn (for the model and vectorizer)

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/sms-spam-classifier.git
   cd sms-spam-classifier
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data:**
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

## 🎯 Usage

1. **Run the application:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to the provided local URL (usually `http://localhost:8501`).

3. **Enter an SMS message** in the text input field.

4. **Click "Predict"** to see if the message is classified as SPAM or HAM.

## 🔍 How It Works

1. **Text Preprocessing:**
   - Convert to lowercase
   - Tokenize the text
   - Remove non-alphanumeric characters
   - Remove stopwords and punctuation
   - Apply stemming using Porter Stemmer

2. **Vectorization:**
   - Transform the preprocessed text using TF-IDF vectorizer

3. **Prediction:**
   - Feed the vectorized text into the trained machine learning model
   - Output: SPAM (1) or HAM (0)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- NLTK for natural language processing
- scikit-learn for machine learning utilities
- Streamlit for the web app framework

---

Made with ❤️ by MANISH  JAISWAR 

