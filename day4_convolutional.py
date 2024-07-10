"""Tích chập (Convolution) là phép toán toán học thực hiện phép nhân từng
phần tử giữa hai ma trận (hoặc mảng) và sau đó cộng tổng các kết quả nhân tại
các vị trí tương ứng để tạo ra một ma trận mới. Ma trận mới này được gọi là ma
trận tích chập.Ma trận mới này được gọi là ma trận tích chập.
• Để tính tích chập giữa hai ma trận này, ta thực hiện các bước sau:
+ Di chuyển ma trận bộ lọc: Di chuyển ma trận bộ lọc từng vị trí trên ma trận
đầu vào. Tại mỗi vị trí, ta nhân từng phần tử của ma trận bộ lọc với phần
tử tương ứng của ma trận đầu vào và cộng tổng các kết quả nhân.
+ Ghi kết quả: Kết quả tính toán tại mỗi vị trí di chuyển của ma trận bộ lọc
được ghi vào một phần tử tương ứng trong ma trận tích chập.
+ Lặp lại: Lặp lại bước 1 và 2 cho đến khi ma trận bộ lọc đã di chuyển qua tất
cả các vị trí trên ma trận đầu vào."""


def convolution(mat_a, kernal):
    lenA = len(mat_a)
    lenK = len(kernal)

    result = [[0 for _ in range(lenA - lenK + 1)]
              for _ in range(lenA - lenK + 1)]

    # 2 vòng for đầu di chuyển kernal đi 1 lượt từ trái sang phải, 
    # từ trên xuống dưới trong mat_a
    for i in range(lenA - lenK + 1):
        for j in range(lenA - lenK + 1):
            # 2 vòng for còn lại nhân từng phần tử của ma trận bộ lọc với
            # phần tử tương ứng của ma trận đầu vào và cộng tổng các kết quả nhân
            for k in range(lenK):
                for l in range(lenK):
                    result[i][j] += mat_a[i+k][j+l] * kernal[k][l]
    return result


mat_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
kernal = [[2, 4], [1, 3]]

print(convolution(mat_a, kernal))

kernal = ([1, 1, 1], [0, 0, 0], [1, 1, 1])
print(convolution(mat_a, kernal))
