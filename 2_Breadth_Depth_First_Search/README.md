Pembahasan
---
Contohnya diketahui 6 simpul dengan graphic seperti berikut :
```
graph = {
    'A':set(['B','C']),
    'B':set(['A','D','E']),
    'C':set(['A','F']),
    'D':set(['B']),
    'E':set(['B']),
    'F':set(['C'])
}
```

Untuk mencapai tujuan yaitu dari titik awal A menuju ke F, dapat menggunakan 2 metode pencarian, yaitu bfs dan dfs dengan penjelasan seperti berikut :

![DFS_BFS](https://github.com/DyningAida/Sistem_Pakar/blob/master/2_Breadth_Depth_First_Search/bfsdfs.png)

Pada skema bfs, urutan yang didapatkan ialah ABCF. Pada bfs, metode yang digunakan ialah seperti antrian. Sehingga bersifat First In, First Out, yang berarti mendahulukan berdasar siapa yang terdahulu pada antrian grafik. Proses pencarian dilakukan secara menyeluruh dan berurutan. Sehingga pada metode ini, jalur yang dikunjungi juga lebih panjang, yakni melalui A - B - C - D- E - F

Sedangkan Pada skema dfs, jalan dari titik awal ke tujuan yang didapat ialah ACF. Dengan dfs, digunakan metode stack/tumpukan, dimana bersifat Last In First Out yang berarti perhitungan atau pengecekan dilakukan melalui stack yang paling akhir(paling atas), sehingga pencarian bisa lebih meminimalkan jalur dan juga memory. Urutan kunjungan pada metode dfs ialah dari A - B - C - D - E - F. 

Pada kasus skema di atas, urutan kunjungan yang dilakukan ialah sama. Namun, biasanya hal yang paling sering terjadi ialah adanya perbedaan urutan kunjungan antara kedua metode pencarian tersebut karena berdasarkan pada perbedaan yang telah dijelaskan sebelumnya, yakni mengenai pengambilan urutan berdasarkan antrian dan juga pengambilan urutan berdasarkan stack/tumpukan.

