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
font_size = 16  # Font size for labels and title
source_text = "Πηγή: Ελλ. Στατ. Υπηρ."  # Source text
source_font_size = 11  # Font size for the source
watermark_text = "www.interai.gr"  # Watermark text

# Configure font for Greek text (for Matplotlib)
plt.rcParams['font.family'] = font_family
plt.rcParams['font.size'] = font_size

# Create a bar chart
plt.figure(figsize=(10, 7.5), dpi=100)  # Figure is a top-level container that holds all the elements of a plot or visualization
plt.bar(days, accidents, color=bar_color)
plt.xlabel("Ημέρες της Εβδομάδας", labelpad=10)  # Adjust label spacing
plt.ylabel("Αριθμός Τροχαίων Ατυχημάτων", labelpad=10)  # Adjust label spacing
plt.title("Τροχαία Ατυχήματα Ανά Ημέρα", pad=10)
plt.subplots_adjust(bottom=0.15)

plt.text(
    0, -0.17, source_text, fontsize=14, ha='left', transform=plt.gca().transAxes
)

# Save the main image
main_image_path = "Τροχαία_Ατυχήματα_Ανά_Ημέρα.png"
plt.savefig(main_image_path)
plt.close()  # Close the plot to release resources

# Generate a watermarked version of the basic image
watermarked_image_path = "Τροχαία_Ατυχήματα_Ανά_Ημέρα_watermarked.png"
with Image.open(main_image_path) as img:
    draw = ImageDraw.Draw(img)
    width, height = img.size
    try:
        font = ImageFont.truetype("arial.ttf", 72)
    except IOError:
        font = ImageFont.load_default()
    # Calculate text size and position for centering
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]  # Calculate width
    text_height = text_bbox[3] - text_bbox[1]  # Calculate height
    position = ((width - text_width) // 2, (height - text_height) // 2)  # Centered position
    # Draw watermark text
    draw.text(position, watermark_text, fill="rgba(255, 255, 255, 128)", font=font)
    img.save(watermarked_image_path)


# Generate a watermarked thumbnail
thumbnail_image_path = "Τροχαία_Ατυχήματα_Ανά_Ημέρα_thumbnail.png"
with Image.open(watermarked_image_path) as img:
    img.thumbnail((500, 375))  # Set thumbnail size
    img.save(thumbnail_image_path)

print(f"Main image saved: {main_image_path}")
print(f"Watermarked image saved: {watermarked_image_path}")
print(f"Watermarked thumbnail saved: {thumbnail_image_path}")
