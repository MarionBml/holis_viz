import streamlit as st
import pandas as pd
from modules.nav import Navbar
from modules.datasets import load_process_data, load_proc_imp, load_proc_imp_npt

st.title(f'📈 Environmental Impact visualisations')

def main():
    Navbar()

proc_imp = load_proc_imp()

ind = st.selectbox(
    "Which indicator are you interested in ?",
    proc_imp.index[3:].unique(),
    index=None,
    placeholder="Select indicator...",
)

on = st.toggle("Comparison in npt")

if on: # 
    data = load_proc_imp_npt()
    
else : 
    data = proc_imp

if ind != None :
    with st.expander("See indicator values"):

        col1, col2 = st.columns(2)
        col1.metric("Acidification", data.loc[ind][0], delta= "mol éq. H+", delta_color="off")
        col2.metric("Ozone depletion", data.loc[ind][1], delta= "kg éq. CFC 11", delta_color="off")
    
        col3, col4 = st.columns(2)
        col3.metric("Climate change", data.loc[ind][2], delta= "kg éq. CO2", delta_color="off")
        col4.metric("Climate change-Biogenic", data.loc[ind][3], delta= "kg éq. CO2", delta_color="off")

        col5, col6 = st.columns(2)
        col5.metric("Climate change-Fossil", data.loc[ind][4], delta= "kg éq. CO2", delta_color="off")
        col6.metric("Freshwater eutrophication", data.loc[ind][5], delta= "kg éq. P", delta_color="off")

        col7, col8 = st.columns(2)
        col7.metric("Marine eutrophication", data.loc[ind][6], delta= "kg éq. N", delta_color="off")
        col8.metric("Terrestrial eutrophication", data.loc[ind][7], delta= "kg éq. N", delta_color="off")

        col9, col10 = st.columns(2) 
        col9.metric("Photochemical ozone formation", data.loc[ind][8], delta= "kg éq. COVNM", delta_color="off")
        col10.metric("Particulate matter", data.loc[ind][9], delta= "diseases incidence", delta_color="off")

        col11, col12 = st.columns(2)
        col11.metric("Ionising radiation", data.loc[ind][10], delta= "éq. kBq U235", delta_color="off")
        col12.metric("Fossile resource use", data.loc[ind][11], delta= "MJ", delta_color="off")

        col13, col14 = st.columns(2)
        col13.metric("Minerals and metal resource use", data.loc[ind][12], delta= "kg éq. Sb", delta_color="off")
        col14.metric("Land use", data.loc[ind][13], delta= "dimensionless (pt)", delta_color="off")

if __name__ == '__main__':
    main()