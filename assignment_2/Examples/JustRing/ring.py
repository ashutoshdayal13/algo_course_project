import numpy as np
import matplotlib.pyplot as plt

# Define the dimensions of the matrix
rows = 150
cols = 150

# Create a 2D matrix with random values between 0 and 255
random_matrix = np.random.randint(256, size=(rows, cols))

p1 = np.zeros((rows, cols))
p2 = np.zeros((rows, cols))

p1[:,:] = random_matrix
p2[:,:] = random_matrix


pattern = np.random.randint(256, size=(rows, cols))

offset=4



# Make a Ring

for i in range(rows):
    for j in range(cols):

        if ((rows//6)**2)<((i-rows//2)**2 + (j-cols//2)**2) <((rows//3)**2):
            p1[i,j] = pattern[i,j]
            if j-offset>=0:
                p2[i,j-offset] = pattern[i,j]





# Display the matrix as an image
plt.imshow(p1, cmap='gray')
plt.axis('off')
plt.show()


# Display the matrix as an image
plt.imshow(p2, cmap='gray')
plt.axis('off')
plt.show()
