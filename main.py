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
camera_sequence = ['Cam 1', 'Cam 4', 'Cam 2', 'Cam 1', 'Cam 4', 'Cam 2',
                   'Cam 2', 'Cam 4', 'Cam 1', 'Cam 4', 'Cam 2', 'Cam 1',
                   'Cam 3', 'Cam 1', 'Cam 4', 'Cam 2', 'Cam 1', 'Cam 3',
                   'Cam 2', 'Cam 3', 'Cam 3', 'Cam 4', 'Cam 3', 'Cam 2',
                   'Cam 1', 'Cam 2', 'Cam 4', 'Cam 2', 'Cam 1', 'Cam 3',
                   'Cam 4', 'Cam 1', 'Cam 3', 'Cam 3', 'Cam 2', 'Cam 3',
                   'Cam 3', 'Cam 4', 'Cam 2', 'Cam 3', 'Cam 4', 'Cam 3',
                   'Cam 2', 'Cam 4', 'Cam 2', 'Cam 2', 'Cam 3', 'Cam 1',
                   'Cam 4', 'Cam 3']

st.title("Camera API")

col1, col2, col3 = st.columns(3)

if 'cut_counter' not in st.session_state:
    st.session_state.cut_counter = 0

with col1:
    st.write("### Actual")
    show_sequence(camera_sequence, cut_counter=st.session_state.cut_counter)

with col2:
    st.write("### Preview")
    show_sequence(camera_sequence, cut_counter=st.session_state.cut_counter
                                               + 1)

with col3:
    if st.button("Cut"):
        st.session_state.cut_counter += 1
        print(st.session_state.cut_counter)

create_seq(20)
