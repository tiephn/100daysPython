"""Phương pháp Newton (Newton’s Method), còn được gọi là phương pháp NewtonRaphson, 
là một phương pháp số học để tìm gần đúng của các nghiệm của một
hàm số thực. Cụ thể, nó thường được sử dụng để tìm gần đúng của các nghiệm
của phương trình f(x) = 0.
• Ngoài ứng dụng trong tìm nghiệm của một hàm số, phương pháp Newton còn có
ứng dụng trong máy học (Machine learning) trong việc tìm nghiệm của đạo hàm
của hàm loss. Tuy nhiên đây là phương pháp không phổ biến bằng thuật toán
gradient descent."""


def find_squared_root(a):
    """ Find the squared root of number a """
    EPSILON = 0.001

    x0 = a
    x1 = (x0 + a/x0) / 2
    n = 0 # n này khai báo xong làm gì nhỉ??
    while True:
        x1 = (x0 + a/x0) / 2  # <= xn - f(xn)/f'(xn)
        if abs(x1 - x0) < EPSILON:
            break
        x0 = x1
    return x1

print(find_squared_root(2))
print(find_squared_root(3))