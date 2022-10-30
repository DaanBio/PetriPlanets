import streamlit as st
import pandas as pd
import time
import random 


df=pd.read_excel("database2.xlsx")


images=st.empty()


#st.title("PetriPlanets MVP")
col1, col2 = st.columns(2)

with col1:

    if st.button("Travel to the next planet"):
        with images.container():
            randnum=random.randint(0, (df.shape[0]-1))
            url1=df["url"][randnum]
            st.markdown(f"![Foo]({url1})")
            st.title(df['Name'][randnum])
            st.markdown(df['stories'][randnum])
            

    
    else:
        pass



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
