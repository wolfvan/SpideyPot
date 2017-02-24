import r2pipe
import os

global BINARIES
global BIN_FUN 


BINARIES = []
BIN_FUN = {}



def open_bin(b):
	r = r2pipe.open(b)
	return r

def anal_bin(b):
	anal = b.cmd("aa")
	
	
def extract_fun(b)
	BIN_FUN[b] = b.cmd("f")


def extract_bin():
	os.listdir("/home/mirais/bin/")
	

def compare_name_functions():
	for i in BIN_FUN.keys():
		for j in BIN_FUN.values()
			list .append(j)
		


def main()
	BINARIES = extract_bin()
	for b in BINARIES:
		openbin = open_bin(b)
		analbin = anal_bin(openbin)
		extract_fun(analbin)
	compare_name_functions()


if __name__ == "__main__":
	main()
