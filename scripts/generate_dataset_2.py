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
failure = np.random.choice([0, 1], num_samples, p=[0.95, 0.05])

# Introduce more anomalies leading to failures
anomaly_indices = np.random.choice(np.where(failure == 1)[0], size=200, replace=False)
temperature[anomaly_indices] = np.random.normal(150, 10, size=200)  # High temperature anomaly
vibration[anomaly_indices] = np.random.normal(20, 5, size=200)     # High vibration anomaly
pressure[anomaly_indices] = np.random.normal(200, 30, size=200)    # High pressure anomaly

# Categorical data
machine_ids = np.random.choice(['A', 'B', 'C', 'D'], num_samples)
operator_ids = np.random.choice(['OP1', 'OP2', 'OP3', 'OP4'], num_samples)

# Text data
comments = ["All systems go", "Minor delay", "Under maintenance", "Performance check", "Operational"] * (num_samples // 5)
random.shuffle(comments)

# Update comments for anomalies
for idx in anomaly_indices:
    comments[idx] = "Failure due to anomaly"

# Highly correlated features
pressure_squared = pressure ** 2
temperature_pressure_ratio = temperature / (pressure + 1)

# Missing values
temperature[np.random.choice(num_samples, size=200, replace=False)] = np.nan
vibration[np.random.choice(num_samples, size=200, replace=False)] = np.nan

# Machine age and operational hours
machine_ages = {machine_id: np.random.randint(1, 10) for machine_id in ['A', 'B', 'C', 'D']}
operational_hours = np.cumsum(np.random.exponential(scale=10, size=num_samples))

machine_age = [machine_ages[machine_id] for machine_id in machine_ids]

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
    'temperature_pressure_ratio': temperature_pressure_ratio,
    'machine_age': machine_age,
    'operational_hours': operational_hours
}

df = pd.DataFrame(data)

# Extract date features
df['day_of_week'] = df['timestamp'].dt.dayofweek
df['month'] = df['timestamp'].dt.month
df['hour'] = df['timestamp'].dt.hour

# Save to CSV
df.to_csv('data/sensor_data_2.csv', index=False)
print(" dataset generated and saved to 'data/sensor_data_2.csv'")
