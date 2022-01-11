import streamlit as st

def main():
    """A love calculator"""
    st.image("images/love.jpg")
    st.markdown("<h5>Welcome to the Love Calculator!</h5>",unsafe_allow_html=True)
    st.markdown("<h8> Not to be taken seriously. Just for fun😍</h8>",unsafe_allow_html=True)

    name1 = st.text_input("What is your name? \n").lower()
    name2 = st.text_input("What is their name? \n").lower()
    check=st.button("Check Your Compatibility")

    concate_both=name1+name2
    t=concate_both.count("t")
    r=concate_both.count("r")
    u=concate_both.count("u")
    e=concate_both.count("e")

    true=t+r+u+e

    l=concate_both.count("l")
    o=concate_both.count("o")
    v=concate_both.count("v")
    e=concate_both.count("e")

    love=l+o+v+e

    score=int(str(true)+str(love))
    if check:
        if name1=="" and name2=="":
            st.warning("Enter both names")
        elif name1=="":
            st.warning("Enter Your Name")
        elif name2=="":
            st.warning("Enter Your Crush's Name")
        
        else:

            if (score < 10) or (score >90):
                st.info(f"Your love score is {score},you go together like coke and mentos.")
            elif (score>=40) and (score<=50):
                st.info(f"Your score is {score},you are alright together")
            else:
                st.info(f"Your score is {score}, you are not compatible")