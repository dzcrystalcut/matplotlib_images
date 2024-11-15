import matplotlib.pyplot as plt
import json

# Sample JSON data for testing: Number of car accidents per day for a week
data_json = '''
{
    "Monday": 10,
    "Tuesday": 15,
    "Wednesday": 7,
    "Thursday": 20,
    "Friday": 25,
    "Saturday": 13,
    "Sunday": 18
}
'''

# Parse JSON data
data = json.loads(data_json)

# Extract days and accident numbers
days = list(data.keys())
accidents = list(data.values())

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(days, accidents, color="skyblue")
plt.xlabel("Days of the Week")
plt.ylabel("Number of Car Accidents")
plt.title("Car Accidents Per Day Over a Week")
plt.savefig("car_accidents_bar_chart.png", dpi=100)
plt.show()
