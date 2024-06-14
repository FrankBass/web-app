##page d'accueil
## python -m streamlit run home.py



import streamlit as st


#titre
st.title("Titre 1")

#sous-titre
st.subheader ("this is teh sub header")



#texte 
st.write ('this is a simple title')


#champ de saisie utilisateur
#st.text_input ("type text")

#champs de saisi
user_input= st.text_input('Tape your text')


# Afficher champ à l'ecran de que l'utilisateur a saisie 
st.write(user_input)

#upload une image 
st.image ('https://cdn.dribbble.com/users/2018170/screenshots/14766274/media/c8002f83ebc7344e5ba383cce7fced83.png?compress=1&resize=400x300&vertical=top')


#creation d'un formulaire 
with st.form('Form1'):
    
    #on demande a l'utilisateur son nom
    user_name= st.text_input('Tape your name:')

    #Bouton "Envoyer"
    if st.form_submit_button('Send'):
        #On affiche le name de l'utilisateur
        st.write(user_name)