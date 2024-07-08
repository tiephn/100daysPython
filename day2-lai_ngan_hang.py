# Số e (còn gọi là hằng số Euler) là một số vô tỷ xuất hiện trong nhiều lĩnh vực
# toán học và khoa học, bao gồm cả lĩnh vực tài chính. Trong ngân hàng, số e được
# sử dụng để tính lãi suất kép, một phương pháp tính lãi suất trong đó tiền lãi được
# cộng vào số tiền gốc để tính lãi cho các kỳ hạn tiếp theo.

# Giả sử bạn có 1 Dollar, và bạn gởi vào ngân hàng và được nhận lãi mỗi ngày,
# vậy điều sẽ xảy ra nếu bạn gởi vào ngân hàng trong 1 năm thì tiền bạn nhận được là bao nhiêu?
# Công thức tính lãi suất hàng ngày:
# Nếu lãi suất hàng năm là 𝑟, thì lãi suất hàng ngày là (1+𝑟/365)

def compute_interest(money, period, annual_rate):
    # Lãi suất hàng ngày
    daily_interest_rate = 1 + annual_rate / 365
    result = money

    for _ in range(period):
        result *= daily_interest_rate

    return round(result, 3)


# Ví dụ sử dụng hàm với lãi 6.7%
print(compute_interest(1, 12, 0.067))  # Test case 1
print(compute_interest(1, 365, 0.067))  # Test case 2
print(compute_interest(1, 730, 0.067))  # Test case 3

# Ví dụ sử dụng hàm theo bài tập, lãi 100%
print(compute_interest(1, 12, 1))  # Test case 1
print(compute_interest(1, 365, 1))  # Test case 2
print(compute_interest(1, 730, 1))  # Test case 3
