print("Sinh vien:Nguyễn Danh Ánh")
print("Mssv:235752021610023")
def kiem_tra_so(chuoi_nhi_phan):
    so_nhi_phan=chuoi_nhi_phan.split(',')
    so_chia_het=[]
    for so in so_nhi_phan:
        so_thap_phan=int(so,2)
        if so_thap_phan%5==0:
            so_chia_het.append(so)
        print(','.join(so_chia_het))
chuoi_nhi_phan=input('nhập chuỗi số nhị phân:')
kiem_tra_so(chuoi_nhi_phan)
