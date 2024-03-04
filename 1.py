def check_number(n):
    result = []
    for i in range(1, n + 1):
        text = ""
        if i % 3 == 0:
            text += "Ping"
        if i % 5 == 0:
            text += "Pong"
        if text:
            result.append(f"{i}: {text}")

    return result


def show_result(n):
    try:
        n = int(n)
        result = check_number(n)

        if result:
            result_str = "\n".join(result)
            result_str = result_str.replace("PingPong", "Ping Pong")
            print(f"\nผลลัพธ์สำหรับ = {n}:\n\n{result_str}")
        else:
            print("ไม่มีตัวเลขที่ตรงตัวตามเงื่อนไข")
    except ValueError:
        print("กรุณากรอกตัวเลขเท่านั้น")

n_value = input("INPUT : ")
show_result(n_value)
