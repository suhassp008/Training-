def write_into_file():
    fp = open("Domenitization.txt", "w")
    data = "The quick brown fox jumped over the lazy dog"
    fp.write(data)
    fp.close()
    print("Inserted Successfully into File")

def read_from_file():
    fp = open("Domenitization.txt", "r")
    st = fp.read()
    print(st)
    fp.close()

while (True):
    ch = int(input("Enter the choice\n 1.Write\n 2.Read\n 3.Exit"))
    if ch == 1:
        write_into_file()
    elif ch == 2:
        read_from_file()
    else:
        exit(0)