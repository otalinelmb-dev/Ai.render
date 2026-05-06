import streamlit as st
import google.generativeai as genai

# TA CLÉ GEMINI (Remplace le texte entre guillemets par ta vraie clé)
GEMINI_API_KEY = "AIzaSyB38Z5b33LSLSJGGbm8jjlzNE6M_s315-o"

# Configuration de la page
st.set_page_config(page_title="ZENITSU AI", page_icon="⚡")

def main():
    # Configuration de Gemini
    genai.configure(api_key=AIzaSyB38Z5b33LSLSJGGbm8jjlzNE6M_s315-o)
    model = genai.GenerativeModel('gemini-1.5-flash')

    st.title("👽Jeffrey AI")
    st.info("jeff_ai.petit.mais.puissant.")

    # Historique de chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Affichage des messages
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    # Zone de saisie
    if prompt := st.chat_input("Dis-moi quelque chose..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                # Ici, c'est l'IA pure qui génère la réponse
                response = model.generate_content(f"Tu es Zenitsu. Réponds à Jeffrey de façon naturelle : {prompt}")
                full_response = response.text
                
                st.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"Erreur Gemini : {e}")

if __name__ == "__main__":
    main()


