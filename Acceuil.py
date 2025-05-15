#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

st.set_page_config(page_title="Accueil - Évaluation Cybersécurité PME", page_icon="images.png")

# Titre principal en bleu et centré
st.markdown(
    "<h1 style='text-align: center; color: #003366;'>Bienvenue dans l'outil d’évaluation de cybersécurité pour PME</h1>",
    unsafe_allow_html=True
)

# Sous-titre centré et en bleu
st.markdown(
    "<h3 style='text-align: center; color:#003366;'>Basé sur la méthode CIS RAM</h3>",
    unsafe_allow_html=True
)

st.image("images.png", use_column_width=True)

# Corps du texte avec titres de section en bleu
st.markdown("""
<h3 style="color:#003366"> Objectif de l’outil :</h3>
Cet outil interactif permet aux petites et moyennes entreprises d’évaluer leur niveau de cybersécurité <b>de manière simple et guidée</b>, sans avoir besoin de compétences techniques poussées.

<h3 style="color:#003366">Pourquoi cet outil ?</h3>
<ul>
  <li>Le CIS RAM permet de <b>prioriser les actions de sécurité</b> en tenant compte des impacts réels sur votre activité.</li>
  <li>Ce guide se veut <b>pédagogique et accessible</b>.</li>
</ul>
<h3 style="color:#003366">Déroulement </h3>
<ol>
  <li>Identification simplifiée de vos activités et ressources.</li>
  <li>Scénarios de menaces courants dans le monde des PME.</li>
  <li>Évaluation de l’impact et probabilité à travers des questions compréhensibles.</li>
  <li>Synthèse des risques et recommandations claires.</li>
</ol>

<h3 style="color:#003366"> Comment utiliser ?</h3>
Utilisez le menu sur la gauche pour commencer. Il est conseillé de suivre les étapes dans l’ordre.
""", unsafe_allow_html=True)

