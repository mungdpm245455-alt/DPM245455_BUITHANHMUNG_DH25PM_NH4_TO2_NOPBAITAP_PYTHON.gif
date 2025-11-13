'''
Dưới đây là một ví dụ sử dụng Giải thuật Hồi Quy Tuyến Tính của thư viện Scikit-learn
để dự báo cân nặng dựa vào chiều cao.
Từ bảng dữ liệu ở trên, hãy viết giải thuật để người dùng nhập vào chiều cao thì xuất ra
cân nặng của họ, sử dụng thư viện Scikit-Learn.
Mã nguồn đầy đủ cho phần hồi quy tuyến tính này (lưu ý khi dùng các thư viện mà chưa
cài đặt thì nó sẽ báo lỗi, Sinh viên tự cài đặt):

'''
from __future__ import print_function
import numpy as np
from sklearn import datasets, linear_model

# ===============================
# DỮ LIỆU ĐẦU VÀO
# ===============================
# Chiều cao (cm) — mỗi hàng là một điểm dữ liệu
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# Cân nặng (kg)
y = np.array([49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

# ===============================
# XÂY DỰNG MA TRẬN Xbar
# ===============================
# Thêm cột 1 vào X để biểu diễn hệ số tự do
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis=1)

# ===============================
# TÍNH TOÁN HỆ SỐ w = [w0, w1]
# ===============================
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)

# ===============================
# MÔ HÌNH HỒI QUY TUYẾN TÍNH BẰNG SCIKIT-LEARN
# ===============================
regr = linear_model.LinearRegression()
regr.fit(X, y)

# ===============================
# SO SÁNH HAI KẾT QUẢ
# ===============================
print("scikit-learn's solution : w_1 = {:.10f}, w_0 = {:.10f}".format(regr.coef_[0], regr.intercept_))
print("our solution             : w_1 = {:.10f}, w_0 = {:.10f}".format(w[1], w[0]))

# ===============================
# DỰ ĐOÁN CÂN NẶNG
# ===============================
yourHeight = int(input("\nInput your height (cm): "))
yourWeight = regr.coef_[0] * yourHeight + regr.intercept_

print("Your height is {:>3} cm → Predicted weight: {:.2f} kg".format(yourHeight, yourWeight))


'''
Ở trên, khi bạn nhập 170 CM thì phần mềm sẽ dự đoán là nặng 61.3 Kg (dựa vào tập dữ
liệu ban đầu để hồi quy ra).
Còn rất nhiều ví dụ thực tế khác được Scikit-Learn trình bày rất kỹ, các bạn nên chủ động
nghiên cứu trên đó.
'''