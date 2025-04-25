from bs4 import UnicodeDammit

def clean_text(text):
    return UnicodeDammit(text).unicode_markup.replace('\n', ' ').replace('\r', '').strip()