# This method converts the format of serials
# For serial import
#
# from: 
# 2222 | 3333 | 
# 4444 | 5555 | 
#
# to:
# 2222
# 3333
# ...

def convert():
    # file in same directory
    startfile = input("[+] Enter filename: ")

    with open(startfile, "r") as file:
        content = file.read()

    inline = content.replace("\n", "")

    lines = inline.replace(" | ", "\n")

    with open("result.txt", "w") as file:
        file.write(lines)

    print("[*] File 'result.txt' successfully created!")


convert()