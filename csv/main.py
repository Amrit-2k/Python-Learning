import pandas

data = pandas.read_csv("csv/weather_data.csv")


monday = data[data.day == "Monday"]

# Get data in column
monday_temp = int(monday.temp)

# Get data in row
monday_temp_F = int(monday.temp) * 9/5 + 32

print(monday_temp_F)

