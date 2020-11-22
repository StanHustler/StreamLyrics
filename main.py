# -*- coding: utf-8 -*-
import sys
import getopt
import Get
import out


def logo():
    _logo = r'''    
    ______                     __            _       
   / __/ /________ ___ ___ _  / /  __ ______(_)______
  _\ \/ __/ __/ -_) _ `/  ' \/ /__/ // / __/ / __(_-<
 /___/\__/_/  \__/\_,_/_/_/_/____/\_, /_/ /_/\__/___/
                                 /___/               
    '''
    print(_logo)


def usage():
    print("waiting")  # ssss


def clierror():
    print("Usage: python3 main.py [name] [language] [options]\n"
          "Use -h or --help for help")


def main(argv):
    try:
        if len(sys.argv) < 3:
            if sys.argv[1] == "-h" or sys.argv[1] == "--help":
                usage()
                sys.exit()
            else:
                clierror()
                sys.exit(2)
        else:
            if sys.argv[2] != "1" and sys.argv[2] != "2":  # check the input
                clierror()
                sys.exit(2)
            else:
                opts, args = getopt.getopt(argv, "po:", ["print", "ofile="])

        lyrics = Get.getlyrics(sys.argv[1], sys.argv[2])

    except getopt.GetoptError:
        print("error: missing a mandatory option.Use -h or --help for help")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-p", "--print"):
            print(lyrics)
        elif opt in ("-o", "--ofile"):
            out.out(arg, lyrics)


if __name__ == "__main__":
    # logo()
    main(sys.argv[3:])
