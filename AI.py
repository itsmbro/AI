import streamlit as st
import openai
import json
import requests
import base64
import re

# Configurazione credenziali dai secrets di Streamlit
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
GITHUB_USER = "itsmbro"  # Sostituisci con il tuo username GitHub
GITHUB_REPO = "AI"
GITHUB_BRANCH = "main"
TASK_MAIN_PATH = "AI.py"  # File principale

# Configura API OpenAI
openai.api_key = OPENAI_API_KEY

# Funzione per ottenere l'ultima modifica creata
def get_latest_modification():
    url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/contents/"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        files = [f["name"] for f in response.json()]
        modifications = [int(f.split("_")[1].split(".")[0]) for f in files if f.startswith("modifica_") and f.endswith(".py")]
        return max(modifications) if modifications else 0
    return 0

# Funzione per salvare una nuova modifica su GitHub
def save_new_modification(updated_code, new_version):
    mod_filename = f"modifica_{new_version}.py"
    url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/contents/{mod_filename}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    json_base64 = base64.b64encode(updated_code.encode()).decode()
    data = {"message": f"Nuova modifica {new_version}", "content": json_base64, "branch": GITHUB_BRANCH}

    response = requests.put(url, headers=headers, json=data)
    return response.status_code in [200, 201]

# Funzione per aggiornare `task.py`
def update_task_main(new_version):
    url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/contents/{TASK_MAIN_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = base64.b64decode(response.json()["content"]).decode()
        
        # Aggiungiamo l'import solo se non è già presente
        new_import = f"from modifica_{new_version} import *\n"
        if new_import not in content:
            content += new_import

        json_base64 = base64.b64encode(content.encode()).decode()
        data = {
            "message": f"Aggiunto import modifica_{new_version}",
            "content": json_base64,
            "sha": response.json()["sha"],
            "branch": GITHUB_BRANCH
        }
        response = requests.put(url, headers=headers, json=data)
        return response.status_code in [200, 201]

    return False

# Funzione per ripulire il codice generato
def clean_code(response_text):
    code = re.sub(r"```python\n(.*?)\n```", r"\1", response_text, flags=re.DOTALL)
    return code.strip()

# Prompt per GPT-4
def generate_prompt(user_request):
    return (
        "crea il codice Python con interfaccia streamlit con la seguente richiesta:\n\n"
        f"{user_request}\n\n"
        "Genera solo il codice Python senza spiegazioni varie."
    )

# UI Streamlit
st.title("Gestione Modifiche Incrementali per `task.py`")

user_input = st.text_area("Descrivi la modifica che vuoi fare:")

if st.button("Genera Modifica"):
    if user_input:
        with st.spinner("Generando codice con GPT..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": generate_prompt(user_input)}],
                    temperature=0.7
                )
                bot_response = response["choices"][0]["message"]["content"]
                updated_code = clean_code(bot_response)

                # Creazione di un nuovo file modifica_N.py
                new_version = get_latest_modification() + 1
                if save_new_modification(updated_code, new_version):
                    update_task_main(new_version)
                    st.success(f"Nuova modifica `modifica_{new_version}.py` salvata e importata in `task.py`!")

            except Exception as e:
                st.error(f"Errore nella comunicazione con OpenAI: {str(e)}")
from modifica_1 import *
from modifica_2 import *
from modifica_3 import *
from modifica_4 import *
from modifica_5 import *
