import exifread
path = input("what is the path of the file do you want to use ? ")
f = open(path, 'rb')
tags = exifread.process_file(f)
f.close()

g = open("exif.txt", mode = "w")
tags_str = str(tags) 
slash = "\\"
tags_replaced = tags_str.replace(slash,"\n")
tags_replaced2 = tags_replaced.replace(",", "\n")
g.write(str(tags_replaced2))
g.close()
print(tags_replaced)