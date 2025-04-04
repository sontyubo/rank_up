"""
classmethodの応用4
クラスの状態を使った統計情報
"""


class User:
    _user_count = 0

    def __init__(self, name):
        self.name = name
        User._user_count += 1

    # @classmethod
    # def user_count(cls):
    #     return cls._user_count


User("Alice")
User("Bob")

# classmethodを使って、クラスの情報を属性と同じように取得する
print(User.user_count())  # 2

# 直接カウンターにアクセスしていて、良い書き方ではない
print(User._user_count)  # 2
