import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Formulaire", page_icon="📝")

# Barre latérale
st.sidebar.title("À propos")
st.sidebar.info(
    """
    BASS\n
    FRANK\n
    [Project Formulaire](http://localhost:8501/formulaire#formulaire-de-contact)
    """
)

# Titre de la page
st.title("Formulaire de contact")

# Création du formulaire
with st.form(key="formulaire"):
    # Champs du formulaire
    first_name = st.text_input("Prénom")
    last_name = st.text_input("Nom de famille")
    age = st.number_input("Âge", min_value=0, max_value=120, step=1)
    education_level = st.selectbox("Niveau d'étude", ["Sans diplôme", "BAC", "BAC+2", "BAC+5", "BAC+8"])

    # Bouton de soumission
    submit_button = st.form_submit_button(label="Soumettre")

# Vérification de la soumission du formulaire
if submit_button:
    if age < 18:
        st.write("Vous êtes mineur")
    elif age > 50:
        st.write("Tu es un ancêtre :)")
    else:
        st.write("Vous êtes majeur")
    st.write(f"Bienvenue, {first_name} {last_name}!"


