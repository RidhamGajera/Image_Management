# utils/db_utils.py

import psycopg2

conn = psycopg2.connect(
    dbname="image_db",
    user="image_user",
    password="image_password",
    host="localhost",
    port="5432"
)

def create_image_record(filename):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO images (filename) VALUES (%s) RETURNING id", (filename,))
    image_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    return image_id

def get_all_images():
    cursor = conn.cursor()
    cursor.execute("SELECT id, filename FROM images")
    images = [{"id": image[0], "filename": image[1]} for image in cursor.fetchall()]
    cursor.close()
    return images

def delete_image_record(image_id):
    cursor = conn.cursor()
    cursor.execute("SELECT filename FROM images WHERE id=%s", (image_id,))
    filename = cursor.fetchone()[0]
    cursor.execute("DELETE FROM images WHERE id=%s", (image_id,))
    conn.commit()
    cursor.close()
    return filename
