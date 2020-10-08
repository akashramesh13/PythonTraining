def hello():
    return "Hello"


def guardian(func):
    def make_secure():
        if user["role"] == "admin":
            return func

    return make_secure


hello = guardian(hello())
user = {"role": "user"}
print(hello())
