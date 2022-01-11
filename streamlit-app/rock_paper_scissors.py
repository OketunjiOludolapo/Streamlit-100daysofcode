import streamlit as st
import random
from PIL import Image
def main():
    st.markdown("<h2> Rock Paper Scissors</h5>",unsafe_allow_html=True)
    col1,col2=st.columns(2)
    with col1:
        st.markdown("**Description of rock-paper-scissors**")
        st.image("images/description of rps.jpg",width=300)
    with col2:
        st.markdown("**Rules of the game**")
        st.image("images/Rules of rps.jpg",width=400)
    rock=Image.open("images/rock.jpg")
    paper=Image.open("images/paper.jpg")
    scissors=Image.open("images/Scissors.jpg")

    game_images = [rock, paper, scissors]
    try:
        user_choice = int(st.number_input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.",min_value=0, max_value=2, value=0, step=1))
        play=st.button("Play")
        if play:
            if user_choice >= 3 or user_choice < 0: 
                st.info("You typed an invalid number, you lose!") 
            else:
                st.markdown("<h5>You chose:</h5",unsafe_allow_html=True)
                st.image(game_images[user_choice])
                computer_choice = random.randint(0, 2)
                st.markdown("<h5>Computer chose:</h5",unsafe_allow_html=True)
                st.image(game_images[computer_choice])


                if user_choice == 0 and computer_choice == 2:
                    st.success("You win!🥁🥁🥁")
                elif computer_choice == 0 and user_choice == 2:
                    st.success("You lose😥😥")
                elif computer_choice > user_choice:
                    st.info("You lose😥😥")
                elif user_choice > computer_choice:
                    st.info("You win!🥁🥁")
                elif computer_choice == user_choice:
                    st.info("It's a draw😊")

    except ValueError:
        st.info("Input a number.")


