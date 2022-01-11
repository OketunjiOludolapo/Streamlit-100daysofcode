import streamlit as st

def main():
    """A script to calculate tip and share bills"""
    st.markdown("<h5>Easily calculate your tip and share bill between friends</h5",unsafe_allow_html=True)
    bill = st.number_input("What was the total bill? $",min_value=1)
    tip = st.number_input("How much tip would you like to give(%)?",min_value=5)
    people = st.number_input("How many people to split the bill?",min_value=1)
    calculate=st.button("Calculate")
    tip_as_percent = tip / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)
    if calculate:
        if people < 2:
            st.info(f"Your final bill is {final_amount}")
        else:
            Share=f"Each person should pay: ${final_amount}"
            st.info(Share)

