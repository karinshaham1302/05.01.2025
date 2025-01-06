import sqlite3
import os


db_name: str = "hw_solution.db"
conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


cursor.execute("DROP TABLE IF EXISTS shopping")



cursor.execute('''
    CREATE TABLE IF NOT EXISTS shopping (
        id INTEGER PRIMARY KEY,
        name TEXT,
        amount INTEGER
    )
''')
print('Table created or already exists')



cursor.execute('''
    INSERT INTO shopping (name, amount)
    VALUES (?, ?)
''',('Avokado', 5))
cursor.execute('''
    INSERT INTO shopping (name, amount)
    VALUES (?, ?)
''',('Milk', 2))
cursor.execute('''
    INSERT INTO shopping (name, amount)
    VALUES (?, ?)
''',('Bread', 3))
cursor.execute('''
    INSERT INTO shopping (name, amount)
    VALUES (?, ?)
''',('Chocolate', 8))
cursor.execute('''
    INSERT INTO shopping (name, amount)
    VALUES (?, ?)
''',('Bamba', 5))
cursor.execute('''
    INSERT INTO shopping (name, amount)
    VALUES (?, ?)
''',('Orange', 10))
print('Data inserted')



cursor.execute("SELECT * FROM shopping")
print('Select - All items:')
result1 = [tuple(row) for row in cursor.fetchall()]
print(result1)
print()


cursor.execute("SELECT * FROM shopping WHERE amount > 5")
print('Select - Items with amount > 5:')
result2 = [tuple(row) for row in cursor.fetchall()]
print(result2)
print()


cursor.execute("DELETE FROM shopping WHERE name LIKE 'Orange'")
conn.commit()


cursor.execute("UPDATE shopping SET name = ? WHERE name LIKE ?",
               ('Bisli', 'Bamba'))
conn.commit()


cursor.execute("UPDATE shopping SET amount = ? WHERE name LIKE ?",
               (1, 'Milk'))
conn.commit()


cursor.execute("SELECT COUNT(*) FROM shopping")
print('Number of items:')
result3 = [tuple(row) for row in cursor.fetchall()]
print(result3)
print()


cursor.execute("SELECT * FROM shopping WHERE id > 0;")
print('Final items:')
result4 = [tuple(row) for row in cursor.fetchall()]
print(result4)
print()


# Bonus:
if os.path.exists(db_name):
    os.remove(db_name)
    print(f"Database file '{db_name}' was deleted.")
else:
    print(f"Database file '{db_name}' does not exist.")


conn.close()
