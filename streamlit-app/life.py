import streamlit as st

def main():
    """A script to calculate estimated remainder of life"""
    st.markdown('<h5>A program to calculate the remainder of our lives in years,months,weeks and days\
        with the assumption that we live for 90 years</h5>', unsafe_allow_html=True)
    age=st.number_input("what is your current age? ",min_value=1)
    calculate=st.button("Calculate")
    if calculate:
        years_remaining= 90-age

        months_remaining= years_remaining*12

        weeks_remaining= years_remaining*52

        days_remaining= years_remaining*365

        total_remaining=f"Assuming you would live to 90 years, you have {years_remaining} years left,{months_remaining} months remaining,\
        {weeks_remaining} weeks remaining and {days_remaining} days left. Ensure you use them wisely. Good Luck!!!"

        st.info(total_remaining) 
    else:
        st.info("Enter a valid age and click on the Calculate button")