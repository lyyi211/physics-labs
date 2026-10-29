#варіант 16 (4)
import string
text=input("Введіть текст: ")
text=text.translate(str.maketrans('', '', string.punctuation)).lower()
words=text.split()
print(words)

dict_count={}

for i in words:
    if i in dict_count:
        dict_count[i]+=1
    else:
        dict_count[i]=1
print("")
print(dict_count)

most_freq_words=set() 
max_count=max(dict_count.values())
for key, value in dict_count.items():
    if  value==max_count:
        most_freq_words.add(key)
print("")
print("Найчастіше,(",max_count,"повторів) зустрічаєтьcя:",most_freq_words)
