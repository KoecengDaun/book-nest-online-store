# BookNest Online Store

## Tautan Aplikasi PWS yang Sudah Dideploy
Aplikasi PWS dapat diakses melalui tautan berikut:
[BookNest Online Store Deployment](https://laurentius-farel-booknestonlinestore2.pbp.cs.ui.ac.id)

---

## Jawaban Pertanyaan

### 1. Implementasi Checklist Secara Step-by-Step

Untuk mengimplementasikan checklist di atas, saya melakukan langkah-langkah berikut:

1. **Mempersiapkan Lingkungan Pengembangan**:
   - Menginstal **Python** dan **Django**.
   - Mengatur **virtual environment** untuk memastikan dependencies proyek terisolasi.
   
2. **Membuat Project Django**:
   - Menjalankan `django-admin startproject BookNest` untuk membuat project baru.
   
3. **Membuat Aplikasi Django**:
   - Menambahkan aplikasi utama menggunakan perintah `python manage.py startapp store`.

4. **Membangun Model**:
   - Membuat model produk buku di `models.py` untuk menyimpan data buku seperti judul, pengarang, dan harga.
   
5. **Mengatur Views dan URL**:
   - Menghubungkan model dengan views di `views.py` untuk menampilkan data buku ke halaman HTML.
   - Mengkonfigurasi `urls.py` agar request dari pengguna diarahkan ke views yang sesuai.

6. **Mendeploy Aplikasi**:
   - Menggunakan **Heroku** atau **Vercel** untuk mendeploy aplikasi ke server live.
   - Menghubungkan dengan **PostgreSQL** sebagai database di deployment environment.

### 2. Bagan Request-Response Django

![Bagan Request-Response](https://imgur.com/a/NiZgMHC)

Bagan di atas menunjukkan alur request dan response antara client dan server pada aplikasi Django:

1. **Client** mengirimkan request ke server melalui URL tertentu.
2. **urls.py** bertanggung jawab mengarahkan request ke view yang sesuai berdasarkan pola URL.
3. **views.py** memproses request, mengambil data dari **models.py** (basis data) jika diperlukan.
4. Setelah data diproses, **views.py** akan merender template HTML dan mengirim response kembali ke client.

Kaitan antara komponen:
- **urls.py**: Mengatur routing request.
- **views.py**: Memproses logika aplikasi dan berinteraksi dengan model.
- **models.py**: Menyimpan dan mengambil data dari database.
- **HTML**: Template untuk menampilkan data di browser.

### 3. Fungsi Git dalam Pengembangan Perangkat Lunak

**Git** adalah sistem kontrol versi yang sangat penting dalam pengembangan perangkat lunak karena beberapa alasan:

- **Versi Kontrol**: Git melacak perubahan pada kode, memungkinkan pengembang untuk kembali ke versi sebelumnya jika ada kesalahan.
- **Kolaborasi**: Git memungkinkan beberapa pengembang untuk bekerja bersama dalam satu proyek tanpa konflik.
- **Manajemen Branch**: Pengembang dapat membuat branch untuk fitur baru, menguji, dan menggabungkannya ke branch utama setelah diuji.

### 4. Mengapa Framework Django Digunakan dalam Pembelajaran Pengembangan Perangkat Lunak?

Django sering digunakan sebagai framework awal karena:

- **Batteries-included**: Django menyediakan banyak fitur bawaan seperti ORM, form, autentikasi, dan admin panel, sehingga memudahkan pengembangan aplikasi web.
- **Arsitektur yang Jelas**: Django mengikuti pola **Model-View-Template (MVT)** yang memisahkan logika bisnis dari tampilan dan data.
- **Komunitas yang Besar**: Django memiliki dokumentasi yang baik dan komunitas yang aktif, membantu dalam pembelajaran dan pengembangan lebih lanjut.

### 5. Mengapa Model pada Django Disebut sebagai ORM?

Django menggunakan ORM (**Object-Relational Mapping**) untuk memetakan model ke database. ORM memungkinkan pengembang untuk:

- Menulis logika database menggunakan **Python** alih-alih menggunakan **SQL** langsung.
- Mengabstraksikan detail dari berbagai database, sehingga mempermudah pengembang dalam bekerja dengan database tanpa harus menulis query SQL yang berbeda untuk setiap database.
- ORM otomatis menangani banyak tugas CRUD (Create, Read, Update, Delete), sehingga lebih efisien dan mengurangi kemungkinan error.

---
