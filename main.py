open_file = open('data_kelas.txt', 'r')

print("Cari Data Mahasiswa")
print("(((Gunakan Huruf Kapital)))")

search = input("Masukkan Nama: ")
found = False
lines = []
for line in open_file:
    if search in line:
        found = True
        print(line)
    lines.append(line)

open_file.close()

if found:
    data_baru = input("Apakah mau menambahkan data baru?(y/n): ")
    if (data_baru == "y" or data_baru == "Y"):
        print("Input Data Baru")
        print("(((Gunakan Huruf Kapital)))")
        data_nama = input("Masukkan Nama Lengkap: ")
        data_NIM = input("Masukkan NIM: ")
        data_alamat = input("Masukkan Alamat: ")
        data_hobi = input("Masukkan Hobi: ")
        file = open('data_kelas.txt', 'a')
        file.write(data_nama + " " + data_NIM + " " + data_alamat + " " + data_hobi  + '\n')
        file.close()
        print("Data berhasil ditambahkan ke dalam file.")
    else:
        exit  
else:
    print("Data Tidak Ditemukan.")
