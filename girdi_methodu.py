import sys

def hello(a,b,c):
	print("DEGISKENLER YAZDIRILIYOR")
	print("AD= ", a)
	print("SOYAD= ", b)
	print("SIRKET= ", c)

if __name__ == "__main__":
	a = str(sys.argv[1])
	b = str(sys.argv[2])
	c = str(sys.argv[3])
	hello(a,b,c)