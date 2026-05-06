import streamlit as st
import google.generativeai as genai

# ==========================================
# 🔑 CONFIGURATION : COLLE TA CLÉ GEMINI ICI
# ==========================================
GEMINI_API_KEY = "AIzaSyB38Z5b33LSLSJGGbm8jjlzNE6M_s315-o"

# Configuration de la page pour le mode Application
st.set_page_config(
    page_title="ZENITSU AI",
    page_icon="👽",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# STYLE CSS MANGA CHIC
st.markdown("""
    <style>
    /* Fond sombre et texte blanc */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }

    /* Titre Style Manga avec effet d'ombre */
    .manga-header {
        font-family: 'Arial Black', sans-serif;
        color: #FFD700;
        text-shadow: 2px 2px #FF4500;
        font-size: 45px;
        text-align: center;
        margin-bottom: 5px;
        text-transform: uppercase;
    }

    /* Sous-titre animé */
    @keyframes blink {
        0% { opacity: 1; }
        50% { opacity: 0.4; }
        100% { opacity: 1; }
    }
    .status-lightning {
        color: #FFD700;
        text-align: center;
        font-size: 14px;
        font-weight: bold;
        animation: blink 1.5s infinite;
        margin-bottom: 30px;
    }

    /* Bulles de discussion Zenitsu (Assistant) */
    .stChatMessage[data-testid="stChatMessageAssistant"] {
        background-color: #FFD700 !important;
        color: #000000 !important;
        border-radius: 15px 15px 15px 0px !important;
    }

    /* Bulles de discussion Jeffrey (Utilisateur) */
    .stChatMessage[data-testid="stChatMessageUser"] {
        background-color: #262730 !important;
        color: #FFFFFF !important;
        border-radius: 15px 15px 0px 15px !important;
        border: 1px solid #FFD700;
    }

    /* Input barre de chat */
    .stChatInputContainer {
        border: 2px solid #FFD700 !important;
        border-radius: 25px !important;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Affichage de l'interface
    st.markdown('<div class="manga-header">⚡ ZENITSU AI ⚡</div>', unsafe_allow_html=True)
    st.markdown('<div class="status-lightning">SOUFFLE DE LA FOUDRE... PRÊT !</div>', unsafe_allow_html=True)

    # Vérification de la clé
    if GEMINI_API_KEY == "AIzaSyB38Z5b33LSLSJGGbm8jjlzNE6M_s315-o":
        st.error("Jeffrey, tu as oublié de mettre ta clé Gemini dans le code !")
        return

    # Initialisation de l'IA
    try:
        genai.configure(api_key=AIzaSyB38Z5b33LSLSJGGbm8jjlzNE6M_s315-o)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"Erreur de config : {e}")
        return

    # Historique des messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Affichage de la discussion
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Zone de saisie
    if prompt := st.chat_input("Parle à ton IA, Jeffrey..."):
        # Afficher le message utilisateur
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Réponse de l'IA
        with st.chat_message("assistant"):
            try:
                # Instruction de personnalité
                full_prompt = f"Tu es Zenitsu Agatsuma. Tu parles à Jeffrey. Réponds avec sa personnalité (peureux mais parfois sérieux), en français, de manière naturelle : {prompt}"
                response = model.generate_content(full_prompt)
                ai_text = response.text
                
                st.markdown(ai_text)
                st.session_state.messages.append({"role": "assistant", "content": ai_text})
            except Exception as e:
                st.error("L'IA est fatiguée... Vérifie ta clé ou ta connexion.")

if __name__ == "__main__":
    main()



