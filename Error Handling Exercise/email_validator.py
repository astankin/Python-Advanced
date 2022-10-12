class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = [".com", ".bg", ".org", ".net"]

while True:
    email = input()
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    user_name, domain = email.split("@")
    if len(user_name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    extension = email.split(".")[-1]
    if f".{extension}" not in valid_domains:
        raise InvalidDomainError(f"Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
