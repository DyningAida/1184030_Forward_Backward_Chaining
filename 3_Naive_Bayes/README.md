Dataset yang digunakan kali ini ialah dataset car.csv, yang didalamnya terdapat 6 atribut dan 1 label.
atribut : buyingprc, maintprc, doors, persons, lug_boot, safety
label : recommend
dataset ini digunakan untuk menghitung probabilitas suatu mobil, apakah recommend ataukah tidak untuk digunakan dengan menggunakan algoritma naive bayes,
output yang dihasilkan pada klasifikasi ini ialah berupa parameter 0(acc), 1(good), 2(unacc), 3(vgood).
algoritma naive bayes pada dataset ini diterapkan dengan 2 cara, yakni dengan menggunakan scikit-learn python pada file main.py, 
dan juga dengan perhitungan excel pada file car_naivebayes_classifier.
1. pada penerapan di excel, diambil suatu contoh studi kasus jika (buypr_low maintpr_med, doors_4, persons_more, lgboot_med, safety_med), maka masuk kategori apakah mobil tersebut?
jawab : mobil tersebut masuk ke kategori unacc dengan perhitungan seperti berikut
- tabel
![image](https://user-images.githubusercontent.com/44889168/113506483-5c74d080-956f-11eb-9bda-f5b3c704f713.png)
- perhitungan
![image](https://user-images.githubusercontent.com/44889168/113506236-c8563980-956d-11eb-9c61-68f2c1093f9c.png)

2. pada penerapan di main.py, berikut ini hasil 
- probabilitas hasil prediksi
![image](https://user-images.githubusercontent.com/44889168/113506337-76fa7a00-956e-11eb-9c03-cdd27c3d7ab9.png)
- dan berikut ini hasil output F1-scorenya
![image](https://user-images.githubusercontent.com/44889168/113506349-94c7df00-956e-11eb-8dab-32a51e720a05.png)
- output dari classification reportnya
![image](https://user-images.githubusercontent.com/44889168/113506253-e1f78100-956d-11eb-837f-158cd1014e90.png)

dari kedua penerapan tersebut, menunjukkan bahwasanya probabilitas mobil dengan kategori unacc(tidak diterima/recommend) ialah yang paling besar dibandingkan kategori yang lainnya.
