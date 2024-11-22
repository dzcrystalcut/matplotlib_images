import psycopg2
from psycopg2.extras import Json


# Variables for the new record
stats_data = {
    "Πρωτεΐνη": {"Roast Beef": 58, "Lentil Soup": 8},
    "Σίδηρος (Fe)": {"Roast Beef": 21, "Lentil Soup": 10},
    "Ψευδάργυρος (Zn)": {"Roast Beef": 73, "Lentil Soup": 6},
    "Σελήνιο (Se)": {"Roast Beef": 55, "Lentil Soup": 2},
    "Φολικό Οξύ": {"Roast Beef": 3, "Lentil Soup": 39},
    "Βιταμίνη B-12": {"Roast Beef": 104, "Lentil Soup": 0}
}  
tags = "Φακή, Μοσχάρι, Θρεπτικά"
slug = "Σύγκριση-Θρεπτικών-Συστατικών-Μοσχαριού-Φακής-241122"
source = "Πηγή: Υπουργείο Γεωργίας Η.Π.Α. (USDA)"
title = "Σύγκριση Θρεπτικών Συστατικών Μοσχαριού - Φακής (100γρ)"
description = "Στο παρόν γράφημα συγκρίνουμε τις ποσότητες 6 θρεπτικών συστατικών που περιέχονται στο ψητό μοσχάρι και στη σούπα φακής. Η σούπα φακής περιλαμβάνει βρασμένες φακές χωρίς αλάτι ως κύριο συστατικό (40γρ/100γρ). Για τη βάση της συνταγής, χρησιμοποιείται μιρεπουά, δηλαδή ένα μείγμα από μαγειρεμένα καρότα, σέλινο και κρεμμύδι (25γρ/100γρ). Προστίθεται πόσιμο νερό βρύσης (35γρ/100γρ) για το μαγείρεμα, μαζί με μια μικρή ποσότητα επιτραπέζιου αλατιού (0.6γρ/100γρ). Η συνταγή ολοκληρώνεται με την προσθήκη φυτικού λαδιού (0.5γρ/100γρ). Το ψητό μοσχάρι περιλαμβάνει διάφορα κομμάτια μοσχαρίσιου κρέατος, μαγειρεμένα με διαφορετικούς τρόπους. Περιλαμβάνει μοσχάρι από σπάλα χωρίς κόκαλο και μόνο το άπαχο μέρος, μαγειρεμένο και βραστό (25γρ/100γρ), καθώς και μοσχάρι από σπάλα χωρίς κόκαλο με άπαχο και λιπαρό μέρος, μαγειρεμένο και βραστό (25γρ/100γρ). Επιπλέον, περιλαμβάνει μοσχάρι από μηρό χωρίς κόκαλο και μόνο το άπαχο μέρος, μαγειρεμένο και ψητό (25γρ/100γρ), καθώς και μοσχάρι από μηρό χωρίς κόκαλο με άπαχο και λιπαρό μέρος, μαγειρεμένο και ψητό (25γρ/100γρ). Προστίθεται επιτραπέζιο αλάτι σε μικρή ποσότητα (0.8γρ/100γρ)."
w_image_file_path = "/stats_images_watermarked/Σύγκριση_Θρεπτικών_Συστατικών_Μοσχαριού_Φακής_watermarked.png"
image_file_path = "/stats_images/Σύγκριση_Θρεπτικών_Συστατικών_Μοσχαριού_Φακής.png"
thumbnail_file_path = "/stats_thumbnails/Σύγκριση_Θρεπτικών_Συστατικών_Μοσχαριού_Φακής_thumbnail.png"

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
