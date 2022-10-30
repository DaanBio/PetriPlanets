import streamlit as st
import pandas as pd
import time
import random 
from streamlit.components.v1 import html

def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)

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
            name=df['Name'][randnum]
            if 'name' not in st.session_state:
                st.session_state.name = name
            st.title(name)
            st.markdown(df['stories'][randnum])
    else:
        pass
    if 'name' not in st.session_state:
        pass
    
    else:         
        if st.button(f"Colonize planet {st.session_state.name}"):
            nav_page("colony")
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
