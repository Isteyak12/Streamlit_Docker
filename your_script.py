from pathlib import Path
from PIL import Image
import streamlit as st

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV "
PAGE_ICON = ":wave:"
NAME = "JJ "
DESCRIPTION = """
To introduce myself to you
"""
EMAIL = "i.ca"


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.title("Hello Friends!")

col1, col2= st.columns(2, gap="small")
     
with col1:
        st.title(NAME)
        st.write(DESCRIPTION)
