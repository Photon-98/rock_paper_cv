from ultralytics import YOLO
import random
import streamlit as st
from PIL import Image



def extract_user_input(image=None):

    id = "1e2pHejcp96q-NT9VmIDEY_hCA-tiFNef"
    output = "trained_model.pt"
    gdown.download(id = id, output = output, quiet=False)

    model = YOLO(output)

    result = model.predict(image)

    names = model.names
    det_cls = []
    for r in result:
        for c in r.boxes.cls:
            det_cls.append(names[int(c)])
    
    return det_cls[0]


def ai_choice():
    choice = random.randint(0,1000000000)

    if choice <=100000:
        choice = "Rock"
    elif choice >101 and choice <=1000000:
        choice = "Paper"
    else:
        choice = "Scissors"
    return choice

def winner(user_input,ai_input):

    if user_input == "Rock":
        if ai_input == "Scissors":
            return "Player 1"
        elif ai_input == "Paper":
            return "AI"
        else:
            return "Draw!!!"
    if user_input == "Paper":
        if ai_input == "Rock":
            return "Player 1"
        elif ai_input == "Scissors":
            return "AI"
        else:
            return "Draw!!!"
    if user_input == "Scissors":
        if ai_input == "Rock":
            return "AI"
        elif ai_input == "Paper":
            return "Player 1"
        else:
            return "Draw!!!"
        

def main():
    col1, col2 = st.columns(2)
    with st.container():
        st.header("Welcome to the Computer Vison powered Rock-Paper-Scissors Game!")
        st.caption("developed by Indranil Bhattacharyya")

        player_name = st.text_input("Please enter your name, Player!: ")
    
    image = st.camera_input("Please upload your image: ")

    if image:
        st.image(image)

        im = Image.open(image)
        rgb_im = im.convert("RGB")

        # exporting the image
        rgb_im.save("user_input.jpg")
                

        user_input = extract_user_input("user_input.jpg")
        user_input_front_end = player_name + " has selected: " + user_input

        st.code(user_input_front_end)
        ai_choice_var = ai_choice()
        ai_choice_front_end = "AI has selected: " + ai_choice_var
        st.code(ai_choice_front_end)
        winner_name = winner(user_input,ai_choice_var)
    
    with st.container():
        if winner_name == "Player 1":
           
            winner_front_end = player_name + " Wins!!!"
            
            st.success(winner_front_end)
        else:
            if winner_name == "AI":
                winner_front_end = winner_name + " Wins!!!"
            else:
                winner_front_end = "It's a " + winner_name

            st.error(winner_front_end)

if __name__ == "__main__":
    main()       
        

