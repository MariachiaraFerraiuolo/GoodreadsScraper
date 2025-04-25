import re
import nltk 
from nltk.corpus import stopwords
import pandas as pd
import spacy
pd.set_option('display.max_rows', None)



#nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
nlp = spacy.load("en_core_web_sm")

def open_file(file1:str):
    file1 = pd.read_excel(file1)
    return file1

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  # remove punctuation/numbers
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text
def lemmatize(text):
    doc = nlp(text)
    return ' '.join(token.lemma_ for token in doc if token.is_alpha and not token.is_stop)


file_path = r'output\cleaned_Goodreads_data.xlsx'
df = open_file(file_path)
plots = df['plot']
#plots = df['plot'].dropna().astype(str)  # drop missing, make sure all are strings
#print(plots.head())

preprocessed_plots = df['plot'].apply(preprocess)
lemmatizer_plots = preprocessed_plots.apply(preprocess)
#lemmatizer_plots.to_excel(r'output\lemmatized_data.xlsx', index=False)
#print(lemmatizer_plots.iloc[])
#lemmatizer_plots
print(lemmatizer_plots.head())
##TODO lemmatize + group by year and genre
#####something interesting would be to make an llm clean the text without using regex##### 

