#Câu 10: Xử lý JSON File - Viết phần mềm Quản Lý Sinh Viên
'''
Yêu cầu:
Viết phần mềm quản lý Sinh Viên
Mỗi một lớp có: Mã lớp, tên; một lớp có nhiều Sinh viên
Mỗi sinh viên có: mã, tên, năm sinh; Mỗi một sinh viên thuộc về một lớp.
Cho phép: lưu mới, sửa, xóa, tìm kiếm, sắp xếp, lưu và đọc JSon File
'''
import json
import os

# ======= KHAI BÁO LỚP =======
class SinhVien:
    def __init__(self, ma_sv, ten_sv, nam_sinh, ma_lop):
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv
        self.nam_sinh = int(nam_sinh)
        self.ma_lop = ma_lop

    def to_dict(self):
        return {
            "ma_sv": self.ma_sv,
            "ten_sv": self.ten_sv,
            "nam_sinh": self.nam_sinh,
            "ma_lop": self.ma_lop
        }


# ======= XỬ LÝ FILE JSON =======
def doc_file(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return [SinhVien(**sv) for sv in data]


def ghi_file(filename, ds_sv):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump([sv.to_dict() for sv in ds_sv], f, ensure_ascii=False, indent=4)


# ======= CÁC CHỨC NĂNG =======
def hien_thi(ds_sv):
    print("\nDANH SÁCH SINH VIÊN:")
    print("{:<10}{:<25}{:<10}{:<10}".format("Mã SV", "Tên sinh viên", "Năm sinh", "Mã lớp"))
    print("-" * 60)
    for sv in ds_sv:
        print(f"{sv.ma_sv:<10}{sv.ten_sv:<25}{sv.nam_sinh:<10}{sv.ma_lop:<10}")
    print()


def them_sinh_vien(ds_sv):
    ma_sv = input("Nhập mã sinh viên: ")
    ten_sv = input("Nhập tên sinh viên: ")
    nam_sinh = input("Nhập năm sinh: ")
    ma_lop = input("Nhập mã lớp: ")
    ds_sv.append(SinhVien(ma_sv, ten_sv, nam_sinh, ma_lop))
    print("✅ Đã thêm sinh viên!\n")


def sua_sinh_vien(ds_sv):
    ma_sv = input("Nhập mã sinh viên cần sửa: ")
    for sv in ds_sv:
        if sv.ma_sv == ma_sv:
            sv.ten_sv = input(f"Tên mới ({sv.ten_sv}): ") or sv.ten_sv
            nam_moi = input(f"Năm sinh mới ({sv.nam_sinh}): ")
            if nam_moi:
                sv.nam_sinh = int(nam_moi)
            sv.ma_lop = input(f"Mã lớp mới ({sv.ma_lop}): ") or sv.ma_lop
            print("✅ Đã cập nhật sinh viên!\n")
            return
    print("❌ Không tìm thấy sinh viên!\n")


def xoa_sinh_vien(ds_sv):
    ma_sv = input("Nhập mã sinh viên cần xóa: ")
    for sv in ds_sv:
        if sv.ma_sv == ma_sv:
            ds_sv.remove(sv)
            print("✅ Đã xóa sinh viên!\n")
            return
    print("❌ Không tìm thấy sinh viên!\n")


def tim_kiem(ds_sv):
    tu_khoa = input("Nhập tên sinh viên cần tìm: ").lower()
    kq = [sv for sv in ds_sv if tu_khoa in sv.ten_sv.lower()]
    if kq:
        hien_thi(kq)
    else:
        print("❌ Không tìm thấy sinh viên!\n")


def sap_xep(ds_sv):
    ds_sv.sort(key=lambda sv: sv.ten_sv)
    print("✅ Đã sắp xếp sinh viên theo tên!\n")
    hien_thi(ds_sv)


# ======= MENU CHÍNH =======
def menu():
    filename = "sinhvien.json"
    ds_sv = doc_file(filename)

    while True:
        print("=== QUẢN LÝ SINH VIÊN ===")
        print("1. Hiển thị danh sách")
        print("2. Thêm sinh viên")
        print("3. Sửa sinh viên")
        print("4. Xóa sinh viên")
        print("5. Tìm kiếm sinh viên")
        print("6. Sắp xếp sinh viên theo tên")
        print("7. Lưu file JSON")
        print("0. Thoát")

        chon = input("Chọn chức năng: ")

        if chon == '1':
            hien_thi(ds_sv)
        elif chon == '2':
            them_sinh_vien(ds_sv)
        elif chon == '3':
            sua_sinh_vien(ds_sv)
        elif chon == '4':
            xoa_sinh_vien(ds_sv)
        elif chon == '5':
            tim_kiem(ds_sv)
        elif chon == '6':
            sap_xep(ds_sv)
        elif chon == '7':
            ghi_file(filename, ds_sv)
            print("💾 Đã lưu dữ liệu vào file JSON!\n")
        elif chon == '0':
            print("👋 Thoát chương trình.")
            break
        else:
            print("⚠️ Lựa chọn không hợp lệ!\n")


# ======= CHẠY CHƯƠNG TRÌNH =======
if __name__ == "__main__":
    menu()

