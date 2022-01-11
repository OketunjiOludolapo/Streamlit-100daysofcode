import streamlit as st
import random

def main():
    """A script to choose who's to pay the bill"""
    st.markdown("<h5> Who will pay today's bill?🤠🤡</h5>",unsafe_allow_html=True)
    names_string = st.text_input("Give me everybody's names, separated by a comma. ")
    names = names_string.split(",")
    name=names_string.split(", ")
    check=st.button("Check")
    length=len(names)

    random_choice=random.randint(0,length-1)
    payer=names[random_choice]
    if check:
       
        if "," not in names_string:
            st.warning("Enter atleast two names")
        else:
            if names or name:
                st.info(f"{payer} will pay this bill")
            

    
  
    
