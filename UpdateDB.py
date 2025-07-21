import sqlite3

koneksi_ke_db = sqlite3.connect('cars.db')

k = koneksi_ke_db.cursor()

k.execute ("""
            update TBcars set
                price = 50000
            where 
                id = 101
    """)

koneksi_ke_db.commit()
koneksi_ke_db.close()