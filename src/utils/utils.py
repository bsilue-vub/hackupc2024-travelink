import pandas as pd

def get_simultaneous_travellers(df, new_traveller):
    """
    Identify travellers who will be in the same city during 
    the overlapping date range of a new traveller.

    Arguments
    ---------
    df (DataFrame):        The dataframe containing existing traveller data.
    new_traveller (dict):  A DataFrame row with travel info of the new traveller.
    
    Returns
    -------
    DataFrame:             A subset of df with entries of people who will be 
                           in the same city during the overlapping timeframe.

    """
    # Convert the dates in the dataframe to datetime format if not already done
    df['Arrival Date'] = pd.to_datetime(df['Arrival Date'], 
                                          format='%d/%m/%Y')
    df['Return Date'] = pd.to_datetime(df['Return Date'], 
                                       format='%d/%m/%Y')
    
    # Extract data from the new traveller row
    arrival_city = new_traveller['Arrival City']
    arrival_date = pd.to_datetime(new_traveller['Arrival Date'], 
                                    format='%d/%m/%Y')
    return_date = pd.to_datetime(new_traveller['Return Date'], 
                                 format='%d/%m/%Y')
    
    # Filter for travellers who are going to the same city
    same_city_travellers = df[df['Arrival City'] == arrival_city]

    # Filter for date overlaps
    overlapping_travellers = same_city_travellers[
        (same_city_travellers['Arrival Date'] <= return_date) &
        (same_city_travellers['Return Date'] >= arrival_date)
    ]
    
    return overlapping_travellers


if __name__ == '__main__':
    # Load dataset
    df = pd.read_csv('./data/datasets/augmented_dataset.csv')

    # Example new traveller
    new_traveller = pd.DataFrame([{
        'Arrival City': 'Paris',
        'Departure Date': '07/11/2024',
        'Return Date': '14/11/2024'
    }]).iloc[0]


    # Get and print simultaneous traveller
    simultaneous_travellers = get_simultaneous_travellers(df, new_traveller)
    print('\n', simultaneous_travellers, '\n')
