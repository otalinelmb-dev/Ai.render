import streamlit as st
import google.generativeai as genai

# ==========================================
# 🔑 COLLE TA CLÉ GEMINI ENTRE LES GUILLEMETS CI-DESSOUS
# ==========================================
GEMINI_API_KEY = "AIzaSyB38Z5b33LSLSJGGbm8jjlzNE6M_s315-o"

st.set_page_config(page_title="ZENITSU AI", page_icon="👽", layout="centered")

# STYLE CSS MANGA CHIC
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .manga-header { font-family: 'Arial Black', sans-serif; color: #FFD700; text-shadow: 2px 2px #FF4500; font-size: 45px; text-align: center; text-transform: uppercase; }
    .status-lightning { color: #FFD700; text-align: center; font-size: 14px; font-weight: bold; animation: blink 1.5s infinite; margin-bottom: 30px; }
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }
    .stChatMessage[data-testid="stChatMessageAssistant"] { background-color: #FFD700 !important; color: #000000 !important; border-radius: 15px 15px 15px 0px !important; }
    .stChatMessage[data-testid="stChatMessageUser"] { background-color: #262730 !important; color: #FFFFFF !important; border-radius: 15px 15px 0px 15px !important; border: 1px solid #FFD700; }
    .stChatInputContainer { border: 2px solid #FFD700 !important; border-radius: 25px !important; }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.markdown('<div class="manga-header">⚡ ZENITSU IA ⚡</div>', unsafe_allow_html=True)
    st.markdown('<div class="status-lightning">SOUFFLE DE LA FOUDRE... PRÊT !</div>', unsafe_allow_html=True)

    # Vérification automatique pour éviter l'erreur de l'image
    if GEMINI_API_KEY == "TA_CLE_API_ICI" or GEMINI_API_KEY == "":
        st.error("Jeffrey, tu as oublié de coller ta clé Gemini dans le code à la ligne 8 !")
        return

    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"Erreur de configuration : {e}")
        return

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Parle à Zenitsu..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                response = model.generate_content(f"Tu es Zenitsu Agatsuma. Réponds à Jeffrey : {prompt}")
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error("Problème de connexion avec Gemini.")

if __name__ == "__main__":
    main()
