def zip_code_vn(zip_code):
    return len(zip_code) == 6 and zip_code.isdigit()
zip_code = "123456"
print(zip_code_vn(zip_code))

