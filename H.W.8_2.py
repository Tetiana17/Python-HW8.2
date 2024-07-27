def is_palindrome(text):
    # видаляємо не алфавітно-цифрові символи і  переворюємо на нижній регістр
    cleaner_text = ''.join(c.lower() for c in text if c.isalnum())
    # перевіряємо чи є рядок паліндромом
    return cleaner_text == cleaner_text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
