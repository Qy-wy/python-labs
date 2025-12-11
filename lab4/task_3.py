import matplotlib.pyplot as plt

categories = ['Седан', 'Кроссовер', 'Хэтчбек', 'Спорткар', 'Пикап']
values = [35, 30, 15, 10, 10]

fig, ax = plt.subplots(figsize=(8, 6))

ax.pie(values, labels=categories, autopct='%1.1f%%')
ax.set_title("Предпочтения пользователей по типам автомобилей")

plt.show()
