import streamlit as st
import random

def main():
    st.title("Welcome to the Password Generator App!")
    st.markdown("**Get a secured and unhackable password now!!! Save the password on your notepad for future reference.\
        Don't get hacked!!!**")
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',\
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']     

    no_letters = st.number_input("How many letters would you like in your password?",min_value=1)
    no_symbols = st.number_input("How many symbols would you like in your password?",min_value=1)
    no_numbers = st.number_input("How many numbers would you like in your password?",min_value=1)
    generate=st.button("Generate Secure Password")

    if generate:
        password_list=[]
        for i in range(1,no_letters+1):
            p=random.choice(letters)
            password_list.append(p)
        for i in range(1,no_symbols+1):
            p=random.choice(symbols)
            password_list.append(p)
        for i in range(1,no_numbers+1):
            p=random.choice(numbers)
            password_list.append(p)

        random.shuffle(password_list)
        password=""
        for word in password_list:
            password+=word
        message=f"Your secure password is {password}\nMake sure to keep it save somewhere like a notepad"
        st.success(message)
    else:
        st.info("What are you waiting for? Click the button to get your secure password!!!")

