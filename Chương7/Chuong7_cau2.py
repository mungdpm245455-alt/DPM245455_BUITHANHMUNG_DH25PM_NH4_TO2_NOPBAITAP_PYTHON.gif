#Câu 2: Xử lý số trong Text File
'''
Yêu cầu:
Cho một tập tin có dữ liệu trên mỗi dòng như dưới đây:
5,6,8,9,-5
-9,5,4,7,8
6,7,8,3,6,46,7,2,-6,-7
a) Viết hàm đọc file, mỗi dòng khởi tạo thành 1 list và xuất ra màn hình
b) Xuất các số âm trên mỗi dòng ra màn hình
'''

#Tạo file XuLyFile.py
def LuuFile(path,data):
 file=open(path,'a',encoding='utf-8')
 file.writelines(data)
 file.writelines("\n")
 file.close()

def DocFile(path):
 arrSo=[]
 file=open(path,'r',encoding='utf-8')
 for line in file:
  data=line.strip()           # ⚙️ Lùi vào trong vòng for
  arr=data.split(',')
  arrSo.append(arr)
 file.close()
 return arrSo

 
 #Tạo file TestLuuFile.py
from XuLyFile import *

LuuFile("csdl_so.txt","-5,4,7,9,3,20")
LuuFile("csdl_so.txt","5,-4,37,-19,24,-21")
LuuFile("csdl_so.txt","15,9,0,-38,-3,15")
LuuFile("csdl_so.txt","5,-4,77,-9,3,-7")
LuuFile("csdl_so.txt","55,44,27")
LuuFile("csdl_so.txt","-50,26")

#Tạo file TestDocFile.py
from XuLyFile import *

arrSo = DocFile("csdl_so.txt")
print(arrSo)

def XuatSoAmTrenMoiDong(arrSo):
 for row in arrSo:
  for element in row:
   number = int(element)
   if number < 0:
    print(number, end='\t')
  print()  # ⚙️ xuống dòng sau mỗi dòng dữ liệu

print("Các số âm trên mỗi dòng:")
XuatSoAmTrenMoiDong(arrSo)

