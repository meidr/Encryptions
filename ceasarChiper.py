'''def encode(shiftCount,plaintText):
    abjat=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for char in plaintText:
        if(plaintText.isalpha() and plaintText.upper()):
            #harus true
            print(plaintText.isalpha())
            #memisahkan stringnya menjadi satu-persatu
            text=[plaintText[i:i + 1]
                for i in range(0, len(plaintText), 1)]
            for i in range(0,len(abjat),shiftCount):
                if(text[i]==abjat[i]):

        else :
            print("maaf tidak bisa memasukan ")


print("Masukan plaintext :")
plaintText=input()
encode(3,plaintText)'''


def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        #cek abjac ada yang besar atau tidak

        if (char.isupper()):
            result += chr((ord(char) + int(s) - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + int(s) - 97) % 26 + 97)
    return result

def decrypt():
    
    print('Masukan kata/kalimat:')
    ciphertext = input()
    print('Masukan nilai value: ')
    shift = int(input())
    ciphertext = ciphertext.split()
    sentence = []
    
    for word in ciphertext:
        
        cipher_ords = [ord(x) for x in word]
        plaintext_ords = [o - shift for o in cipher_ords]
        plaintext_chars = [chr(i) for i in plaintext_ords]
        plaintext = ''.join(plaintext_chars)
        sentence.append(plaintext)
        
    sentence = ' '.join(sentence)
    print('Hasil Dekripsi:', sentence)


print("Masukan plaintext : ")
plaintText= input()
print("Masukan shiftCount : ")
shiftCount=input()
print("Plain Text : " + str(plaintText))
print("Shift pattern : " + str(shiftCount))
print("Cipher: " + encrypt(str(plaintText), shiftCount))
print("========================================================")
print("========================================================")
decrypt()
