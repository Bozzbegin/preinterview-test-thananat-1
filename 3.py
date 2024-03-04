def search_and_display():
    
    a_input = input("กรอกคำที่ต้องการ (คั่นด้วย ,): ")
    x = input("คำที่ต้องการค้นหา: ")

    a = [word.strip() for word in a_input.split(',')]
    
    result = [word for word in a if x.lower() in word.lower()]
    indices = [a.index(word) for word in result]

    if result:
        result_str = f"คำที่เจอ: {result} index : {indices}"
    else:
        result_str = "No results found."

    print(result_str)

search_and_display()

