import exifread
path = input("what is the path of the file do you want to use ? ")
with open(path, 'rb') as f:
    tags = exifread.process_file(f, strict=True)
f.close()

g = open("exif.txt", mode = "w")
tags_str = str(tags) 
slash = "\\"
tags_str = tags_str.replace(slash,"\n")
tags_str = tags_str.replace(",", "\n")
g.write(str(tags_str))
g.close()
print(tags_str)