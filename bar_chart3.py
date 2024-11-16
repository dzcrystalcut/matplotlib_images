import matplotlib.pyplot as plt
import json
from PIL import Image, ImageDraw, ImageFont

# Sample JSON data for testing: Number of car accidents per day for a week
data_json = '''
{
    "Δευ": 10,
    "Τρι": 15,
    "Τετ": 7,
    "Πεμ": 20,
    "Παρ": 25,
    "Σαβ": 13,
    "Κυρ": 18
}
'''

# Parse JSON data
data = json.loads(data_json)

# Extract days and accident numbers
days = list(data.keys())
accidents = list(data.values())

# Variables for customization
bar_color = "skyblue"  # Customize bar color
font_family = "Arial"  # Font for labels and title
font_size = 12  # Font size for labels and title
source_text = "Πηγή: Ελλ. Στατ. Υπηρ."  # Source text
source_font_size = 11  # Font size for the source

# Configure font for Greek text (for Matplotlib)
plt.rcParams['font.family'] = font_family
plt.rcParams['font.size'] = font_size

# Create a bar chart
plt.figure(figsize=(10, 7.5))  # Figure is a top-level container that holds all the elements of a plot or visualization
plt.bar(days, accidents, color=bar_color)
plt.xlabel("Ημέρες της Εβδομάδας", labelpad=15)  # Adjust label spacing
plt.ylabel("Αριθμός Τροχαίων Ατυχημάτων", labelpad=15)  # Adjust label spacing
plt.title("Τροχαία Ατυχήματα Ανά Ημέρα")

# Adjust padding
# matplotlib.pyplot.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)  # The position of the left edge of the subplots, as a fraction of the figure width.
plt.subplots_adjust(
    left = 0.05,
    bottom = 0.05,
    right = 0.05,
    top = 0.05,
)

# Save the main image
main_image_path = "Τροχαία_Ατυχήματα_Ανά_Ημέρα.png"
plt.savefig(main_image_path, dpi=100, bbox_inches="tight")
plt.close()  # Close the plot to release resources

# Add source text to the image using Pillow
with Image.open(main_image_path) as img:
    # Create a drawing context
    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Load a font for the source text
    try:
        font = ImageFont.truetype("arial.ttf", source_font_size)
    except IOError:
        font = ImageFont.load_default()  # Fallback if Arial is not available

    # Calculate the position for the source text
    text_width, text_height = draw.textbbox((0, 0), source_text, font=font)[2:]
    text_x = (width - text_width) // 2  # Center horizontally
    text_y = height - text_height - 40 

    # Draw the source text
    draw.text((text_x, text_y), source_text, font=font, fill="black")

    # Save the updated image
    img.save(main_image_path)

# Generate a thumbnail
thumbnail_image_path = "Τροχαία_Ατυχήματα_Ανά_Ημέρα_s.png"
with Image.open(main_image_path) as img:
    img.thumbnail((280, 210))  # Set thumbnail size
    img.save(thumbnail_image_path)
