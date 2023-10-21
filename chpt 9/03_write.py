f = open('anotha.txt', 'w')
data = f.write("add this in the file ye")                #tis replaces so we apend
f.close()


f = open('anotha.txt','a')
data = f.write(" am appending ie adding to the end")
f.close()
