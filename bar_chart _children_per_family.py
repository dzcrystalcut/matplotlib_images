import matplotlib.pyplot as plt
import json
from PIL import Image, ImageDraw, ImageFont

# JSON data for the number of families and percentages
data_json = '''
{
  "1_children_families": 1028658,
  "1_children_families_percentage": 53.3,
  "2_children_families": 720909,
  "2_children_families_percentage": 37.4,
  "3_children_families": 144023,
  "3_children_families_percentage": 7.5,
  "4_children_families": 28641,
  "4_children_families_percentage": 1.5,
  "5_children_families": 6302,
  "5_children_families_percentage": 0.3
}
'''

# Parse JSON data
data = json.loads(data_json)

# Extract categories, values, and percentages
categories = ["1", "2", "3", "4", "5+"]
values = [
    data["1_children_families"],
    data["2_children_families"],
    data["3_children_families"],
    data["4_children_families"],
    data["5_children_families"],
]
percentages = [
    data["1_children_families_percentage"],
    data["2_children_families_percentage"],
    data["3_children_families_percentage"],
    data["4_children_families_percentage"],
    data["5_children_families_percentage"],
]

# Variables for customization
bar_color = "red"  # Color for the bars
font_family = "Arial"  # Font for labels and title
font_size = 18  # Font size for labels and title
source_text = "Πηγή: Απογραφή 2021, Ελληνική Στατιστική Αρχή"  # Source text
source_font_size = 17  # Font size for the source
watermark_text = "www.interai.gr"  # Watermark text

# Configure font for Greek text (for Matplotlib)
plt.rcParams['font.family'] = font_family
plt.rcParams['font.size'] = font_size

# Create a vertical bar chart
plt.figure(figsize=(12, 8), dpi=100)
x = range(len(categories))  # X-axis positions
bars = plt.bar(x, percentages, color=bar_color)

plt.ylim(0, 70)

# Add integers above each bar
for i, bar in enumerate(bars):
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # X position
        bar.get_height() + 2,  # Y position (slightly above the bar)
        f"{values[i]:,}".replace(",", "."),  # Format with dots for thousands
        ha="center",
        fontsize=18,
        color="black",
    )

# Customize chart
plt.xlabel("Αριθμός παιδιών ανά οικογένεια", labelpad=10)
plt.ylabel("Ποσοστό οικογενειών (%)", labelpad=10)
plt.title("Κατανομή Οικογενειών ανά Αριθμό Παιδιών", pad=15)
plt.xticks(x, categories, ha='center')
plt.subplots_adjust(bottom=0.25)

# Add source text
plt.text(
    0, -0.3, source_text, fontsize=source_font_size, ha='left', transform=plt.gca().transAxes
)

# Save the main image
main_image_path = "Κατανομή_Οικογενειών_ανά_Αριθμό_Παιδιών.png"
plt.savefig(main_image_path)
plt.close()

# Generate a watermarked version of the basic image
watermarked_image_path = "Κατανομή_Οικογενειών_ανά_Αριθμό_Παιδιών_watermarked.png"
with Image.open(main_image_path) as img:
    draw = ImageDraw.Draw(img)
    width, height = img.size
    try:
        font = ImageFont.truetype("arial.ttf", 72)
    except IOError:
        font = ImageFont.load_default()
    # Calculate text size and position for centering
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    position = ((width - text_width) // 2, (height - text_height) // 2)
    # Draw watermark text
    draw.text(position, watermark_text, fill="rgba(255, 255, 255, 128)", font=font)
    img.save(watermarked_image_path)

# Generate a watermarked thumbnail
thumbnail_image_path = "Κατανομή_Οικογενειών_ανά_Αριθμό_Παιδιών_thumbnail.png"
with Image.open(watermarked_image_path) as img:
    img.thumbnail((500, 375))  # Set thumbnail size
    img.save(thumbnail_image_path)

print(f"Main image saved: {main_image_path}")
print(f"Watermarked image saved: {watermarked_image_path}")
print(f"Watermarked thumbnail saved: {thumbnail_image_path}")
