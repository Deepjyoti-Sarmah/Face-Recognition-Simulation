import numpy as np
import matplotlib.pyplot as plt

# Create a sample data array
data = np.random.rand( 5, 10)

# Create a heatmap
plt.imshow(data, cmap='viridis', interpolation='nearest')
plt.colorbar()

plt.title('Sample Heatmap')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')

plt.show()


####################################################

# import matplotlib.pyplot as plt
# import matplotlib.cm as cm

# # Create a list of topics and the number of papers published in each topic
# topics = ['Face detection', 'Face recognition', 'Drones',
#           'Ambient intelligence', 'Humanized computing']
# papers = [10, 20, 30, 40, 50]

# # Create a figure and a subplot
# fig, ax = plt.subplots()

# # Plot the heatmap
# plt.imshow(papers, cmap=cm.hot, interpolation='nearest')
# plt.xticks(range(len(topics)), topics, rotation=45)
# plt.ylabel('Number of papers')

# # Add a title to the heatmap
# plt.title('Topic heatmap for Journal of Ambient Intelligence and Humanized Computing')

# # Show the heatmap
# plt.show()