import streamlit as st

def main():
    """Leap year checker"""
    st.write("<h5>A program for checking if a year is a leap year</h5>",unsafe_allow_html=True)
    year=st.number_input("Enter your year of interest",min_value=1800)
    leap=st.button("Check the year")
    if leap:
        if year%4==0:
            if year%100==0:
                if year%400:
                    st.info("leap year")
                else:
                    st.info("Not a leap year")
            else:
                st.info("leap year")
        else:
            st.info("Not a leap year")