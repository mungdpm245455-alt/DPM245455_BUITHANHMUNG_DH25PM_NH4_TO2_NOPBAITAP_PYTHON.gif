#Câu 9: Xử lý Text File - Viết phần mềm Quản Lý sản phẩm
'''
Yêu cầu:
Viết phần mềm Quản Lý sản phẩm
Mỗi danh mục có: Mã , tên; Một danh mục có nhiều sản phẩm
Mỗi sản phẩm có: Mã, tên, đơn giá; Mỗi một sản phẩm thuộc về một danh mục.
Cho phép: lưu mới, sửa, xóa, tìm kiếm, sắp xếp, lưu và đọc Text File
'''
import os

# ======== CẤU TRÚC DỮ LIỆU ========
class SanPham:
    def __init__(self, ma_sp, ten_sp, don_gia, ma_dm):
        self.ma_sp = ma_sp
        self.ten_sp = ten_sp
        self.don_gia = float(don_gia)
        self.ma_dm = ma_dm

    def __str__(self):
        return f"{self.ma_sp};{self.ten_sp};{self.don_gia};{self.ma_dm}"


# ======== HÀM XỬ LÝ FILE ========
def doc_file(filename):
    ds_sp = []
    if not os.path.exists(filename):
        return ds_sp
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                ma_sp, ten_sp, don_gia, ma_dm = line.split(';')
                ds_sp.append(SanPham(ma_sp, ten_sp, don_gia, ma_dm))
    return ds_sp


def ghi_file(filename, ds_sp):
    with open(filename, 'w', encoding='utf-8') as f:
        for sp in ds_sp:
            f.write(str(sp) + '\n')


# ======== CÁC CHỨC NĂNG QUẢN LÝ ========
def hien_thi(ds_sp):
    print("\nDanh sách sản phẩm:")
    print("{:<10}{:<25}{:<10}{:<10}".format("Mã SP", "Tên sản phẩm", "Đơn giá", "Mã DM"))
    print("-" * 60)
    for sp in ds_sp:
        print(f"{sp.ma_sp:<10}{sp.ten_sp:<25}{sp.don_gia:<10}{sp.ma_dm:<10}")
    print()


def them_san_pham(ds_sp):
    ma_sp = input("Nhập mã sản phẩm: ")
    ten_sp = input("Nhập tên sản phẩm: ")
    don_gia = input("Nhập đơn giá: ")
    ma_dm = input("Nhập mã danh mục: ")
    ds_sp.append(SanPham(ma_sp, ten_sp, don_gia, ma_dm))
    print("✅ Đã thêm sản phẩm thành công!\n")


def sua_san_pham(ds_sp):
    ma_sp = input("Nhập mã sản phẩm cần sửa: ")
    for sp in ds_sp:
        if sp.ma_sp == ma_sp:
            sp.ten_sp = input(f"Tên mới ({sp.ten_sp}): ") or sp.ten_sp
            don_gia_moi = input(f"Đơn giá mới ({sp.don_gia}): ")
            if don_gia_moi:
                sp.don_gia = float(don_gia_moi)
            sp.ma_dm = input(f"Mã danh mục mới ({sp.ma_dm}): ") or sp.ma_dm
            print("✅ Đã cập nhật sản phẩm!\n")
            return
    print("❌ Không tìm thấy sản phẩm!\n")


def xoa_san_pham(ds_sp):
    ma_sp = input("Nhập mã sản phẩm cần xóa: ")
    for sp in ds_sp:
        if sp.ma_sp == ma_sp:
            ds_sp.remove(sp)
            print("✅ Đã xóa sản phẩm!\n")
            return
    print("❌ Không tìm thấy sản phẩm!\n")


def tim_kiem(ds_sp):
    tu_khoa = input("Nhập tên sản phẩm cần tìm: ").lower()
    kq = [sp for sp in ds_sp if tu_khoa in sp.ten_sp.lower()]
    if kq:
        hien_thi(kq)
    else:
        print("❌ Không tìm thấy sản phẩm nào!\n")


def sap_xep(ds_sp):
    ds_sp.sort(key=lambda sp: sp.don_gia)
    print("✅ Đã sắp xếp sản phẩm theo đơn giá tăng dần!\n")
    hien_thi(ds_sp)


# ======== MENU CHÍNH ========
def menu():
    filename = "sanpham.txt"
    ds_sp = doc_file(filename)

    while True:
        print("=== QUẢN LÝ SẢN PHẨM ===")
        print("1. Hiển thị danh sách")
        print("2. Thêm sản phẩm")
        print("3. Sửa sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Tìm kiếm sản phẩm")
        print("6. Sắp xếp sản phẩm theo giá")
        print("7. Lưu file")
        print("0. Thoát")

        chon = input("Chọn chức năng: ")

        if chon == '1':
            hien_thi(ds_sp)
        elif chon == '2':
            them_san_pham(ds_sp)
        elif chon == '3':
            sua_san_pham(ds_sp)
        elif chon == '4':
            xoa_san_pham(ds_sp)
        elif chon == '5':
            tim_kiem(ds_sp)
        elif chon == '6':
            sap_xep(ds_sp)
        elif chon == '7':
            ghi_file(filename, ds_sp)
            print("💾 Đã lưu dữ liệu vào file!\n")
        elif chon == '0':
            print("👋 Thoát chương trình.")
            break
        else:
            print("⚠️ Lựa chọn không hợp lệ!\n")


# ======== CHẠY CHƯƠNG TRÌNH ========
if __name__ == "__main__":
    menu()
