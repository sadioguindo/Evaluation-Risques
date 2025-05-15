#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Étape 4 - Synthèse", page_icon="images.png")

# Titre principal stylisé
st.markdown(
    "<h1 style='text-align: center; color: #003366;'>Étape 4 : Synthèse des Risques et Recommandations</h1>",
    unsafe_allow_html=True
)

# Vérification que les évaluations sont disponibles
if 'evaluations' not in st.session_state:
    st.warning("Veuillez d'abord compléter l'étape d’évaluation.")
    st.stop()

evaluations = pd.DataFrame(st.session_state['evaluations'])

# Sous-titre stylisé
st.markdown("<h3 style='color: #003366;'>Résumé des risques évalués</h3>", unsafe_allow_html=True)
st.dataframe(evaluations)

# Classement par niveau de risque
top_risks = evaluations.sort_values(by="Score de Risque", ascending=False)

# Autre sous-titre stylisé
st.markdown("<h3 style='color: #003366;'>Top 5 des risques les plus élevés :</h3>", unsafe_allow_html=True)
st.dataframe(top_risks.head(5))

# Graphique interactif des scores de risque
fig = px.bar(
    top_risks,
    x='Actif',
    y='Score de Risque',
    color='Menace',
    barmode='group',
    title="Scores de Risque par Actif et Menace"
)
st.plotly_chart(fig)

# Sous-titre recommandations
st.markdown("<h3 style='color: #003366;'>Recommandations générales :</h3>", unsafe_allow_html=True)

# Recommandations et explications enrichies

def get_detailed_recommendation(menace):
    menace = menace.lower()
    if "phishing" in menace:
        return "Former les employés à repérer les e-mails frauduleux, utiliser un filtre anti-phishing et activer l’authentification à deux facteurs."
    elif "malware" in menace or "ransomware" in menace:
        return "Installer un antivirus à jour, effectuer des sauvegardes régulières hors ligne et limiter les privilèges d’accès aux fichiers sensibles."
    elif "intrusion" in menace or "accès non autorisé" in menace:
        return "Renforcer les mots de passe, utiliser des connexions sécurisées (VPN) et surveiller les journaux d’accès."
    elif "fuite" in menace or "vol de données" in menace:
        return "Mettre en œuvre le chiffrement des données sensibles, restreindre l’accès par rôle, et surveiller les transferts de données sortants."
    elif "erreur humaine" in menace:
        return "Mettre en place des procédures de validation, former les utilisateurs et réaliser des simulations régulières d’incident."
    elif "attaque ddos" in menace:
        return "Utiliser des services de protection DDoS, renforcer l’infrastructure réseau et contacter son hébergeur pour des solutions de mitigation."
    elif "vulnérabilité" in menace or "mise à jour" in menace:
        return "Planifier des mises à jour régulières, utiliser des outils de détection de vulnérabilités et désinstaller les logiciels obsolètes."
    else:
        return "Mettre en place une politique de sécurité adaptée, sensibiliser le personnel et réaliser des audits réguliers."


def get_detailed_explanation(menace):
    menace = menace.lower()
    if "phishing" in menace:
        return "Le phishing vise à tromper l’utilisateur pour lui soutirer des informations sensibles (identifiants, mots de passe) via de faux messages ou sites."
    elif "malware" in menace or "ransomware" in menace:
        return "Un logiciel malveillant peut chiffrer, détruire ou voler vos données. Les ransomwares exigent souvent une rançon pour restaurer l’accès."
    elif "intrusion" in menace or "accès non autorisé" in menace:
        return "Une intrusion correspond à un accès sans autorisation aux systèmes ou données, menaçant leur intégrité et confidentialité."
    elif "fuite" in menace or "vol de données" in menace:
        return "Une fuite de données survient lorsqu’une information sensible est exposée, souvent de manière involontaire, à des tiers non autorisés."
    elif "erreur humaine" in menace:
        return "Les erreurs humaines, comme une mauvaise configuration ou l’envoi d’informations au mauvais destinataire, sont à l’origine de nombreuses failles."
    elif "attaque ddos" in menace:
        return "Une attaque DDoS vise à rendre un service indisponible en saturant les ressources réseau ou système via de multiples requêtes."
    elif "vulnérabilité" in menace or "mise à jour" in menace:
        return "Les vulnérabilités sont des failles techniques exploitables si elles ne sont pas corrigées par des mises à jour régulières."
    else:
        return "Cette menace peut impacter la disponibilité, l’intégrité ou la confidentialité de vos systèmes ou données."

# Affichage Streamlit enrichi

for _, row in top_risks.head(3).iterrows():
    menace = row['Menace']
    actif = row['Actif']
    score = row['Score de Risque']

    recommandation = get_detailed_recommendation(menace)
    explication = get_detailed_explanation(menace)

    st.markdown(f"""
    - **{actif} - {menace}** : Risque élevé détecté (**Score : {score}**)
        - 🔍 **Explication** : {explication}
        - ✅ **Action recommandée** : {recommandation}
    """)


# Message de fin stylisé
st.markdown(
    "<div style='text-align: center; color: #003366; font-size: 18px; padding-top: 20px;'>"
    "✅ Analyse terminée ! Vous pouvez revenir en arrière pour modifier vos réponses si besoin."
    "</div>",
    unsafe_allow_html=True
)

