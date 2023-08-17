import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

### Title ###
st.title('Streamlit 超入門')

### SideBar ###
st.sidebar.write('Interactive Widgets')

text = st.sidebar.text_input('あなたの趣味を教えてください。')
condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)

'あなたの趣味：',text
'コンディション：',condition




