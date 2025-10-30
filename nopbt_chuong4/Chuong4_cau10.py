#Câu 10: Vẽ hình dùng Sleep
'''
'''
import time
import os

# Hàm xóa màn hình (Windows)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Danh sách các hình cần vẽ
hinh1 = """
    *
   * *
  *   *
 *     *
*********
*       *
*       *
"""

hinh2 = """
   * * * *
  *       *
 *         *
 *         *
  *       *
   * * * *
"""

hinh3 = """
*******
*      
*      
*******
*      
*      
*******
"""

hinh4 = """
*******
*     *
*     *
*******
*   *
*    *
*     *
"""

# Danh sách các hình
cac_hinh = [hinh1, hinh2, hinh3, hinh4]

# Hiển thị từng hình, mỗi hình cách nhau 5 giây
for hinh in cac_hinh:
    clear()
    print(hinh)
    time.sleep(5)
