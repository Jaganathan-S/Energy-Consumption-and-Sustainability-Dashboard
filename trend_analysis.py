import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('data/processed_energy_data.xlsx')


plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['temperature'], marker='o', label='Average Temperature (°C)')
plt.title('Average Daily Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.savefig('data/temperature_trends.png')
plt.show()
print("Temperature trends analyzed and plotted.")
