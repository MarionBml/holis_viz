import streamlit as st
import pandas as pd
from modules.nav import Navbar
from modules.datasets import load_process_data, load_proc_imp, load_proc_imp_npt 

st.title(f'📈 Environmental Impact visualisations')

def main():
    Navbar()

process_details = load_process_data()
process_details['Flux Name']=process_details['Flux Name'].str.strip()
proc_imp = load_proc_imp()

cat_lev1 = st.multiselect(
    "Categorization 1",
    process_details['Categorization (level 1)'].unique(),
    [])

if cat_lev1 == [] : 
    pro = st.selectbox(
            "Which process are you interested in ?",
            process_details['Flux Name'].unique(),
            index=None,
            placeholder="Select process...",)

else : 
    pr_det_filt1 = process_details[process_details['Categorization (level 1)'].isin(cat_lev1)]
    cat_lev2 = st.multiselect(
            "Categorization 2",
            pr_det_filt1['Categorization (level 2)'].unique(),
            [])

    if cat_lev2 == []: 
        st.text("The subset currently selected contains "
            + str(pr_det_filt1['Flux Name'].nunique()) + " processes ranked in "
            + str(pr_det_filt1['Categorization (level 2)'].nunique()) + " sub-categories.")
        pro = st.selectbox(
            "Which process are you interested in ?",
            pr_det_filt1['Flux Name'].unique(),
            index=None,
            placeholder="Select process...",)
        if pro != None :
            p_d_filtered = pr_det_filt1[process_details['Flux Name'] == pro]
        
    else :
        pr_det_filt2 = pr_det_filt1[process_details['Categorization (level 2)'].isin(cat_lev2)]
        pro = st.selectbox(
            "Which process are you interested in ?",
            pr_det_filt2['Flux Name'].unique(),
            index=None,
            placeholder="Select process...",)

on = st.toggle("Visualisation in npt")

if on: # 
    data = load_proc_imp_npt()
    units = ["npt"] * 14
    
    if pro != None :
        stacked = st.toggle("Stacked")
        score = round(data.loc[pro].sum(),2)
        st.text("This process has a total environmental score of " + str(score) + " npt.")
        graph_data = data[data.index == pro]
        graph_data.columns = proc_imp.iloc[0]
        graph_data = graph_data.drop('Climate change', axis=1) # On enlève Climate change, pour ne pas compter en double climate change fossils et climate change biogénique 

        # On réorganise les valeurs par ordre décroissant

        if stacked :
            st.bar_chart(graph_data, x_label = 'Score in npt', horizontal=True, stack=None)
        else :
            st.bar_chart(graph_data, x_label = 'Score in npt', y_label = "Environmental indicators", horizontal=True, stack=False)
    
else : 
    data = proc_imp
    data.columns = proc_imp.iloc[0]
    units = data.iloc[2]

    if pro != None :
        gr0, gr1, gr2 = st.columns(3)
        gr0_data = { 'Value': float(data[data.index == pro].iloc[:,0]) , 'Max': float(data.iloc[3:,0].max())}
        gr0.bar_chart(gr0_data, x_label = data.columns[0], y_label=units[0], stack=False)

        gr1_data = { 'Value': float(data[data.index == pro].iloc[:,1]) , 'Max': float(data.iloc[3:,1].max())}
        gr1.bar_chart(gr1_data, x_label = data.columns[1], y_label=units[1], stack=False)

        gr2_data = { 'Value': float(data[data.index == pro].iloc[:,2]) , 'Max': float(data.iloc[3:,2].max())}
        gr2.bar_chart(gr2_data, x_label = data.columns[2], y_label=units[2], stack=False)

        gr3, gr4, gr5 = st.columns(3)
        gr3_data = { 'Value': float(data[data.index == pro].iloc[:,3]) , 'Max': float(data.iloc[3:,3].max())}
        gr3.bar_chart(gr3_data, x_label = data.columns[3], y_label=units[3], stack=False)

        gr4_data = { 'Value': float(data[data.index == pro].iloc[:,4]) , 'Max': float(data.iloc[3:,4].max())}
        gr4.bar_chart(gr4_data, x_label = data.columns[4], y_label=units[4], stack=False)

        gr5_data = { 'Value': float(data[data.index == pro].iloc[:,5]) , 'Max': float(data.iloc[3:,5].max())}
        gr5.bar_chart(gr5_data, x_label = data.columns[5], y_label=units[5], stack=False)
    
        gr6, gr7, gr8 = st.columns(3)
        gr6_data = { 'Value': float(data[data.index == pro].iloc[:,6]) , 'Max': float(data.iloc[3:,6].max())}
        gr6.bar_chart(gr6_data, x_label = data.columns[6], y_label=units[6], stack=False)

        gr7_data = { 'Value': float(data[data.index == pro].iloc[:,7]) , 'Max': float(data.iloc[3:,7].max())}
        gr7.bar_chart(gr7_data, x_label = data.columns[7], y_label=units[7], stack=False)

        gr8_data = { 'Value': float(data[data.index == pro].iloc[:,8]) , 'Max': float(data.iloc[3:,8].max())}
        gr8.bar_chart(gr8_data, x_label = data.columns[8], y_label=units[8], stack=False)

        gr9, gr10, gr11 = st.columns(3)
        gr9_data = { 'Value': float(data[data.index == pro].iloc[:,9]) , 'Max': float(data.iloc[3:,9].max())}
        gr9.bar_chart(gr9_data, x_label = data.columns[9], y_label=units[9], stack=False)

        gr10_data = { 'Value': float(data[data.index == pro].iloc[:,10]) , 'Max': float(data.iloc[3:,10].max())}
        gr10.bar_chart(gr10_data, x_label = data.columns[10], y_label=units[10], stack=False)

        gr11_data = { 'Value': float(data[data.index == pro].iloc[:,11]) , 'Max': float(data.iloc[3:,11].max())}
        gr11.bar_chart(gr11_data, x_label = data.columns[11], y_label=units[11], stack=False)

        gr12, gr13, gr14 = st.columns(3)
        gr12_data = { 'Value': float(data[data.index == pro].iloc[:,12]) , 'Max': float(data.iloc[3:,12].max())}
        gr12.bar_chart(gr12_data, x_label = data.columns[12], y_label=units[12], stack=False)

        gr13_data = { 'Value': float(data[data.index == pro].iloc[:,13]) , 'Max': float(data.iloc[3:,13].max())}
        gr13.bar_chart(gr13_data, x_label = data.columns[13], y_label=units[13], stack=False)



if pro != None:
    with st.expander("See indicator values"):

        col1, col2 = st.columns(2)
        col1.metric("Acidification", data.loc[pro][0], delta= units[0], delta_color="off")
        col2.metric("Ozone depletion", data.loc[pro][1], delta= units[1], delta_color="off")
    
        col3, col4 = st.columns(2)
        col3.metric("Climate change", data.loc[pro][2], delta= units[2], delta_color="off")
        col4.metric("Climate change-Biogenic", data.loc[pro][3], delta= units[3], delta_color="off")

        col5, col6 = st.columns(2)
        col5.metric("Climate change-Fossil", data.loc[pro][4], delta= units[4], delta_color="off")
        col6.metric("Freshwater eutrophication", data.loc[pro][5], delta= units[5], delta_color="off")

        col7, col8 = st.columns(2)
        col7.metric("Marine eutrophication", data.loc[pro][6], delta= units[6], delta_color="off")
        col8.metric("Terrestrial eutrophication", data.loc[pro][7], delta= units[7], delta_color="off")

        col9, col10 = st.columns(2) 
        col9.metric("Photochemical ozone formation", data.loc[pro][8], delta= units[8], delta_color="off")
        col10.metric("Particulate matter", data.loc[pro][9], delta= units[9], delta_color="off")

        col11, col12 = st.columns(2)
        col11.metric("Ionising radiation", data.loc[pro][10], delta= units[10], delta_color="off")
        col12.metric("Fossile resource use", data.loc[pro][11], delta= units[11], delta_color="off")

        col13, col14 = st.columns(2)
        col13.metric("Minerals and metal resource use", data.loc[pro][12], delta= units[12], delta_color="off")
        col14.metric("Land use", data.loc[pro][13], delta= units[13], delta_color="off")

if __name__ == '__main__':
    main()