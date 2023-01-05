#membuat dictionary untuk menyimpan nama, harga laptop, dan total tabungan
tabungan = {
	"nama"	:	["Aradea", "Safwan", "Fatima"],
	"harga"	:	[500, 300, 250],
	"total"	:	[[125,100,0,0] , [50,150,0,0] , [75,75,0,0]],
	}
#membuat fungsi terbanyak
#deklarasi fungsi
def terbanyak():
        #perulangan for
	for i in tabungan.items():
                # untuk mencari jumlah tabungan terbanyak
		a = (max(tabungan.get('total')))
	# percabangan
	# memeriksa jumlah tabungan dan nama mahasiswa
	if (a == [125,100,0,0]):
		b = "Aradea"
	elif (a == [50,150,0,0]):
		b = "Safwan"
	elif (a == [75,75,0,0]):
		b = "Fatima"
	# output
	print('Tabungan yang terbanyak adalah {} dengan jumlah {} = {} USD'.format(b,a,sum(a)))
#membuat fungsi juara
# deklarasi fungsi
def juara():
    # membuat variable untuk menampung list
    a = []
    #perulangan terhadap list a
    for i in range(len(tabungan["total"])): # i digunakan untuk menampung indeks #range dimulai dari 0
        a.append(tabungan['harga'][i] - sum(tabungan['total'][i])) # hasilnya akan dimasukkan ke dalam list di variable a
        #dengan fungsi append maka kita menambahkan list di variable a
    # panggil fungsi
    man = min(a) # untuk menentukan jumlah terkecil (jumlah terkecil sama dengan jumlah nominal tabungan yang mendekati harga laptop)

    nama  = [] # membuat variable untuk menampung list
    # perulangan terhadap list nama
    for i in range(len(tabungan["total"])) :
        #pengkondisian        
        if (man == (tabungan["harga"][i] - sum(tabungan["total"][i]))):
            nama.append(tabungan['nama'][i]) #hasilnya akan dimasukan ke dalam list di variable nama
    # output                    
    print('Tabungan paling mendekati harga laptop adalah {} '.format(nama))
# main program untuk menampilkan dicrionary dan memanggil fungsi terbanyak dan fungsi juara
def main():
        # pencetakan secara berulang
	i=0
	for key in tabungan:
		print (tabungan['nama'][i],tabungan['harga'][i],tabungan['total'][i]) # output untuk menampilkan nama, harga laptop,total tabungan.
		i+=1
	terbanyak() # panggil fungsi terbanyak
	juara() #panggil fungsi juara
main() # panggil fungsi main
 
