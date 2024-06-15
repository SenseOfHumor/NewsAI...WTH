import streamlit as st
import sys
import time

import base64

# # To use a local image, but i believe, if a json file is used, the image can be stored in the json file.. dunno, will find out
# with open("flat-design-illustration-wallpaper-preview.jpg", "rb") as f:
#     data = f.read()
#     encoded = base64.b64encode(data)
# data = "data:image/png;base64," + encoded.decode("utf-8")

data = "https://media.cnn.com/api/v1/images/stellar/prod/c-gettyimages-1953206469.jpg?c=16x9&q=w_800,c_fill"


def card1():  ## inspired by https://github.com/gamcoh/st-card
    from streamlit_card import card

    card = card(
    title="",
    text="pip install love",
    image=data,
    #url="https://github.com/gamcoh/st-card"


    styles={
        "card": {
            "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
            "height": "300px" # <- if you want to set the card height to 300px
            
        }
    }

    )



if st.button("show card"):  # function call to test the functionality of the card
    card1()
    from skeletonTest import skeleton
    skeleton()
