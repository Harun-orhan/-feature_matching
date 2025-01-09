Chocolate Image Matching using ORB and SIFT
Bu proje, çikolata resimlerini tanıyıp, ORB ve SIFT özellik çıkarıcıları kullanarak resimler arasındaki eşleşmeleri bulur ve görselleştirir. Kullanıcı, farklı çikolata türlerini içeren resimlerin eşleşmelerini karşılaştırabilir.

Proje Açıklaması
Bu projede, çikolata resimlerini kullanarak görsel eşleşme algoritmaları olan ORB (Oriented FAST and Rotated BRIEF) ve SIFT (Scale-Invariant Feature Transform) kullanılmıştır. Proje, verilen çikolata resimleri arasında ortak özellikleri bulmaya çalışarak, bu resimler arasındaki benzerlikleri analiz eder.

Gereksinimler
Projeyi çalıştırmak için aşağıdaki bağımlılıkların kurulu olması gerekir:

Python 3.x
OpenCV (opencv-python, opencv-contrib-python)
Matplotlib
Bağımlılıkların Yüklenmesi
Projenin bağımlılıklarını yüklemek için aşağıdaki komutu kullanabilirsiniz:

code parçası --->{pip install opencv-python opencv-contrib-python matplotlib}

Projeyi Çalıştırma
Çikolata Resimlerini Ekleyin:

image_paths listesine yeni çikolata resimlerinin dosya yollarını ekleyin.
Kod, bu resimler arasındaki eşleşmeleri bulacaktır.
Kodun Çalıştırılması:

Python dosyasını çalıştırarak eşleşmeleri görselleştirebilirsiniz:

python chocolate_matching.py

Görselleştirme:
Kod çalıştıktan sonra, eşleşmelerin görsel sonuçlarını matplotlib kullanarak görselleştirecektir.

Kod Açıklaması
1. Resim Yükleme ve Görselleştirme
Proje, belirtilen dosya yollarındaki resimleri yükler ve gri tonlamada gösterir.

2. ORB ile Eşleşme
ORB (Oriented FAST and Rotated BRIEF) algoritması, resimler arasındaki benzer noktaları tespit etmek için kullanılır.
BFMatcher (Brute-Force Matcher) kullanarak bu noktalar eşleştirilir.
3. SIFT ile Eşleşme
SIFT (Scale-Invariant Feature Transform) algoritması, daha güçlü eşleşmeler elde etmek için kullanılır.
KNN eşleşmesi yapılır ve iyi eşleşmeler filtrelenir (0.75 mesafe kriteriyle).
4. Eşleşmelerin Görselleştirilmesi
cv2.drawMatches ve cv2.drawMatchesKnn fonksiyonları kullanılarak eşleşen noktalar çizilir.
matplotlib ile bu eşleşmeler görsel olarak gösterilir.
Katkıda Bulunma
Bu projeye katkıda bulunmak isterseniz, pull request gönderebilir ya da bir issue açabilirsiniz. Katkılarınız için teşekkür ederiz!

Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakabilirsiniz.
