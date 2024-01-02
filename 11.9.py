def tiec(nguoi_den, ten):
    """
    Kiểm tra xem một vị khách có đến trễ tiệc hay không.
    
    Parameters:
    - arrivals: danh sách các tên khách
    - name: tên của vị khách cần kiểm tra
    
    Returns:
    - True nếu vị khách đến trễ tiệc, False nếu ngược lại.
    """
    so_khach = len(arrivals)
    index_of_guest = arrivals.index(ten)
    
    return index_of_guest >= so_khach / 2 and index_of_guest != so_khach - 1

# Ví dụ sử dụng
arrivals = ['nguyen','thai','hieu','chuyen','trang']

name_to_check = 'thai'
result = tiec (arrivals, name_to_check)

print(name_to_check, "có đến trễ tiệc hay không:", result)
