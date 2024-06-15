import streamlit as st
import time

def skeleton():
    with st.spinner("Showing skeleton..."):
        placeholder = st.empty()  # creating a placeholder

        # show the skeleton in the placeholder
        from streamlit.proto.Skeleton_pb2 import Skeleton as SkeletonProto
        placeholder._enqueue("skeleton",  SkeletonProto())

        time.sleep(2)  # wait for 2 seconds -> change this to whatever time delay (in seconds) you want

        placeholder.empty() # clear the placeholder
        st.write("Cleared the skeleton") # just to signify that the skeleton has been cleared -> can be removed

