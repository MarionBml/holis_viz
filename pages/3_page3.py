import streamlit as st
import pandas as pd
from modules.nav import Navbar
from modules.datasets import load_process_data

st.title(f'🔍 Metadata Overview')

def main():
    Navbar()
    
process_details = load_process_data()

st.text("The provided data regarding processes gives us information on 1609 processes, ranked in " + str(process_details['Categorization (level 1)'].nunique()) + " categories." )
        
cat_lev1 = st.multiselect(
    "Categorization 1",
    process_details['Categorization (level 1)'].unique(),
    [])

pr_det_filt1 = process_details[process_details['Categorization (level 1)'].isin(cat_lev1)]

    
if cat_lev1 != [] : 
    cat_lev2 = st.multiselect(
            "Categorization 2",
            pr_det_filt1['Categorization (level 2)'].unique(),
            [])

    if cat_lev2 == []: 
        st.text("The subset currently selected contains "
            + str(pr_det_filt1['Flux Name'].nunique()) + " processes ranked in "
            + str(pr_det_filt1['Categorization (level 2)'].nunique()) + " sub-categories.")
        fav = st.multiselect(
            "Interesting Process",
            pr_det_filt1['Flux Name'].unique(),
            [])
        p_d_filtered = pr_det_filt1[process_details['Flux Name'].isin(fav)]
        
    else :
        pr_det_filt2 = pr_det_filt1[process_details['Categorization (level 2)'].isin(cat_lev2)]
        cat_lev3 = st.multiselect(
            "Categorization 3",
            pr_det_filt2['Categorization (level 3)'].unique(),
            [])

        if cat_lev3 == [] : 
            st.text("The subset currently selected contains "
                + str(pr_det_filt2['Flux Name'].nunique()) + " processes ranked in "
                + str(pr_det_filt2['Categorization (level 3)'].nunique()) + " sub-categories.")
            
            fav = st.multiselect(
                "Interesting Process",
                pr_det_filt2['Flux Name'].unique(),
                [])

            p_d_filtered = pr_det_filt2[process_details['Flux Name'].isin(fav)]

        else:
            pr_det_filt3 = pr_det_filt2[process_details['Categorization (level 3)'].isin(cat_lev3)]
            cat_lev4 = st.multiselect(
                        "Categorization 4",
                        pr_det_filt3['Categorization (level 4)'].unique(),
                        [])
            if cat_lev4 == [] :
                st.text("The subset currently selected contains "
                    + str(pr_det_filt3['Flux Name'].nunique()) + " processes.")
            
                fav = st.multiselect(
                    "Interesting Process",
                    pr_det_filt3['Flux Name'].unique(),
                    [])
                
                p_d_filtered = pr_det_filt3[process_details['Flux Name'].isin(fav)]

            else : 
                pr_det_filt4 = pr_det_filt3[process_details['Categorization (level 4)'].isin(cat_lev4)]
            
                fav = st.multiselect(
                    "Interesting Process",
                    pr_det_filt4['Flux Name'].unique(),
                    [])

                p_d_filtered = pr_det_filt4[process_details['Flux Name'].isin(fav)]


    #Possibilité de ne montrer que les lignes qui ont au moins une valeur ? -> ne fonctionne pas
    for index in p_d_filtered.index: 
        p_d_filtered.loc[index] = p_d_filtered.loc[index].str.strip()

    p_d_filtered = p_d_filtered.loc[:, ~p_d_filtered.apply(lambda x: all(v == '' for v in x), axis=0)] 

    if p_d_filtered.shape[0] != 0 :
        st.dataframe(p_d_filtered.T,
                    use_container_width=True,)

if __name__ == '__main__':
    main()