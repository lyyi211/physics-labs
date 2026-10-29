#варіант 16, №3

a=input('Введіть числові елементи списку: ').split()
numbers=list(map(float, a))
print(numbers)

def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        value=numbers[i]
        j=i
        while j>0 and numbers[j-1]>value:
            numbers[j]=numbers[j-1]
            j-=1
        numbers[j]=value
insertion_sort(numbers)
print(numbers)

series_lenght=0
quantity=1
previous=numbers[0]
modes=[]

for i in range(1,len(numbers)):
    if numbers[i]==previous:
        quantity+=1
    else:
        if quantity>series_lenght:
            series_lenght=quantity
            modes=[previous]
        elif quantity==series_lenght:
            modes.append(previous)   
        quantity=1
    previous=numbers[i]
    
if quantity>series_lenght:
    series_lenght=quantity
    modes=[previous]
elif quantity==series_lenght:
    modes.append(previous)


if series_lenght==1:
    print("Моди немає")
else:
    print("Мода:",modes)
    
#спочатку зробили сортування вставкою, складність О(m^2); потім пошук моди через найдовшу серію повторень, складність О(m).
#щоб знайти моду без попереднього сортування треба змінити алгоритм її пошуку.

a=input('Введіть числові елементи списку: ').split()
numbers=list(map(float, a))
print(numbers)

unique_numbers=[]
frequencies=[]

for num in numbers:
    if num in unique_numbers:
        index=unique_numbers.index(num)
        frequencies[index]+=1
    else:
        unique_numbers.append(num)
        frequencies.append(1)
max_freq=max(frequencies)

modes=[]
for i in range(len(unique_numbers)):
    if frequencies[i]==max_freq:
        modes.append(unique_numbers[i])

if max_freq==1:
    print("Моди немає")
else:
    print("Мода:",modes)

#складність така ж як і у випадку з сортуванням: О(m^2); отже використання сортування недоцільне.
