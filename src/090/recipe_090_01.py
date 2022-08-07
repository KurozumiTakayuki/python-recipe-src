class User:
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail

    def __str__(self):
        return "ユーザ名:" + self.name + ", メールアドレス:" + self.mail

    def __repr__(self):
        return str({'name': self.name, 'mail': self.mail})


user = User("Suzuki", "suzuki@hoge.com")
print(user)
print(repr(user))
