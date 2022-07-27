
# CONVERT PLAIN TEXT TO 'ASTERISK CODE'


# plain to binary function ==============================
def plain_to_bin(word):
    
    # convert to ascii value
    # ======================

    code = []
    for char in list(word):
        a = ord(char)
        # print(a)
        
        code.append(a)
    print()


    # ascii to plain text
    # ===================
    # print(chr(114))


    # convert to binary
    # =================

    plain_to_bin.binary = []
    for c in code:
        b = bin(c)
        b = b.replace("0b", "")

        # print(b)

        plain_to_bin.binary.append(b)  

    return plain_to_bin.binary 

# end of function =====================================

entry = input("\nenter a string of characters: ")
# entry = "https://www.youtube.com/watch?v=I2O7blSSzpI"
# entry = "youtube.com/watch?v=I2O7blSSzpI"

print(f"string length: {len(entry)}")

plain_to_bin(entry)
# print(plain_to_bin('random'))



# asterisk function ==========================================
def binToAsterisk(entry_name="title"):

    title = "Asterisk code"
    print()
    print(title)
    print(len(title) * "=", "\n")


    # ac - asterisk code
    ac = []
    map = plain_to_bin.binary
    for point in map:

        for switch in point:

            # print(switch, end=" ")

            if switch == '1':
                print("*", end="")
                ac.append("*")

            elif switch == '0':
                print(" ", end="")
                ac.append(" ")

        ac.append("\n")       
        print()

    print(len(title) * "=", "\n")

    print(ac)

    # writing to text file
    import datetime
    a = datetime.datetime.now()
    name = (a.strftime("%Y-%m-%d %H-%M-%S")) + entry_name 
    
    f = open(f"{name}.txt", "w")
    for p in ac:
        f.write(p)


# end of function ==============================

n = input("enter a name for this entry: ")
# n = "a string"
binToAsterisk(n)

# === end ===============================================


# idea - convert 'asterisk' to plain text
