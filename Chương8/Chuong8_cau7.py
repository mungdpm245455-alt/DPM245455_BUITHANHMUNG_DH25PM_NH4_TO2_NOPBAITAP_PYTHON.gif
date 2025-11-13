#Câu 7: Thiết kế màn hình chuyển năm Dương Lịch thành Âm Lịch
'''
Yêu cầu:
Viết phần mềm để chuyển một năm Dương lịch qua Âm lịch
'''
# Chương trình chuyển năm Dương Lịch sang năm Âm Lịch

# Danh sách Thiên Can và Địa Chi
can = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

# Nhập năm Dương lịch
nam_duong = int(input("Nhập năm Dương lịch: "))

# Tính Can và Chi
nam_can = can[(nam_duong + 6) % 10]
nam_chi = chi[(nam_duong + 8) % 12]

# Ghép lại
nam_am = nam_can + " " + nam_chi

# Xuất kết quả
print(f"Năm âm: {nam_am}")