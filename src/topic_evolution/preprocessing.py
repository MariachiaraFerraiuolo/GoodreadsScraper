import re
import nltk 
from nltk.corpus import stopwords
import pandas as pd
import spacy
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
#from src.scraper.scraper import GoodreadsScraper

pd.set_option('display.max_rows', None)

#nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
nlp = spacy.load("en_core_web_sm")

class Preprocess():
    def __init__(self, file_path):
        self.file_path = file_path
        self.open_file()
    def open_file(self):
        if self.file_path.endswith('.csv'):
            self.df = pd.read_csv(self.file_path, sep='|', encoding='utf-8')
        else:
            self.df = pd.read_excel(self.file_path)

    def text_cleaning(self, text):
        text = text.lower()
        text = re.sub(r'[^a-z\s]', '', text)
        text = ' '.join(word for word in text.split() if word not in stop_words)
        return text

    def lemmatize_text(self, text): 
        doc = nlp(text)
        return ' '.join(token.lemma_ for token in doc if token.is_alpha and not token.is_stop)

    def preprocessing(self):
        self.df['plot_cleaned'] = self.df['plot'].fillna('').astype(str).apply(self.text_cleaning)
        self.df['plot_lemmatized'] = self.df['plot_cleaned'].apply(self.lemmatize_text)
        return self.df

    def save(self, output_path):
        self.df.to_excel(output_path, index=False) 

file_path = r'output\cleaned_Goodreads_data.xlsx'
output_path = r'output\lemmatized_data.xlsx'
preprocessor = Preprocess(file_path)
df_processed = preprocessor.preprocessing()
preprocessor.save(output_path)

