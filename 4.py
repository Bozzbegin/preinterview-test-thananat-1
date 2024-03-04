from datetime import datetime

def check_date_range():
    x_str = input("Date x = : ") 
    y_str = input("Date y = : ")
    m_str = input("Date m = : ")

    try:
        x = datetime.strptime(x_str, "%d/%m/%Y")
        y = datetime.strptime(y_str, "%d/%m/%Y")
        m = datetime.strptime(m_str, "%d/%m/%Y")

        in_range = x <= m <= y
        days_difference = (m - x).days

        print(f"{in_range}, {days_difference} Days")
    except ValueError:
        print("ไม่พบข้อมูล Date x, y, m")

check_date_range()

