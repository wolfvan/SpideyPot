import json
import r2pipe

global FILE
FILE = "nuevo" 

def main():
	addr_int = []

	r2file = open_file()
	aaanal_file(r2file)
	export_int_file(r2file)
	addr_int = import_int_file()
	extract_eax(r2file, addr_int)


def open_file():
	ff = r2pipe.open(FILE)
	return ff

def aaanal_file(ff):
	ff.cmd("aaa")

def export_int_file(ff):
	intr = ff.cmd("/c int 0x80")
	listaa = []
	a = intr.split("\n")
	for i in a:
		b = i.split("	")
		for j in b:
			if "0x0" in j:
				listaa.append(j)
	f = open("interrupt.txt", "w")
	for i in intr:
		f.write(i)

def import_int_file():
	f = open("interrupt.txt", "r")
	addrmem = []
	for line in f:
		addrmem.append(line.split(" ")[0])
	return addrmem
		
def extract_eax(ff, addrss):
	f = open("eeax_file.txt", "a")
	for i in addrss:
		print "************"
		print "Analyzing "+i+" \n"
		eaax = ff.cmd("pdf @"+ i)
		f.write(eaax)

if __name__ == "__main__":
	main()
