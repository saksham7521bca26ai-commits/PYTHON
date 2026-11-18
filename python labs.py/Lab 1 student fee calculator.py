student_name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

tuition_fee = int(input("Enter Tuition Fee: "))
lab_fee = int(input("Enter Lab Fee: "))
library_fee = int(input("Enter Library Fee: "))
exam_fee = int(input("Enter Exam Fee: "))

# Discount
discount = 2000

# Calculate total fee before discount
total_fee = tuition_fee + lab_fee + library_fee + exam_fee

# Calculate fee after discount
fee_after_discount = total_fee - discount

# Calculate annual fee
annual_fee = fee_after_discount * 2

# Calculate monthly installment
monthly_installment = annual_fee / 12

# Display fee receipt
print("\n========== FEE RECEIPT ==========")
print("Student Name:", student_name)
print("Roll Number:", roll_no)
print("---------------------------------")
print("Tuition Fee:", tuition_fee)
print("Lab Fee:", lab_fee)
print("Library Fee:", library_fee)
print("Exam Fee:", exam_fee)
print("---------------------------------")
print("Total Fee:", total_fee)
print("Discount:", discount)
print("Fee After Discount:", fee_after_discount)
print("Annual Fee:", annual_fee)
print("Monthly Installment:", round(monthly_installment, 2))
print("=================================")