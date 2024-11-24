import matplotlib.pyplot as plt
import json
from PIL import Image, ImageDraw, ImageFont
import textwrap

# JSON data
data_json = '''
{
  "Περιφέρεια Αττικής": {
    "πριν από το 1980": 848195,
    "1980 και μετά": 788478,
    "Ποσοστά": {
      "πριν από το 1980": "52%",
      "1980 και μετά": "48%"
    }
  },
  "Περιφερειακή ενότητα Θεσσαλονίκης": {
    "πριν από το 1980": 208880,
    "1980 και μετά": 248241,
    "Ποσοστά": {
      "πριν από το 1980": "46%",
      "1980 και μετά": "54%"
    }
  },
  "Υπόλοιπον Ελλάδος": {
    "πριν από το 1980": 1064149,
    "1980 και μετά": 1161207,
    "Ποσοστά": {
      "πριν από το 1980": "48%",
      "1980 και μετά": "52%"
    }
  }
}
'''

# Parse JSON data
data = json.loads(data_json)

# Extract locations and values
locations = list(data.keys())
percentages_before_1980 = [int(data[location]["Ποσοστά"]["πριν από το 1980"].strip('%')) for location in locations]
percentages_after_1980 = [int(data[location]["Ποσοστά"]["1980 και μετά"].strip('%')) for location in locations]
values_before_1980 = [data[location]["πριν από το 1980"] for location in locations]
values_after_1980 = [data[location]["1980 και μετά"] for location in locations]

# Variables for customization
font_family = "Arial"
font_size = 18
source_text = "Πηγή: Απογραφή 2021, Ελληνική Στατιστική Αρχή"  # Source text
source_font_size = 17
watermark_text = "www.interai.gr"

# Configure font for Greek text (for Matplotlib)
plt.rcParams['font.family'] = font_family
plt.rcParams['font.size'] = font_size

# Create a grouped bar chart
plt.figure(figsize=(12, 8), dpi=100)
x = range(len(locations))  # X-axis positions for locations
bar_width = 0.4

bars_before = plt.bar(
    [pos - bar_width / 2 for pos in x],
    percentages_before_1980,
    bar_width,
    color="red",
    label="πριν από το 1980"
)
bars_after = plt.bar(
    [pos + bar_width / 2 for pos in x],
    percentages_after_1980,
    bar_width,
    color="grey",
    label="1980 και μετά"
)

plt.ylim(0, 80)

# Add absolute numbers above each bar
for bars, values in [(bars_before, values_before_1980), (bars_after, values_after_1980)]:
    for bar, value in zip(bars, values):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 2,  # Slightly above the bar
            f"{value:,}".replace(",", "."),
            ha="center",
            fontsize=17,
            color="black",
        )

# Customize chart
plt.title("Κατοικούμενες κατοικίες ανά περίοδο κατασκευής", pad=15)
wrapped_labels = [textwrap.fill(label, width=20) for label in locations]
plt.xticks(x, wrapped_labels, ha='center')

plt.legend(
    ["πριν από το 1980", "μετά από το 1980"],  # Labels for the legend
    loc="upper left",  # Location of the legend
    fontsize=17,  # Font size for the legend text
    frameon=True,  # Add a border around the legend
    facecolor="white",  # Background color of the legend
    edgecolor="black"  # Border color of the legend
)


plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x)}%"))

plt.subplots_adjust(bottom=0.15)

# Add source text
plt.text(
    0, -0.18, source_text, fontsize=source_font_size, ha='left', transform=plt.gca().transAxes
)

# Save the main image
main_image_path = "Κατοικούμενες_Κατοικίες_Ανά_Περίοδο_Κατασκευής.png"
plt.savefig(main_image_path)
plt.close()

# Generate a watermarked version of the basic image
watermarked_image_path = "Κατοικούμενες_Κατοικίες_Ανά_Περίοδο_Κατασκευής_watermarked.png"
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

# Generate a thumbnail version of the watermarked image
thumbnail_image_path = "Κατοικούμενες_Κατοικίες_Ανά_Περίοδο_Κατασκευής_thumbnail.png"
with Image.open(watermarked_image_path) as img:
    img.thumbnail((500, 375))  # Set thumbnail size
    img.save(thumbnail_image_path)

print(f"Main image saved: {main_image_path}")
print(f"Watermarked image saved: {watermarked_image_path}")
print(f"Thumbnail image saved: {thumbnail_image_path}")
