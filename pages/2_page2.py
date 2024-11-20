import streamlit as st
import pandas as pd
from modules.nav import Navbar

def main():
    Navbar()
    st.title(f'🔍 Metadata Overview')


@st.cache_data
def load_data():    
    process_details = pd.read_excel('data/BI_2.02__02_Procedes_Details.xlsx', index_col=1)
    process_details = process_details.T
    process_details.columns = process_details.columns.str.strip()
    process_details.set_index('UUID', inplace = True)
    process_details = process_details.drop(process_details.columns[[5, 7, 8, 9, 10]],axis = 1)
    process_details.drop(process_details.index[0], inplace = True)
    process_details.rename(columns={process_details.columns[1]: "Flux Name" }, inplace = True)
    process_details.drop(process_details.columns[process_details.nunique() == 1], axis=1, inplace=True)
    process_details = process_details.drop(['Biomass ratio', 'Thermal solar ratio', 'Geothermal ratio', 'Tide ratio', 
                                        'Other ratio comment', 'Transmission losses consider', 'Losses ratio',  'Mix comment'], axis=1)
    return process_details

process_details = load_data()

if __name__ == '__main__':
    main()