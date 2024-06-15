import streamlit as st
import time

def skeleton():
    with st.spinner("Showing skeleton..."):
        placeholder = st.empty()  # create a placeholder

        # show the skeleton in the placeholder
        from streamlit.proto.Skeleton_pb2 import Skeleton as SkeletonProto
        placeholder._enqueue("skeleton",  SkeletonProto())

        time.sleep(2)  # wait for 2 seconds

        placeholder.empty() 
        st.write("Cleared the skeleton") # clear the placeholder


if st.button("show skeleton"):
        skeleton()