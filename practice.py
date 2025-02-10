import pandas as pd
import random
import seaborn as sns  
import numpy as np
import matplotlib.pyplot as plt

# Variables for generating data
names = ['Emily', 'Sarah', 'Jessica', 'Amanda', 'Beth', 'Olivia', 'Hannah', 'Sophia', 'Grace', 'Mia']
locations = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami', 'Boston', 'Dallas', 'San Francisco', 'Seattle', 'Atlanta']
sock_types = ['Ankle', 'Crew', 'No-Show', 'Knee-High', 'Toe', 'Thigh-High', 'Slip-On', 'Low-Cut']
smell_indicators = ['Yes', 'No']
smell_descriptions = ['Cheesy', 'Fresh', 'Vinegar', 'Neutral', 'Musty', 'Sour', 'Sweaty', 'Floral']
prices = [round(random.uniform(3.99, 15.99), 2) for _ in range(50000)]

# Generating the larger dataset
data_large = {
    'Name': [random.choice(names) for _ in range(50000)],
    'Age': [random.randint(20, 25) for _ in range(50000)],
    'Location': [random.choice(locations) for _ in range(50000)],
    'Sock Type': [random.choice(sock_types) for _ in range(50000)],
    'Smell Indicator': [random.choice(smell_indicators) for _ in range(50000)],
    'Smell Description': [random.choice(smell_descriptions) for _ in range(50000)],
    'Price': prices
}

# Creating the large pandas DataFrame
df = pd.DataFrame(data_large)
print(df)

df1 = df[  (df['Location'].isin(['Chicago', 'Dallas']) ) & (df['Smell Description'] == 'Sour'  ) ] [['Name', 'Price', 'Location', 'Smell Description']]
print(df1.head())