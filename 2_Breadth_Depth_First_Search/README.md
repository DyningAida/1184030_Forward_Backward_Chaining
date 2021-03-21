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

Pada skema bfs, urutan yang didapatkan ialah sebagai berikut ABCF. Hal itu karena, pada bfs, metode yang digunakan ialah seperti antrian. Sehingga bersifat Fist In, First Out, yang berarti mendahulukan berdasar siapa yang terdahulu pada antrian, pada skema ini berarti pada grafik.

Pada skema dfs, urutan yang didapat ialah sebagai berikut ACF. Hal ini karena, dengan metode dfs, ialah menggunakan metode stack/tumpukan, dimana bersifat Last In First Out yang berarti perhitungan atau pengecekan dilakukan melalui stack yang paling akhir dimasukkan ke dalamnya.

