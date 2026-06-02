student_records = [
    {
        "student_id": "RA01",
        "name": "Nguyễn Văn Code",
        "current_points": 1500,
        "spent_points": 500,
        "refunded_points": 0,
        "multiplier": 1.0
    },
    {
        "student_id": "RA02",
        "name": "Trần Thị Bug",
        "current_points": 800,
        "spent_points": 1200,
        "refunded_points": 100,
        "multiplier": 1.5
    },
    {
        "student_id": "RA03",
        "name": "Lê Văn Fix",
        "current_points": 300,
        "spent_points": 0,
        "refunded_points": 0,
        "multiplier": 2.0
    }
]

def validate_point(point):
    if point <= 0:
        return False
    else:
        return True
    
def find_student(find_id, record):
    for i, student in enumerate(record):
        if student['student_id'] == find_id:
            return i
    return -1

def display_statements(records):
    print('--- SAO KÊ ĐIỂM SỐ ---')
    for i, student in enumerate(records):
        print(f'{i+1}. Mã: {student['student_id']} | Tên: {student['name']} | Hiện có: {student['current_points']} | Đã tiêu: {student['spent_points']} | Hoàn trả: {student['refunded_points']} | Hệ số: x{student['multiplier']} | Trạng thái: {'Cần tích lũy thêm' if student['current_points'] < 500 else ('Thành viên tiềm năng' if student['current_points'] <= 1500 else 'Thành viên ưu tú')} ')

def redeem_rewards(records):
    find_id = input('Nhập mã học viên đổi quà: ').strip().upper()
    find_index = find_student(find_id, records)
    if find_index == -1:
        print('Không tìm thấy hồ sơ học viên')
    else:
        while True:
            spent_point = int(input('Nhập số điểm cần tiêu: '))
            if not(validate_point(spent_point)):
                print('Phải nhập số nguyên dương')
            elif spent_point > records[find_index]['current_points']:
                print('Số dư điểm không đủ để thực hiện giao dịch')
            else:
                break
        records[find_index]['current_points'] -= spent_point
        records[find_index]['spent_points'] += spent_point
        print(f'>> Giao dịch thành công! {records[find_index]['name']} đã tiêu {spent_point} điểm. Số dư còn lại: {records[find_index]['current_points']} điểm')

def appeal_score(records):
    find_id = input('Nhập mã học viên cần phúc khảo: ').strip().upper()
    find_index = find_student(find_id, records)
    if find_index == -1:
        print('Không tìm thấy hồ sơ học viên')
    else:
        while True:
            refund_point = int(input('Nhập số điểm hoàn lại: '))
            if not(validate_point(refund_point)):
                print('Phải nhập số nguyên dương')
            elif refund_point > records[find_index]['spent_points']:
                print('Không thể hoàn số điểm lớn hơn tổng điểm đã tiêu')
            else:
                break
        records[find_index]['spent_points'] -= refund_point
        records[find_index]['current_points'] += refund_point
        records[find_index]['refunded_points'] += refund_point
        print(f'>> Hoàn điểm thành công! {records[find_index]['name']} được cộng lại {refund_point} điểm.')

def activate_multiplier(records):
    find_id = input('Nhập mã học viên nhận hệ số: ').strip().upper()
    find_index = find_student(find_id, records)
    if find_index == -1:
        print('Không tìm thấy hồ sơ học viên')
    else:
        while True:
            new_multiplier = input('Nhập hệ số nhân mới (1.0 - 3.0): ')
            try:
                new_multiplier = float(new_multiplier)
                if 1 <= new_multiplier <= 3:
                    break
                else:
                    print('Hệ số nhân không hợp lệ. Chỉ chấp nhận số từ 1.0 đến 3.0')
            except:
                print('Hệ số nhân không hợp lệ. Chỉ chấp nhận số từ 1.0 đến 3.0')
        records[find_index]['multiplier'] = new_multiplier
        print(f'>> Đã kích hoạt hệ số x{new_multiplier} cho học viên {records[find_index]['name']}')

def grade_assignment(records):
    find_id = input('Nhập mã học viên nhận hệ số: ').strip().upper()
    find_index = find_student(find_id, records)
    if find_index == -1:
        print('Không tìm thấy hồ sơ học viên')
    else:
        while True:
            get_point = int(input('Nhập số điểm gốc đạt được: '))
            if not(validate_point(get_point)):
                print('Phải nhập số nguyên dương')
            else:
                break
        real_get_point = get_point * records[find_index]['multiplier']
        print(f'>> Hệ số hiện tại của {records[find_index]['name']} là x{records[find_index]['multiplier']}. Điểm thực nhận: {real_get_point}')
        records[find_index]['current_points'] += real_get_point
        print(f'>> Đã cộng {real_get_point} điểm vào tài khoản!')

while True:
    choice = input('''
===== HỆ THỐNG NGÂN HÀNG ĐIỂM SỐ RIKKEI ACADEMY =====
1. Hiển thị sao kê điểm số
2. Đổi điểm lấy phần thưởng
3. Phúc khảo bài thi (Hoàn điểm)
4. Kích hoạt (Hệ số nhân điểm)
5. Chấm bài (thêm điểm)
6. Thoát chương trình
=====================================================
> Nhập lựa chọn: ''')
    if choice == '1':
        display_statements(student_records)
    elif choice == '2':
        redeem_rewards(student_records)
    elif choice == '3':
        appeal_score(student_records)
    elif choice == '4':
        activate_multiplier(student_records)
    elif choice == '5':
        grade_assignment(student_records)
    elif choice == '6':
        print('chào tạm biệt')
        break
    else:
        print('Lựa chọn không hợp lệ')