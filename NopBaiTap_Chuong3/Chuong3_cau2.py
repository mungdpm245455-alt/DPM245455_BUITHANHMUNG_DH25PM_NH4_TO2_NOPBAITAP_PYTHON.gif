#Câu 2: Đếm số ngày trong tháng
'''
Yêu cầu:
Nhập vào 1 tháng, xuất tháng đó có bao nhiêu ngày.
1,3,5,7,8,10,12➔31 ngày
4,6,9,11➔có 30 ngày
Nếu là tháng 2 thì yêu cầu nhập thêm năm. Năm nhuần thì tháng 2 có 29 ngày,
không nhuần có 28 ngày
'''
print("Chương trình đếm số ngày trong tháng")
month=int(input("Nhập vào 1 tháng:"))
if month in (1,3,5,7,8,10,12):
 print("Tháng ", month, " có 31 ngày")
elif month in (4,6,9,11):
 print("Tháng ", month, " có 30 ngày")
elif month==2:
 year=int(input("Mời bạn nhập vào năm:"))
 if (year % 4 ==0 and year % 100 != 0) :
            print("Tháng ",month, " có 29 ngày")
 elif year % 400 ==0:
            print("Tháng ", month, " có 28 ngày")
else:
   print("Tháng ", month, " không hợp lệ")