import pandas as pd

raw_data = pd.read_csv(r'data/raw_energy_data.csv')

raw_data.dropna(inplace=True)
raw_data['timestamp'] = pd.to_datetime(raw_data['timestamp'])

daily_data = raw_data.resample('D', on='timestamp').mean().reset_index()
daily_data.rename(columns={'timestamp': 'date'}, inplace=True)

daily_data.to_excel('data/processed_energy_data.xlsx', index=False)
print("Energy data processed and saved.")
