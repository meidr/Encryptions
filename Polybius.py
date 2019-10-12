def generate_table():
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    
    tabel = [[0] * 5 for row in range(5)]
    pos = 0
    for x in range(5):
        for y in range(5):
            tabel[x][y] = alphabet[pos]
            pos += 1
    return tabel


def getStr(x, format='%02s'):
    return ''.join(format % i for i in x)

def print_table(table):
    print(' ' + getStr(range(1, 6)))
    for row in range(0, len(table)):
        print(str(row + 1) + getStr(table[row]))


def encrypt(table, words):
    string = table
    cipher = ''

    for ch in words.upper():
        if ch == "J": ch = "I"
        for row in range(len(table)):
            if ch in table[row]:
                x = str((table[row].index(ch) + 1))
                y = str(row + 1)
                cipher += y + x
    return cipher


def decrypt(table, numbers):
    text = ''
    for index in range(0, len(numbers), 2):
        y = int(numbers[index]) - 1
        x = int(numbers[index + 1]) - 1
        if table[y][x] == "I":
            table[y][x] = "(I/J)"
        text += table[y][x]
    return text


if __name__ == '__main__':
    
    table = generate_table()
  
    print_table(table)
    
    cyp = input("Masukkan Plain Text: ")
    ciphertext = encrypt(table, cyp)

    print(ciphertext)

    print(decrypt(table, ciphertext))
