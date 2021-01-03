import csv


def insertData():

    with open('data.csv', 'a', newline='') as csv_file:
        fieldnames = ['Nama Barang', 'Jumlah Barang', 'Harga']
        write = csv.DictWriter(csv_file, fieldnames=fieldnames)

        namaBarang = input("Nama Barang   : ")
        jumlahBarang = int(input("Jumlah Barang : "))
        harga = int(input("Harga Barang  : "))

        write.writerow({'Nama Barang': namaBarang,
                        'Jumlah Barang': jumlahBarang, 'Harga': harga})
        print("\nBerhasil disimpan!")


def showData():

    with open('data.csv') as csv_file:

        reader = csv.DictReader(csv_file)
        line = list(reader)

        no = 1
        if len(line) <= 0:
            print('BELUM ADA DATA')
        elif len(line) > 0:
            print(
                f'{"NO":^3}| {"NAMA BARANG":^15}| {"JUMLAH BARANG":^15}| {"HARGA":^10}')
            print('-'*48)
            for row in line:
                print(
                    f'{no:^3}| {row["Nama Barang"]:<15}| {row["Jumlah Barang"]:<15}| {row["Harga"]:<10}')
                no += 1


def deleteData():

    datadb = []

    with open('data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        datadb = list(csv_reader)

        if len(datadb) > 0:
            showData()
            while True:
                print('\n0 > Kembali ke menu')
                noBarang = int(input("Hapus no barang > "))
                if noBarang == 0:
                    break
                elif 0 < noBarang <= len(datadb):
                    datadb.remove(datadb[noBarang-1])
                    print("\nData sudah terhapus")
                    break
                elif noBarang > len(datadb) or noBarang < 0:
                    print('No barang tidak tersedia, silahkan input kembali\n')

            with open('data.csv', 'w', newline='') as csv_file:
                fieldnames = ['Nama Barang',
                              'Jumlah Barang', 'Harga']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for newData in datadb:
                    writer.writerow(
                        {'Nama Barang': newData['Nama Barang'],
                         'Jumlah Barang': newData['Jumlah Barang'], 'Harga': newData['Harga']})

        else:
            print('BELUM ADA DATA')


def update():
    with open('data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        datadb = list(csv_reader)

        if len(datadb) > 0:
            showData()
            while True:
                print('\n0 > Kembali ke menu')
                noBarang = int(input("Update no barang > "))
                if noBarang == 0:
                    break
                elif 0 < noBarang <= len(datadb):
                    noBarang -= 1
                    datadb[noBarang]['Nama Barang'] = input('Nama Barang : ')
                    datadb[noBarang]['Jumlah Barang'] = input(
                        'Jumlah Barang : ')
                    datadb[noBarang]['Harga'] = input('Harga: ')
                    break
                elif noBarang > len(datadb) or noBarang < 0:
                    print('No barang tidak tersedia, silahkan input kembali\n')

            with open('data.csv', 'w', newline='') as csv_file:
                fieldnames = ['Nama Barang',
                              'Jumlah Barang', 'Harga']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for newData in datadb:
                    writer.writerow(
                        {'Nama Barang': newData['Nama Barang'],
                         'Jumlah Barang': newData['Jumlah Barang'], 'Harga': newData['Harga']})

        else:
            print('BELUM ADA DATA')


def show_menu():
    print("\n")
    print("----------- MENU TRANSAKSI ----------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Delete Data")
    print("[4] Update Data")
    print("[5] Exit")

    menu = input("PILIH MENU> ")
    print("\n")

    if menu == '1':
        showData()
    elif menu == '2':
        insertData()
    elif menu == '3':
        deleteData()
    elif menu == '4':
        update()
    elif menu == '5':
        exit()
    else:
        print("Pilihan menu tidak tersedia!")


while(True):
    show_menu()
