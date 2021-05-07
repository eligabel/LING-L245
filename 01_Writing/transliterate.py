#import system
import sys

#set up dictionary called letter equivalent
letEquiv = {"а":"a", "б":"b", "в":"v", "г":"g", "д":"d", "е":"ye","ё":"yo", "ж":"zh", "з":"z", "и":"i", "й":"y", "к":"k", "л":"l", "м":"m", "н":"n", "о":"o", "п":"p", "р":"r", "с":"s", "т":"t", "у":"u", "ф":"f", "х":"kh", "ц":"ts", "ч":"ch", "ш":"sh", "щ":"sh", "ъ":"", "ы":"y", "ь":"", "э":"e", "ю":"yu", "я":"ya"}

#define main function
def main():
        for c in sys.stdin.read():

                if c in letEquiv:
                        print(letEquiv[c], end='')
                else:
                        print(c, end='')
#call main function
main()
