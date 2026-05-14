# 🧠 NLP GUI Application

> A Python-based desktop application that performs **Sentiment Analysis** and **Named Entity Recognition (NER)** on real-time user input — built with Tkinter, VADER & spaCy.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-spaCy%20%7C%20VADER-09A3D5?style=for-the-badge)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange?style=for-the-badge)
![JSON](https://img.shields.io/badge/Storage-JSON-lightgrey?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

---

## 📌 About

This is a **real-world NLP desktop app** built entirely from scratch using Python.  
It takes raw text input from the user and instantly returns:
- 🎭 The **sentiment** (Positive / Negative / Neutral)
- 🏷️ The **named entities** (People, Organizations, Locations, etc.)

All results are stored locally using a **JSON-based database** for history tracking.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎭 Sentiment Analysis | Detects Positive / Negative / Neutral sentiment using **VADER** |
| 🏷️ Named Entity Recognition | Identifies People, Organizations, Locations using **spaCy** |
| 🖥️ Desktop GUI | Clean, interactive interface built with **Tkinter** |
| 💾 JSON Storage | Saves user input & results locally using **JSON database** |
| ⚡ Real-Time Processing | Instant analysis on text submission |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python | Core programming language |
| 🖥️ Tkinter | Desktop GUI framework |
| 🎭 VADER Sentiment | Rule-based sentiment analysis |
| 🏷️ spaCy | Industrial-strength NLP & NER |
| 📄 JSON | Lightweight local data storage |

---

## 📁 Project Structure

```bash
NLP-GUI-APP/
│
├── 📄 app.py              # Main application — GUI + logic
├── 📄 myapi.py            # NLP processing — VADER & spaCy
├── 📄 mydb.py             # JSON database read/write handler
├── 📄 db.json             # Local storage for results history
├── 📄 requirements.txt    # All dependencies
└── 📄 README.md
```

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/amit-0333/NLP-GUI-APP.git

# 2. Navigate into the folder
cd NLP-GUI-APP

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Download the spaCy English model
python -m spacy download en_core_web_sm

# 5. Run the app
python app.py
```

---

## 🎯 Example

**Input:**
```
Elon Musk is very happy about Tesla's latest results
```

**Output:**
```
Sentiment  →  Positive 😊
Entities   →  Elon Musk (PERSON),  Tesla (ORG)
```

---

## 🔮 Future Improvements

- [ ] Add emotion detection model (joy, anger, fear, surprise)
- [ ] Improve GUI design with modern styling
- [ ] Add full database history view in the app
- [ ] Convert into a web-based app using Flask or Streamlit
- [ ] Support multiple languages

---

## 👨‍💻 Author

**Amit Kumar**  
[![GitHub](https://img.shields.io/badge/GitHub-amit--0333-181717?style=flat&logo=github)](https://github.com/amit-0333)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Amit%20Kumar-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/amit-kumar-a62a3640a/)
[![Kaggle](https://img.shields.io/badge/Kaggle-amitkumar038975-20BEFF?style=flat&logo=kaggle)](https://www.kaggle.com/amitkumar038975)

---

⭐ **Star this repo if you found it useful!**
