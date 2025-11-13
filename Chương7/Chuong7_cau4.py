#Câu 4: Xử lý JSON File, Chuyển đổi String Json qua Python Object 
'''
Yêu cầu:
Cho string Json có cấu trúc sau:
'{ "ma":"nv1", "age":50, "ten":"Trần Duy Thanh"}'
Hãy viết mã lệnh chuyển đổi qua Python Object

'''
import json
jsonString = '{ "ma":"nv1", "age":50, "ten":"Trần Duy Thanh"}'
dataObject=json.loads(jsonString)
print(dataObject)
print("Mã=",dataObject["ma"])
print("Tên=",dataObject["age"])
print("Tuổi=",dataObject["ten"])
