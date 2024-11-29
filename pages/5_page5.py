import streamlit as st
import pandas as pd
from modules.nav import Navbar
from modules.datasets import load_process_data, load_proc_imp, load_proc_imp_npt

st.title(f'⚖️ Comparative rankings within categories')

def main():
    Navbar()

process_details = load_process_data()
process_details['Flux Name'] = process_details['Flux Name'].str.strip()
proc_imp = load_proc_imp()
level = 0

cat_level_1 = st.multiselect(
    "Categorization 1",
    process_details['Categorization (level 1)'].unique(),
    [])

if cat_level_1 != [] :
    level = 1
    pr_det_filter_1 = process_details[process_details['Categorization (level 1)'].isin(cat_level_1)]
    cat_level_2 = st.multiselect(
        "Categorization 2",
        pr_det_filter_1['Categorization (level 2)'].unique(),
        [])
    
    if cat_level_2 != [] :
        level = 2
        pr_det_filter_2 = process_details[process_details['Categorization (level 2)'].isin(cat_level_2)]
        cat_level_3 = st.multiselect(
            "Categorization 3",
            pr_det_filter_2['Categorization (level 3)'].unique(),
            [])
        
        if cat_level_3 != [] :
            level = 3
            pr_det_filter_3 = process_details[process_details['Categorization (level 3)'].isin(cat_level_3)]

# note globale ou choix d'un indicateur
on = st.toggle("Cross-indicators comparison in npt")

if on: # Indicates one comparison as a stacked horizontal bar chart with npt score
    data = load_proc_imp_npt().iloc[:, :14]
    if level == 3 : 
        data = data[data.index.isin(pr_det_filter_3['Flux Name'])]
    elif level == 2 :
        data = data[data.index.isin(pr_det_filter_2['Flux Name'])]
    elif level == 1 :
        data = data[data.index.isin(pr_det_filter_1['Flux Name'])]

    data.columns = proc_imp.iloc[0]
    data['score'] = data.sum(axis=1)
    graph_data = data.sort_values(by='score', ascending = False).head(10)
    graph_data = graph_data.drop('score', axis=1)
    st.bar_chart(graph_data, x_label = "Impact in npt", y_label = "", horizontal=True)

else : 
    data = proc_imp
    if level == 3 : 
        data = data[data.index.isin(pr_det_filter_3['Flux Name'])]
    elif level == 2 :
        data = data[data.index.isin(pr_det_filter_2['Flux Name'])]
    elif level == 1 :
        data = data[data.index.isin(pr_det_filter_1['Flux Name'])]

    data.columns = proc_imp.iloc[0]
    selection = st.pills("Environmental indicators to compare", data.columns, selection_mode="multi")

    #Pour chaque indicateur sélectionné, on affiche un graphe qui classe le top 10 des process 
    for indicator in selection :
        #x_label = "Impact in " + str(proc_imp[indicator][2]) # aller chercher l'unité
        x_label = ""
        data = data.iloc[3:].astype('float32')
        graph_data = data[indicator].sort_values(ascending=False).head(10)
        st.bar_chart(graph_data, x_label = x_label, y_label = indicator, horizontal=True, stack=False)


if __name__ == '__main__':
    main()