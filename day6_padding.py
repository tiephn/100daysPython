"""Padding là kỹ thuật thêm các đường viền xung quanh ảnh đầu vào trước khi
thực hiện phép tích chập.
• Mục đích chính của padding là:
+ Giữ nguyên kích thước ảnh đầu ra: Sau khi áp dụng phép tích chập, ảnh
đầu ra thường có kích thước nhỏ hơn ảnh đầu vào. Padding giúp bù đắp lại
phần kích thước bị mất đi này, đảm bảo rằng ảnh đầu ra có kích thước tương
đương hoặc gần bằng ảnh đầu vào.
+ Giảm thiểu mất thông tin: Khi thực hiện phép tích chập, các pixel ở rìa ảnh
thường bị bỏ qua do kernel không thể bao phủ toàn bộ ảnh. Padding giúp
bổ sung thêm các pixel xung quanh ảnh, đảm bảo rằng tất cả các pixel đều
được tham gia vào quá trình tính toán và không có thông tin nào bị mất đi.
+ Kiểm soát kích thước của ảnh đầu ra: Padding có thể được sử dụng để điều
chỉnh kích thước của ảnh đầu ra. Ví dụ, nếu muốn ảnh đầu ra có kích thước
lớn hơn ảnh đầu vào, ta có thể sử dụng padding với kích thước lớn hơn kích
thước kernel.
• Một trong những phương pháp padding phổ biến nhất là Zero padding là một
kỹ thuật được sử dụng phổ biến trong xử lý tín hiệu số (DSP) và mạng nơ-ron tích
chập (CNN) để bổ sung thêm các giá trị 0 vào viền ngoài của ảnh trước khi thực
hiện các phép toán tiếp theo. Việc này giúp kiểm soát kích thước đầu ra của tín
hiệu sau khi xử lý và tránh tình trạng mất thông tin ở rìa dữ liệu. Sau khi thêm
các giá trị 0 vào viền ngoài của ảnh chúng ta thực hiện cách tính convolution như
đã được học ở bài trước đó để ra kết quả output cuối cùng."""

# hàm tích chập
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

# add thêm 0 vào viền cho mat_a trước khi đưa vào tính convolution
def zeropadding(mat_a):
    lenA = len(mat_a)
    result = [[0 for _ in range(lenA + 2)]
              for _ in range(lenA + 2)]
    for i in range(lenA):
        for j in range(lenA):
            result[i+1][j+1] = mat_a[i][j]
    return result


mat_a = [[0, 0, 0], [0, 4, 0], [0, 1, 0]]
kernal = [[1, 1], [1, 1]]

print(convolution(zeropadding(mat_a), kernal))

kernal = ([0, 1, 0], [0, 1, 0], [0, 1, 0])
print(convolution(zeropadding(mat_a), kernal))
