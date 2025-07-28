import streamlit as st
def linia_pozioma():
    st.markdown("""
        <div style="
            height: 100%;
            width: 100%;
            display: flex;
            justify-content: center;
            ">
            <div style="border-bottom: 2px solid gray; width: 100%;"></div>
        </div>
    """, unsafe_allow_html=True)
    
def linia_pionowa():
    st.markdown("""
        <div style="
            height: 100%;
            width: 100%;
            display: flex;
            justify-content: center;
            ">
            <div style="border-right: 2px solid gray; height: 135vh;"></div>
        </div>
        """, unsafe_allow_html=True)
    
def naglowek(tekst, podkreslenie=True):
    if podkreslenie:
        st.markdown(f"<h2 style='text-decoration: underline;'>{tekst}</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2>{tekst}</h2>", unsafe_allow_html=True)