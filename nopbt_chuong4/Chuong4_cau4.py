#Câu 4: Viết Hàm tính ROI
'''
Yêu cầu:
− ROI (Return On Investment), một thuật ngữ quan trọng trong marketing, mà đặc
biệt là SEO, tạm dịch là tỷ lệ lợi nhuận thu được so với chi phí bạn đầu tư. Có thể
hiểu ROI một cách đơn giản chính là chỉ số đo lường tỷ lệ những gì bạn thu về so
với những gì bạn phải bỏ ra.
− Hiểu đúng bản chất của ROI, bạn sẽ đo lường được hiệu quả đồng vốn đầu tư của
mình cho các chi phí như quảng cáo, chạy Adwords, hay chi phí marketing online
khác.
− Vì ROI dựa vào các chỉ số cụ thể, nên nó cũng là một thước đo rất cụ thể:
− ROI = (Doanh thu – Chi phí)/Chi phí
− Viết chương trình cho phép người dùng nhập vào Doanh thu và Chi phí và xuất ra
tỉ lệ ROI cho người dùng, đồng thời hãy cho biết nên hay không nên đầu tư dự án
khi biết ROI (giả sử mức tổi thiểu ROI =0.75 thì mới đầu tư).
'''

def ROI(dt, cp):
    return (dt - cp) / cp

def GoiYDauTu(roi):
    if roi >= 0.75:
        return "Nên đầu tư"
    else:
        return "Không nên đầu tư"

print("Chương trình tính ROI")
dt = int(input("Nhập Doanh Thu: "))
cp = int(input("Nhập Chi Phí: "))

roi = ROI(dt, cp)
print("Tỉ lệ ROI =", roi)
print("==>", GoiYDauTu(roi))

