import cv2
import os

# Klasör yolu
folder_path = "klasör yolunu giriniz:"

# Klasördeki tüm dosyaları al
files = os.listdir(folder_path)

# Sadece .jpg dosyalarını listele
img_path_list = [f for f in files if f.endswith(".jpg")]

# Yüz tespitini gerçekleştirecek classifier
detector = cv2.CascadeClassifier("klasör yolu/haarcascade_frontalcatface.xml")

# Her bir resim üzerinde işlem yap
for img_name in img_path_list:
    # Görüntü yolu
    image_path = os.path.join(folder_path, img_name)
    
    # Görüntüyü oku
    image = cv2.imread(image_path)
    
    if image is None:
        continue  # Eğer resim okunamazsa geç

    # Görüntüyü gri tonlamaya çevir
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Yüz tespiti yap
    rects = detector.detectMultiScale(gray, scaleFactor=1.045, minNeighbors=2)

    # Yüzleri işaretle
    for (i, (x, y, w, h)) in enumerate(rects):
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.putText(image, "Kedi {}".format(i + 1), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 255), 2)

    # İşlenmiş resmi göster
    cv2.imshow(img_name, image)

    # Kullanıcı 'q' tuşuna basana kadar bekle
    if cv2.waitKey(0) & 0xFF == ord("q"):
        cv2.destroyAllWindows()

cv2.destroyAllWindows()
