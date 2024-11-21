import matplotlib.pyplot as plt
import json
from PIL import Image, ImageDraw, ImageFont

# Sample JSON data for testing
data_json = '''
{
    "Πρωτεΐνη": {"Roast Beef": 58, "Lentil Soup": 8},
    "Φυτικές Ίνες": {"Roast Beef": 0, "Lentil Soup": 13},
    "Ψευδάργυρος (Zn)": {"Roast Beef": 73, "Lentil Soup": 6},
    "Σελήνιο (Se)": {"Roast Beef": 55, "Lentil Soup": 2},
    "Φολικό Οξύ": {"Roast Beef": 3, "Lentil Soup": 39},
    "Βιταμίνη B-12": {"Roast Beef": 104, "Lentil Soup": 0}
}
'''

# Parse JSON data
data = json.loads(data_json)

# Extract labels and values for the chart
nutrients = list(data.keys())
roast_beef_values = [data[nutrient]["Roast Beef"] for nutrient in nutrients]
lentil_soup_values = [data[nutrient]["Lentil Soup"] for nutrient in nutrients]

# Variables for customization
bar_width = 0.4  # Width of each bar
bar_color_rb = "#A84A40"  # Color for Roast Beef bars
bar_color_ls = "#B59B64"  # Color for Lentil Soup bars
font_family = "Arial"  # Font for labels and title
font_size = 12  # Font size for labels and title
source_text = "Πηγή: Δεδομένα Διατροφής"  # Source text
source_font_size = 11  # Font size for the source
watermark_text = "www.interai.gr"  # Watermark text

# Configure font for Greek text (for Matplotlib)
plt.rcParams['font.family'] = font_family
plt.rcParams['font.size'] = font_size

# Create a grouped bar chart
plt.figure(figsize=(12, 8), dpi=100)
x = range(len(nutrients))  # X-axis positions
plt.bar([pos - bar_width / 2 for pos in x], roast_beef_values, bar_width, color=bar_color_rb, label="Ψητό μοσχάρι")
plt.bar([pos + bar_width / 2 for pos in x], lentil_soup_values, bar_width, color=bar_color_ls, label="Σούπα Φακής")

# Customize chart
plt.xlabel("Θρεπτικά Συστατικά", labelpad=10)
plt.ylabel("% Ημερήσιας Συνιστώμενης Ποσότητας", labelpad=10)
plt.title("Σύγκριση Θρεπτικών Συστατικών (100γρ)", pad=15)
plt.xticks(x, nutrients, rotation=20, ha='right')
plt.legend(loc="upper right")
plt.subplots_adjust(bottom=0.25)

# Add source text
plt.text(
    0, -0.2, source_text, fontsize=source_font_size, ha='left', transform=plt.gca().transAxes
)

# Save the main image
main_image_path = "Σύγκριση_Θρεπτικών_Συστατικών.png"
plt.savefig(main_image_path)
plt.close()

# Generate a watermarked version of the basic image
watermarked_image_path = "Σύγκριση_Θρεπτικών_Συστατικών_watermarked.png"
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
thumbnail_image_path = "Σύγκριση_Θρεπτικών_Συστατικών_thumbnail.png"
with Image.open(watermarked_image_path) as img:
    img.thumbnail((500, 375))  # Set thumbnail size
    img.save(thumbnail_image_path)

print(f"Main image saved: {main_image_path}")
print(f"Watermarked image saved: {watermarked_image_path}")
print(f"Watermarked thumbnail saved: {thumbnail_image_path}")
