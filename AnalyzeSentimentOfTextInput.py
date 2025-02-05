from textblob import TextBlob

import pandas as pd 
import numpy as np

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    
    text = input("Enter text: ")
    sentiment = analyze_sentiment(text)
    print(f"Sentiment: {sentiment}")


