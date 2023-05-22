# Segmentasi-Citra
Untuk membuat segmentasi citra menggunakan Python, Anda dapat menggunakan berbagai pustaka dan algoritma yang tersedia. Salah satu pendekatan yang umum digunakan adalah segmentasi citra berdasarkan pewarnaan (color-based segmentation) menggunakan algoritma seperti K-means clustering atau metode berbasis intensitas seperti Thresholding. Berikut ini adalah contoh penggunaan algoritma K-means clustering untuk segmentasi citra menggunakan Python dan pustaka OpenCV:

```python
import cv2
import numpy as np

# Membaca citra
image = cv2.imread('path/to/your/image.jpg')

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
```

Berikut gambar yang sudah di eksekusi
![image](https://github.com/Omniamutanturnihilinterit/Segmentasi-Citra/assets/92959023/ba69b39e-2881-4275-becf-060406a085e0)


Pastikan untuk mengganti `'path/to/your/image.jpg'` dengan jalur berkas citra yang ingin Anda segmentasi. Kode di atas membaca citra, melakukan segmentasi menggunakan K-means clustering dengan jumlah cluster yang ditentukan, dan menampilkan citra asli serta citra hasil segmentasi.

Anda juga dapat mengeksplorasi pustaka lain seperti scikit-image, PIL, atau algoritma segmentasi lainnya seperti metode pemrosesan tepi (edge-based methods) atau segmentasi berdasarkan perbedaan tekstur (texture-based segmentation) tergantung pada kebutuhan spesifik Anda.
