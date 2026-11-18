
print("======================================================")
print("             DATA CONVERSION UTILITY")
print("======================================================")

product_name = input("Enter Product Name: ")
price = float(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))

# Calculations
total_price = price * quantity
tax = total_price * 0.18
final_amount = total_price + tax

# Type casting
amount_str = str(final_amount)
quantity_float = float(quantity)

print("------------------------------------------------------")
print("               TYPE CASTING SUMMARY")
print("------------------------------------------------------")
print("Variable       Value          Python Type")
print("------------------------------------------------------")

print("product_name  ", product_name, "       ", type(product_name))
print("price         ", price, "             ", type(price))
print("quantity      ", quantity, "               ", type(quantity))
print("total_price   ", total_price, "          ", type(total_price))
print("amount_str    ", amount_str, "        ", type(amount_str))
print("quantity_float", quantity_float, "           ", type(quantity_float))

print("------------------------------------------------------")
print("                   TAX INVOICE")
print("------------------------------------------------------")

print("Product Name  :", product_name)
print("Price         : Rs.", price)
print("Quantity      :", quantity)
print("Subtotal      : Rs.", round(total_price, 2))
print("GST (18%)     : Rs.", round(tax, 2))
print("Invoice Total : Rs.", round(final_amount, 2))

print("======================================================")
