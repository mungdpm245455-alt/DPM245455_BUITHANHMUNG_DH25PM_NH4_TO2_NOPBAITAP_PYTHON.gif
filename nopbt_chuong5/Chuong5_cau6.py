#Câu 6: Trích lọc số âm trong chuỗi
'''
Yêu cầu:
Viết một hàm đặt tên là NegativeNumberInStrings(str). Hàm này có đối số truyền vào
là một chuỗi bất kỳ, Hãy viết lệnh để xuất ra các số nguyên âm trong chuỗi.
Ví dụ: Nếu nhập vào chuỗi “abc-5xyz-12k9l--p” thì hàm phải xuất ra được 2 số nguyên
âm đó là -5 và -12
'''
def NegativeNumberInStrings(s):
    result = []
    i = 0
    while i < len(s):
        # Nếu gặp dấu '-' và ký tự sau là chữ số thì bắt đầu đọc số âm
        if s[i] == '-' and i + 1 < len(s) and s[i + 1].isdigit():
            num = '-'
            i += 1
            # Đọc liên tục các chữ số sau dấu '-'
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
            result.append(int(num))
        else:
            i += 1

    # In ra kết quả
    if result:
        print("Các số nguyên âm trong chuỗi là:", result)
    else:
        print("Không có số nguyên âm nào trong chuỗi.")

# --- Chương trình chính ---
s = input("Nhập chuỗi: ")
NegativeNumberInStrings(s)

