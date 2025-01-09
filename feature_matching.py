import cv2
import matplotlib.pyplot as plt

#gorsellestirme fonksiyonu
def imshow_img(img, title):
    plt.figure(), plt.imshow(img, cmap="gray"), plt.title(title)

# Çikolata resimlerinin yolları
image_paths = [
    "Resim yolu/chocolates.jpg",   # Chocolates
    "Resim yolu/nestle.jpg",       # Nestle
    "Resim yolu/snickers.jpg",     # Snickers
    # Diğer çikolataları buraya ekleyebilirsiniz
]

# Resimleri oku ve görselleştir
images = []
for path in image_paths:
    img = cv2.imread(path, 0)  # Resimleri gri tonlamada oku
    images.append(img)
    imshow_img(img, f"Resim: {path.split('/')[-1]}")

# ORB için tanımlayıcı
orb = cv2.ORB_create()

# Brute-force matcher
bf_orb = cv2.BFMatcher(cv2.NORM_HAMMING)

# ORB ile eşleşme
for i in range(len(images)):
    kp1, des1 = orb.detectAndCompute(images[i], None)
    for j in range(i+1, len(images)):
        kp2, des2 = orb.detectAndCompute(images[j], None)
        
        # Noktaları eşleştir
        matches = bf_orb.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)

# SIFT için tanımlayıcı
sift = cv2.xfeatures2d.SIFT_create()

# SIFT ile eşleşme
bf_sift = cv2.BFMatcher()

for i in range(len(images)):
    kp1, des1 = sift.detectAndCompute(images[i], None)
    for j in range(i+1, len(images)):
        kp2, des2 = sift.detectAndCompute(images[j], None)
        
        # KNN eşleşmesi
        matches = bf_sift.knnMatch(des1, des2, k=2)
        
        # Güzel eşleşmeleri seçme
        good_matches = []
        for match1, match2 in matches:
            if match1.distance < 0.75 * match2.distance:
                good_matches.append([match1])
        
        # Eşleşmeleri görselleştir
        sift_matches = cv2.drawMatchesKnn(images[i], kp1, images[j], kp2, good_matches, None, flags=2)
        imshow_img(sift_matches, f"SIFT Match {i+1} vs {j+1}")

# Sonuçları göster
plt.show()
