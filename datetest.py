# from datetime import datetime

# # Define the day of the month that rent is due
# rent_due_day = 1

# # Get the current date
# current_date = datetime.today().date()

# # Check if the current date is on or after the day that rent is due
# if current_date.day >= rent_due_day:
#     print("Rent is due this month.")
# else:
#     print("Rent is not due this month.")



# from datetime import datetime

# # Prompt the user to enter the current date
# current_date_str = input("Enter the current date (in format DD/MM/YYYY): ")

# # Convert the current date string to a datetime object
# current_date = datetime.strptime(current_date_str, "%d/%m/%Y")

# # Print the current date
# print("The current date is:", current_date)



# from datetime import datetime

# # ตั้งค่าราคาเช่าห้องพัก
# room_rent = 5000

# # รับวันที่ลูกค้า Check in
# check_in_str = input("Enter check-in date (in format DD/MM/YYYY): ")
# check_in = datetime.strptime(check_in_str, "%d/%m/%Y")

# # คำนวณจำนวนเดือนที่ลูกค้าอยู่อาศัย
# now = datetime.now()
# num_months = (now.year - check_in.year) * 12 + (now.month - check_in.month)

# # ตรวจสอบว่าถึงวันที่ควรชำระค่าเช่าหรือไม่
# if now.day >= 1 and now.day <= 7:
#     num_months += 1

# # คำนวณค่าเช่าห้องพัก
# total_rent = room_rent * num_months

# # แสดงผลลัพธ์
# print(f"Total rent is {total_rent} baht for {num_months} months of stay.")


from datetime import datetime
import sqlite3
# Input check-in date
check_in = input("Enter check-in date (in format DD/MM/YYYY): ")
check_in_date = datetime.strptime(check_in, "%d/%m/%Y")

# Input check-out date
check_out = input("Enter check-out date (in format DD/MM/YYYY): ")
check_out_date = datetime.strptime(check_out, "%d/%m/%Y")

# Calculate the duration of stay
duration = (check_out_date - check_in_date).days

# Calculate the total rent
rent_per_month = 5000
rent_total = rent_per_month * ((duration // 30))
print("Total rent is", rent_total, "baht for", (duration // 30), "months of stay.")