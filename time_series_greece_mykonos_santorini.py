import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Load the JSON file
file_path = "greece-mykonos-santorini-pageviews-20151101-20241031.json"
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract the three series
series_labels = ["Greece", "Santorini", "Mykonos"]
series_data = {series["page"]: series for series in data}

# Parse the data for each series, extracting only monthly values
monthly_data = {}
for label in series_labels:
    monthly_data[label] = {k: v for k, v in series_data[label].items() if k.startswith("201") or k.startswith("202")}

# Convert to a DataFrame
df = pd.DataFrame(monthly_data).astype(float)

# Sort by date and ensure all months are covered
df.index = pd.to_datetime(df.index, format="%Y-%m")
df = df.sort_index()

# Plot the time series
plt.figure(figsize=(10, 7), dpi=100)
plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 18

colors = ["blue", "green", "red"]  # Colors for the lines

for i, label in enumerate(series_labels):
    # Plot the actual data
    plt.plot(df.index, df[label], label=label, color=colors[i])

    # Add the label directly to the line
    plt.text(
        df.index[-1],  # Position at the last point of the line
        df[label].iloc[-1],  # The last value of the series
        label,  # The name of the series
        fontsize=18,
        color=colors[i],
        ha="left",
        va="center",
    )

    # Calculate and plot the trendline
    x_numeric = np.arange(len(df.index))
    coefficients = np.polyfit(x_numeric, df[label], 1)  # Linear fit
    trendline = np.polyval(coefficients, x_numeric)
    plt.plot(df.index, trendline, linestyle="--", color=colors[i], alpha=0.6)

# Customize chart
plt.title("Επισκέψεις σελίδων στη Wikipedia από 11/2015 έως 10/2024 ανά μήνα", pad=25, fontsize=18)
plt.xlabel("Μήνας", labelpad=5)
plt.ylabel("Επισκέψεις", labelpad=5)

# Format x-axis labels to show only January labels in Greek
x_labels = [dt.strftime("%b %Y") if dt.month == 1 else "" for dt in df.index]
plt.xticks(
    ticks=df.index[df.index.month == 1],  # Only include indices where the month is January
    labels=[f"ΙAN {dt.year}" for dt in df.index if dt.month == 1],
    rotation=45,
    ha="right",
    fontsize=18
)
plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", ".")))

# Remove the legend
plt.legend().remove()
plt.subplots_adjust(left=0.15, bottom=0.25, right=0.90, top=0.85)

# Add source text
plt.text(
    0, -0.35, "Πηγή: Wikipedia", fontsize=16, ha="left", transform=plt.gca().transAxes
)

# Save the main image
main_image_path = "greece_mykonos_santorini_wikipedia_pageviews_timeseries.png"

plt.savefig(main_image_path)
plt.close()

# Generate a watermarked version of the main image
watermarked_image_path = "greece_mykonos_santorini_wikipedia_pageviews_timeseries_watermarked.png"
with Image.open(main_image_path) as img:
    draw = ImageDraw.Draw(img)
    width, height = img.size
    watermark_text = "www.interai.gr"
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
thumbnail_image_path = "greece_mykonos_santorini_wikipedia_pageviews_timeseries_thumbnail.png"
with Image.open(watermarked_image_path) as img:
    img.thumbnail((500, 375))  # Set thumbnail size
    img.save(thumbnail_image_path)

print(f"Main image saved: {main_image_path}")
print(f"Watermarked image saved: {watermarked_image_path}")
print(f"Thumbnail image saved: {thumbnail_image_path}")
