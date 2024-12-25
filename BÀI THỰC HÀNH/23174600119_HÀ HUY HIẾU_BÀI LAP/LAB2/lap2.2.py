import pandas as pd
import numpy as np

# Đọc dữ liệu CSV
data = pd.read_csv(r'F:\23174600119_HÀ HUY HIẾU\BÀI TẬP THỰC HÀNH\LAB2\diem_hoc_phan.csv')
numpy_data = data.to_numpy()

# Qui đổi điểm
scores = numpy_data[:, 2:].astype(float)
def grade(score):
    if score >= 8.5:
        return 'A'
    elif score >= 8.0:
        return 'B+'
    elif score >= 7.0:
        return 'B'
    elif score >= 6.5:
        return 'C+'
    elif score >= 5.5:
        return 'C'
    elif score >= 5.0:
        return 'D+'
    elif score >= 4.0:
        return 'D'
    else:
        return 'F'

vectorized_grade = np.vectorize(grade)
letter_grades = vectorized_grade(scores)
print("Điểm chữ:", letter_grades)

# Chia tách và phân tích
for i, col in enumerate(data.columns[2:]):
    print(f"Phân tích {col}:")
    print("Tổng:", np.sum(scores[:, i]))
    print("Trung bình:", np.mean(scores[:, i]))
    print("Độ lệch chuẩn:", np.std(scores[:, i]))