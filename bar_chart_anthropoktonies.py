import matplotlib.pyplot as plt
import json
from PIL import Image, ImageDraw, ImageFont

# JSON data
data_json = '''
{
    "2000": 282,
    "2005": 253,
    "2010": 250,
    "2015": 280,
    "2020": 232,
    "2023": 265
}
'''

# Parse JSON data
data = json.loads(data_json)

# Extract years and values for the chart
years = list(data.keys())
values = list(data.values())

# Chart customization variables
bar_color = "black"  # Color of the bars
font_family = "Arial"  # Font for labels and title
font_size = 18  # Font size for labels and title
source_text = "Πηγή: Ελληνική Στατιστική Αρχή"  # Source text
source_font_size = 17  # Font size for the source
watermark_text = "www.interai.gr"  # Watermark text

# Configure font for Greek text (for Matplotlib)
plt.rcParams['font.family'] = font_family
plt.rcParams['font.size'] = font_size

# Create the bar chart
plt.figure(figsize=(12, 8), dpi=100)
plt.bar(years, values, color=bar_color, width=0.6)

# Add labels and title
plt.title("Ανθρωποκτονίες με δόλο, ετήσια δεδομένα", pad=20)
plt.xlabel("", labelpad=10)
plt.ylabel("")  # No label for the Y-axis

# Add values on top of the bars
for i, value in enumerate(values):
    plt.text(i, value + 5, str(value), ha='center', va='bottom', fontsize=17)

# Add source text
plt.text(
    0, -0.16, source_text, fontsize=source_font_size, ha='left', transform=plt.gca().transAxes
)

# Adjust layout and save the main chart image
plt.ylim(0, 350)
plt.subplots_adjust(bottom=0.15, top=0.85)
# plt.tight_layout()
main_image_path = "Ανθρωποκτονίες_με_δόλο_Ετήσια_Δεδομένα.png"
plt.savefig(main_image_path)
plt.close()

# Generate a watermarked version of the main image
watermarked_image_path = "Ανθρωποκτονίες_με_δόλο_Ετήσια_Δεδομένα_watermarked.png"
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

# Generate a thumbnail of the watermarked image
thumbnail_image_path = "Ανθρωποκτονίες_με_δόλο_Ετήσια_Δεδομένα_thumbnail.png"
with Image.open(watermarked_image_path) as img:
    img.thumbnail((500, 375))  # Set thumbnail size
    img.save(thumbnail_image_path)

print(f"Main image saved: {main_image_path}")
print(f"Watermarked image saved: {watermarked_image_path}")
print(f"Watermarked thumbnail saved: {thumbnail_image_path}")
