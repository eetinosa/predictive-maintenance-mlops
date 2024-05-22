import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Parameters
num_samples = 10000
start_date = datetime(2023, 1, 1)

# Generate timestamps
timestamps = [start_date + timedelta(minutes=10*i) for i in range(num_samples)]

# Generate random data
np.random.seed(42)
temperature = np.random.normal(70, 10, num_samples)
vibration = np.random.normal(5, 2, num_samples)
pressure = np.random.normal(100, 20, num_samples)
failure = np.random.choice([0, 1], num_samples, p=[0.98, 0.02])

# Categorical data
machine_ids = np.random.choice(['A', 'B', 'C', 'D'], num_samples)
operator_ids = np.random.choice(['OP1', 'OP2', 'OP3', 'OP4'], num_samples)

# Text data
comments = ["All systems go", "Minor delay", "Under maintenance", "Performance check", "Operational"] * (num_samples // 5)
random.shuffle(comments)

# Highly correlated features
pressure_squared = pressure ** 2
temperature_pressure_ratio = temperature / (pressure + 1)

# Missing values
temperature[np.random.choice(num_samples, size=200, replace=False)] = np.nan
vibration[np.random.choice(num_samples, size=200, replace=False)] = np.nan

# Create DataFrame
data = {
    'timestamp': timestamps,
    'temperature': temperature,
    'vibration': vibration,
    'pressure': pressure,
    'failure': failure,
    'machine_id': machine_ids,
    'operator_id': operator_ids,
    'comments': comments[:num_samples],
    'pressure_squared': pressure_squared,
    'temperature_pressure_ratio': temperature_pressure_ratio
}

df = pd.DataFrame(data)

# Extract date features
df['day_of_week'] = df['timestamp'].dt.dayofweek
df['month'] = df['timestamp'].dt.month
df['hour'] = df['timestamp'].dt.hour

# Save to CSV
df.to_csv('data/sensor_data.csv', index=False)
print("Sample dataset generated and saved to 'data/sensor_data.csv'")
