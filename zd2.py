test =['a big shot'
       'a shot big'
       'big a shot']
def check_if_palindrome(string):
    prepared_str = string.replace('  ',  '').lower()
    if prepared_str == prepared_str[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
        for item in test:
            print('Строка является палиндромом:', check_if_palindrome(item))