import streamlit as st
import pandas as pd
from io import StringIO
import base64

 
# Markdown with HTML to center and color the title
st.markdown(
    '<h1 style="color:red; text-align:center;">Meat Lovers</h1>',
    unsafe_allow_html=True
)



# List of countries
countries = ['Greece', 'Italy', 'Albania', 'Bulgaria', 'Turkey', 'Malta', 'Cyprus', 'Romania', 'Spain', 'Portugal' ,'North Macedonia' ,'Ukrain', 'Moldova' ,'Serbia' , 'Kosovo' , 'Croatia' , 'Slovenia' ,'Switzerland' , 'Austria' , 'Germany' , 'Poland' , 'Netherlands' , 'Belgium' , 'Denmark' , 'Norway' , 'Sweden' , 'Finland' , 'Estonia' , 'Belarus' , 'UK' , 'Ireland' ,'Russia ' ,'United States', 'Canada', 'Mexico', 'Colombia' , 'Venezuela', 'Brazil', 'Peru' ,'Argentina', 'Austarlia', 'China' , 'Japan', 'India']

# Country Selection (Dropdown)
selected_country = st.selectbox("Choose your Country or State", countries)

# Display selected country
st.write(f"You selected: {selected_country}")

# simple file uploader 
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
 
    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)
 
    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)
 
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
