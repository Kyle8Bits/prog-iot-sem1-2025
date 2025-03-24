import sqlite3
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.lines import Line2D


# Connect to SQLite database
conn = sqlite3.connect('../TaskA/climate.db')

# Example: load data from the "temperature" table
cursor = conn.cursor()
cursor.execute("SELECT id, value FROM temperature")  # Select only the required columns

# Fetch all rows from the executed query
rows = cursor.fetchall()

# Close the connection
conn.close()

# Separate the data into two lists: one for 'id' and one for 'value'
ids = [row[0] for row in rows]
values = [row[1] for row in rows]

average = sum(ids) / len(ids)

# Scatter Plot
plt.plot(ids, values, linewidth=4, color='black')
plt.title('Temperature Chart')

plt.ylabel('Temperature')

plt.axhspan(0, 15, color='blue', alpha=0.1)  # Red area for 10-20 range
plt.axhspan(15, 25, color='green', alpha=0.1)  # Yellow area for 20-25 range
plt.axhspan(25, 50, color='red', alpha=0.1)  # Green area for 25-30 range


# Custom legend with different shapes
custom_legend = [
    Line2D([0], [0], marker='s', color='w', markerfacecolor='red', alpha = 0.5, markersize=10, label='Hot'),
    Line2D([0], [0], marker='s', color='w', markerfacecolor='green', alpha = 0.5, markersize=10, label='Comfortable'),
    Line2D([0], [0], marker='s', color='w', markerfacecolor='blue', alpha = 0.5, markersize=10, label='Cold')
]

# Create the custom legend
plt.legend(handles=custom_legend, loc='upper right')


plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.savefig('temperature.png')  # Save scatter plot as a PNG file
plt.show()  # Display scatter plot
