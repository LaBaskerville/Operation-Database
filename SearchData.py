import sqlite3

koneksi_ke_db = sqlite3.connect("cars.db")

k = koneksi_ke_db.cursor()

k.execute ("""
            select * from TBcars
            where
                id = 101
    """)
print(k.fetchall())

koneksi_ke_db.close()