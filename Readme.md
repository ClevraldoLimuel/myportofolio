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
