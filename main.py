import random

import streamlit as st


def create_seq(num):
    seq = []
    for _ in range(num):
        index = random.randint(0, 3)
        seq.append(cameras_list[index])
    return seq


def show_sequence(camera_sequence, cut_counter=0):
    for cam in camera_sequence[cut_counter:]:
        st.write(cam)


# Your list of items
cameras_list = ["Cam 1", "Cam 2", "Cam 3", "Cam 4"]

st.title("Camera API")

camera_sequence = create_seq(50)

col1, col2, col3 = st.columns(3)

with col1:
    st.write("### Actual")
    show_sequence(camera_sequence, 0)

with col2:
    st.write("### Preview")
    show_sequence(camera_sequence, 1)



create_seq(20)
