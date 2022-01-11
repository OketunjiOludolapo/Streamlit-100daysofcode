import streamlit as st



def main():
    """"A BMI Calculator"""
    st.image("images/bmi.jpg",width=300)
    st.markdown("One of the most important aspects of the human health is the body mass index (BMI).\
        Being able to calculate your BMI enables you to determine your total body fat at any given time.\
        Whether you're a man, woman or teen, you can learn how to calculate your BMI using the BMI calculator")
    #Asking for height and weight
    height=st.number_input("Enter your height(m)",min_value=1)
    weight=st.number_input("Enter your weight(kg)",min_value=1)
    calculate=st.button("Calculate")
    if calculate:
        bmi=float(weight)/float(height)**2
        if bmi<18.5:
            st.success(f"Your bmi is {bmi},thus you are underweight")
        elif bmi>18.5 and bmi<25:
            st.success(f"Your bmi is {bmi},thus you have normal weight")
        elif bmi>25 and bmi<35:
            st.success(f"Your bmi is {bmi},thus you are obese")
        else:
            st.warning(f"Your bmi is {bmi},thus you are clinically obese")






