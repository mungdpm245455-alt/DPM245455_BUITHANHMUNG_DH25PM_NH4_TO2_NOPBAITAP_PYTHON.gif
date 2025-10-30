#Câu 7: Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày vừa nhập (ngày/tháng/năm).
'''
'''
import datetime

def ngay_ke_tiep(ngay, thang, nam):
    try:
        ngay_hien_tai = datetime.date(nam, thang, ngay)
        ngay_sau = ngay_hien_tai + datetime.timedelta(days=1)
        return ngay_sau.strftime("%d/%m/%Y")
    except ValueError:
        return "Ngày không hợp lệ. Vui lòng kiểm tra lại."


ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))


print("Ngày kế tiếp là:", ngay_ke_tiep(ngay, thang, nam))
