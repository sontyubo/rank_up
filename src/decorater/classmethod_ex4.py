"""
classmethodの応用3
登録パターン（レジストリ）に使う
"""


class Plugin:
    registry = {}

    @classmethod
    def register(cls, name):
        def decorator(subclass):
            cls.registry[name] = subclass
            return subclass

        return decorator


@Plugin.register("plugin_a")
class CSVPlugin(Plugin):
    pass


@Plugin.register("plugin_b")
class JSONPlugin(Plugin):
    pass


print(Plugin.registry)
