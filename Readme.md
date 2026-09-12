Nama : Clevraldo Limuel


NPM  : 2506656583


Kelas: PBP B


## WEEK 1

### Progress:

- Menyelesaikan setup awal (django dan PWS (dengan ))

- Membuat halaman profile dan interest dengan HTML5 dan CSS3 dasar

- Memisahkan isi style.css dengan file css lain yang digunakan untuk masing-masing page, supaya perubahan selanjutnya dapat dilakukan secara mudah dan reusable

- Membuat layout kedua page responsive terhadap perubahan ukuran viewport


### Challenges:

Salah satu tantangan utama adalah membuat layout tetap terlihat baik ketika ukuran viewport berubah. Pada awalnya, beberapa elemen menggunakan ukuran dan posisi yang terlalu bergantung pada desktop sehingga layout menjadi kurang baik pada layar yang lebih kecil.
Pemahaman mendalam mengenai behavior layout grid maupun flexbox juga merupakan hal yang perlu didalami sehingga penggunaannya dapat memeberikan hasil yang diinginkan. Pemilihan warna dan font juga menjadi salah satu tantangan yang saya hadapi karena jika kurang tepat dapat menyebabkan hasil yang kurang enak dibaca bagi user.


### AI Disclosure:

Saya menggunakan AI sebagai alat bantu selama proses pengembangan portfolio website, terutama untuk memahami konsep HTML/CSS, mencari alternatif solusi ketika mengalami masalah layout, dan memeriksa kemungkinan penyebab error. Contoh:

Q:
Apakah mungkin membuat layout CSS Grid yang awalnya tersusun secara horizontal menjadi vertikal dengan display grid ketika dibuka pada layar mobile?

A:
Kamu bisa menggunakan media query. Misalnya:

.interest-content {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
}

@media (max-width: 600px) {
    .interest-content {
        grid-template-columns: 1fr;
    }
}

Dengan begitu, pada layar dengan lebar maksimal 600px, ketiga kolom akan ditumpuk menjadi satu kolom.

Q: Berarti jumlah columnnya dikurangi menjadi 1 kolom saja? Kenapa tidak membuat 3 baris lalu di-assign satu persatu?
A: Bisa saja menggunakan tiga baris dan mengatur setiap elemen secara eksplisit, tetapi sebenarnya tidak diperlukan jika tujuan kita hanya menumpuk ketiga elemen secara vertikal.

Dengan mengubah grid-template-columns menjadi 1fr, CSS Grid secara otomatis akan menempatkan setiap item pada baris berikutnya ketika hanya tersedia satu kolom. Jadi ketiga elemen tetap tersusun menjadi tiga baris tanpa perlu menentukan posisi masing-masing secara manual.


## TUGAS 1
1. Ya, elemen semantik html5 dapat memberikan clarity dan meningkatkan readibility code, meskipun hasilnya tetap sama jika menggunakan div. Masing-masing elemen dipakai sesuai dengan kebutuhannya, misalnya section untuk mengelompokkan elemen denan topik atau bagian yang serupa, article untuk bagian yang dapat berdiri sendiri, dan aside untuk elemen tambahan yang berhubungan dengan bagian utama.
   
2. Mengenai tata letak, saya menghadapi tantangan dalam mengatur ukuran dan alignment elemen photo pada halaman awal, sehingga elemen photo tetap bersinggungan dengan header dan footer sesuai dengan design yang saya inginkan. Sistem grid dan flexbox juga merupakan konsep yang bagi saya dibutuhkan pemahaman mendalam supaya dapat digunakan dengan optimal.
   
3. Reaktivitas. Html memberikan struktur dan konten dan CSS memberikan style dan menyokong layout, tetapi keduanya tidak bisa memberikan respon kompleks terhadap input user. Mungkin pada iterasi proyek selanjutnya saya ingin memberikan fungsi tampilan informasi lebih lanjut yang disembunyikan secara default lalu ditampilkan dengan input klik tanpa meninggalkan halaman atau berpindah section. Saya juga ingin membuat counter berapa banyak user yang telah mengakses web ini.



## WEEK 2

### Progress:

- Menambahkan Education Page dan Database yang berkaitan dengan MVT

- Menggunakan url string builder untuk Interest pada NavBar

- Menambahkan TestCases untuk menguji fungsionalitas aplikasi

- Menerapkan MVT untuk semua halaman


### Challenges:

Tantangan yang saya hadapi pada minggu kedua ini antara lain menentukan sistem basis data yang diperlukan untuk halaman seperti Interest dan Education, memahami konfigurasi routing URL, dan menentukan layout data yang akan ditampilkan di halaman Education


### AI Disclosure:

Saya menggunakan AI (chatGPT dan Claude) sebagai alat bantu selama proses pengembangan portfolio website, terutama untuk memahami konsep HTML/CSS, mencari alternatif solusi ketika mengalami masalah layout, dan memeriksa kemungkinan penyebab error. Contoh:

Q:
Bagaimana caranya supaya ketika viewport di-squeeze secara vertikal, isi elemen tidak overlap?

A:
Overlap biasanya terjadi karena adanya elemen dengan posisi absolute maupun fixed, atau margin elemen tersebut bernilai negatif. Overlap juga bisa terjadi jika terdapat limitasi terhadap ukuran elemen seperti max-height.

Q: 
Tetapi tidak ada elemen dengan position absolute maupun fixed yang overlap. Oh ini karena adanya elemen dengan max-width yang menggunakan satuan vh, sehingga pada viewport pendek, max-height nya juga ikut pendek
A: 
Yep, benar sekali, dan ini memang salah satu jebakan vh: viewport pendek tidak selalu berarti viewport sempit, tapi vh memperlakukan keduanya seolah-olah ukuran yang sama-sama menentukan lebar.


## TUGAS 2
1. Alur yang terjadi yaitu: Request → urls → View → Model → View → Template → Response. User mengirim request ke server, yang kemudian memeriksa urls.py project. urls.py meng-reroute request ke urls.py pada app sesuai dengan list pada urlpatterns. urls.py pada app menentukan fungsi pada views mana yang akan dijalankan. Views memproses request, mengambil data pada models, dan mereturn render dari template yang dilengkapi dengan context (yaitu data-data) sebagai response yang akan ditampilkan di User.
   
2. Data yang disimpan di models adalah data yang dapat berubah, baik diedit, dihapus, maupun ditambah. Untuk halaman yang datanya dapat berubah-ubah seperti experience, education, dan interest, penggunaan models dapat memudahkan perubahan data, sedangkan halaman yang statis seperti main yang hanya berisi data sederhana tidak membutuhkan model (overkill). Penggunaan model memungkinkan pemeliharaan dan pengembangan aplikasi yang lebih stabil dan reaktif terhadap perubahan data dan jumlah data.
   
3. makemigrations membuat file yang berisi informasi rencana perubahan model database, sedangkan migrate menerapkan perubahan tersebut pada database. Perubahan yang memerlukan kedua perintah tersebut adalah perubahan yang melibatkan perubahan bentuk, jumlah atribut, karakteristik atribut, perubahan entitas, dan sebagainya, seperti menambah entitas baru (Education dan Interest). Penambahan data dan perubahan pada instance suatu entitas tidak memerlukan kedua perintah tersebut. Simpelnya, lakukan makemigrations dan migrate jika mengubah template data, tidak perlu jika mengubah instance data.
