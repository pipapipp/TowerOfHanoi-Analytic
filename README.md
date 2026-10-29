# Tower of Hanoi - Multi-Peg Solver

Program penyelesaian masalah Tower of Hanoi yang mendukung konfigurasi multi-tiang (*multi-peg*), tiang awal (*initial peg*), serta tiang tujuan (*goal peg*) secara dinamis menggunakan algoritma pencarian **DFS**, **DLS**, dan **IDS**.

## Cara Menjalankan Program

1. Pastikan Python 3 sudah terpasang.
2. Buat atau letakkan file konfigurasi input berformat `.txt` di folder `input/`.
3. Jalankan perintah berikut dari direktori utama proyek:

```bash
python main.py
```

Program membaca **semua file `.txt`** di folder `input/`. Setiap file diproses secara terpisah.

## Format file input

```text
disks = 3
methods = dfs,dls,ids
pegs = 3
dls_limit = 7
initial_peg = 1
goal_peg = 3
```

- `disks`: jumlah disk, minimal 1.
- `methods`: satu atau beberapa metode, dipisahkan koma. Pilihan: `dfs`, `dls`, `ids`.
- `pegs`: jumlah peg (tiang), minimal 3.
- `dls_limit`: batas kedalaman untuk DLS. IDS menentukan batasnya sendiri.
- `initial_peg`: peg awal, default 1.
- `goal_peg`: peg tujuan.


Baris komentar diawali `#`. Urutan pengaturan bebas.

## File output
Hasil ditulis ke folder `output/`, dengan pola:

`<nama_input>_<metode>_output.txt`

Contoh: `kasus1_dfs_output.txt`. Jika suatu metode dipilih pada beberapa input, masing-masing hasil tetap terpisah berdasarkan nama file input.

## Catatan
- DFS menggunakan pencarian graf dengan visited set.
- DLS membatasi kedalaman pencarian sesuai `dls_limit`.
- IDS mengulang DLS dengan batas kedalaman yang meningkat.
- Untuk input yang sama, nama file output yang sama akan ditimpa saat program dijalankan kembali.
