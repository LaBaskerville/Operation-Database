import sqlite3

koneksi_ke_db = sqlite3.connect('cars.db')

k = koneksi_ke_db.cursor()

k.execute("""
        create table if not exists TBcars(
            id integer primary key autoincrement,
            nama text not null,
            brand text not null,
            model text not null,
            price real not null
        )
        """)

koneksi_ke_db.commit()
koneksi_ke_db.close()