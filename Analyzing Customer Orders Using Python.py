#List of customer names.
customers = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Judy']

#List of tuples containing customer name, item purchased, item price, and item category.
order_details = [
    (customers[0], 'Skin Cleanser', 25.00, 'Essentials'),
    (customers[0], 'Mouth Wash', 11.00, 'Essentials'),
    (customers[1], 'Headphones', 50.00, 'Electronics'),
    (customers[2], 'Silver Bracelet', 45.00, 'Accessories'),
    (customers[3], 'Digital Camera', 300.00, 'Electronics'),
    (customers[3], 'Leather Jacket', 150.00, 'Apparel'),
    (customers[4], 'Compression Pants', 60.00, 'Apparel'),
    (customers[4], 'Compression Shirt', 55.00, 'Apparel'),
    (customers[5], 'Bluetooth Speaker', 80.00, 'Electronics'),
    (customers[6], 'Leather Wallet', 17.00, 'Accessories'),
    (customers[6], 'Cargo Short', 40.00, 'Apparel'),
    (customers[7], 'Running Shoes', 120.00, 'Apparel'),
    (customers[8], 'Smart Watch', 200.00, 'Electronics'),
    (customers[9], 'Sunglasses', 75.00, 'Accessories'),
    (customers[9], 'Headphones', 95.00, 'Electronics'),
]

#Calculating total spending per customer.
order_total = {
    customers[0]: sum(item[2] for item in order_details if item[0] == customers[0]),
    customers[1]: sum(item[2] for item in order_details if item[0] == customers[1]),
    customers[2]: sum(item[2] for item in order_details if item[0] == customers[2]),
    customers[3]: sum(item[2] for item in order_details if item[0] == customers[3]),
    customers[4]: sum(item[2] for item in order_details if item[0] == customers[4]),
    customers[5]: sum(item[2] for item in order_details if item[0] == customers[5]),
    customers[6]: sum(item[2] for item in order_details if item[0] == customers[6]),
    customers[7]: sum(item[2] for item in order_details if item[0] == customers[7]),
    customers[8]: sum(item[2] for item in order_details if item[0] == customers[8]),
    customers[9]: sum(item[2] for item in order_details if item[0] == customers[9]),
}

#Sorting customers spending total in descending order.
sorted_order_total = dict(sorted(order_total.items(), key=lambda item: item[1], reverse=True))

#Printing formatted output of sorted spending total.
print('Sorted order totals (high to low):')
for customer, total in sorted_order_total.items():
    print(f"{customer}: ${total:.2f}")

#Creating dictionary to list out items purchased.
purchase_dict = {
    'Alice': [item[1] for item in order_details if item[0] == customers[0]],
    'Bob': [item[1] for item in order_details if item[0] == customers[1]],
    'Charlie': [item[1] for item in order_details if item[0] == customers[2]],
    'David': [item[1] for item in order_details if item[0] == customers[3]],
    'Eva': [item[1] for item in order_details if item[0] == customers[4]],
    'Frank': [item[1] for item in order_details if item[0] == customers[5]],
    'Grace': [item[1] for item in order_details if item[0] == customers[6]],
    'Hannah': [item[1] for item in order_details if item[0] == customers[7]],
    'Ian': [item[1] for item in order_details if item[0] == customers[8]],
    'Judy': [item[1] for item in order_details if item[0] == customers[9]],
}

#Creating dictionary to list out items by category.
category_dict = {
    'Essentials': [item[1] for item in order_details if item[3] == 'Essentials'],
    'Electronics': [item[1] for item in order_details if item[3] == 'Electronics'],
    'Accessories': [item[1] for item in order_details if item[3] == 'Accessories'],
    'Apparel': [item[1] for item in order_details if item[3] == 'Apparel'],
}

#Using conditional statements to classify each customer based on their total spending.
print('Spending classification:')
for i in range(len(order_total)):
    if order_total[customers[i]] >= 100.00:
        print(f'High-value buyer: {customers[i]}')
    elif order_total[customers[i]] >= 50.00 and order_total[customers[i]] < 100.00:
        print(f'Moderate buyer: {customers[i]}')
    else:
        print(f'Low-value buyer: {customers[i]}')

#Calculating the total revenue generated per category.
category_total = {
    'Essentials': sum(item[2] for item in order_details if item[3] == 'Essentials'),
    'Electronics': sum(item[2] for item in order_details if item[3] == 'Electronics'),
    'Accessories': sum(item[2] for item in order_details if item[3] == 'Accessories'),
    'Apparel': sum(item[2] for item in order_details if item[3] == 'Apparel')
}

#Creating a set of all unique items purchased.
item_set = set(item[1] for item in order_details)

#Creating list of customers who purchased from specific categories.
essential_buyers = [item[0] for item in order_details if item[3] == 'Essentials']
electronic_buyers = [item[0] for item in order_details if item[3] == 'Electronics']
accessory_buyers = [item[0] for item in order_details if item[3] == 'Accessories']
apparel_buyers = [item[0] for item in order_details if item[3] == 'Apparel']

#Using set operations to determine customers who purchased from multiple categories.
multi_category_buyers = set(essential_buyers) & set(electronic_buyers) | \
set(essential_buyers) & set(accessory_buyers) | \
set(essential_buyers) & set(apparel_buyers) | \
set(electronic_buyers) & set(accessory_buyers) | \
set(electronic_buyers) & set(apparel_buyers) | \
set(accessory_buyers) & set(apparel_buyers)

#Using set operations to determine customers who purchased from both Electronics and Apparel.
bi_category_buyers = set(electronic_buyers) & set(apparel_buyers)

#Printing results of categorical set operations.
print('Customers who purchased from multiple categories:', multi_category_buyers)
print('Customers who purchased from both Electronics and Apparel:', bi_category_buyers)