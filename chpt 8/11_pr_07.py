# stri = "    before and after"
# print(stri)
# print(stri.strip())

def remov_strip(string, word):
    newstr = string.replace(word, " ")
    return print(newstr.strip())

harry = "   ye no why    "
n = remov_strip(harry, "yes")


