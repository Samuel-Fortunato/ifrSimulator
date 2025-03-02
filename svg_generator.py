import sys

if len(sys.argv) != 2:
    sys.exit("Wrong number of arguments")

else:
    filename = sys.argv[1]
    exec(open(filename).read())
