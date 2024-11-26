import psycopg2
from psycopg2.extras import Json


# Variables for the new record
stats_data = {
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
tags = "Αλλοδαποί, Φύλο Αλλοδαπών, Στατιστικές Αλλοδαπών"
slug = "Ποσοστά-ανδρών-γυναικών-κατά-ιθαγένεια-241126"
source = "Πηγή: Απογραφή 2021, Ελληνική Στατιστική Αρχή"
# source = "Πηγή: Ελληνική Στατιστική Αρχή"
title = "Αξιοσημείωτα ποσοστά ανδρών - γυναικών κατά ιθαγένεια στην Ελλάδα"
description = "Στο παρόν γράφημα παρουσιάζονται τα ποσοστά ανδρών γυναικών στο σύνολο των αλλοδαπών και επιλεγμένων χωρών στη χώρα μας. Επιθυμείται να δειχθεί ότι κάποιες κοινωνικές ομάδες βρίσκονται σε ανισορροπία από άποψη κατανομής του φύλου και ενδεχόμενα αυτό έχει ευρύτερες κοινωνικές επιπτώσεις."
w_image_file_path = "/stats_images_watermarked/Αξιοσημείωτα_Ποσοστά_Αλλοδαπών_Ανδρών_Γυναικών_watermarked.png"
image_file_path = "/stats_images/Αξιοσημείωτα_Ποσοστά_Αλλοδαπών_Ανδρών_Γυναικών.png"
thumbnail_file_path = "/stats_thumbnails/Αξιοσημείωτα_Ποσοστά_Αλλοδαπών_Ανδρών_Γυναικών_thumbnail.png"

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
