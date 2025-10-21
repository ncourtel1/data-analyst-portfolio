import streamlit as st

pg = st.navigation([st.Page("pages/home/home.py"), st.Page("pages/strava/strava-project.py")])
pg.run()