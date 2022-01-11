#Importing all neccessary libraries and modules(the other files)
# Apart from streamlit, all the other imported modules are files with python scripts on the same folder
import streamlit as st
import bmi
import leap
import welcome
import life
import Tip_calculator
import love_calculator
import bill_roulette
import rock_paper_scissors
import password


st.set_page_config(page_title='100 days of code challenge', layout='centered') #setting page name

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True) # Hiding the default nav bar and header

PAGES = { 
    
    "BMI Calculator": bmi,
    "Leap Year Identifier": leap,
    "Life Remainder Program": life,  
    "Tip and Bill Sharing": Tip_calculator,
    "Love Calculator": love_calculator,
   "Pay the bill":bill_roulette,
   "Rock paper scissors":rock_paper_scissors,
   "Password Generator":password
}

choice=st.sidebar.radio("Choose Level",["Welcome","Beginner","Intermediate","Advanced"]) # Creating a radio button for the 4 levels
if choice=="Welcome":
    welcome.main() #this main is the name of the function in the welcome file. Same goes for others
elif choice=="Beginner":
    selection = st.sidebar.radio("Projects", list(PAGES.keys()))
    page = PAGES[selection]
    if selection=="BMI Calculator":
        page.main()
    elif selection=="Leap Year Identifier":
        page.main()
    elif selection=="Life Remainder Program":
        life.main()
    elif selection=="Tip and Bill Sharing":
        Tip_calculator.main()
    elif selection=="Love Calculator":
        love_calculator.main()
    elif selection=="Pay the bill":
        bill_roulette.main()
    elif selection=="Rock paper scissors":
        rock_paper_scissors.main()
    elif selection=="Password Generator":
        password.main()
elif choice=="Intermediate":
    st.markdown("<h3> The challenge is still ongoing and still in the beginners level.</h3>",unsafe_allow_html=True)
    st.image("images/Coming soon.jpg",use_column_width=True) 
else:
    st.markdown("<h3> The challenge is still ongoing and still in the beginners level.</h3>",unsafe_allow_html=True)
    st.image("images/Coming soon.jpg",use_column_width=True) 

# Generating a customized footer
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Created and Developed by <a style='#display: block; text-align: center;' href="https://www.linkedin.com/in/oludolapo-oketunji" target="_blank">Oketunji Oludolapo </a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)