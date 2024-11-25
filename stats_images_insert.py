import psycopg2
from psycopg2.extras import Json


# Variables for the new record
stats_data = {
    "2000": 282,
    "2005": 253,
    "2010": 250,
    "2015": 280,
    "2020": 232,
    "2023": 265
}
tags = "Δολοφονίες"
slug = "Ανθρωποκτονίες-με-δόλο-ετήσια-δεδομένα-241125"
# source = "Πηγή: Απογραφή 2021, Ελληνική Στατιστική Αρχή"
source = "Πηγή: Ελληνική Στατιστική Αρχή"
title = "Ανθρωποκτονίες με δόλο, ετήσια δεδομένα"
description = "Στο παρόν γράφημα παρουσιάζεται η κατανομή των Ανθρωποκτονιών με δόλο με ετήσια δεδομένα για 6 έτη μεταξύ των ετών 2020-2023. Το γράφημα καταδεικνύει ότι για πάνω από 20 χρόνια δεν έχει σημειωθεί καμία πρόοδος στην αποφυγή των δολοφονιών."
w_image_file_path = "/stats_images_watermarked/Ανθρωποκτονίες_με_δόλο_Ετήσια_Δεδομένα_watermarked.png"
image_file_path = "/stats_images/Ανθρωποκτονίες_με_δόλο_Ετήσια_Δεδομένα.png"
thumbnail_file_path = "/stats_thumbnails/Ανθρωποκτονίες_με_δόλο_Ετήσια_Δεδομένα_thumbnail.png"

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
