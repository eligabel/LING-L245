#import system
import sys

#set up dictionary called letter equivalent
letEquiv = {"A":"A","a":"a","б":"b"}

#define main function
def main():
        for c in sys.stdin.read():

                if c in letEquiv:
                        print(letEquiv[c], end='')
                else:
                        print(c, end='')
#call main function
main()
