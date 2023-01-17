import random
import string
total = string.ascii_letters + string.digits + string.punctuation
length = 16
password = "".join(random.sample(total, length))
print(password)

city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
print("Выбор случайного города из списка - ", random.choice(city_list))