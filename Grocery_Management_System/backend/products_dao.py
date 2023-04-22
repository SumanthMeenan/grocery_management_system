from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id=uom.uom_id")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

def get_product_sales(connection):
    cursor = connection.cursor(buffered=True)
    query = "select * from product_sales;"
    cursor.execute(query)
    connection.commit()
    response = []
    for (product_id, name, total_quantity, total_sales) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'total_quantity': total_quantity,
            'total_sales': total_sales,
        })
    return response

def customer_products(connection):
    cursor = connection.cursor(buffered=True)
    query = "SELECT o.customer_name, p.name, od.total_price FROM order o JOIN order_details od ON o.order_id = od.order_id JOIN products p ON od.product_id = p.product_id"
    cursor.execute(query)
    connection.commit()
    response = []
    for (customer_name, name, total_price) in cursor:
        response.append({
            'customer_name': customer_name,
            'name': name,
            'total_price': total_price,
        })
    return response

def search_customer(connection, customer_name):
    cursor = connection.cursor(buffered=True)
    query = "SELECT * FROM orders WHERE customer_name=" + "'" + str(customer_name) + "'"
    print(query)
    cursor.execute(query)
    connection.commit()
    response = []
    for (order_id, customer_name, total, datetime) in cursor:
        response.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'total': total,
            'datetime':datetime
        })
    return response    

if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))
    print(insert_new_product(connection, {
        'product_name': 'potatoes',
        'uom_id': '1',
        'price_per_unit': 10
    }))