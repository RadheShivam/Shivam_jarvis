import csv
import sqlite3

conn = sqlite3.connect('jarvis.db')

cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'C:\\Users\\shiva\\anaconda3\\python.exe')"
# cursor.execute(query)
# conn.commit()





# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'exam', 'https://lpucolab438.examly.io/')"
# cursor.execute(query)
# conn.commit()





# # Create a table with the desired coloumns
# cursor.execute(" CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)")





# # insert contect number with csv file
# desired_columns_indices = [0, 18]  # name, mobile

# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)

#     next(csvreader)  # ✅ skip header row (VERY IMPORTANT)

#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]

#         cursor.execute(
#             "INSERT INTO contacts (name, mobile_no) VALUES (?, ?);",
#             tuple(selected_data))

# conn.commit()
# conn.close()





# insert contect number one by one
# query = "INSERT INTO contacts VALUES (null, 'Shivam Kumar', '9876543210''null)"
# cursor.execute(query) 
# conn.commit()



# Find the number
query = "Papa"
query = query.strip().lower()

cursor.execute(
    """
    SELECT mobile_no 
    FROM contacts 
    WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?
    """,
    ('%' + query + '%', query + '%')
)

results = cursor.fetchall()

if results:
    print(results[0][0])
else:
    print("No contact found")
