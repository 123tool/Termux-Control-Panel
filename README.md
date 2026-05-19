## Termux Control Panel Web

---

`Termux.Control-Panel` adalah platform manajemen dan ekosistem kontrol perangkat Android berbasis web yang dijalankan langsung dari dalam lingkungan Termux. Berbeda dengan pengontrol remote tradisional yang menggunakan logika kode permanen (*hardcoded*)

Alat ini dirancang dengan mengutamakan aspek keamanan tinggi (*Secure Execution Layer*), menggunakan eksekusi proses berbasis list array tanpa melalui interupsi shell mentah, sehingga sepenuhnya kebal terhadap serangan *Shell/Command Injection*.

---

## Fitur :
* **Schema-Driven Dynamic Form:** Cukup ubah/tambah perintah di file konfigurasi backend (`command_schema.py`), maka tampilan form web, filter, tipe data input, dan validasi di frontend akan otomatis menyesuaikan diri tanpa perlu menyentuh kode HTML/JS.
* **Hardened Security Layer:** Validasi input menggunakan kombinasi Regex sisi klien dan server, serta pemanfaatan `subprocess` yang aman tanpa flag `shell=True`.
* **Full Termux-API Support:** Siap mengontrol fitur perangkat keras Android (Senter, Level Volume, Text-to-Speech, Sensor Getar, Status Baterai, GPS Lokasi, hingga Notifikasi Layar).

---

## 🛠️ Panduan Instalasi :
Ikuti langkah-langkah di bawah ini untuk memasang dan menjalankan panel kontrol pada aplikasi Termux Anda :

## 1. Persiapan Lingkungan Termux (Prasyarat)
Pastikan Termux Anda telah memiliki akses ke fitur internal Android dengan memasang paket **Termux:API**.

## Perbarui repositori dan instal paket utama
```
pkg update && pkg upgrade -y
pkg install python termux-api git -y
```

## ​⚠️ Catatan Penting :

***Anda juga wajib menginstal aplikasi pendukung bernama Termux:API melalui F-Droid pada perangkat Android Anda. Setelah terinstal, pastikan memberikan semua izin aplikasi yang diperlukan (seperti izin Lokasi, Kamera, SMS, dll.) agar perintah dapat dieksekusi dengan lancar.***

## Clone Repositori
​Cloning repositori ini ke dalam penyimpanan lokal Termux Anda :
```
git clone https://github.com/123tool/Termux-Control-Panel.git
cd Termux-Control-Panel
```
## Installasi Depensensi :
​Instal pustaka micro-framework Flask untuk menjalankan server backend lokal :
```
pip install flask
```
## Menjalankan :
​Langkah 1 :
- Jalankan Server Lokal
- ​Jalankan server Flask dari dalam direktori proyek Anda di Termux dengan mengetik perintah :
```
python3 app.py
```
Jika berhasil, terminal akan menampilkan log aktif yang menandakan server berjalan pada alamat lokal port 5000
```
http://127.0.0.1:5000
```

Langkah 2 :
Akses Melalui Browser Perangkat
Buka aplikasi browser pilihan Anda di Android (Chrome, Firefox, Kiwi Browser, dll).

Ketik alamat URL berikut pada kolom navigasi:
```
http://127.0.0.1:5000
```
## Langkah 3 : Eksekusi
* Pilih salah satu fungsi kontrol pada **Menu Kontrol** di bilah sisi kiri (misal: *Text-to-Speech* atau *Senter*).
* Komponen form input akan otomatis di-render di layar sebelah kanan.
* Masukkan parameter yang diinginkan, lalu klik tombol **Kirim Perintah Ke Android 🚀**.
* Pantau status eksekusi berhasil atau gagal pada kotak **Console Log** di bagian bawah secara *real-time*.

---

## ⚙️ Mengembangkan / Menambah Perintah Baru
Untuk menambahkan perintah baru, Anda tidak perlu mengedit file `index.html` atau membuat file HTML baru. Anda hanya perlu membuka file `command_schema.py` dan menambahkan skema perintah baru ke dalam dictionary `COMMAND_SCHEMAS`. 

**Contoh Struktur Skema Baru :**
```
python
"nama_id_perintah": {
    "title": "Nama Judul di UI",
    "description": "Deskripsi fungsi yang akan tampil di bawah judul.",
    "binary": "termux-nama-binary",
    "params": [
        {
            "name": "nama_variabel",
            "label": "Label Teks di Input Form",
            "type": "text", # Bisa diisi text, number, select, atau range
            "placeholder": "Petunjuk input...",
            "default": "Nilai awal bawaan",
            "validation": "^[a-zA-Z0-9]+$" # Validasi keamanan regex
        }
    ]
}
```
## Lisensi & Disclaimer

***​Proyek ini didistribusikan di bawah lisensi MIT untuk tujuan eksplorasi utilitas internal, otomatisasi perangkat pribadi, dan riset pengembangan antarmuka pengolahan data. Pengembang di bawah merek SPY-E & 123Tool tidak bertanggung jawab atas penyalahgunaan atau modifikasi ilegal di luar instruksi resmi panduan ini.***
