import streamlit as st
from modules.datasets import load_expl
from modules.nav import Navbar

st.title(f'👁️ Environmental indicator explanations')

def main():
    Navbar()
# Load data 
cat_impacts = load_expl()


# Pick language 
#on = st.toggle("Switch to french names")

#if on:
    #options = cat_impacts['French Name']
    #selection = st.pills("Indicator.s", options, selection_mode="multi")
    #st.markdown(f"Your selected options: {selection}.")
#else : 
options = cat_impacts['English Name']
selection = st.pills("Indicator.s", options, selection_mode="multi")
    #st.markdown(f"Your selected options: {selection}.")
    
#Possibilité de garder une option sélectionnée si on switch de langue en cours de route ? 

c_i_filtered = cat_impacts[options.isin(selection)]

#Possibilité de ne montrer que les lignes qui ont au moins une valeur ?

if c_i_filtered.shape[0] != 0 :
    st.dataframe(c_i_filtered.T,
                use_container_width=True,)


if __name__ == '__main__':
    main()
    
