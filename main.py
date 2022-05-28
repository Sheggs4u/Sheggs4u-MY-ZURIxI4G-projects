def readfile(filename):
    openfile = open("./story.txt","r")
    read_file = openfile.read()
    print(read_file)
    print("openfile")

    return read_file


def countwords():
    text = readfile("./story.txt")
    split_text = text.split()
    #print(split_text)
    count ={}
    for i in split_text:
        if i in count:
            count[i] += 1
        else:
            count[i] =1
    return count

print(countwords())