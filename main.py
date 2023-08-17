import streamlit as st
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

### 2カラムレイアウト ###
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

### expader ###
expader = st.expander('お問い合わせ1')
expader.write('お問合せ回答1')
expader = st.expander('お問い合わせ2')
expader.write('お問合せ回答2')
expader = st.expander('お問い合わせ3')
expader.write('お問合せ回答3')
expader = st.expander('お問い合わせ4')
expader.write('お問合せ回答4')
expader = st.expander('お問い合わせ5')
expader.write('お問合せ回答5')

