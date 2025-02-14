import streamlit as st
import random
import nltk
nltk.download('words')
from nltk.corpus import words

def generate_random_word():
    return random.choice(words.words())

if st.button('Generate Random Word'):
    st.write(generate_random_word())