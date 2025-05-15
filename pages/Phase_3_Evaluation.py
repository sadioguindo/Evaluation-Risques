#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Étape 3 - Évaluation du risque", page_icon="images.png")

# Titre en bleu et centré
st.markdown(
    "<h1 style='text-align: center; color: #003366;'>Étape 3 : Évaluer l’impact et la probabilité des menaces</h1>",
    unsafe_allow_html=True
)

# Vérifier que les données des étapes précédentes existent
if 'assets' not in st.session_state or 'threats' not in st.session_state:
    st.warning("Veuillez compléter les étapes précédentes.")
    st.stop()

# Barèmes
impact_levels = ["Faible", "Moyen", "Élevé"]
probability_levels = ["Rare", "Possible", "Fréquent"]
impact_scores = {"Faible": 1, "Moyen": 2, "Élevé": 3}
probability_scores = {"Rare": 1, "Possible": 2, "Fréquent": 3}

evaluated_threats = []

# Texte d'instruction en bleu et centré
st.markdown(
    "<p style='text-align: center; color: #003366;'>Indiquez pour chaque menace son <strong>impact</strong> et sa <strong>probabilité</strong> :</p>",
    unsafe_allow_html=True
)

# Boucle sur les actifs et leurs menaces
for asset, threats in st.session_state['threats'].items():
    for threat in threats:
        # Sous-titre en bleu pour chaque menace
        st.markdown(
            f"<h4 style='color: #003366;'>{asset} - {threat}</h4>",
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)
        with col1:
            impact = st.selectbox(f"Impact de la menace {threat} sur {asset}", impact_levels, key=f"impact_{asset}_{threat}")
        with col2:
            probability = st.selectbox(f"Probabilité que la menace {threat} se produise", probability_levels, key=f"prob_{asset}_{threat}")
        
        risk_score = impact_scores[impact] * probability_scores[probability]
        
        evaluated_threats.append({
            "Actif": asset,
            "Menace": threat,
            "Impact": impact,
            "Probabilité": probability,
            "Score de Risque": risk_score
        })

# Enregistrer l'évaluation dans la session
st.session_state['evaluations'] = evaluated_threats

# Afficher un aperçu
st.markdown("---")
st.markdown("<h3 style='color: #003366;'>Aperçu des évaluations :</h3>", unsafe_allow_html=True)
st.dataframe(evaluated_threats)

