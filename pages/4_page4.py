import streamlit as st
import pandas as pd
from modules.nav import Navbar
from modules.datasets import load_process_data, load_proc_imp, load_proc_imp_mpt

st.title(f'📈 Environmental Impact visualisations')

def main():
    Navbar()

proc_imp = load_proc_imp()
proc_imp_mpt = load_proc_imp_mpt()

ind = st.selectbox(
    "Which indicator are you interested in?",
    proc_imp.index[3:].unique(),
    index=None,
    placeholder="Select indicator...",
)

on = st.toggle("Comparison in mpt")

if on: # 
    data = proc_imp 
else : 
    data = proc_imp_mpt

if ind != None :
    col1, col2 = st.columns(2)
    col1.metric("Acidification", data.loc[ind][0], "")
    col2.metric("Ozone depletion", data.loc[ind][1], "")
    
    col3, col4 = st.columns(2)
    col3.metric("Climate change", data.loc[ind][2], "")
    col4.metric("Climate change-Biogenic", data.loc[ind][3], "")

    col5, col6 = st.columns(2)
    col5.metric("Climate change-Fossil", data.loc[ind][4], "")
    col6.metric("Freshwater eutrophication", data.loc[ind][5], "")

    col7, col8 = st.columns(2)
    col7.metric("Marine eutrophication", data.loc[ind][6], "")
    col8.metric("Terrestrial eutrophication", data.loc[ind][7], "")

    col9, col10 = st.columns(2) 
    col9.metric("Photochemical ozone formation", data.loc[ind][8], "")
    col10.metric("Particulate matter", data.loc[ind][9], "")

    col11, col12 = st.columns(2)
    col11.metric("Ionising radiation", data.loc[ind][10], "")
    col12.metric("Fossile resource use", data.loc[ind][11], "")

    col13, col14 = st.columns(2)
    col13.metric("Minerals and metal resource use", data.loc[ind][12], "")
    col14.metric("Land use", data.loc[ind][13], "")


if __name__ == '__main__':
    main()