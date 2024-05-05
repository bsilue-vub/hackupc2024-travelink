import re
import torch
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from transformers import AutoModelForSequenceClassification, AutoTokenizer


# Load tokenizer and model from Hugging Face
tokenizer = AutoTokenizer.from_pretrained('Minej/bert-base-personality')
model = AutoModelForSequenceClassification.from_pretrained('Minej/bert-base-personality')
model.eval()  # Best practice for inference

# Labels for the personality traits based on the model's output configuration
labels = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]

def predict_personality(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():  # Ensure no gradients are calculated during inference
        outputs = model(**inputs)
    logits = outputs.logits
    probabilities = torch.nn.functional.softmax(logits, dim=-1)
    results = {label: prob for label, prob in zip(labels, probabilities[0])}
    return results

def main(df):
    # Initialize a list to store results
    results = []

    for index, row in df.iterrows():
        personality_profile = predict_personality(row['tweet'])
        results.append({
            'Traveller Name': row['Traveller Name'],
            'Tweet': row['tweet'],
            'Personality Profile': personality_profile
        })

    # Convert results to a DataFrame and save or display
    df = pd.DataFrame(results)
    df['Personality Profile'] = df['Personality Profile'].astype(str)

    # Function to manually extract float values from tensor strings
    def extract_trait_value(profile_str, trait):
        # Find the trait in the string and extract the numeric value
        pattern = rf"{trait}': tensor\(([\d\.]+)\)"
        match = re.search(pattern, profile_str)
        if match:
            return float(match.group(1))  # Convert the matched string to float
        return 0.0  # Return 0.0 if no match is found

    # Traits to extract
    traits = ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism']

    # Apply the extraction for each trait
    for trait in traits:
        df[trait] = df['Personality Profile'].apply(lambda x: extract_trait_value(x, trait))

    # Normalize the features for clustering
    scaler = StandardScaler()
    features = df[traits]
    scaled_features = scaler.fit_transform(features)

    # Apply K-Means clustering with 5 clusters
    kmeans = KMeans(n_clusters=5, random_state=0)
    df['cluster'] = kmeans.fit_predict(scaled_features)

    # Group by 'cluster' and list names and tweets
    grouped_names = df.groupby('cluster')
    
    return grouped_names

