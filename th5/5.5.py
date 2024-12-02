print ("Nguyễn Danh Ánh")
print ("235752021610023")
print ("###########")
import mymodule
n=int(input("nhập một danh sách: "))
lst=[]
for i in range(n):
    value = float(input("nhập giá trị phần tử thứ {i + 1}:"))
    lst.append(value)
    
danh_sach_sap_xep=mymodule.sap_xep_danh_sach(lst)
value_max=mymodule.gia_tri_lon_nhat(lst)
value_min=mymodule.gia_tri_nho_nhat(lst)

print('danh sách đã sắp xếp là: ', danh_sach_sap_xep)
print('giá trị lớn nhất là:',value_max)
print('giá trị nhỏ nhất là:',value_min)
