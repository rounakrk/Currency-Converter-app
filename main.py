import numpy as np
import pandas as pd
import json
import requests
import streamlit as st
import datetime
import PIL
from PIL import Image
from currency import all_currencies

def gui():

    url="https://static4.depositphotos.com/1001877/509/i/950/depositphotos_5093742-stock-photo-currency-exchange-dollar.jpg"
    im = Image.open(requests.get(url, stream=True).raw)
    im = im.resize((500,500))

    st.sidebar.title("Money Exchange")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.image(im, use_column_width=True)
    st.title("Currency Converrter")

    number = st.number_input('Input the Value')
    number = round(number,2)

    # option = st.sidebar.selectbox(
    # 'Which number do you like best?',
    #  df['first column'])

    # option = st.selectbox('', ['INR','USD'], key=1)
    option = st.selectbox('', all_currencies, key=1)

    value = st.empty()

    option2 = st.selectbox('', all_currencies, key=2)

    left_column, right_column = st.beta_columns(2)
    pressed = left_column.button('Press me?')
    if pressed:
        sta = str(option)+"_"+str(option2)
        url = "https://free.currconv.com/api/v7/convert?q="+sta+"&compact=ultra&apiKey=<apikey>"
        response = requests.get(url)
        status_get = response.content
        status_get = status_get.decode('utf-8')
        status_json = json.loads(status_get)
        value.success(status_json[sta]*number)
        converter = "1 "+option+" = "+str(status_json[sta])+" "+option2
        right_column.write(converter)
        # st.write(status_json[sta])

if __name__=="__main__": 
    gui()