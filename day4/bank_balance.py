bank_balance = {"user1": ("password", 1000), "user2": ("pass", 2000)}


def balance(name):
    return f"Bank balance of {name} is: {bank_balance[name][1]}"


def guardian(func, name, pwd):
    def secured():
        if bank_balance[name][0] == pwd:
            return func(name)

    return secured


username = "user2"
password = "pass"
balance = guardian(balance, username, password)

print(balance())