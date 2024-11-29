import streamlit as st
import pandas as pd
from modules.nav import Navbar
from modules.datasets import load_process_data, load_proc_imp, load_proc_imp_npt

st.title(f'⚖️ Comparative rankings within categories')

def main():
    Navbar()

process_details = load_process_data()
proc_imp = load_proc_imp()

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
on = st.toggle("Cross-indicators comparison in npt")

if on: # Indicates one comparison as a stacked horizontal bar chart with npt score
    data = load_proc_imp_npt().iloc[:, :14] 
    data.columns = proc_imp.iloc[0]
    data['score'] = data.sum(axis=1)
    graph_data = data.sort_values(by='score', ascending = False).head(10)
    st.bar_chart(graph_data, x_label = "Impact in npt", y_label = "", horizontal=True)

else : 
    data = proc_imp
    data.columns = proc_imp.iloc[0]
    selection = st.pills("Environmental indicators to compare", data.columns, selection_mode="multi")

    #Pour chaque indicateur sélectionné, on affiche un graphe qui classe le top 10 des process 
    for indicator in selection :
        x_label = "Impact in " + str(proc_imp[indicator][2]) # aller chercher l'unité
        data = data.iloc[3:].astype('float32')
        graph_data = data[indicator].sort_values(ascending=False).head(10)
        st.bar_chart(graph_data, x_label = x_label, y_label = indicator, horizontal=True, stack=False)


if __name__ == '__main__':
    main()