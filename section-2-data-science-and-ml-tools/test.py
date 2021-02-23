# Import and get matplotlib ready
import matplotlib.pyplot as plt
import numpy as np

# Prepare data (create two lists of 5 numbers, X & y)
X = np.linspace(0,100,5)
y = np.random.randint(0,50,5)

# Setup figure and axes using plt.subplots()
fig, ax = plt.subplots()

# Add data (X, y) to axes
line = ax.plot(X,y);

# Customize plot by adding a title, xlabel and ylabel



# Save the plot to file using fig.savefig()
