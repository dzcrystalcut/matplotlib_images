import matplotlib.pyplot as plt
import json
from PIL import Image, ImageDraw, ImageFont
import textwrap

# JSON data
data_json = '''
{
  "Συνολικά": {
    "Άνδρες": 389689,
    "Γυναίκες": 375913,
    "Ποσοστά": {
      "Άνδρες": "51%",
      "Γυναίκες": "49%"
    }
  },
  "Πακιστάν": {
    "Άνδρες": 33494,
    "Γυναίκες": 1812,
    "Ποσοστά": {
      "Άνδρες": "95%",
      "Γυναίκες": "5%"
    }
  },
  "Μπαγκλαντές": {
    "Άνδρες": 16049,
    "Γυναίκες": 1137,
    "Ποσοστά": {
      "Άνδρες": "93%",
      "Γυναίκες": "7%"
    }
  },
  "Αίγυπτος": {
    "Άνδρες": 9254,
    "Γυναίκες": 3199,
    "Ποσοστά": {
      "Άνδρες": "74%",
      "Γυναίκες": "26%"
    }
  },
  "Τουρκία": {
    "Άνδρες": 3146,
    "Γυναίκες": 2459,
    "Ποσοστά": {
      "Άνδρες": "56%",
      "Γυναίκες": "44%"
    }
  },
  "Ουκρανία": {
    "Άνδρες": 3106,
    "Γυναίκες": 13302,
    "Ποσοστά": {
      "Άνδρες": "19%",
      "Γυναίκες": "81%"
    }
  }
}
'''

# Parse JSON data
data = json.loads(data_json)

# Extract locations and values
locations = list(data.keys())
percentages_men = [int(data[location]["Ποσοστά"]["Άνδρες"].strip('%')) for location in locations]
percentages_women = [int(data[location]["Ποσοστά"]["Γυναίκες"].strip('%')) for location in locations]
values_men = [data[location]["Άνδρες"] for location in locations]
values_women = [data[location]["Γυναίκες"] for location in locations]

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

bars_men = plt.bar(
    [pos - bar_width / 2 for pos in x],
    percentages_men,
    bar_width,
    color="#3399FF",
    label="Άνδρες"
)
bars_women = plt.bar(
    [pos + bar_width / 2 for pos in x],
    percentages_women,
    bar_width,
    color="pink",
    label="#FF6699"
)

plt.ylim(0, 120)

# Add absolute numbers above each bar
# for bars, values in [(bars_men, values_men), (bars_women, values_women)]:
#     for bar, value in zip(bars, values):
#         plt.text(
#             bar.get_x() + bar.get_width() / 2,
#             bar.get_height() + 2,  # Slightly above the bar
#             f"{value:,}".replace(",", "."),
#             ha="center",
#             fontsize=17,
#             color="black",
#         )

# Customize chart
plt.title("Αξιοσημείωτα ποσοστά ανδρών - γυναικών κατά ιθαγένεια", pad=20)
wrapped_labels = [textwrap.fill(label, width=20) for label in locations]
plt.xticks(x, wrapped_labels, ha='center')

plt.legend(
    ["Άνδρες", "Γυναίκες"],  # Labels for the legend
    loc="upper right",  # Location of the legend
    fontsize=17,  # Font size for the legend text
    frameon=True,  # Add a border around the legend
    facecolor="white",  # Background color of the legend
    edgecolor="black"  # Border color of the legend
)

plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x)}%"))

plt.subplots_adjust(bottom=0.15)

# Add source text
plt.text(
    0, -0.18, source_text, fontsize=source_font_size, ha='left', transform=plt.gca().transAxes)

# Add absolute numbers above each bar
for bars, values, label in [(bars_men, values_men, "Άνδρες"), (bars_women, values_women, "Γυναίκες")]:
    for bar, value, location in zip(bars, values, locations):
        if label == "Άνδρες" and location == "Συνολικά":
            # Move upward only for Συνολικά men's number
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 7,  # Higher position for Συνολικά men's number
                f"{value:,}".replace(",", "."),
                ha="center",
                fontsize=17,
                color="black",
            )
        elif not (label == "Άνδρες" and location == "Συνολικά"):
            # Default position for all other cases
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 2,  # Default position
                f"{value:,}".replace(",", "."),
                ha="center",
                fontsize=17,
                color="black",
            )

    


# Save the main image
main_image_path = "Αξιοσημείωτα_Ποσοστά_Αλλοδαπών_Ανδρών_Γυναικών.png"
plt.savefig(main_image_path)
plt.close()

# Generate a watermarked version of the basic image
watermarked_image_path = "Αξιοσημείωτα_Ποσοστά_Αλλοδαπών_Ανδρών_Γυναικών_watermarked.png"
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
thumbnail_image_path = "Αξιοσημείωτα_Ποσοστά_Αλλοδαπών_Ανδρών_Γυναικών_thumbnail.png"
with Image.open(watermarked_image_path) as img:
    img.thumbnail((500, 375))  # Set thumbnail size
    img.save(thumbnail_image_path)

print(f"Main image saved: {main_image_path}")
print(f"Watermarked image saved: {watermarked_image_path}")
print(f"Thumbnail image saved: {thumbnail_image_path}")
