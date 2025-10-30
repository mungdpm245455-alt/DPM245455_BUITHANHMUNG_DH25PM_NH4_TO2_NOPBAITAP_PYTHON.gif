#Câu 1: Kiểm tra chuỗi đối xứng
'''
Yêu cầu:
Dùng vòng lặp while vĩnh cửu, cho phép Nhập vào một Chuỗi➔Xuất Chuỗi này có phải
đối xứng hay không? Hỏi người sử dụng có tiếp tục phần mềm. Nếu tiếp tục thì nhập
Chuỗi mới, còn không thì thoát và thông báo cảm ơn
'''
def CheckDoiXung(s):
    flag = True
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            flag = False
            break
    return flag

def main():
    print("Nhập 1 chuỗi:")
    s = input()
    if CheckDoiXung(s):
        print("Chuỗi bạn nhập đối xứng")
    else:
        print("Chuỗi bạn nhập không đối xứng")

while True:
    main()
    print("Tiếp không Thím? (c/k):")
    s = input().strip().lower()
    if s == "k":
        break

print("CÁM ƠN THÍM")