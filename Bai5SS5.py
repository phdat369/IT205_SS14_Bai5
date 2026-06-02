# Phân tích 
# Ở bài này thì chúng ta cần làm một menu gồm 3 chức năng: nhập và xem báo cáo,xem hướng dẫn và thoát 
# Thì trong bài này chúng ta cần dùng 1 vòng lặp while và match_case để làm menu, để chương trình chạy đến lúc nào người dùng muốn kết thúc 
# Để vòng lặp chạy đúng thì điều kiện vòng lặp là để điều kiện biến chọn là khác 3 hoặc true sau đó break ở chức năng 3 để kết thúc
# Ở chức năng 1 thì chúng ta cho người dùng nhập vào 3 biến tương ứng số chi nhánh, số lớp từng chi nhánh và số học viên 
# Sau đó dùng câu điều kiện để check đúng với các trường hợp đó và sau đó hiển thị ra  
# Chức năng 2 thì chỉ cần print ra dòng thông báo hướng dẫn 
# Và chức năng 3 là thoát vòng lặp và kết thúc chương trình 
while True:
    choose = int(input("=== MENU === \n" 
    "1.Nhập dữ liệu và xem báo cáo \n" 
    "2.Xem hướng dẫn sử dụng chương trình \n" 
    "3.Thoát chương trình \n")) 
    match choose:
        case 1:
            quantity_branch = int(input("Nhập số chi nhánh: "))
            max_students = 0
            best_branch = 0
            for branch in range(1,quantity_branch+1):
                quantity_class = int(input(f"Nhập số lớp của chi nhánh {branch}: "))
                sum_student = 0
                class_low_student = False
                for class_room in range(1,quantity_class+1):
                    student_quantity = int(input(f"Nhập số học viên đi học của lớp: {class_room}: "))
                    while student_quantity < 0 :
                        print("Số học viên không hợp lệ. Vui lòng nhập lại")
                        student_quantity = int(input(f"Nhập số học viên đi học của lớp: {class_room}: "))
                    sum_student = sum_student + student_quantity 
                    if student_quantity < 10: 
                        if class_low_student == False:
                            print("Các lớp có sĩ số dưới 10 học viên:", end=" ")
                    print(class_room, end=" ")
                    class_low_student = True
                print(f"Tổng số học viên của chi nhánh: {branch}: {sum_student}")
                if sum_student > max_students:
                    max_students = sum_student
                    best_branch = branch

                if class_low_student == False:
                    print("Không có lớp nào dưới 10 học viên")
            print(f"Chi nhánh có số học sinh nhiều nhất: {best_branch}")
        case 2: 
            print("Nhập số chi nhánh, nhập số lớp và nhập số học sinh theo yêu cầu, nhập số nguyên lớn hơn không, không nhâp chuỗi hoặc số rỗng không có ý nghĩa gì")
        case 3:
            break
        case _:
            print("Lựa chọn không hợp lệ")
print("=== Chương trình kết thúc ===")