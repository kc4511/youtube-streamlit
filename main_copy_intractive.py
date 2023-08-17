import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title('Streamlit 超入門')

st.write('Interactive Widgets')

### Slider ###
condition = st.slider('あなたの今の調子は？',0,100,50)
'コンディション：',condition

### TextBox ###
# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味：',text

### SelectBox ###
# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、',option,'です。'

### CheckBox ###
# if st.checkbox('Show Image'):
#     img = Image.open('img_test.jpg')
#     st.image(img, caption='kazuta', use_column_width=True)



