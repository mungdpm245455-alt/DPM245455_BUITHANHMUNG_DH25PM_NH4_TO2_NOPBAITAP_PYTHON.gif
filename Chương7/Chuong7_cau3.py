#Câu 3: Xử lý XML File
'''
Yêu cầu:
Cho 1 file XML có cấu trúc và dữ liệu như dưới đây (employees.xml):
<?xml version="1.0" encoding="UTF-8" ?>
<employees>
 <employee>
 <id>1</id>
 <name>Trần Duy Thanh</name>
 </employee>
 <employee>
 <id>2</id>
 <name>Lê Hoành Sử</name>
 </employee>
 <employee>
 <id>3</id>
 <name>Hồ Trung Thành</name>
 </employee>
</employees>
Hãy dùng XML DOM để đọc dữ liệu lên màn hình.
'''
from xml.dom.minidom import parse
import xml.dom.minidom
# Mở file xml bằng minidom parser
DOMTree = xml.dom.minidom.parse("employees.xml")
collection = DOMTree.documentElement
# Lấy tất cả tag là employee
employees = collection.getElementsByTagName("employee")
# Duyệt vòng lặp để lấy toàn bộ dữ liệu ra
for employee in employees:
 tag_id = employee.getElementsByTagName('id')[0]
 id=tag_id.childNodes[0].data
 tag_name = employee.getElementsByTagName('name')[0]
 name=tag_name.childNodes[0].data
 print(id,'\t',name)
