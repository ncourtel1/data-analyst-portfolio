import streamlit as st

st.title("🏃‍♂️ Strava Urban Trail — Analyse des segments")

st.markdown("""
Bienvenue sur la page **Strava Urban Trail** !
Cette carte présente l’ensemble de mes activités Strava analysées et visualisées à l’aide de **Folium**.
L’objectif est de repérer les segments les plus fréquentés et d’imaginer un parcours pour une future **course urbaine**. 
""")

# Bouton pour afficher la carte
if st.button("🗺️ Afficher la carte"):
    with open("pages/strava/maps/activities.html", "r", encoding="utf-8") as f:
        map_html = f.read()
    st.components.v1.html(map_html, height=600, scrolling=False)

st.markdown("""
---
📊 *Données issues de l'API Strava et retraitées via Python / Pandas / Folium.*
""")
