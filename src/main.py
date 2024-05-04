import streamlit as st

# Title and mission statement
# -----------------------------

st.title('Welcome to TraveLink')
st.text('Our mission: Making your trip fun, meaningful, and hopefully unforgettable.')

# Collecting travel information
# -----------------------------

st.header('Enter Your Travel Information')

# Load city and company options from file
def load_cities(file_path):
    with open(file_path, 'r') as file:
        cities = file.read().splitlines()
    return cities

cities = load_cities('./src/data/datasets/cities.txt')
companies = load_cities('./src/data/datasets/companies.txt')

# Dropdown for selecting arrival city
arrival_city = st.selectbox('Select your arrival city.', cities)

# Input for the company the traveler works for
company = st.selectbox('Company Name', 
                       companies)

# Creating columns for the dates to appear side by side
col1, col2 = st.columns(2)
with col1:
    arrival_date = st.date_input('Arrival Date', format="DD/MM/YYYY")
with col2:
    return_date = st.date_input('Return Date', format="DD/MM/YYYY")

# Submission button
if st.button('Submit'):
    st.success('Travel Information Received')
    st.write('Arrival City:', arrival_city)
    st.write('Company:', company)
    st.write('Arrival Date:', arrival_date)
    st.write('Return Date:', return_date)
    # TODO: Insert this retrieved data into a DataFrame and process it further
