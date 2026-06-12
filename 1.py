import logging
logging.basicConfig(
    filename='momo_transactions.log',
    level=logging.INFO,
    format='[%(asctime)s]-[%(filename)s]-%(message)s'
)
BALANCE=0
def display_menu():
    print("========== VÍ MOMO GIẢ LẬP ==========")
    print("1. Nạp tiền vào ví")
    print("2. Chuyển tiền")
    print("3. Xem lịch sử hệ thống")
    print("4. Xem số dư tài khoản")
    print("5. Thoát chương trình ")
def add_deposit():
    print("--- NẠP TIỀN VÀO VÍ ---")
    global BALANCE
    while True:
        try:
            user_input=input("Nhập số tiền muốn nạp: ").strip()
            if not user_input:
                print("Lỗi: Số tiền không được để trống.")
                continue
            new_money=int(user_input)
            if new_money<=0:
                print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
                logging.error(f"InvalidAmountError: Attempted to process {new_money} VND")
                continue
            else:
                BALANCE += new_money
                print(f"Nạp tiền thành công:+{new_money}")
                print(f"Số dư hiện tại:{BALANCE}")
                logging.info(f"Deposit successful:{new_money}VND . Current Balance:{BALANCE}")
                break
        except ValueError:
            print("Lỗi: Vui lòng nhập số tiền hợp lệ.")
            logging.error("ValueError: Invalid numeric input for deposit.")
            continue
def transfer_deposit():
    print("--- CHUYỂN TIỀN ---")
    global BALANCE
    while True:
        try:
            user_item=input("Nhập số điện thoại người nhận: ")
            if not user_item:
                print("Số điện thoại không để trống.")
                continue
            user_input=input("Nhập số tiền cần chuyển: ")
            if not user_input:
                print("Lỗi: Số tiền không được để trống.")
                continue
            new_sdt=int(user_item)
            new_money=int(user_input)
            if new_money <=0:
                print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
                logging.error(f"InvalidAmountError: Attempted to process {new_money} VND.")
                continue
            elif new_money>BALANCE:
                print("Giao dịch thất bại: Số dư của bạn không đủ")
                print(f"Số dư hiện tại: {BALANCE}")
                logging.error(f"InsufficientBalanceError: Attempted to transfer {new_money} VND with balance {BALANCE} VND.")
                break
            elif new_money>=10000000:
                BALANCE -= new_money
                print(f"Chuyển tiền thành công tới số điện thoại {new_sdt}")
                print(f"Số tiền đã chuyển:{new_money}")
                print(f"Số dư còn lại:{BALANCE}")
                logging.warning(f"High value transaction detected: {new_money} VND to {new_sdt}")
                logging.info(f"Transfer successful: -{new_money} VND to {new_sdt}. Current Balance: {BALANCE}")
                break
            else:
                BALANCE -= new_money
                print(f"Chuyển tiền thành công tới số điện thoại {new_sdt}")
                print(f"Số tiền đã chuyển:{new_money}")
                print(f"Số dư còn lại:{BALANCE}")
                logging.info(f"Transfer successful: -{new_money} VND to {new_sdt}. Current Balance: {BALANCE}")
                break
        except ValueError:
            print("Lỗi: phải nhập số nguyên.")
            continue
def read_logs():
    try:
        with open('momo_transactions.log', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        if not lines:
            print("\nChưa có lịch sử giao dịch nào trong hệ thống.")
            return
        print("\n--- 5 SỰ KIỆN GẦN NHẤT TRONG HỆ THỐNG ---")
        last_5_logs = lines[-5:]
        for idx, line in enumerate(last_5_logs, 1):
            print(f"{idx}. {line.strip()}")
            
    except FileNotFoundError:
        # Xử lý trường hợp file chưa từng được tạo ra
        print("\nChưa có lịch sử giao dịch nào trong hệ thống.")

def view_balance():
    print("\n--- SỐ DƯ VÍ MOMO ---")
    print(f"Số dư hiện tại: {BALANCE:,} VND")
    logging.info(f"Balance checked. Current Balance: {BALANCE}")
while True:
    display_menu()
    try:
        choice=int(input("Nhập lựa chọn : "))
    except ValueError:
        print("Chức năng không hợp lệ")
        continue
    match choice:
        case 1:
            add_deposit()
        case 2:
            transfer_deposit()
        case 3:
            read_logs()
        case 4:
            view_balance()
        case 5:
            break
        case _:
            print("Chức năng không hợp lệ")