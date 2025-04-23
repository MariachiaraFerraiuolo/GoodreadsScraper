import re
import nltk 
from nltk.corpus import stopwords
import pandas as pd


#nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def open_file(file1:str):
    file1 = pd.read_excel(file1)
    return file1

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  # remove punctuation/numbers
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text

file_path = r'data_analysis\cleaned_Goodreads_data.xlsx'
df = open_file(file_path)
plots = df['plot']
#plots = df['plot'].dropna().astype(str)  # drop missing, make sure all are strings
#print(plots.head())

preprocessed_plots = plots.apply(preprocess)

print(preprocessed_plots.head())


##TODO lemmatize + group by year and genre
