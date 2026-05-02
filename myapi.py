# APPROACH:
# Sentiment → VADER (rule-based, fast)
# Emotion → NRCLex (lexicon-based)
# NER → spaCy (pretrained NLP pipeline)

# TC:
# All operations ~ O(N) where N = length of text

# SC:
# O(N) for storing tokens and outputs

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spacy


class API:

    def __init__(self):
        # Initialize models once
        self.sentiment_model = SentimentIntensityAnalyzer()
        self.nlp = spacy.load("en_core_web_sm")

    # ---------------- SENTIMENT ----------------
    def sentiment_analysis(self, text):

        scores = self.sentiment_model.polarity_scores(text)

        result = (
            f"Positive : {scores['pos']}\n"
            f"Neutral  : {scores['neu']}\n"
            f"Negative : {scores['neg']}\n"
            f"Compound : {scores['compound']}"
        )

        return result

    # ---------------- EMOTION ----------------
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

    def emotion_analysis(self, text):

        analyzer = SentimentIntensityAnalyzer()
        score = analyzer.polarity_scores(text)

        print("SENTIMENT SCORE:", score)

        # simple interpretation
        if score["compound"] >= 0.5:
            return "Positive 😊"
        elif score["compound"] <= -0.5:
            return "Negative 😡"
        else:
            return "Neutral 😐"
    # ---------------- NER ----------------
    def ner(self, text):

        doc = self.nlp(text)

        if not doc.ents:
            return "No entities found"

        result = ""
        for ent in doc.ents:
            result += f"Name : {ent.text} | Category : {ent.label_}\n\n"

        return result