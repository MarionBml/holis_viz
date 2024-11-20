import streamlit as st

from modules.nav import Navbar

def main():
    Navbar()

    st.title(f'📈 Environmental Impact visualisations')


if __name__ == '__main__':
    main()