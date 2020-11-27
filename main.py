# -*- coding: utf-8 -*-
import sys
import getopt
import Get
import out
import Post
import Copy


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
                opts, args = getopt.getopt(argv, "so:pc", ["show", "ofile=", "post", "copy"])

        lyrics = Get.getlyrics(sys.argv[1], sys.argv[2])

    except getopt.GetoptError:
        print("error: missing a mandatory option.Use -h or --help for help")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-s", "--show"):
            print(lyrics)
        elif opt in ("-o", "--ofile"):
            out.out(arg, lyrics)
        elif opt in ("-p", "--post"):
            try:
                for i in range(0, 100):
                    input(i + 1)
                    Post.post("♬" + lyrics.splitlines()[i][10:].replace(" ", ""))
                    print("♬" + lyrics.splitlines()[i][10:].replace(" ", ""))
            except:
                print("输出完成")
        elif opt in ("-c", "--copy"):
            try:
                for i in range(1, 100):
                    Copy.inputtxt("🎵" + lyrics.splitlines()[i][10:].replace(" ", ""))
                    print("🎵" + lyrics.splitlines()[i][10:].replace(" ", ""))
                    input(i + 1)
            except:
                print("输出完成")


if __name__ == "__main__":
    logo()
    main(sys.argv[3:])
