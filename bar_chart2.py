import matplotlib.pyplot as plt
import json
from PIL import Image

# Sample JSON data for testing: Number of car accidents per day for a week
data_json = '''
{
    "Δευτέρα": 10,
    "Τρίτη": 15,
    "Τετάρτη": 7,
    "Πέμπτη": 20,
    "Παρασκευή": 25,
    "Σάββατο": 13,
    "Κυριακή": 18
}
'''

# Parse JSON data
data = json.loads(data_json)

# Extract days and accident numbers
days = list(data.keys())
accidents = list(data.values())

# Configure font for Greek text
plt.rcParams['font.family'] = 'Arial'  # Replace with a Greek-compatible font available in your system

# Create a bar chart
plt.figure(figsize=(10, 7.5))
plt.bar(days, accidents, color="skyblue")
plt.xlabel("Ημέρες της Εβδομάδας")
plt.ylabel("Αριθμός Τροχαίων Ατυχημάτων")
plt.title("Τροχαία Ατυχήματα Ανά Ημέρα")

# Save the main image
main_image_path = "car_accidents_bar_chart.png"
plt.savefig(main_image_path, dpi=100)
plt.show()

# Generate a thumbnail
thumbnail_image_path = "car_accidents_thumbnail.png"
with Image.open(main_image_path) as img:
    img.thumbnail((280, 210))  # Set thumbnail size
    img.save(thumbnail_image_path)
