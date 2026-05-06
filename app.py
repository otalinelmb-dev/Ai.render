import streamlit as st
import os
from groq import Groq

# CLÉ API INTÉGRÉE (Plus besoin de réglages dans Render)
GROQ_API_KEY = "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"

# Configuration de l'interface
st.set_page_config(page_title="ZENITSU AI", page_icon="⚡")

def main():
    # Initialisation du client Groq
    client = Groq(api_key=GROQ_API_KEY)

    st.title("⚡ ZENITSU AI")
    st.subheader("Souffle de la Foudre, premier mouvement !")
    st.info("Statut : Connecté avec succès, Jeffrey.")

    # Gestion de l'historique de discussion
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Affichage des messages précédents
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    # Zone de saisie utilisateur
    if prompt := st.chat_input("Parle à Zenitsu..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                chat = client.chat.completions.create(
                    model="llama3-8b-8192",
                    messages=[
                        {"role": "system", "content": "Tu es Zenitsu Agatsuma. Tu es peureux mais protecteur. Tu appelles l'utilisateur Jeffrey."},
                        {"role": "user", "content": prompt}
                    ]
                )
                response = chat.choices[0].message.content
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Erreur de connexion : {e}")

if __name__ == "__main__":
    main()
