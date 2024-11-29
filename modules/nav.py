import streamlit as st
from modules.datasets import load_process_data

process_details = load_process_data()

def Navbar():
    with st.sidebar:
        st.page_link('streamlit_app.py', label='Home Page', icon='🏠')
        st.page_link('pages/2_page2.py', label='Indicator explanations', icon='👁️')
        st.page_link('pages/3_page3.py', label='Metadata Overview', icon='🔍')
        st.page_link('pages/4_page4.py', label='Impact visualisations', icon='📈')
        st.page_link('pages/5_page5.py', label='Comparative rankings', icon='⚖️')
        
        