#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Évaluation Cybersécurité PME")

# Titre principal en bleu et centré
st.markdown(
    "<h1 style='text-align: center; color: #003366;'> Étape Auto-évaluation </h1>",
    unsafe_allow_html=True
)


# Sous-titre en bleu et centré
st.markdown(
    "<h3 style='text-align: center; color: #003366;'> Quels sont les actifs importants pour votre entreprise ?</h3>",
    unsafe_allow_html=True
)

# Texte d'instruction centré et bleu
st.markdown(
    "<p style='text-align: center; color: #003366;'> Sélectionnez les éléments qui sont essentiels à votre activité :</p>",
    unsafe_allow_html=True
)

# Choix multiples
assets = st.multiselect(
    "Actifs critiques",
    [
        "Ordinateurs des employés",
        "Systèmes de facturation",
        "Messagerie professionnelle",
        "Site internet de l’entreprise",
        "Données clients",
        "Données comptables",
        "Accès à distance aux fichiers",
        "Logiciels métier spécifiques"
    ]
)

# Affichage si des actifs sont sélectionnés
if assets:
    st.session_state['assets'] = assets  # ENREGISTRER DANS LA SESSION
    st.success("Vous avez identifié les actifs suivants :")
    for asset in assets:
        st.write(f"- {asset}")
else:
    st.info("Veuillez sélectionner au moins un actif pour continuer.")

