---
title: LAPORAN CHALLENGE KELOMPOK ALGORITMA PEMROGRAMAN TEORI
---

# Kelompok 5 :

1.  **Muhammad Ali Pratama Putra (5220411416)**

2.  Jati Kurniawan (5220411448) 3.Diki Hendrik Setyawan (5220411435)

# Overview

> Kami membuat program aplikasi to-do list sehari-hari yang kami beri
> nama "Aplikasi Catat.". Pada project ini, kami menggunakan mekanisme
> program modular dan sedikit implementasi OOP (object oriented
> programming) pada kasus koneksi database. Untuk actor dari aplikasi
> ini terdapat 2 akses, yaitu admin dan user. Pada dasarnya, aplikasi
> ini bertujuan untuk memanajemen task/pekerjaan. Aplikasi ini dapat
> menerapkan implementasi CRUD (Create, Update, Update, and Delete) pada
> beberapa task yang disimpan di database server, menerapkan filter data
> berdasarkan tanggal, melakukan sorting data (disini kami memakai
> algoritma bubble sort), menampilkan menu CLI(Command Line Interface)
> dengan penerapan while loop, dan melakukan enkripsi data menggunakan
> metode assymetric encryption.
>
> Berikut adalah use case UML diagram nya:

![](vertopal_5c9352773d99417ba5b573d23439f201/media/image1.jpeg){width="5.936111111111111in"
height="3.3777777777777778in"}

> Berikut adalah beberapa flowchart sederhana dari sub program:
>
> *(implementasi materi week 2)*

![](vertopal_5c9352773d99417ba5b573d23439f201/media/image2.jpeg){width="0.8270833333333333in"
height="2.613888888888889in"}

> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image5.jpeg){width="1.3770833333333334in"
> height="3.4375in"}
> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image6.jpeg){width="0.8979166666666667in"
> height="3.435416666666667in"}
> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image7.jpeg){width="0.8458333333333333in"
> height="3.4125in"}

![](vertopal_5c9352773d99417ba5b573d23439f201/media/image8.jpeg){width="0.8576388888888888in"
height="3.283333333333333in"}

B.  # Penyusun Aplikasi

    -   **Library** *(implementasi materi week 10)*

> Kami menggunakan beberapa library, diantaranya:

1.  Library Built-in untuk menggunakan fungsi dasar bawaan python.

2.  Library Os untuk merapihkan menu CLI (Command Line Interface).

3.  Library Datetime untuk mengatur waktu.

4.  Library mysql.connector untuk menyambungkan database server.

5.  Library cryptography.fernet untuk enkripsi dan dekripsi data string.

    -   **Sub Program** *(implementasi materi week 6)*

> Aplikasi ini terdiri dari 22 sub program (10 fungsi non-parameter dan
> 12 fungsi berparameter), 1 class untuk session berisikan 4 atribut dan
> 2 method.

-   Struktur Database *(implementasi materi week 12)*

> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image10.jpeg){width="5.409027777777778in"
> height="1.7541666666666667in"}Tabel db_user
>
> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image11.jpeg){width="5.508333333333334in"
> height="1.7194444444444446in"}Tabel db_task

-   Tampilan Database pada phpMyAdmin *(implementasi materi week 12)*

> Tabel db_user
>
> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image12.jpeg){width="5.483333333333333in"
> height="1.9222222222222223in"}
>
> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image13.jpeg){width="5.733333333333333in"
> height="5.411111111111111in"}Tabel db_task

# Output (Keluaran)

1.  ## Output User

    -   Menu awal:

> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image14.png){width="3.091666666666667in"
> height="1.2284722222222222in"}
>
> User melakukan login terlebih dahulu

-   User dapat mengubah password dengan memilih no 1

> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image15.png){width="3.3361111111111112in"
> height="0.9979166666666667in"}

-   Setelah login layar akan menampilkan beberapa menu.

> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image16.png){width="3.4631944444444445in"
> height="1.975in"}

-   Jika user memilih no 2 maka tampilan akan seperti ini

> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image17.jpeg){width="5.108333333333333in"
> height="1.5354166666666667in"}
>
> User dapat menambahkan task seperti diatas.

-   Jika user memilih no 3 maka akan sepeti berikut

> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image18.png){width="4.30625in"
> height="1.675in"}
>
> User dapat memilih tampilan task seperti berikut:

-   Jika user memeilih no 1 maka:

![](vertopal_5c9352773d99417ba5b573d23439f201/media/image19.png){width="4.2034722222222225in"
height="1.7659722222222223in"}

-   Jika user memilih no 2 maka:

![](vertopal_5c9352773d99417ba5b573d23439f201/media/image20.png){width="4.104166666666667in"
height="1.7027777777777777in"}

-   Jika user memilih no 3 maka:

![](vertopal_5c9352773d99417ba5b573d23439f201/media/image21.png){width="4.572222222222222in"
height="2.0694444444444446in"}

-   User juga dapat mengedit tasknya dengan memilih no 4

![](vertopal_5c9352773d99417ba5b573d23439f201/media/image22.jpeg){width="5.3180555555555555in"
height="2.7777777777777777in"}

-   User juga dapat menghapus task dengan memilih no 5

> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image23.jpeg){width="5.534722222222222in"
> height="2.415277777777778in"}

-   Keluar dengan memilih no 0

> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image24.png){width="5.011805555555555in"
> height="0.6875in"}

2.  ## Output Admin

    -   Ini adalah tampilan menu dari admin

> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image25.png){width="3.83125in"
> height="1.6680555555555556in"}

-   Admin dapat melihat semua akun dengan memilih no 1

> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image26.png){width="5.2625in"
> height="1.5145833333333334in"}

-   Admin juga dapat membuat akun baru dengan memilih no 2

> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image27.jpeg){width="4.475in"
> height="2.4916666666666667in"}

-   Admin juga dapat mengubah password dengan memilih no 3

> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image15.png){width="3.2881944444444446in"
> height="0.9833333333333333in"}

-   Admin juga dapat menghapus akun dengan memilih no 4

> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image28.png){width="5.3875in"
> height="2.0868055555555554in"}

-   Keluar dengan memilih no 0

> ![](vertopal_5c9352773d99417ba5b573d23439f201/media/image29.png){width="5.125694444444444in"
> height="0.7541666666666667in"}
