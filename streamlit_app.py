import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('my parents healthy dinner')
streamlit.header('Breakfast menu')
streamlit.text('🍌Omega 3 & blueberry oatmeal')
streamlit.text('🍌kale.spinach & rocket smoothie')
streamlit.text('🍌Hard boiled free range egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.dataframe(my_fruit_list)
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not_fruit_choice:
    streamlite.error('enter the correct fruit name')
  else:
    streamlit.write('The user entered ', fruit_choice)
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)

  
except URLError as e:
  streamlit.error()
    
streamlit.stop()

#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values('from streamlit')")
my_data_row = my_cur.fetchall()
streamlit.header("Hello from Snowflake:")
streamlit.dataframe(my_data_row)

my_add_fruit = streamlit.text_input('what fruit do you want to add?','apple')
streamlit.write('the user entered',my_add_fruit)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + my_add_fruit)

