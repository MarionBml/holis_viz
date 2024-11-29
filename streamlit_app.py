import streamlit as st
from modules.datasets import load_process_data

st.set_page_config(page_title='Home page')

st.title("📊 Holis Interview - Data Visualization")

st.write(
    "Welcome to this user-friendly data visualisation dashboard using the Base Impacts subset from the Empreinte database."," \n ",
    "This dashboard involves illuminating datasets, highlighting their environmental impact in line with French regulations."," \n ",
    "The data used for that purpose have been extracted from the  version 2.02 of the Base Impacts:\n ",
    "\n \n",
    "This dashboard features: \n",
        "* A metadata overview section.\n",
        "* A dropdown for dataset selection.\n",
        "* Environmental impact visualisations.\n",
        "* Comparative rankings within categories."
)

from modules.nav import Navbar

def main():
    Navbar()
    

if __name__ == '__main__':
    main()