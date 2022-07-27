
# CONVERT 'asterisk' code to bin, then to plain text

# DONE !!!
# 2 functions 

#1 start of function ===========================================
def asteriskToBin(reading=str):

    asteriskToBin.rd = reading
    f = open(f'{asteriskToBin.rd}.txt', 'r')

    g = f.readlines()

    # from https://stackoverflow.com/questions/8282553/removing-character-in-list-of-strings
    # print([s.strip('\n') for s in g])

    h = []
    for line in g:
        l = line.strip("\n")
        # print(l)
        # print(line)
        h.append(l)

    # print()


    bin = []
    for i in h:
        for point in i:
            if point == "*":
                # print(1, end="")
                bin.append(1)

            elif point == " ":
                # print(0, end="")
                bin.append(0)

        bin.append("\n")
        # print()


    # writing to text file
    asteriskToBin.r = f"{reading} (result).txt"
    result = open(asteriskToBin.r, "w")

    for j in bin:
        result.write(str(j))

    print("\n<<< function process complete >>>")

# end of function ===============================

print()
print("Enter the text file that you want to read ")
print("Note: ")
print(" - the text file has to be in the same directory as this program")
print(" - don't include the file extension when entering the file name \n")

r = input(" > ")

# r = ""
asteriskToBin(r)




#2 start of function ===========================================
# bin to plain 
def binplain():

    file = open(asteriskToBin.r, "r")

    # writing to new file
    decode = f"{asteriskToBin.rd} (decode).txt"
    new = open(decode, "w")
    
    
    for line in file.readlines():
        ln = line.replace("\n", "")
        
        # from https://www.codegrepper.com/code-examples/python/binary+to+text+python
        # "".join([chr(int(binary, 2)) for binary in a_binary_string.split(" ")])
        le = chr(int(ln, 2))

        # print(le)
        print(le, end="")

        new.write(le)

# end of function ==========================
binplain()
