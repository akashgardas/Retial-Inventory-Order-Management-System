# Retial-Inventory-Order-Management-System

# Customers Module
## Scenario:
 	The store now wants to manage customer information. Each customer can place multiple orders. You must build features to handle Customer Management.

### Tasks:
1. Create a new customer with details → name, email, phone, city.
    Validate that email must be unique.
    If email already exists, show an error.

2. Update a customer’s phone or city.

3. Delete a customer:
    Allow deletion only if the customer has no orders.
    If orders exist, block deletion with an error message.

4. List all customers.

5. Search customer by email or city

---

# Orders Module
## Scenario:
 	A customer comes to buy products. The system must create an order, assign products to it, calculate total amount, and manage stock.

### Tasks:
1. Create a new order for a customer.
    Input: customer_id and a list of products with quantities (e.g., [{prod_id: 1, qty: 2}, 	{prod_id: 3, qty: 1}]).
	
	Check that the customer exists.
	Check each product’s stock → if not enough stock, reject order with error.
	Deduct stock for purchased products.
	Insert order into orders table and order_items table.
	Save the total_amount.

2. Fetch full details of an order (order info + customer info + order items).

3. List all orders of a customer.

4. Cancel an order:
    Allowed only if status = PLACED.
	Restore product stock.
    Update order status = CANCELLED.

5. Mark an order as COMPLETED after payment is successful (payment service)

---

# Payments Module:
## Scenario:
    The store now wants to track payments for each order.

### Tasks:
1. When an order is created, insert a pending payment record with the total amount.

2. Process payment → mark payment as PAID with method (Cash/Card/UPI).
    Update the order status to COMPLETED.

4. Support refunds: If an order is cancelled, mark the payment as REFUNDED.

---

# Reporting Module 
## Scenario:
	The manager wants to see sales reports.

### Tasks:
1. Show top 5 selling products (by total quantity).

2. Show total revenue in the last month.

3. Show total orders placed by each customer.

4. Show customers who placed more than 2 orders.


