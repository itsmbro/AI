import streamlit as st
import random
import string

def generate_random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(10))

if st.button('Generate Random Word'):
    st.write(generate_random_string())