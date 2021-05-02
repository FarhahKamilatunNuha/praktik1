def urutasc(mylist):
    for i in range(len(mylist)-1, 0, -1):
        for j in range(i):
            if mylist[j] > mylist[j+1]:
                simpan = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = simpan
    print(mylist)

def urutdsc(mylist):
    for i in range(len(mylist)-1, 0, -1):
        for j in range(i):
            if mylist[j] < mylist[j+1]:
                simpan = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = simpan
    print(mylist)

print('Program mengurutkan data dengan metode bubble sort')

bilangan1 = int(input('Masukkan bilangan ke 1 : '))
bilangan2 = int(input('Masukkan bilangan ke 2 : '))
bilangan3 = int(input('Masukkan bilangan ke 3 : '))
bilangan4 = int(input('Masukkan bilangan ke 4 : '))
bilangan5 = int(input('Masukkan bilangan ke 5 : '))
bilangan6 = int(input('Masukkan bilangan ke 6 : '))
bilangan7 = int(input('Masukkan bilangan ke 7 : '))
bilangan8 = int(input('Masukkan bilangan ke 8 : '))
bilangan9 = int(input('Masukkan bilangan ke 9 : '))
bilangan10 = int(input('Masukkan bilangan ke 10 : '))

bilangan = [bilangan1, bilangan2, bilangan3, bilangan4, bilangan5,
         bilangan6, bilangan7, bilangan8, bilangan9, bilangan10]

print('===========================')
print('pilih metode pengurutan : ')
print('1. Sorting Ascending \n2.Sorting Deccending')
pilih = input('metode yang dipilih : ')

print('===========================')
print('data sebelum diurutkan : ')
print(bilangan)
print('data sebelum diurutkan : ')

if pilih == ('1'):
    urutasc(bilangan)
elif pilih == ('2'):
    urutdsc(bilangan)
else:
    print("Angka yang anda masukkan salah")

home = input("kembali ke menu utama (Y/N)? ")
text = print('Program mengurutkan data dengan metode bubble sort')
back = ('')
garis = ('===========================')
if home == ('Y'):
    garis
    text
    bilangan1 = int(input('Masukkan bilangan ke 1 : '))
    bilangan2 = int(input('Masukkan bilangan ke 2 : '))
    bilangan3 = int(input('Masukkan bilangan ke 3 : '))
    bilangan4 = int(input('Masukkan bilangan ke 4 : '))
    bilangan5 = int(input('Masukkan bilangan ke 5 : '))
    bilangan6 = int(input('Masukkan bilangan ke 6 : '))
    bilangan7 = int(input('Masukkan bilangan ke 7 : '))
    angka8 = int(input('Masukkan bilangan ke 8 : '))
    angka9 = int(input('Masukkan bilangan ke 9 : '))
    angka10 = int(input('Masukkan bilangan ke 10 : '))
    bilangan = [bilangan1, bilangan2, bilangan3, bilangan4, bilangan5,
            bilangan6, bilangan7, bilangan8, bilangan9, bilangan10]
    garis
    print('pilih metode pengurutan : ')
    print('1. Sorting Ascending \n2. Sorting Deccending')
    pilih = input('metode yang dipilih : ')
    print('===========================')
    print('data sebelum diurutkan : ')
    print(bilangan)
    print('data setelah diurutkan : ')
    if pilih == ('1'):
        urutasc(bilangan)
    else :
        urutdsc(bilangan)
    home = input("kembali ke menu utama (Y/N)? ")
else:
    back