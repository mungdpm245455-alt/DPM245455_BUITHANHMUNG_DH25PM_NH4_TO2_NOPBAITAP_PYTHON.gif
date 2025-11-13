#Câu 5: Xử lý JSON File, Chuyển đổi Python Object qua String Json
'''
Yêu cầu:
Cho Python Object có cấu trúc sau:

pythonObject = {
    "ten": "Trần Duy Thanh",
    "tuoi": 50,
    "ma": "nv1"
}

'''
import json

# Khai báo Python Object
pythonObject = {
    "ten": "Trần Duy Thanh",
    "tuoi": 50,
    "ma": "nv1"
}

# Chuyển đổi Python Object sang chuỗi JSON
jsonString = json.dumps(pythonObject)

# Kết quả là một chuỗi JSON
print(jsonString)
