import streamlit as st

# Helper functions
# ----------------

def load_txt_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    data = sorted(data)
    return data

def newlines(amount):
    for _ in range(amount):
        st.write("")

# Title and mission statement
# -----------------------------

st.title('Welcome to TraveLink')
st.text('Our mission: Making your trip fun, meaningful, and hopefully unforgettable.')

# Collect travel information
# --------------------------

st.header('Enter your travel information')

cities = load_txt_data('./src/data/datasets/cities.txt')
companies = load_txt_data('./src/data/datasets/companies.txt')

# Dropdown for selecting arrival city
arrival_city = st.selectbox('Arrival city', cities)

# Input for the company the traveler works for
company = st.selectbox('Company Name', 
                       companies)

# Creating columns for the dates to appear side by side
col1, col2 = st.columns(2)
with col1:
    arrival_date = st.date_input('Arrival Date', format="DD/MM/YYYY")
with col2:
    return_date = st.date_input('Return Date', format="DD/MM/YYYY")

# Collect interest information
# ----------------------------
newlines(1)
st.header('Tell us more about you')

travel_interests = ['Relaxation', 'Sightseeing', 'Adventure', 'Any']

# Dropdown for selecting travel interest
travel_interest = st.selectbox('What type travel do you enjoy most?', 
                               travel_interests)

# Dropdown for selecting networking interest
networking = st.selectbox('Are you in the mood to network and meet new people?', 
                               ["Yes", "No"])

# Dropdown for selecting free time
free_time = st.selectbox('What time of day are you generally free?', 
                         ["Evenings", "Mornings"])

# Submission
# ----------

newlines(3)

if st.button('Submit'):
    st.success('Travel Information Received')
    st.write('Arrival City:', arrival_city)
    st.write('Company:', company)
    st.write('Arrival Date:', arrival_date)
    st.write('Return Date:', return_date)
    # TODO: Insert this retrieved data into a DataFrame and process it further