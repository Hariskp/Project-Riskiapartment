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


# from datetime import datetime
# import sqlite3
# # Input check-in date
# check_in = input("Enter check-in date (in format DD/MM/YYYY): ")
# check_in_date = datetime.strptime(check_in, "%d/%m/%Y")

# # Input check-out date
# check_out = input("Enter check-out date (in format DD/MM/YYYY): ")
# check_out_date = datetime.strptime(check_out, "%d/%m/%Y")

# # Calculate the duration of stay
# duration = (check_out_date - check_in_date).days

# # Calculate the total rent
# rent_per_month = 5000
# rent_total = rent_per_month * ((duration // 30))
# print("Total rent is", rent_total, "baht for", (duration // 30), "months of stay.")


from datetime import datetime

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

# Calculate payment date
start_date = datetime(check_in_date.year, check_in_date.month, 1).date()
end_date = datetime(check_out_date.year, check_out_date.month+1, 1).date()
payment_date = start_date
while payment_date < end_date:
    print("Payment due on", payment_date.strftime("%d/%m/%Y"), "is", rent_per_month, "baht.")
    payment_date = datetime(payment_date.year, payment_date.month+1, 1).date()

print("Total rent is", rent_total, "baht for", (duration // 30), "months of stay.")



# def calculaterent():
#     #Fetch customer
#     sql = 'SELECT * FROM customer WHERE phonenumber=?'
#     cursor.execute(sql, [phone_servicelog.get()])
#     db_customer = cursor.fetchone()
#     #Fetch room
#     sql = 'SELECT * FROM room WHERE room_number=?'
#     cursor.execute(sql, [db_customer[1]])
#     db_room = cursor.fetchone()
#     #Fetch service_log
#     sql = 'SELECT * FROM service_log WHERE phonenumber=?'
#     cursor.execute(sql, [db_customer[0]])

#     #Get Check in date
#     check_in = db_room[9]
#     check_in_date = datetime.strptime(check_in, "%d/%m/%Y")
#     #Get Check out date
#     check_out = db_room[10]
#     check_out_date = datetime.strptime(check_out, "%d/%m/%Y")

#     #Calculate duration of stay
#     duration = (check_out_date - check_in_date).days

#     #Calculate the total rent
#     rent_per_month = db_room[3]
#     rent_total = rent_per_month * ((duration // 30))

#     #Calculate payment date
#     start_date = datetime(check_in_date.year, check_in_date.month, 1).date()
#     end_date = datetime(check_out_date.year, check_out_date.month+1, 1).date()
#     payment_date = start_date
#     payment_list = []
#     while payment_date < end_date:
#         payment_list.append(rent_per_month)
#         payment_date = datetime(payment_date.year, payment_date.month+1, 1).date()

#     total_months = (duration // 30)
#     total_rent = rent_total

#     return total_months, total_rent, payment_list



# #Check payment status
#     paid = True
#     for row in cursor.fetchall():
#         if row[4] != 'paid':
#             paid = False
#             break
#     if paid:
#         print("ชำระเงินแล้ว")
#         #Show new payment list to customer
#         current_month = datetime.now().month
#         current_year = datetime.now().year
#         payment_list_display = []
#         for payment_month in range(current_month, current_month+total_months):
#             payment_list_display.append(f"{payment_month}/{current_year}")
#         print("ค่าห้องในรอบถัดไปที่ต้องชำระ:")
#         for payment in payment_list_display[1:]:
#             print(f" - {db_room[1]}: {db_room[3]} บาท ({payment})")
#     else:
#         print("ยังไม่ได้ชำระเงิน")



def calculaterent_backend():
    # Fetch customer
    sql = 'SELECT * FROM customer WHERE phonenumber=?'
    cursor.execute(sql, [phone_servicelog.get()])
    db_customer = cursor.fetchone()

    # Fetch room
    sql = 'SELECT * FROM room WHERE room_number=?'
    cursor.execute(sql, [db_customer[1]])
    db_room = cursor.fetchone()
    
    #Fetch service_log
    sql = 'SELECT * FROM service_log WHERE phonenumber=?'
    cursor.execute(sql, [db_customer[0]])
    db_log = cursor.fetchone()

    # Get check-in date
    check_in = db_room[9]
    check_in_date = datetime.strptime(check_in, "%d/%m/%Y")

    # Get check-out date
    check_out = db_room[10]
    check_out_date = datetime.strptime(check_out, "%d/%m/%Y")

    # Calculate duration of stay
    duration = (check_out_date - check_in_date).days

    # Calculate the total rent
    rent_per_month = db_room[3]
    rent_total = 0

    # Calculate the rent for full months
    full_months = duration // 30
    if full_months > 0:
        rent_total += rent_per_month * full_months

    # Calculate the rent for the partial month
    partial_month_duration = duration % 30
    if partial_month_duration > 0:
        rent_total += rent_per_month * (partial_month_duration / 30)

    # Calculate payment date
    start_date = datetime(check_in_date.year, check_in_date.month, 1).date()
    end_date = datetime(check_out_date.year, check_out_date.month+1, 1).date()
    payment_date = start_date
    payment_list = []
    while payment_date < end_date:
        payment_list.append(rent_per_month)
        payment_date = datetime(payment_date.year, payment_date.month+1, 1).date()

    total_months = full_months
    if partial_month_duration > 0:
        total_months += 1

    print(total_months)
    print(rent_total)
    print(payment_list)

    # Check payment status
    paid = True  # "ชำระเงินแล้ว"
    for row in cursor.fetchall():
        if row[4] != 'paid':
            paid = False  # "ยังไม่ได้ชำระเงิน"
            break

    if db_log[10] == 'ชำระเงินแล้ว':
        print("ชำระเงินแล้ว")
        # Show new payment list to customer
        current_month = datetime.now().month
        current_year = datetime.now().year
        payment_list_display = []
        for payment_month in range(current_month, current_month+total_months):
            payment_list_display.append(f"{payment_month}/{current_year}")
        print("ค่าห้องในรอบถัดไปที่ต้องชำระ:")
        for payment in payment_list_display[1:]:
            print(f" - {db_room[1]}: {rent_per_month} บาท ({payment})")
    else:
        print("ยังไม่ได้ชำระเงิน")
