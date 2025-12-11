import matplotlib.pyplot as plt

categories = ['Mazda', 'Toyota', 'Audi', 'Honda', 'Ford']
values = [30, 70, 40, 65, 55]

fig, ax = plt.subplots(figsize=(8, 6))

ax.barh(categories, values, color='skyblue')

ax.set_title('Популярность автомобильных марок')
ax.set_xlabel('Количество пользователей')
ax.set_ylabel('Марка')

ax.grid(axis='x', linestyle='--', alpha=0.4)

plt.show()
