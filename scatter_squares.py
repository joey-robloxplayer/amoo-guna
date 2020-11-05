import matplotlib.pyplot as plt
plt.style.use('seaborn')
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = 'violet' )



ax.set_title("among us", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis='both', labelsize=14)


ax.axis( [0, 1100, 0, 1100000])

plt.show()