import streamlit as st
import pandas as pd
from modules.nav import Navbar
from modules.datasets import load_process_data, load_proc_imp

st.title(f'⚖️ Comparative rankings within categories')

def main():
    Navbar()

process_details = load_process_data()

level = st.slider("Until which categorisation level do you want to compare ?", 1, 4)

cat_level_1 = st.multiselect(
    "Categories",
    process_details['Categorization (level 1)'].unique(),
    [])

pr_det_filter_1 = process_details[process_details['Categorization (level 1)'].isin(cat_level_1)]

if level > 1 : 
    cat_level_2 = st.multiselect(
        "Categorization 2",
        pr_det_filter_1['Categorization (level 2)'].unique(),
        [])

# note globale ou choix d'un indicateur
on = st.toggle("Comparison in mpt")

#if on: # Indicates one comparison as a stacked horizontal bar chart with μpt score
    
#else : # Indicates several comparisons as a 
    

if __name__ == '__main__':
    main()