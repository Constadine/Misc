string = "Burning in Water, Drowning in Flame"
print("capitalize: " + string.capitalize())
print("lower: " + string.lower())
print("casefold: " + string.casefold())
print("upper: " + string.upper())
print("title: " + string.title())
print("swapcase: " + string.swapcase())

print("alnum     : 123abc  : " + str("123abc".isalnum()))
print("alnum     : 123abc# : " + str("123abc#".isalnum()))
print("alpha     : abcDδΔ  : " + str("abcDδΔ".isalpha()))
print("alpha     : δαες12  : " + str("δαες12".isalpha()))
print("digit     : 123456  : " + str("123456".isdigit()))
print("digit     : 123a34  : " + str("123a34".isdigit()))
print("space     :         : " + str("    ".isspace()))
print("printable : aA12 #  : " + str("aA12 #".isprintable()))
print("printable : \\na    : " + str("\na   ".isprintable()))
print("identifier: is_var  : " + str("is_var".isidentifier()))
print("identifier: 12ar    : " + str("12ar".isidentifier()))
print("lower     : abca34  : " + str("abca34".islower()))
print("upper     : ABFa34  : " + str("ABFa34".isupper()))
print("title     : Tik Tok : " + str("Tik Tok".istitle()))


string = "Some people never go crazy. What truly horrible lives they must lead."
print("startswith: " + str(string.startswith("Some")))
print("startswith with bounds: " + str(string.startswith("people", 5)))
print("startswith with bounds: " + str(string.startswith("people", 5, 8)))
print("endswith: " + str(string.endswith("people", 0, 11)))
print("find: " + str(string.find("crazy")))
print("position(s) of \"o\": ", end="")
pos = -1
lpos = string.rfind("o")
while pos != lpos:
    pos = string.find("o", pos+1)  # all positions of a word in text
    print(pos, end=" ")

print("\nreplace: " + string.replace("o", "0", 3))

string = "   Factotum "
print("lstrip : |" + string.lstrip() + "|")
print("rstrip : |" + string.rstrip() + "|")
print("strip  : |" + string.strip() + "|")
print("ljust  : |" + string.strip().ljust(30) + "|")
print("rjust  : |" + string.strip().rjust(30) + "|")
print("center : |" + string.strip().center(30, "-") + "|")

string = "abcd"
print("zfill(2) : " + string.zfill(2))
print("zfill(10): " + string.zfill(10))


string = "You have to die a few times before you can really live."
print("split(by blanks): " + str(string.split()))
print("split(by a's): " + str(string.split("a")))
print("split(by blanks): " + str(string.split(" ", 2)))
print("rsplit(by blanks): " + str(string.rsplit(" ", 2)))
print("partition(by 'few'): " + str(string.partition("few")))
print("rpartition(by 'r'): " + str(string.rpartition("r")))

mult_line = """Some lose all mind and become soul, insane.
some lose all soul and become mind, intellectual.
some lose both and become accepted"""
print("splitlines: " + str(mult_line.splitlines()))
