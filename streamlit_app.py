import streamlit as st
from pathlib import Path

pg = st.navigation([
    st.Page("home_page_0.py"),
    st.Page(str(Path(__file__).parent / "strava" / "strava_page_1.py")),
    st.Page("page_2.py")
])
pg.run()
