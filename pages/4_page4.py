import streamlit as st
import pandas as pd
from modules.nav import Navbar
from modules.datasets import load_process_data, load_proc_imp

st.title(f'📈 Environmental Impact visualisations')

def main():
    Navbar()

proc_imp = load_proc_imp()

ind = st.selectbox(
    "Which indicator are you interested in?",
    proc_imp.index[3:].unique(),
    index=None,
    placeholder="Select indicator...",
)

if ind != None :
    col1, col2 = st.columns(2)
    col1.metric("Acidification", proc_imp.loc[ind][0], "")
    col2.metric("Ozone depletion", proc_imp.loc[ind][1], "")
    
    col3, col4 = st.columns(2)
    col3.metric("Climate change", proc_imp.loc[ind][2], "")
    col4.metric("Climate change-Biogenic", proc_imp.loc[ind][3], "")

    col5, col6 = st.columns(2)
    col5.metric("Climate change-Fossil", proc_imp.loc[ind][4], "")
    col6.metric("Freshwater eutrophication", proc_imp.loc[ind][5], "")

    col7, col8 = st.columns(2)
    col7.metric("Marine eutrophication", proc_imp.loc[ind][6], "")
    col8.metric("Terrestrial eutrophication", proc_imp.loc[ind][7], "")

    col9, col10 = st.columns(2) 
    col9.metric("Photochemical ozone formation", proc_imp.loc[ind][8], "")
    col10.metric("Particulate matter", proc_imp.loc[ind][9], "")

    col11, col12 = st.columns(2)
    col11.metric("Ionising radiation", proc_imp.loc[ind][10], "")
    col12.metric("Fossile resource use", proc_imp.loc[ind][11], "")

    col13, col14 = st.columns(2)
    col13.metric("Minerals and metal resource use", proc_imp.loc[ind][12], "")
    col14.metric("Land use", proc_imp.loc[ind][13], "")


if __name__ == '__main__':
    main()