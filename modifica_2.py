import streamlit as st
import random

def main():
    st.title("Emoji Generator")
    if st.button('Generate Random Emoji'):
        emoji_list = ['😮', '🐻', '🥰', '🥹', '☺️', '🫨', '😔']
        emoji = random.choice(emoji_list)
        st.write(emoji)

if __name__ == '__main__':
    main()