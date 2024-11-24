import psycopg2
from psycopg2.extras import Json


# Variables for the new record
stats_data = {
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
tags = "Κατοικίες, Περιφέρεια Αττικής, Περιφερειακή ενότητα Θεσσαλονίκης, Αντισεισμικός Σχεδιασμός Κτιριακών Κατασκευών"
slug = "Κατοικούμενες-κατοικίες-ανά-περίοδο-κατασκευής-241124"
# source = "Πηγή: Απογραφή 2021, Ελληνική Στατιστική Αρχή"
source = "Πηγή: Απογραφή 2021, Ελληνική Στατιστική Αρχή"
title = "Κατοικούμενες κατοικίες ανά περίοδο κατασκευής"
description = "Στο παρόν γράφημα παρουσιάζεται η κατανομή των κατοικούμενων κατοικιών ανά περίοδο κατασκευής, πριν και μετά το 1980, για την Περιφέρεια Αττικής, την Περιφερειακή ενότητα Θεσσαλονίκης και το Υπόλοιπον Ελλάδος. Στο βαθμό που οι κατοικίες πριν το 1980, δεν σχεδιαζόντουσαν με αυστηρά αντισεισμικά κριτήρια και λόγω ηλικίας των κτιρίων, το ποσοστό των κτιρίων που κατασκευάστηκαν πριν το 1980, αντανακλά τον κίνδυνο μειωμένων αντοχών σε περιπτώσεις ισχυρών σεισμών."
w_image_file_path = "/stats_images_watermarked/Κατοικούμενες_Κατοικίες_Ανά_Περίοδο_Κατασκευής_watermarked.png"
image_file_path = "/stats_images/Κατοικούμενες_Κατοικίες_Ανά_Περίοδο_Κατασκευής.png"
thumbnail_file_path = "/stats_thumbnails/Κατοικούμενες_Κατοικίες_Ανά_Περίοδο_Κατασκευής_thumbnail.png"

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
