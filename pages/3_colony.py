import streamlit as st



st.title(f"So you want to colonize {st.session_state.name}?")


st.markdown(f"Colonizing {st.session_state.name} will give you a number of benefits depending on the amount of effort you put in your colonization. There are four tiers of colonization. Every new tier comes at a new cost. \n * #### **Colonization I --$100** \n You plant a flag and the planet is yours. This is documented in an NFT (Non-Fungible Token) and includes the story and the artwork. \n * #### **Colonization II --$200** \n You start to perform scientific research on your new planet, next to the NFT you'll get the artwork printed out on the highest quality foto print with high quality perspex. \n \n If you want to colonize this planet send a message to daan@vandervorm.com and include the name of the planet you wnat to colonize.")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

