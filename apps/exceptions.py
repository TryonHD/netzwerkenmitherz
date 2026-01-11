class PasswordNotMatched(Exception):
    def __init__(self):
        self.message = "Password not matched"

    def __str__(self):
        return repr(self.message)


class EmailAddressExists(Exception):
    def __init__(self):
        self.message = "Email already exists"

    def __str__(self):
        return repr(self.message)
