import pandas as pd
import streamlit as st
from utils.utils import (
    get_simultaneous_travellers,
    get_similar_travellers
)

# Helper functions
# ----------------

def load_txt_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    data = sorted(data)
    return data

def newlines(amount):
    for _ in range(amount):
        st.write('')

# Load data
# ---------

cities = load_txt_data('./src/data/datasets/cities.txt')
companies = load_txt_data('./src/data/datasets/companies.txt')
travel_df = pd.read_csv('./src/data/datasets/augmented_dataset.csv')

# Sidebar
# -------

st.sidebar.title('Settings')
developer_view = st.sidebar.checkbox("Developer view")

# Title and mission statement
# -----------------------------

st.title('Welcome to TraveLink')
st.text('Our mission: Making your trips fun, meaningful, and unforgettable.')
st.markdown('---')

# Collect travel information
# --------------------------

st.header('Enter your travel information')

# Dropdown for selecting arrival city
arrival_city = st.selectbox('Arrival city', cities)

# Input for the company the traveler works for
company = st.selectbox('Company Name', 
                       companies)

# Creating columns for the dates to appear side by side
col1, col2 = st.columns(2)
with col1:
    arrival_date = st.date_input('Arrival Date', format='DD/MM/YYYY')
with col2:
    return_date = st.date_input('Return Date', format='DD/MM/YYYY')

# Collect interest information
# ----------------------------

newlines(1)
st.header('Tell us a bit more about you')

moods = ['Relaxation', 'Sightseeing', 'Adventure', 'Any']

# Dropdown for selecting activity interest
mood = st.selectbox('What kind of activities are you in the mood for?', 
                    moods)

# Dropdown for selecting networking interest
networking = st.selectbox('Are you looking to network and meet new people?', 
                          ['Yes', 'No'])
networking = True if networking == 'Yes' else False

# Dropdown for selecting free time
free_time = st.selectbox('What time of day are you generally free?', 
                         ['Evenings', 'Mornings'])

# Submission
# ----------

newlines(1)
submit_button = st.button('Submit')
st.markdown('---')

if submit_button:
    st.session_state['submitted'] = True
    st.session_state['new_traveller'] = {
        'Trip': None,
        'ID': None,
        'Traveller Name': None,
        'Arrival Date': arrival_date,
        'Return Date': return_date,
        'Departure City': None,
        'Arrival City': arrival_city,
        'company': company,
        'networking': networking,
        'mood': mood,
        'free_time': free_time,
        'accommodation': None
    }

if 'submitted' in st.session_state and st.session_state['submitted']: 

    # Get new traveller data
    new_traveller = pd.DataFrame([st.session_state['new_traveller']]).iloc[0]

    # Get simultaneous travellers
    simultaneous_travellers = get_simultaneous_travellers(travel_df, 
                                                          new_traveller)
    
    # Get simultaneous travellers
    similar_travellers = get_similar_travellers(simultaneous_travellers,
                                                new_traveller)
    
    # Hotel recommendations
    # ---------------------

    st.header('Hotel recommendations')
    hotels = ['Hilton Hotel', 'The Hotel', 'Ibis Hotel', 'Elite Hotel', 'Novotel']
    
    if similar_travellers.empty:
        st.write(f'We recommend the following hotels:')
        for hotel in hotels:
            col1, col2 = st.columns([4, 1])  # Adjust column width ratios as needed
            with col1:
                st.write(f'- {hotel} {arrival_city}')
            with col2:
                st.button('Book now', key=hotel)
    
    else:
        # Count the occurrences of each accommodation and sort them by this count
        accommodation_counts = similar_travellers['accommodation'].value_counts().reset_index()
        accommodation_counts.columns = ['Accommodation', 'Count']  # Renaming columns for clarity
        
        # Sort accommodations by count in descending order
        sorted_accommodations = accommodation_counts.sort_values(by='Count', ascending=False)

        st.write(f'Based on your specific preferences, we recommend any of the following hotels:')
        for index, row in sorted_accommodations.iterrows():
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f'&nbsp;&nbsp;{index + 1}. {str(row["Accommodation"])}  {arrival_city}', unsafe_allow_html=True)
            with col2:
                st.button('Book now', key=row["Accommodation"])

        st.markdown('---')

    # Event recommendations
    # ---------------------

    # TODO: Event recommendations
    
    # Developer view
    # --------------

    if developer_view:
        st.header('Developer view')
        st.write('Simultaneous travellers', simultaneous_travellers)
        st.write('Similar travellers', similar_travellers)

