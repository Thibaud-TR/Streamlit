import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)


def accueil():

    st.title("Bienvenue sur la page d'accueil")
    st.image('https://img.freepik.com/photos-gratuite/mot-bienvenue-disponible-lancement-ouvert_53876-124476.jpg?semt=ais_hybrid')
    
def photos():

    st.title("Bienvenue sur la page photos")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Panda 1")
        st.image("https://img.freepik.com/photos-gratuite/vue-ours-panda-dans-nature_23-2150453056.jpg?ga=GA1.1.1585893942.1733311562&semt=ais_hybrid")

    with col2:
        st.header("Panda 2")
        st.image("https://img.freepik.com/photos-gratuite/ours-panda-geant-allonge-dos-mangeant-pousses-bambou_493961-11.jpg?t=st=1733311784~exp=1733315384~hmac=1ab3a86de8ec6f2ffd93e6fdeaff69377d56580b974f3fb8da452144924f1440&w=740")

    with col3:
        st.header("Panda 3")
        st.image("https://img.freepik.com/photos-gratuite/vue-rapprochee-animal-feutre_23-2151728573.jpg?t=st=1733311847~exp=1733315447~hmac=59594370bbaae6e5edf0dfbad5f839360b1b6d126df9508ef8e7196b27790527&w=740")

authenticator.login()

if st.session_state["authentication_status"]:
    with st.sidebar :
        authenticator.logout("Déconnexion")
        selection = option_menu( menu_title = 'Navigation', options = ["Accueil", "Photos"], icons=['house', 'journal'])

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
    selection = 'connec'
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
    selection = 'connec'


if selection == 'connec' :
    st.title("Saisir vos identifiants et mot de passe")
elif selection == "Accueil":
    accueil()
elif selection == "Photos":
    photos()