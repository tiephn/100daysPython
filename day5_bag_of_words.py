"""Bag of Words là một thuật toán hỗ trợ xử lý ngôn ngữ tự nhiên và mục đích
của BoW là phân loại text hay văn bản. Ý tưởng của BoW là phân tích và phân
nhóm dựa theo “Bag of Words” (corpus). Với test data mới, tiến hành tìm ra số
lần từng từ của test data xuất hiện trong “Bag”. Cách thức thực hiện như sau:
– Bước 1: Chia nhỏ văn bản thành các từ riêng lẻ.
– Bước 2: Tạo một tập hợp các từ xuất hiện trong văn bản. Tập hợp này không
có phần tử trùng nhau.
– Bước 3: Biểu diễn văn bản input ở dạng vector: Mỗi câu (mỗi input) được
biểu diễn bằng một vector, với mỗi phần tử trong vector thể hiện số lần xuất
hiện của từ đó trong input."""

corpus = ["Tôi thích môn Toán", "Tôi thích AI", "Tôi thích âm nhạc"]


def bag_of_words(corpus):
    bag = []
    for sentence in corpus:
        for word in sentence.split():
            if word not in bag:
                bag.append(word)
    bag.sort()
    return bag


bag = bag_of_words(corpus)

sentence = "Tôi thích AI thích Toán"
vector = [0]*len(bag)
# Đây là số lần xuất hiện của từng từ trong từ điển ['AI', 'Toán', 'Tôi', 'môn', 'nhạc', 'thích', 'âm'] trong câu "Tôi thích AI thích Toán".
for word in sentence.split():
    if word in bag:
        # vector.append(bag.index(word))
        vector[bag.index(word)] += 1
        # print(vector)
        # print(f"{word}: {vector[bag.index(word)]}")

print(f"{sentence}: {vector}")
print(f"Bag of Words: {bag}")
