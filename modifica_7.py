Ecco un esempio di un'applicazione Streamlit che visualizza un grafico a torta basato su dati inseriti dall'utente:

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titolo dell'applicazione
st.title('Streamlit Pie Chart App')

# Input dell'utente
st.subheader('Inserisci i tuoi dati qui:')
keys = st.text_input('Inserisci le etichette (separate da virgola):')
values = st.text_input('Inserisci i valori (separati da virgola):')

if st.button('Genera grafico a torta'):
    keys = keys.split(',')
    values = [int(i) for i in values.split(',')]
    df = pd.DataFrame({'values': values}, index=keys)

    # Creazione del grafico a torta
    fig, ax = plt.subplots()
    ax.pie(df['values'], labels=df.index, autopct='%1.1f%%')
    plt.title('Grafico a torta')
    
    # Visualizzazione del grafico
    st.pyplot(fig)

Nel codice sopra, l'utente può inserire le etichette e i valori per il grafico a torta. Quando l'utente fa clic sul pulsante "Genera grafico a torta", l'applicazione genera un grafico a torta con i dati inseriti.