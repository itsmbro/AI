import streamlit as st
import random

def generate_joke():
    jokes = ["Perché gli scuba diver si immergono sempre all'indietro e mai frontalmente? Perché se si immergessero in avanti cadrebbero ancora sulla barca.",
            "Perché non si può fidarsi degli atomi? Perché fanno sempre tutto a pezzi.", 
            "Perché il libro è andato in ospedale? Perché aveva bisogno di un check-up della trama.", 
            "Perché il mare è blu? Perché il pesce fa blu blu.",
            "Che cosa fa un abete al computer? Naviga in pino-net!"]
    return random.choice(jokes)

if st.button('Genera barzelletta'):
    joke = generate_joke()
    st.write(joke)