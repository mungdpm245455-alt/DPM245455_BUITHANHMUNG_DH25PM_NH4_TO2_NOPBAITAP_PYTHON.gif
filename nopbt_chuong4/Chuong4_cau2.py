#Câu 2: Viết Hàm để chơi Game Đoán Số
'''
Yêu cầu:
Máy ra 1 số trong đoạn [1...100]
Người chơi đoán số, chỉ được phép đoán sai 7 lần. Mỗi lần đoán sẽ thông báo số
người chơi đoán nhỏ hơn hay lớn hơn số của mày và hiển thị số lần đoán
Game kết thúc khi: Đoán sai quá 7 lần hoặc đoán trúng trước 7 lần.
Sau khi game kết thúc hỏi người chơi có tiếp tục hay không?
'''
from random import randrange

while True:
    somay = randrange(1, 101)
    solandoan = 0
    win = False

    while solandoan < 7:
        solandoan += 1
        songuoi = int(input("Máy đoán [1..100], mời bạn đoán: "))
        print("Bạn đoán lần thứ", solandoan)

        if somay == songuoi:
            print("Chúc mừng bạn đoán đúng, số máy là =", somay)
            win = True
            break

        if somay > songuoi:
            print("Bạn đoán sai, số máy > số bạn")
        elif somay < songuoi:
            print("Bạn đoán sai, số máy < số bạn")

    if win == False:
        print("GAME OVER! Số máy =", somay)

    hoi = input("Tiếp không? (gõ 'k' để thoát): ")
    if hoi == "k":
        break

print("Cám ơn bạn đã chơi Game!")
