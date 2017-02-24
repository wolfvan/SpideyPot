import r2pipe
import os

global BINARIES
global BIN_FUN 
BIN_FUN = {}

def open_bin(b):
	r = r2pipe.open(b)
	return r

def anal_bin(b):
	anal = b.cmd("aa")


def extract_bin():
	os.listdir("/home/mirais/bin/")


def main()
	BINARIES = extract_bin()
	for b in BINARIES:
		openbin = open_bin(b)
		analbin = anal_bin(openbin)


if __name__ == "__main__":
	main()
