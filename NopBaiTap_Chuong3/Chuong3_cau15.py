#Câu 15: Giải thích cách chạy các dòng lệnh range
'''
Yêu cầu:
(a) range(5)
(b) range(5, 10)
(c) range(5, 20, 3)
(d) range(20, 5, -1)
(e) range(20, 5, -3)
(f) range(10, 5)
(g) range(0)
(h) range(10, 101, 10)
(i) range(10, -1, -1)
(j) range(-3, 4)
(k) range(0, 10, 1)
                          
 
                        Bài làm 
                        (a) range(5)

Tương đương: range(0, 5, 1)

Kết quả: [0, 1, 2, 3, 4]

Bắt đầu từ 0, đến trước 5, mỗi bước +1.

(b) range(5, 10)

Kết quả: [5, 6, 7, 8, 9]

Bắt đầu từ 5, đến trước 10, mỗi bước +1.

(c) range(5, 20, 3)

Kết quả: [5, 8, 11, 14, 17]

Bắt đầu từ 5, đến trước 20, mỗi bước +3.

(d) range(20, 5, -1)

Kết quả: [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]

Bắt đầu từ 20, đến trước 5, giảm dần mỗi bước -1.

(e) range(20, 5, -3)

Kết quả: [20, 17, 14, 11, 8]

Bắt đầu từ 20, đến trước 5, giảm dần mỗi bước -3.

(f) range(10, 5)

Mặc định bước là +1, nhưng start > stop, nên không thỏa điều kiện chạy.

-> Kết quả: [] (rỗng)

(g) range(0)

Giống range(0, 0), không có giá trị nào để duyệt.

-> Kết quả: [] (rỗng)

(h) range(10, 101, 10)

Kết quả: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

Bắt đầu từ 10, đến trước hoặc bằng 100, bước +10.

(i) range(10, -1, -1)

Kết quả: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

Bắt đầu từ 10, giảm dần đến 0.

(j) range(-3, 4)

Kết quả: [-3, -2, -1, 0, 1, 2, 3]

Bắt đầu từ -3, tăng đến trước 4, bước +1.

(k) range(0, 10, 1)

Kết quả: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Bắt đầu từ 0, tăng đến trước 10, bước +1.
'''