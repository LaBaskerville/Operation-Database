import sqlite3

koneksi_ke_db = sqlite3.connect('cars.db')

k = koneksi_ke_db.cursor()

k.execute ("""
            delete from TBcars
            where 
                id = 102
    """)
print(k.fetchall())

koneksi_ke_db.commit()
koneksi_ke_db.close()