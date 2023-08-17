import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

### Title ###
st.title('Streamlit 超入門')

### main ###
st.write('Interactive Widgets')

### 2カラムレイアウト ###
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

### expader ###
expader = st.expander('お問い合わせ')
expader.write('問合せ回答1')
expader.write('問合せ回答2')
expader.write('問合せ回答3')
expader.write('問合せ回答4')
expader.write('問合せ回答5')




