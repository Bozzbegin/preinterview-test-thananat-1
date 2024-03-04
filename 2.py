def check_numbers(n, i, j):
    result = []
    for num in range(1, n + 1):
        text = ""
        if num % i == 0:
            text += "Ping"
        if num % j == 0:
            text += "Pong"
        if text:
            result.append(f"{num}: {text}")
    return result

def show_result(n, i, j):
    try:
        n = int(n)
        i = int(i)
        j = int(j)

        result = check_numbers(n, i, j)

        if result:
            result_str = "\n".join(result)
            result_str = result_str.replace("PingPong", "Ping Pong")
            print(f"\nผลลัพธ์สำหรับ n = {n}, i = {i}, j = {j}:\n\n{result_str}")
        else:
            print("ไม่มีตัวเลขที่ตรงตามเงื่อนไข")
    except ValueError:
        print("กรุณากรอกตัวเลขเท่านั้น")

n = input("n: ")
i = input("i: ")
j = input("j: ")

show_result(n, i, j)
