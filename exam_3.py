
card_num = input("Enter the card number: ")


def credit_card(num):
    num = "".join(num.split("-"))
    return f"****-****-****-{num[8:12]}"


print(credit_card(card_num))


def palindrome(string):
    if string == string[::-1]:
        return True
    return False

print(palindrome("cat"))