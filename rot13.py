#!/usr/bin/python


def main():
	with open ("employer.txt", "r") as myfile:
		data=myfile.read()
		os = data.encode( "rot13" )
		print( os )


#stub to launch main
if __name__ == '__main__':
	    main()
