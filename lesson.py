from optparse import OptionParser


def main():
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage)
    parser.add_option("-f", "--file", action="store", type="string",
                      dest="filename", help="File name")
    options, args = parser.parse_args()
    print(options.filename)
    print(args)


def sample_func():
    print("git merge2")
    
    pass

def feature_func():
    pass


if __name__ == "__main__":
    main()
