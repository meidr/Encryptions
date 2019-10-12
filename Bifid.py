def generate_table():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXZ'
    
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
        print(str(row) + getStr(table[row]))


def encrypt(table, words):
    string = table
    cipher = ''

    bar = []
    kol = []
    for ch in words.upper():
        if ch == "Y": ch = "Z"
        for baris in range(len(table)):
            if ch in table[baris]:
                bar.append(str(baris+1));
                kol.append(str((table[baris].index(ch) + 1)))    
    barkolom = bar + kol
    
    x = 0
    while x < len(barkolom):
        b = int(barkolom[x])
        k = int(barkolom[x+1])
        cipher += table[b-1][k-1]
        x += 2
    return cipher


def decrypt(table, cypertext):
    text = ''
    
    data = []
    
    for ch in cypertext.upper():
        for baris in range(len(table)):
            if ch in table[baris]:
                k = table[baris].index(ch)
                b = baris
                d = [b,k]
                data.append(d)

    dataString = ''
    for i in range(len(data)):
        for j in range(len(data[i])):
            dataString += str(data[i][j])+" "
    
    data = dataString.split()
    n = int(len(data)/2)
    data1 = data[:n]
    data2 = data[n:]
    
    for x in range(n):
        b = int(data1[x])
        k = int(data2[x])
        text += str(table[b][k])
    return text


if __name__ == '__main__':
    
    table = generate_table()
  
    print_table(table)
    
    cyp = input("Masukkan Plain Text: ")
    ciphertext = encrypt(table, cyp)

    print(ciphertext)

    print(decrypt(table, ciphertext))
