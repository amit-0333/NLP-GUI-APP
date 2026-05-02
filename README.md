# NLP-GUI-APP

# NLP GUI Application

A Python-based Natural Language Processing (NLP) desktop application with a graphical user interface (Tkinter). The project performs sentiment analysis and named entity recognition on user input text in real time.

## Features
- Sentiment Analysis using VADER
- Named Entity Recognition using spaCy
- Simple GUI for user input and output display
- JSON-based data storage support

## Tech Stack
Python, Tkinter, VADER Sentiment, spaCy, JSON

## Project Structure
nlp-gui-app/
├── app.py
├── myapi.py
├── mydb.py
├── db.json
├── requirements.txt
├── README.md

## How to Run
1. Clone the repository  
   git clone https://github.com/amit-0333/NLP-GUI-APP

2. Install dependencies  
   pip install -r requirements.txt  

3. Download spaCy model  
   python -m spacy download en_core_web_sm  

4. Run the app  
   python app.py  

## Example
Input: Elon Musk is very happy about Tesla results  
Output:  
Sentiment → Positive 😊  
Entities → Elon Musk (PERSON), Tesla (ORG)

## Future Improvements
- Add emotion detection model
- Improve GUI design
- Add database history tracking
- Convert into web-based app

## Author
AMIT KUMAR
Python NLP GUI Project
