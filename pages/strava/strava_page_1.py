import streamlit as st

# Charger la carte HTML sauvegardée
with open("pages/strava/maps/activities.html", "r", encoding="utf-8") as f:
    map_html = f.read()

# Afficher la carte dans Streamlit
st.components.v1.html(map_html, height=600, scrolling=False)