#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Étape 2 - Menaces", page_icon="images.png")

# Titre en bleu et centré
st.markdown(
    "<h1 style='text-align: center; color: #003366;'>Étape 2 : Quelles menaces concernent vos actifs ?</h1>",
    unsafe_allow_html=True
)

# Vérifier si des actifs ont été sélectionnés à l'étape précédente
if 'assets' not in st.session_state:
    st.warning("Veuillez retourner à l'étape précédente pour sélectionner des actifs.")
    st.stop()


# Récupérer les actifs sélectionnés
selected_assets = st.session_state['assets']
st.success(f"Actifs sélectionnés : {', '.join(selected_assets)}")

# Texte d'instruction stylisé
st.markdown(
    "<p style='text-align: center; color: #003366;'>Pour chaque actif, sélectionnez les menaces qui vous semblent les plus pertinentes :</p>",
    unsafe_allow_html=True
)

# Dictionnaire des menaces
menaces_possibles = {
    "Ordinateurs des employés": ["Malware", "Phishing", "Perte ou vol"],
    "Systèmes de facturation": ["Intrusion", "Erreur humaine", "Ransomware"],
    "Messagerie professionnelle": ["Phishing", "Spam", "Accès non autorisé"],
    "Site internet de l’entreprise": ["Défaillance", "Attaque DDoS", "Injection SQL"],
    "Données clients": ["Fuite de données", "Accès non autorisé", "Altération des données"],
    "Données comptables": ["Fuite d'information", "Modification frauduleuse", "Ransomware"],
    "Accès à distance aux fichiers": ["Intrusion", "Accès non sécurisé", "Vol de données"],
    "Logiciels métier spécifiques": ["Vulnérabilité logicielle", "Mise à jour non appliquée"]
}

# Interface de sélection
selected_threats = {}
for asset in selected_assets:
    menaces = menaces_possibles.get(asset, ["Menace non définie"])
    choix = st.multiselect(f"Menaces pour : {asset}", options=menaces)
    selected_threats[asset] = choix

# Sauvegarde dans session_state
st.session_state['threats'] = selected_threats

