def Longest_word(s):
    words=s.split()
    if not words:
        return ""
    max_word=words[0]
    m=0
    for i in max_word:
        m+=1
    for word in words:
        k=0
        for j in word:
            k+=1
        if k>m:
            m=k
            max_word=word
    return max_word
def test_Longest_word():
    if Longest_word("Привет")==("Привет"):
        print("+")
    else:
        print(f"error,для 'Привет' ожидается:'Привет', а у вас")
    if Longest_word("a b c d") ==("a"):
        print("+")
    else:
        print(f"error,для 'a b c d' ожидается:'a', а у вас")
    if Longest_word("Третие задание") == ("задание"):
        print("+")
    else:
        print(f"error,для 'Третие задание' ожидается:'задание', а у вас")
    if Longest_word("собака кошка попугай слон") == ("попугай"):
        print("+")
    else:
        print(f"error,для 'собака кошка попугай слон' ожидается:'попугай', а у вас")
    if Longest_word("тетрадь ручка блокнот сумка вода") == ("тетрадь"):
        print("+")
    else:
        print(f"error,для 'тетрадь ручка блокнот сумка вода' ожидается:'тетрадь', а у вас")
test_Longest_word()
s=str(input())
print(Longest_word(s))