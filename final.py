from tabulate import tabulate

isi_kuota =[[0,'happy','3gb','30hari',20000],
            [1,'sweet','5gb','30hari',50000],
            [2,'corn', '10gb','7hari', 15000],
            [3,'fine','2gb','2hari', 5000],
            [4,'cool', '10gb','30hari',50000]]

list_harian =[[0,'seharibisa','5gb','1hari',5000],
              [1,'duaharicukup','2gb','2hari',5000],
              [2,'murahmeriah', '10gb','7hari', 15000],
              [3,'harianmeriah','5gb','3hari', 15000],
              [4,'habisinaja', '10gb','2hari',20000]]  

list_bulanan =[[0,'bulananoke','25gb','30hari',50000],
               [1,'gassebulan','50gb','30hari',75000],
               [2,'murahbulan', '10gb','30hari',25000],
               [3,'2bulancukup','80gb','60hari',150000],
               [4,'happyhemat','100gb','90hari',180000]]


isi_pulsa =[[0,'5rb',5500],
            [1,'10rb',10500],
            [2,'15rb',15500],
            [3,'20rb',20500],
            [4,'25rb',25500],
            [5,'30rb',30500],
            [6,'40rb',42500],
            [7,'50rb',52500],
            [8,'50rb',52500],                  
            [9,'60rb',62500],
            [10,'70rb',72500],
            [11,'80rb',82500],
            [12,'90rb',92500],           
            [13,'100rb',103500]]  
  

def menu ():
    print(''' 
pilihan menu:
1. admin
2. customer
3. exit''')

def admin ():
    print(''' 
pilihan menu:
1. lihat data
2. tambah data
3. ubah data
4. hapus data
5. exit''')

def bacaan():
    print(''' 
pilihan menu:
1. rekomendasi
2. harian
3. bulanan
4. pulsa
5. exit''')
    
def bacaan2():
    print(''' 
pilihan menu:
1. tampilkan
2. cari berdasarkan kode
3. exit
''')
    
def keluar():
    print(''' 
pilihan menu:
1. ya
2. tidak
''')
def ubah():
    print(''' 
pilihan menu:
1. tambah data
2. exit
''')
def update():
    print(''' 
pilihan menu:
1. update
2. exit
''')

def hapus():
    print(''' 
pilihan menu:
1. hapus
2. exit
''')
    

tambah=[]
def isi_admin():
    while True:
        print('==> silahkan log in terlebih dahulu')
        id='cruzh'
        password ='czh78'
        nama=input('masukan id anda:')
        pwd=input('masukan password anda:')
        if nama==id and pwd==password:
            print()
            print('''>>>>>>>>>>>login succes<<<<<<<<<<<''')
            print('\t<<<<< <> >>>>>')
            print(f'>>selamat datang kembali {id}<<')
            break
        else:
            print('gagal')
    


def read(asli):
    bacaan2()
    print()
    baca3=int(input('masukan pilihan: '))
    if baca3==1: 
        print()
        print('============stok kuota yang tersedia============')
        print()
        for item in (asli):
            if item in (asli):
                table = tabulate(
                (asli), 
                headers=["kode", "nama", "jumlah",'berlaku','harga'], 
                tablefmt="grid")
            print(table)  
            break
        else:
            print('\t:((((data tidak di temukan)))):')  
    elif baca3==2:
        print()
        print('=========== silahkan di input ===========')
        angka2=int(input('masukan angka :'))
        if angka2 not in range(len((asli))):
            print()
            print('=-----= mohon maaf data tidak tersedia =-----=')
        else:
            baca=[]
            print()
            print('==========>data tersedia<==========')
            print()
            baca.append((asli)[angka2])
            for item in baca:
                table = tabulate(
                baca, 
                headers=["kode", "nama", "jumlah",'berlaku','harga'], 
                tablefmt="grid")
            print(table)  
            print()
    else:
        True
        

def create(asli):
    tambah=[]
    panjang=len(isi_kuota)
    ubah()
    print()
    baru1= int(input('masukan pilihan: '))
    if baru1==1:
        print()
        print('silahkan input produk baru')
        kode1 = int(input('masukan angka:'))
        if kode1 in range(len((asli))):
            print()
            print('========data sudah ada==========')
        else:
            nama = input('masukan nama: ')
            jumlah = input('masukan jumlah/gb: ')
            berlaku = input('waktu berlaku: ')
            harga = int(input('harga: '))
            tambah.append(kode1)
            tambah.append(nama)
            tambah.append(jumlah)
            tambah.append(berlaku)
            tambah.append(harga)
            print()
            print('apakah data sudah sesuai?')
            print()
            print(f'data ==>{kode1}/{nama}/{jumlah}/{berlaku}/{harga}')
            print()
            keluar()
            kode2=int(input('masukan pilihan: '))
            if kode2 == 1: 
                (asli).append(tambah)
                tambah=[]
                panjang += 1  
                table = tabulate(
                    (asli), 
                    headers=["kode", "nama", "jumlah",'berlaku','harga'], 
                    tablefmt="grid")
                print(table)  
            elif kode2==2:
                True 
    elif baru1==2:
        True
def up(asli):
    update()
    baru1= int(input('masukan pilihan: '))
    if baru1==1:
        print()
        print('\t===========input kode===========')
        baru2=int(input('masukan kode data:'))
        if baru2 not in range(len((asli))):
            print()
            print('=-----= mohon maaf data tidak tersedia =-----=')
            
        else:
            baca=[]
            print()
            print('==========>data tersedia<==========')
            print()
            def baru():
                table = tabulate(
                hasil, 
                headers=["kode", "1", "2",'3','4'], 
                tablefmt="grid")
                print(table)   
            hasil=[(asli)[baru2]]
            baru()
            print()
            print('==>apakah anda ingin lanjut update?')
            keluar()
            baru3=int(input('pilihan anda: '))
            if baru3 == 1:
                baru()
                angka2=int(input('pilih index: '))
                if angka2 in range(1,4):
                    inp=input('perubahan: ')
                    print()
                    print('apakah anda yakin: ')
                    keluar()
                    baru5=int(input('pilihan anda:'))
                    if baru5==1:
                        hasil[0][angka2]=inp
                        table = tabulate(
                            (asli), 
                            headers=["kode", "nama", "jumlah",'berlaku','harga'], 
                            tablefmt="grid")
                        print(table)   
                    else:
                       True
                else:
                    inp=int(input('harga: '))
                    print()
                    print('apakah anda yakin: ')
                    keluar()
                    baru4=int(input('pilihan anda:'))
                    if baru4==1:
                        hasil[0][angka2]=inp
                        table = tabulate(
                            (asli), 
                            headers=["kode", "nama", "jumlah",'berlaku','harga'], 
                            tablefmt="grid")
                        print(table)   
                    elif baru4==2:
                        True          
    else:
        keluar()
        kel=int(input('pilihan: '))
        if kel == 1:
            mainmenu()
        else:
            True        
                                 
def delete(asli):
    hapus()
    baru7=int(input('masukan pilihan: ')) 
    if baru7 == 1:
        print()
        print('\t===========input kode===========')
        baru2=int(input('masukan kode data:'))
        if baru2 not in range(len((asli))):
            print()
            print('=-----= mohon maaf data tidak tersedia =-----=')
            
        else:
            baca=[]
            print()
            print('==========>data tersedia<==========')
            print()
            def baru():
                table = tabulate(
                hasil, 
                headers=["kode", "nama", "jumlah",'berlaku','harga'], 
                tablefmt="grid")
                print(table)   
            hasil=[(asli)[baru2]]
            baru()
            print()
            print('==>apakah anda yakin ingin menghapus?')
            keluar()
            baru3=int(input('pilihan anda: '))
            if baru3==1:
                del (asli)[baru2]
                print()
                print('================ data berhasil di hapus ================')
                for i in range(len((asli))):
                        (asli)[i][0] = i
                i+=1
            elif baru3==2:
                True
            else:
                print('input salah')       
    else:
        keluar()
        kel=int(input('pilihan: '))
        if kel == 1:
            mainmenu()
        if kel ==2:
            True
        else:
            print('input salah')
#============================ menu read =============================#
def baca():
    while True: 
        admin()
        print()
        baca1=int(input('masukan pilihan: '))
        while baca1==1:
            bacaan()
            print()
            baca2=int(input('masukan pilihan: '))
            if baca2 == 1:#rekomendasi
                read(isi_kuota)
                
            elif baca2==2:#harian
                read(list_harian)
            elif baca2==3:#bulanan
                read(list_bulanan)
                    
            elif baca2==4:#pulsa
                read(isi_pulsa)
            elif baca2==5:
                admin()
                print()
                baca1=int(input('masukan pilihan: '))
        
#====================== menu create ========================================#                          
        while baca1==2:
            bacaan()
            baru = int(input('masukan pilihan: '))
            if baru==1:
                create(isi_kuota)
            if baru==2:
                create(list_harian)
            elif baru==3:
                create(list_bulanan)
            elif baru==4:
                create(isi_pulsa)
            elif baru==5:
                admin()
                print()
                baca1=int(input('masukan pilihan: '))
            else:
               print('input gagal')
#=================== update ======================#
        while baca1==3:
            bacaan()
            print()
            baru4=int(input('masukan angka: '))
            if baru4==1:
                up(isi_kuota)
            elif baru4==2:
                up(list_harian)
            elif baru4==3:
                up(list_bulanan)
            elif baru4==4:
                   up(isi_pulsa)
            elif baru4 == 5:
                admin()
                print()
                baca1=int(input('masukan pilihan: ')) 
#=================== hapus data =========================#
        while baca1==4:
            bacaan()
            print()
            baru6=int(input('masukan angka: '))
            if baru6==1:
                delete(isi_kuota)
            elif baru6==2:
                delete(list_harian)
            elif baru6 == 3:
                delete(list_bulanan)  
            elif baru6==4:
                delete(isi_pulsa)        
            elif baru6==5:
                admin()
                print()
                baca1=int(input('masukan pilihan: ')) 
            else:
                ('input gagal')
                                  
        while baca1==5:
                keluar()
                print()
                keluar1=int(input('pilihan anda:'))
                if keluar1 == 1:
                    mainmenu()
                else:
                    admin()
                    print()
                    baca1=int(input('masukan pilihan: '))


#===========================admin fitur=========================================

#===========================customer fitur=========================================
def mcustomer():
    print(''' 
selamat datang di bima3
1. rekomendasi
2. beli kuota
3. beli pulsa
4. keranjang
5. exit ''')


def hotsale():
    print(
'''
1. HOT SALE (kuota)
2. back''')

def submenu1():
    print(
'''
1. beli
2. tambah ke keranjang
3. exit''')

def submenu2():
    print(
'''
1. harian
2. bulanan
3. back''')

def cart():
    print(
'''
1. kuota
2. pulsa
3. back''')

def cartcart():
    print(
'''
1. check out
2. back''')
def store(asli):
    print()
    print('=============> pilihan yang tersedia <=============')
    print()
    table = tabulate(
        (asli), 
        headers=["kode", "nama", "jumlah",'berlaku','harga'], 
        tablefmt="grid")
    print(table)  
    submenu1()
    ckode3=int(input('masukan angka: '))
    if ckode3 == 1:
        print('===============> masukan kode produk <===============')
        beli=int(input('masukan kode produk: '))
        def baru():
                table = tabulate(
                beli, 
                headers=["kode", "nama", "jumlah",'berlaku','harga'], 
                tablefmt="grid")
                print(table) 
        beli=[(asli)[beli]]
        baru()
        print('==>produk terpilih, lanjut membeli?')
        keluar()
        keluar1=int(input('masukan angka: '))
        while keluar1 == 1:
            beli1=beli[0][4]
            print(f'jumlah yang harus di bayar {beli1}')
            bayar=int(input('masukan saldo(harus sesuai):'))
            if bayar==beli1:
                print()
                print('===============selamat transaksi berhasil===============')
                break
            else:
                keluar1==1               
    
    elif ckode3 == 2:
        print('===============> masukan kode produk <===============')
        beli=int(input('masukan kode produk: '))
        def baru():
                table = tabulate(
                beli, 
                headers=["kode", "nama", "jumlah",'berlaku','harga'], 
                tablefmt="grid")
                print(table) 
        beli=[(asli)[beli]]
        baru()
        print('==>produk terpilih, apakah anda yakin?')
        keluar()
        keluar1=int(input('masukan angka: '))
        if keluar1 == 1:
            print()
            print('===============berhasil===============')
            keranjang.extend(beli)        
        else:
            True
    elif ckode3 == 3:
            True
    
    else:
        print()
        print('x===============x input tidak sesuai x===============x')
        


keranjang=[]
keranjang1=[]
def customer():
    while True:
        mcustomer()
        ckode1=int(input('masukan angka: '))
        if ckode1 ==1:
            hotsale()
            ckode2=int(input('masukan angka: '))
            if ckode2==1:
                store(isi_kuota)
               
        elif ckode1==2:
            submenu2()
            ckode2=int(input('masukan angka: '))
            if ckode2==1:
                store(list_harian)
            elif ckode2==2:
                store(list_bulanan)
    
        elif ckode1==3:
           store(isi_pulsa)
        elif ckode1 == 4:
            def baru():
                    table = tabulate(
                    keranjang,
                    headers=["kode", "nama", "jumlah",'berlaku','harga'], 
                    tablefmt="grid")
                    print(table)
            def baru1():
                    table = tabulate(
                    keranjang1,
                    headers=["kode", "nama", "jumlah",'berlaku','harga'], 
                    tablefmt="grid")
                    print(table)
            cart()
            cart1=int(input('masukan angka: '))
            if cart1==1:
                baru()
                print()
                cartcart()
                cart1=int(input('masukan angka: '))
                while cart1==1:
                    total_harga=0
                    for kode,nama,jumlah,berlaku,harga in keranjang:
                        total_harga = total_harga + harga
                    print(f'total yang harus di bayarkan: {total_harga}')
                    print()
                    bayar1=int(input('masukan saldo(harus sesuai): '))
                    if bayar1==total_harga:
                        print('================transaksi berhasil================')
                        keranjang.clear()
                        break
                    else:
                        print('================ gagal ================')
                        cart1==1
            elif cart1==2:
                baru1()
                print()
                cartcart()
                cart1=int(input('masukan angka: '))
                while cart1==1:
                    total_harga=0
                    for kode,jumlah,harga in keranjang1:
                        total_harga = total_harga + harga
                    print(f'total yang harus di bayarkan: {total_harga}')
                    print()
                    bayar1=int(input('masukan saldo(harus sesuai): '))
                    if bayar1==total_harga:
                        print('================transaksi berhasil================')
                        keranjang1.clear()
                        break
                    else:
                        print('================ gagal ================')
                        cart1==1    
        elif ckode1 == 5:
            keluar()
            print()
            keluar1=int(input('pilihan anda:'))
            if keluar1==1:
                mainmenu()
            elif keluar1==2:
                True 
    
#===================================== main menu================================#
def mainmenu():
    angka=0
    while angka !=5:
        print('\n^-^ selamat datang di czhcell ^-^')
        menu()
        angka = int(input('masukan pilihan: '))
        if angka == 1:
            isi_admin()
            baca()
        elif angka == 2:
            customer()
        elif angka == 3:
            pass
     
mainmenu()