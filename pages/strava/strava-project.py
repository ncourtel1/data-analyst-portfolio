import streamlit as st

st.title("🏃‍♂️ Strava Urban Trail — Analyse des segments")

st.markdown("""
Bienvenue sur la page **Strava Urban Trail** !
Cette carte présente l’ensemble de mes activités Strava analysées et visualisées à l’aide de **Folium**.
L’objectif est de repérer les segments les plus fréquentés et d’imaginer un parcours pour une future **course urbaine**. 
""")

# Bouton pour afficher la carte des activites
if st.toggle("Afficher la carte des activites 🗺️"):
    with open("pages/strava/maps/activities.html", "r", encoding="utf-8") as f:
        map_html = f.read()
    st.components.v1.html(map_html, height=400, scrolling=False)

st.markdown("""
---
📊 *Données issues de l'API Strava et retraitées via Python / Pandas / Folium.*
""")

# Buton pour la carte des segments avec D+
if st.toggle("Afficher la carte des segments et leur D+ 🗺️"):
    with open("pages/strava/maps/segments.html", "r", encoding="utf-8") as f:
        map_html = f.read()
    st.components.v1.html(map_html, height=400, scrolling=False)


import streamlit as st
from PIL import Image

st.subheader("📊 Analyse des segments Strava")

st.write(
    "Voici une visualisation réalisée sur **Tableau Public**, "
    "présentant mes segments les plus fréquents et leurs caractéristiques."
)

# --- Afficher une image statique du tableau (exportée depuis Tableau Public)
image = Image.open("pages/strava/segments-d+.png")  # adapte le chemin
st.image(image, caption="Visualisation Tableau Public – Segments Strava", use_container_width=True)

# --- Ajouter un bouton pour accéder à la version interactive
tableau_url = "https://public.tableau.com/views/strava-segments-d/Feuille1?:language=fr-FR&:display_count=n&:origin=viz_share_link"

st.markdown(
    f"""
    <div style="text-align: center; margin-top: 1rem;">
        <a href="{tableau_url}" target="_blank" style="
            background-color:#4c8bf5;
            color:white;
            padding:0.6em 1.2em;
            border-radius:8px;
            text-decoration:none;
            font-weight:600;
            font-size:16px;">
            🌐 Ouvrir la version interactive sur Tableau Public
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
