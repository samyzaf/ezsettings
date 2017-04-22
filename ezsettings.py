class Settings(dict):
    def __init__(self, d=None, **opt):
        if not d is None:
            self.update(d)
        for key in opt:
            self[key] = opt[key]

    def set(self, key, value):
        self[key] = value
        return value

    def get(self, key, default_value):
        if key in self:
            return self[key]
        else:
            self.set(key, default_value)
            return default_value

    def remove(self, key):
        if key in self:
            return self.pop(key)
        else:
            return None
