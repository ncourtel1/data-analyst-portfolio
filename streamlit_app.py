import streamlit as st

pg = st.navigation([st.Page("pages/home/home_page_0.py"), st.Page("pages/strava/strava_page_1.py")])
pg.run()