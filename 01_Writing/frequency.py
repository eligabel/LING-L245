#import system
import sys

#set up dictionary called letter equivalent
letEquiv = {"p":"_","r":"E","c":"T","a":"H","d":"A","b":"I","h":"S","y":"N","'":"W","l":"D","v":"O","s":"R","u":"F","k":"C",",":"B","m":"L",".":"G","n":".","g":"Y",
"x":"P","e":"K","t":"V","w":"U","i":","," ":"M","q":"Q","o":"X","f":"'"}

#define main function
def main():
	for c in sys.stdin.read():

		if c in letEquiv:
			print(letEquiv[c], end='')
		else:
			print(c, end='')
#call main function
main()

