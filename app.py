import streamlit as st
import google.generativeai as genai

# ==========================================
# 🔑 TA CLÉ GEMINI (Vérifiée)
# ==========================================
GEMINI_API_KEY = "AIzaSyB38Z5b33LSLSJGGbm8jjlzNE6M_s315-o"

st.set_page_config(page_title="ZENITSU AI", page_icon="⚡", layout="centered")

# STYLE CSS (Interface Manga Noir & Or)
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .manga-header { font-family: 'Arial Black', sans-serif; color: #FFD700; text-shadow: 2px 2px #FF4500; font-size: 40px; text-align: center; margin-bottom: 5px; }
    .stChatMessage[data-testid="stChatMessageAssistant"] { background-color: #FFD700 !important; color: #000000 !important; border-radius: 15px; }
    .stChatMessage[data-testid="stChatMessageUser"] { background-color: #262730 !important; border: 1px solid #FFD700; border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.markdown('<div class="manga-header">⚡ ZENITSU IA ⚡</div>', unsafe_allow_html=True)

    # 1. ON VÉRIFIE LA CONFIGURATION EN PREMIER (EN HAUT)
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"⚠️ Erreur de configuration initiale : {e}")
        return

    # Historique
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Affichage de l'historique
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Zone de saisie
    if prompt := st.chat_input("Parle à Zenitsu..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # 2. ON GÈRE L'ERREUR DE GÉNÉRATION ICI SANS TOUT BLOQUER
            try:
                persona = "Tu es Zenitsu Agatsuma. Tu parles à Jeffrey. Réponds avec courage ou peur, en français."
                response = model.generate_content(f"{persona}\n\nJeffrey: {prompt}")
                
                if response.text:
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                else:
                    st.warning("Zenitsu est sans voix... Réessaie dans un instant.")
            except Exception as e:
                # L'erreur s'affichera juste ici au lieu de tout en bas de façon moche
                st.error("⚡ Oups ! La foudre a coupé la connexion. Vérifie ta clé API sur Google Studio.")

if __name__ == "__main__":
    main()

