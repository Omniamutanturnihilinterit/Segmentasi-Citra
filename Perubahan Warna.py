import cv2
import numpy as np

# Membaca citra
image = cv2.imread('path/to/your/input.jpg')

# Mengubah format citra BGR ke RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Mengubah dimensi citra menjadi satu dimensi
pixel_values = image_rgb.reshape((-1, 3))

# Mengubah tipe data piksel menjadi float32
pixel_values = np.float32(pixel_values)

# Kriteria penghentian iterasi
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

# Jumlah cluster yang diinginkan (misalnya 5)
k = 5

# Melakukan segmentasi citra menggunakan K-means clustering
_, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Mengkonversi nilai pusat cluster ke tipe data integer
centers = np.uint8(centers)

# Melakukan mapping label ke nilai pusat cluster
segmented_data = centers[labels.flatten()]

# Mengubah dimensi kembali ke dimensi asli citra
segmented_image = segmented_data.reshape(image_rgb.shape)

# Menampilkan citra asli dan hasil segmentasi
cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
