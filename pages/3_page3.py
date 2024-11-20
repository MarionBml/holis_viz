import streamlit as st

from modules.nav import Navbar

def main():
    Navbar()

    st.title(f'👁️ Environmental indicator explanations')


if __name__ == '__main__':
    main()