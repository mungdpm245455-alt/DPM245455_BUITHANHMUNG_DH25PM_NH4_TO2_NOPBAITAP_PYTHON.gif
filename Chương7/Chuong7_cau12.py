#Câu 12: Xử lý CSV File - Viết phần mềm Quản Lý Nhân Viên
'''
Yêu cầu:
Viết hàm cho phép lưu tập tin dưới dạng CSV file, yêu cầu khởi tạo là 10 dòng, mỗi
dòng sẽ có 10 số ngẫu nhiên bất kỳ cách nhau bởi dấu “;”. Xem hình minh họa:
Tiếp theo viết hàm cho phép đọc tập tin ở mục trên, xuất ra tổng giá trị của các phần tử
trên mỗi dòng.
'''
import csv
import random

FILE_NAME = "dulieu.csv"

# --- Hàm 1: Ghi file CSV ---
def tao_file_csv():
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file, delimiter=';')

        for _ in range(10):  # 10 dòng
            dong = [random.randint(1, 100) for _ in range(10)]  # 10 số ngẫu nhiên
            writer.writerow(dong)

    print("✅ Đã tạo file CSV thành công!")

# --- Hàm 2: Đọc file CSV và tính tổng từng dòng ---
def doc_file_csv_va_tinh_tong():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file, delimiter=';')
        print("📊 Tổng giá trị của từng dòng:")
        for i, dong in enumerate(reader, start=1):
            # Chuyển từng phần tử sang số nguyên rồi tính tổng
            tong = sum(int(x) for x in dong if x.strip() != "")
            print(f"Dòng {i}: {tong}")

# --- Chương trình chính ---
if __name__ == "__main__":
    tao_file_csv()
    doc_file_csv_va_tinh_tong()
