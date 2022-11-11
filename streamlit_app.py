import streamlit

streamlit.title('my parents healthy dinner')
streamlit.header('Breakfast menu')
streamlit.text('🍌Omega 3 & blueberry oatmeal')
streamlit.text('🍌kale.spinach & rocket smoothie')
streamlit.text('🍌Hard boiled free range egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
