#Câu 13: Xử lý XML File - Viết phần mềm Quản Lý Thiết Bị
'''
Yêu cầu:
Chương trình quản lý thiết bị gồm có 2 tập dữ liệu
Tập lưu danh sách nhóm thiết bị có tên nhomthietbi.xml có dữ liệu mẫu và format như
dưới đây:
<?xml version="1.0" encoding="UTF-8" ?>
<nhoms>
    <nhom>
        <ma>n1</ma>
        <ten>Nhóm 1</ten>
    </nhom>
    <nhom>
        <ma>n2</ma>
        <ten>Nhóm 2</ten>
    </nhom>
    <nhom>
        <ma>n3</ma>
        <ten>Nhóm 3</ten>
    </nhom>
</nhoms>

Theo cấu trúc ở trên thì mỗi Nhóm sẽ có: Mã nhóm, tên nhóm.
Chương trình phải đọc dữ liệu danh sách nhóm thiết bị.
Tập dữ liệu thiết bị được lưu trong file ThietBi.xml, có dữ liệu và cấu trúc như sau:

<?xml version="1.0" encoding="UTF-8" ?>
<thietbis>
    <thietbi manhom="n1">
        <ma>tb1</ma>
        <ten>Thiết bị 1</ten>
    </thietbi>
    <thietbi manhom="n1">
        <ma>tb2</ma>
        <ten>Thiết bị 2</ten>
    </thietbi>
    <thietbi manhom="n2">
        <ma>tb3</ma>
        <ten>Thiết bị 3</ten>
    </thietbi>
    <thietbi manhom="n3">
        <ma>tb4</ma>
        <ten>Thiết bị 4</ten>
    </thietbi>
    <thietbi manhom="n3">
        <ma>tb5</ma>
        <ten>Thiết bị 5</ten>
    </thietbi>
</thietbis>

'''
import xml.etree.ElementTree as ET
from collections import defaultdict

# Tên file XML
FILE_NHOM = "nhomthietbi.xml"
FILE_THIETBI = "thietbi.xml"


# --- Hàm đọc danh sách nhóm thiết bị ---
def doc_nhom_thiet_bi():
    tree = ET.parse(FILE_NHOM)
    root = tree.getroot()
    nhoms = []
    for n in root.findall("nhom"):
        ma = n.find("ma").text
        ten = n.find("ten").text
        nhoms.append({"ma": ma, "ten": ten})
    return nhoms


# --- Hàm đọc danh sách thiết bị ---
def doc_thiet_bi():
    tree = ET.parse(FILE_THIETBI)
    root = tree.getroot()
    thietbis = []
    for tb in root.findall("thietbi"):
        manhom = tb.get("manhom")
        ma = tb.find("ma").text
        ten = tb.find("ten").text
        thietbis.append({"manhom": manhom, "ma": ma, "ten": ten})
    return thietbis


# --- Hiển thị danh sách nhóm thiết bị ---
def hien_thi_nhom():
    nhoms = doc_nhom_thiet_bi()
    print("\n📂 Danh sách nhóm thiết bị:")
    for n in nhoms:
        print(f"  - {n['ma']}: {n['ten']}")


# --- Hiển thị toàn bộ thiết bị ---
def hien_thi_thiet_bi():
    tbs = doc_thiet_bi()
    print("\n🔧 Danh sách thiết bị:")
    for tb in tbs:
        print(f"  - {tb['ma']} | {tb['ten']} (Nhóm: {tb['manhom']})")


# --- Lọc thiết bị theo nhóm ---
def loc_theo_nhom(ma_nhom):
    tbs = doc_thiet_bi()
    kq = [tb for tb in tbs if tb["manhom"] == ma_nhom]
    print(f"\n📋 Thiết bị thuộc nhóm {ma_nhom}:")
    if not kq:
        print("  → Không có thiết bị nào.")
    else:
        for tb in kq:
            print(f"  - {tb['ma']} | {tb['ten']}")


# --- Xuất nhóm có nhiều thiết bị nhất ---
def nhom_nhieu_thiet_bi_nhat():
    tbs = doc_thiet_bi()
    dem = defaultdict(int)
    for tb in tbs:
        dem[tb["manhom"]] += 1

    max_so_luong = max(dem.values())
    nhoms_max = [k for k, v in dem.items() if v == max_so_luong]

    print("\n🏆 Nhóm có nhiều thiết bị nhất:")
    for ma in nhoms_max:
        print(f"  - {ma} ({dem[ma]} thiết bị)")


# --- Chương trình chính ---
if __name__ == "__main__":
    hien_thi_nhom()
    hien_thi_thiet_bi()

    ma = input("\n🔍 Nhập mã nhóm cần lọc (vd: n1, n2, n3): ")
    loc_theo_nhom(ma)

    nhom_nhieu_thiet_bi_nhat()
