import streamlit
import pandas

streamlit.title("My parents new healthy dinner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega 3 & Blueberry oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket smoothie")
streamlit.text("🐔 Hard-boiled Free-Range egg")
streamlit.text("🥑🍞 Avocado Toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberry'])
