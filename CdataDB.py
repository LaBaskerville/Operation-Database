import sqlite3

koneksi_ke_db = sqlite3.connect('cars.db')

k = koneksi_ke_db.cursor()

k.execute("""
        insert into TBcars(
            id,
            name, 
            brand,
            model,
            price
        )
        values (
            '101',
            'red car',
            'honda',
            'CRV',
            12000
        )
        """)

koneksi_ke_db.commit()
koneksi_ke_db.close()