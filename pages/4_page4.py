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

if __name__ == '__main__':
    main()