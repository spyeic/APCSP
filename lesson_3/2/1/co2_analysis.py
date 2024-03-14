import matplotlib.pyplot as plt
import pandas as pd
import math


co2_data = pd.read_csv("co2_data.csv", header=0)
print(co2_data)
co2_data['Average'] = co2_data['Average'].replace(-99.99, math.nan)
print(co2_data)
co2_data.dropna(subset=['Average'], inplace=True)
print(co2_data)

plt.plot(co2_data["decimal_year"], co2_data["Average"], color="blue")
plt.ylabel("CO2 in ppm")
plt.xlabel("Years")
plt.title("Change in CO2 Levels")
plt.show()
exit()

# TODO #3: Plot LOWESS in a line graph
plt.plot(co2_data["Year"], co2_data["LOWESS"], color="red")
# plt.show()

# TODO #4: Use matplotlib to make a bar chart
plt.bar(co2_data["Year"], co2_data["Anomaly"], align="center", color="green")
plt.ylabel("Temperature Anomalies in Celsius")
plt.xlabel("Years")
plt.title("Change in Temperatures")
plt.show()

# TODO #5: Calculate min, max, and avg anomaly and the corresponding min/max years
min_anomaly = co2_data["Anomaly"][0]
max_anomaly = co2_data["Anomaly"][0]
min_year = co2_data["Year"][0]
max_year = co2_data["Year"][0]
sum_anomaly = 0
avg_anomaly = 0

for i in range(len(co2_data["Anomaly"])):
    if co2_data["Anomaly"][i] < min_anomaly:
        min_anomaly = co2_data["Anomaly"][i]
        min_year = co2_data["Year"][i]
    if co2_data["Anomaly"][i] > max_anomaly:
        max_anomaly = co2_data["Anomaly"][i]
        max_year = co2_data["Year"][i]
    sum_anomaly += co2_data["Anomaly"][i]

avg_anomaly = sum_anomaly / len(co2_data["Anomaly"])
print("Min anomaly: ", min_anomaly, " in year ", min_year)
print("Max anomaly: ", max_anomaly, " in year ", max_year)
print("Average anomaly: ", avg_anomaly)
print("Sum of anomalies: ", sum_anomaly)

