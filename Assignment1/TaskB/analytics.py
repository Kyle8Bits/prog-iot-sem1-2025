import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.lines import Line2D


# Connect to SQLite database
conn = sqlite3.connect('../TaskA/climate.db')

# Example: load a table into a pandas DataFrame
df = pd.read_sql_query("SELECT * FROM temperature", conn)

# Don't forget to close the connection when done
conn.close()

average = sum(df['id'])/len(df['id'])

# Scatter Plot
plt.plot(df['id'], df['value'], linewidth = 4, color='black')
plt.title('Scatter Plot Example')

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
plt.savefig('scatter_plot.png')  # Save scatter plot as a PNG file
plt.show()  # Display scatter plot
