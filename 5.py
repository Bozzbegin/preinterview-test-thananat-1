class WebsiteHistory:
    def __init__(self):
        self.history = []
        self.current_index = -1

    def input_url(self, url):
        self.history = self.history[:self.current_index + 1]
        self.history.append(url)
        self.current_index = len(self.history) - 1
        print(f"เพิ่ม {url} ลงในประวัติการเข้าชม")

    def previous(self):
        if self.current_index > 0:
            self.current_index -= 1
            print(f"{self.history[self.current_index]}")
        else:
            print("No website to previous.")

    def next(self):
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
            print(f"{self.history[self.current_index]}")
        else:
            print("No website to go.")

    def current(self):
        print(f"Now you are on {self.history[self.current_index]}")

    def all(self):
        print("Website History:")
        for index, url in enumerate(self.history):
            print(f"{index + 1}. {url}")

history_system = WebsiteHistory()

while True:
    user_input = input("ป้อนคำสั่ง: ") #input: ต่อด้วย URL #input: prev, next, current, all, exit ได้เลยครับ
    
    if user_input.startswith("input "):
        url = user_input.split(" ")[1]
        history_system.input_url(url)
    elif user_input == "prev":
        history_system.previous()
    elif user_input == "next":
        history_system.next()
    elif user_input == "current":
        history_system.current()
    elif user_input == "all":
        history_system.all()
    elif user_input == "exit":
        print("ออกจากโปรแกรม")
        break
    else:
        print("ไม่ถูกต้อง กรุณาลองอีกครั้ง !!")
