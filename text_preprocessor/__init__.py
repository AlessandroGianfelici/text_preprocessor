import json
import os
import pandas as pd
from langdetect import detect_langs
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob
import nltk
import spacy
import re

nltk.download('stopwords')

def read_json(filename: str):
    with open(filename, 'r') as f:
        return json.load(f)


class TextPreprocessor:
    
    def __init__(self, language: str = 'en'):
        self.language = language
        self.nlp = spacy.load(self.match_spacy_model(language))
        self.stopwords = stopwords.words(self.match_language(language))

    @staticmethod
    def language(text: str) -> str:
        """
        Use langdetect library to return the language detected
        text: string
        """
        return detect_langs(text)[0].lang
        
    def translate(self, text: str, lang: str)-> str:
        """Translate the text given a string into language
           we are using TextBlob for translation
           text -> string of text to translate
           language -> language string in which translate the text"""
        try:
            if (self.language(text) != lang):
                return TextBlob(text).translate(to=lang)
            else:
                return text
        except:
            return text

    def lemmatize(self, text: str)-> str:
        lemmas = map(lambda w: w.lemma_, self.nlp(text))
        return " ".join(list(lemmas)) 
    
    @staticmethod
    def match_language(lang: str)-> str:
        if lang == 'it':
            return 'italian'
        elif lang == 'en':
            return 'english'
        else:
            raise NotImplementedError('Language not supported yet!')

    @staticmethod
    def match_spacy_model(lang: str)-> str:
        if lang == 'it':
            return "it_core_news_sm"
        elif lang == 'en':
            return 'en_core_web_sm'
        else:
            raise NotImplementedError('Language not supported yet!')

    def remove_stopwords(self, text: str, stop_words: str = None)-> str:
        
        stop_words = stop_words or self.stopwords

        filtered = filter(lambda w: w not in stop_words, word_tokenize(text))
        return " ".join(list(filtered)) 
    
    @staticmethod
    def remove_punctuation(text: str)-> str: 
        return re.sub(r'[^a-zA-ZÀ-ÿ]', ' ', text)