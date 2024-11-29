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

        st.text('\n \n')
        st.text("The provided data gives us information on 1609 processes, ranked in " + str(process_details['Categorization (level 1)'].nunique()) + " categories." ) 
        #for n in range(0,15):
        #for n in [4, 11, 5, 6, 1, 9, 2, 14, 0, 10, 7, 8, 3, 13, 12]:
            #st.text(process_details['Categorization (level 1)'].unique()[n] + " : " 
                #+ str(process_details[process_details['Categorization (level 1)'] == process_details['Categorization (level 1)'].unique()[n]].shape[0]) + " processes.")
        