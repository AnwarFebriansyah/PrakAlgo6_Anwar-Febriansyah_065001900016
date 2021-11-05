import math
print("MENGHITUNG KECEPATAN AKHIR GLBB (diketahui jarak tempuh)")
v0 = int(input("Masukan v0 : "))
a = int(input("Masukan a : "))
s = int(input("Masukan s : "))
print("Jarak tempuh jika kecepatan awal = "+str(v0)+", percepatan = "+str(a)+" dan jarak tempuh "+str(s)+" adalah "+str(math.sqrt(pow(v0,2)+(2*a*s))))
