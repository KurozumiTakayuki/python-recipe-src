class User:
    """ ユーザクラス """

    def __init__(self, name, mail):
        self.name = name
        self.mail = mail

    def print_user_info(self):
        print("ユーザ名:" + self.name)
        print("メールアドレス:" + self.mail)


class StudentUser(User):
    def __init__(self, name, mail, grade):
        super().__init__(name, mail)
        self.grade = grade

    def answer_question(self):
        print("問題を回答します")

    def print_grade(self):
        print(str(self.grade) + "年生です")

# StudentUserオブジェクト生成
student = StudentUser("Suzuki", "suzuki@example.com", 3)

# Userのメソッド実行
student.print_user_info()

# StudentUserのメソッド実行
student.answer_question()
student.print_grade()
