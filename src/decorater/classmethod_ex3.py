"""
classmethodの応用2
クラスごとに違う設定値を与えるファクトリーメソッド
"""


class Config:
    def __init__(self, db_url):
        self.db_url = db_url

    @classmethod
    def for_production(cls):
        return cls("postgres://prod-db")

    @classmethod
    def for_development(cls):
        return cls("sqlite://dev-db")


prod_config = Config.for_production()
dev_config = Config.for_development()

print(prod_config.db_url)  # postgres://prod-db
print(dev_config.db_url)  # sqlite://dev-db
