
# Can Chi là một hệ thống tính toán giờ, ngày, tháng, năm âm lịch của người trung
# quốc cổ đại. Can Chi có 10 thiên can và 12 địa chi. Tên gọi 10 thiên can Canh,
# Tân, Nhâm, Quý, Giáp, Ất, Bính, Đinh, Mậu, Kỷ. Tên gọi 12 địa chi Thân, Dậu,
# Tuất, Hợi, Tý, Sửu, Dần, Mão, Thìn, Tỵ, Ngọ, Mùi

# Bài tập chủ yếu dùng lệnh If-Else nên sẽ dùng để xử lý
def calculate_can_chi_calendar(year):
    result = ''

    # Can: lấy năm sinh chia cho 10 và lấy phần dư. Nếu phần dư bằng 0 tương
    # ứng với Canh, 1 tương ứng với Tân, tiếp tục cho tới 9 tương ứng với Kỷ
    # remainder => "phần dư" hoặc "số dư"
    remainder = year % 10

    if remainder == 0:
        result = 'Canh'
    elif remainder == 1:
        result = 'Tân'
    elif remainder == 2:
        result = 'Nhâm'
    elif remainder == 3:
        result = 'Quý'
    elif remainder == 4:
        result = 'Giáp'
    elif remainder == 5:
        result = 'Ất'
    elif remainder == 6:
        result = 'Bính'
    elif remainder == 7:
        result = 'Đinh'
    elif remainder == 8:
        result = 'Mậu'
    elif remainder == 9:
        result = 'Kỷ'

    # Chi: lấy năm sinh chia cho 12 và lấy phần dư. Nếu phần dư bằng 0 tương
    # ứng với Thân, 1 tương ứng với Dậu, tiếp tục cho tới 11 tương ứng với Mùi
    remainder2 = year % 12

    if remainder2 == 0:
        result += ' Thân'
    elif remainder2 == 1:
        result += ' Dậu'
    elif remainder2 == 2:
        result += ' Tuất'
    elif remainder2 == 3:
        result += ' Hợi'
    elif remainder2 == 4:
        result += ' Tý'
    elif remainder2 == 5:
        result += ' Sửu'
    elif remainder2 == 6:
        result += ' Dần'
    elif remainder2 == 7:
        result += ' Mão'
    elif remainder2 == 8:
        result += ' Thìn'
    elif remainder2 == 9:
        result += ' Tỵ'
    elif remainder2 == 10:
        result += ' Ngọ'
    elif remainder2 == 11:
        result += ' Mùi'

    return result

# Sử dụng List


def calculate_can_chi_calendar2(year):
    can_list = ['Canh', 'Tân', 'Nhâm', 'Quý',
                'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
    chi_list = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý',
                'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi']

    can = can_list[year % 10]
    chi = chi_list[year % 12]

    return f"{can} {chi}"


print(f"Cách 1 if-else: {calculate_can_chi_calendar(2024)}")
print(f"Cách 2 list: {calculate_can_chi_calendar2(2024)}")

print(f"Cách 1 if-else: {calculate_can_chi_calendar(1982)}")
print(f"Cách 2 list: {calculate_can_chi_calendar2(1982)}")
