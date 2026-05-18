import pandas as pd

data = pd.read_csv("clean_sensor_data.txt",header=None)
data.columns = ["Sensor_Value"]
print(data)
print(data.describe())

high_values = data[data["Sensor_Value"] > 50]
print(high_values)
high_values.to_csv("high_sensor_values.csv", index = False)
