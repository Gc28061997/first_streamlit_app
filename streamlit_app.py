import streamlit
import pandas
streamlit.title('My Parent New healthy diner')
streamlit.header('Breakfast Favriots')
streamlit.text('🥣 omega 3 and Blueberry Oatmeal')
streamlit.text(' 🥗 Kale,Spinach & Rocket Smoothei')

streamlit.text('🐔 Hard Boiled Free_Rang Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

