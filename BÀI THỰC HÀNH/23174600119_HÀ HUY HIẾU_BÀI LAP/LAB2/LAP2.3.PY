import numpy as np

def read_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f]

efficiency = list(map(float, read_file(r'F:\23174600119_HÀ HUY HIẾU\BÀI TẬP THỰC HÀNH\LAB2\efficiency.txt')))
shifts = read_file(r'F:\23174600119_HÀ HUY HIẾUBÀI TẬP THỰC HÀNH\LAB2\shifts.txt')

np_efficiency = np.array(efficiency)
np_shifts = np.array(shifts)

# Tính hiệu suất trung bình
def avg_efficiency(shift):
    return np.mean(np_efficiency[np_shifts == shift])

print("Hiệu suất ca Morning:", avg_efficiency('Morning'))
print("Hiệu suất các ca khác:", np.mean(np_efficiency[np_shifts != 'Morning']))

# Mảng structured array
workers = np.array(list(zip(np_shifts, np_efficiency)), dtype=[('shift', 'U10'), ('efficiency', 'float')])
sorted_workers = np.sort(workers, order='efficiency')

print("Ca làm việc hiệu suất cao nhất:", sorted_workers[-1])
print("Ca làm việc hiệu suất thấp nhất:", sorted_workers[0])

