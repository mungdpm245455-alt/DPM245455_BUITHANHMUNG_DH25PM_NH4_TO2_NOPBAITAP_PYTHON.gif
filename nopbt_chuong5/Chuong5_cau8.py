#Câu 8: Tách lấy tên bài hát
'''
Yêu cầu:
Cho một chuỗi là đường dẫn của 1 file nhạc, ví dụ: d:\\music\muabui.mp3
Hãy viết 2 hàm để:
- Lấy ra muabui.mp3
- Lấy ra muabui
Lưu ý đường dẫn bài hát là bất kỳ. Nên khi truyền vào bài hát nào thì lấy chính xác theo
bài hát đó.
'''
def LayTenFile(full_path):
    # Tách theo dấu "\" và lấy phần cuối cùng
    return full_path.split('\\')[-1]

def LayTenBaiHat(full_path):
    ten_file = LayTenFile(full_path)
    # Tách phần mở rộng (đuôi .mp3, .wav, .flac, ...)
    return ten_file.split('.')[0]

# --- Chương trình chính ---
path = input("Nhập đường dẫn file nhạc: ")

print("Tên file có phần mở rộng:", LayTenFile(path))
print("Tên bài hát (không có phần mở rộng):", LayTenBaiHat(path))