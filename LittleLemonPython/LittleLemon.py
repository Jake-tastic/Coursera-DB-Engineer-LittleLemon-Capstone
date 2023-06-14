#establishing connection to the database
import mysql.connector as connection
connection = connection.connect(username = "root", password = "Corntruck85!", database = "littlelemondb")
cursor = connection.cursor()

#diplaying all tables within the database
#cursor.execute("SHOW TABLES")
#for table in cursor:
#    print(table)

#query to find customer and order info on orders over $60
total_cost = """
SELECT orders.OrderID, orders.TotalCost, customers.FullName, customers.ContactNumber, customers.Email 
FROM orders
JOIN customers ON orders.CustomerID = customers.CustomerID
WHERE orders.TotalCost > 60;"""

#extracting results
cursor.execute(total_cost)
results = cursor.fetchall()
print("Orders over $60:")
print(cursor.column_names)
for r in results:
    print(r)