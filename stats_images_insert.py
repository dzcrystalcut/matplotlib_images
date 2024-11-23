import psycopg2
from psycopg2.extras import Json


# Variables for the new record
stats_data = {
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
tags = "Παιδιά, Οικογένεια, Παιδιά ανά οικογένεια"
slug = "Κατανομή-Οικογενειών-ανά-Αριθμό-Παιδιών-241123"
source = "Πηγή: Απογραφή 2021, Ελληνική Στατιστική Αρχή"
title = "Κατανομή Οικογενειών ανά Αριθμό Παιδιών"
description = "Στο παρόν γράφημα παρουσιάζεται η Κατανομή Οικογενειών ανά Αριθμό Παιδιών προκειμένου να δειχθεί το μεγάλο ποσοστό των οικογενειών με ένα παιδί, γεγονός που θα έχει σημαντικές επιπτώσεις στην κοινωνία."
w_image_file_path = "/stats_images_watermarked/Κατανομή_Οικογενειών_ανά_Αριθμό_Παιδιών_watermarked.png"
image_file_path = "/stats_images/Κατανομή_Οικογενειών_ανά_Αριθμό_Παιδιών.png"
thumbnail_file_path = "/stats_thumbnails/Κατανομή_Οικογενειών_ανά_Αριθμό_Παιδιών.png"

# Database connection details
db_config = {
    "dbname": "et",           # Replace with your database name
    "user": "postgres",  # Replace with your username
    "password": "Georgia",  # Replace with your password
    "host": "209.105.239.52",      # Replace with your database host
    "port": 5432              # Default PostgreSQL port
}

try:
    # Connect to the database
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()
    
    # Insert query
    query = """
        INSERT INTO stats_images (
            stats_data, tags, slug, source, title, description, 
            w_image_file_path, image_file_path, thumbnail_file_path
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    # Execute the query
    cursor.execute(query, (
        Json(stats_data), tags, slug, source, title, description, 
        w_image_file_path, image_file_path, thumbnail_file_path
    ))
    
    # Commit the transaction
    connection.commit()
    print("Record inserted successfully!")

except psycopg2.Error as e:
    print(f"An error occurred: {e}")
finally:
    # Close the connection
    if connection:
        cursor.close()
        connection.close()
