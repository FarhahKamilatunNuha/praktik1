while True :
    name_siswa = input("Masukan Nama Anda : ")
    nilai_harian = int(input("Masukan Nilai Harian : "))
    nilai_uts = int(input("Masukkan Nilai UTS : "))
    nilai_uas = int(input("Masukkan Nilai UAS : "))
    nilai_akhir = int(nilai_harian+nilai_uts+nilai_uas)/3

    if nilai_akhir >= 85:
        predikat_nilai = 'AMAT BAIK'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)

    elif nilai_akhir >= 75:
        predikat_nilai = 'BAIK'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)
    
    elif nilai_akhir >= 65:
        predikat_nilai = 'CUKUP'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai) 

    elif nilai_akhir >= 55:
        predikat_nilai = 'KURANG'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)

    else :
        predikat_nilai = 'KURANG SEKALI'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)