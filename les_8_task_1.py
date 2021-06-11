"""
1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:
func("papa")
6
func("sova")
9
"""


text = input("Введите какой-нибудь текст")
sub_text = dict()
len_text = len(text)
for i in range(1, len_text):
    j = 0
    while j + i < len_text+1:
        spam = text[j: j + i]
        spam_hash = hash(spam)
        if spam_hash not in sub_text:
            sub_text[spam_hash] = spam
        j += 1
print(f"Количество подстрок в строке:\n{text} = {len(sub_text)}")
print(sub_text)
