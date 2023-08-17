import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

### Title ###
st.title('Streamlit 超入門')

### main ###
st.write('プログレスバーの表示')
'start!!'

latest_itaration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_itaration.text(f'Itaration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!'
