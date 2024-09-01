import os

# 'input_data.txt' からデータを読み取る
with open('input_data.txt', 'r') as file:
    data = file.read()

# 'data.txt' にデータを書き込む
with open('data.txt', 'w') as file:
    file.write(data)
