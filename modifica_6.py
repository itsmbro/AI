# Importare le librerie necessarie
import streamlit as st
import pandas as pd

# Creare l'app
def main():
    # Titolo dell'app
    st.title('La mia app Streamlit')

    # Sottotitolo
    st.subheader('Una semplice app di esempio')

    # Creare un input testuale
    user_input = st.text_input("Inserisci qualcosa")

    # Mostra l'input dell'utente
    if st.button('Mostra input'):
        st.write('Hai inserito: ', user_input)

    # Funzionalità aggiuntiva: Caricare un file CSV
    file = st.file_uploader("Carica un file CSV", type=['csv'])
    if file is not None:
        data = pd.read_csv(file)
        st.dataframe(data)  # Mostra il dataframe

# Esegui l'app
if __name__ == '__main__':
    main()