from datetime import datetime

#Function to calculate age
def Calculate_Age(dob_str):
    try:
        dob = datetime.strptime(dob_str, "%d-%m-%Y")
    except ValueError:
        print("Invalid date format! Please use DD-MM-YYYY.")
        return

    today = datetime.today()

    if dob > today:
        print("DOB cannot be in the future.")
        return
    
    years, months, days = today.year - dob.year, today.month - dob.month, today.day - dob.day

    # Adjust for negative days
    if days < 0:
        months -= 1
        prev_month = (today.month - 1) or 12
        prev_month_year = today.year if today.month != 1 else today.year - 1
        days += (datetime(prev_month_year, prev_month % 12 + 1, 1) - datetime(prev_month_year, prev_month, 1)).days

    # Adjust for negative months
    if months < 0:
        years -= 1
        months += 12

    print(f"\nYou are {years} years, {months} months, and {days} days old.")

# Main program
dob_input = input("Enter your date of birth in DD-MM-YYYY format: ")
Calculate_Age(dob_input)
