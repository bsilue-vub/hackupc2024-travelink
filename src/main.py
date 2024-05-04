import streamlit as st

# Title of the page
st.title('My First Streamlit App')

# Header/Subheader
st.header('This is a header')
st.subheader('This is a subheader')

# Text
st.text('Hello Streamlit. This is regular text.')

# Displaying code
st.text('This is a code block:')
st.code('import numpy as np', language='python')

# Display data
st.write('Here is some json data:')
st.write({'Name': 'Alice', 'Age': 25})

# Display a table
import pandas as pd
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write('Here is a table:')
st.table(df)

# Display a chart
st.write('Here is a chart:')
st.line_chart(df)
