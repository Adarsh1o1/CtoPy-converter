import os
filename="sample.c"
def line_counter():
    content = True
    i = 1
    with open(filename) as f:
        while content:
            content = f.readline()
            if content.endswith("}"):
                # print(i)
                pass
            i += 1
    return i-2


def rename_final_file():
    pass
    # with open("python.py") as f3:
    #     content=f3.read()
    # with open(new_name+".py","w") as f2:
    #     f2.write(content)
    # os.remove("python.py")


# new_name=input("\nRename your Python File: ")
f1 = open("python.py", "w")
f1.write("#Disclaimer: This is a machine generated code.\n")

list = ["void main()", "int main()", "return 0;",";", "{", "}","main()"]


def datatype_extractor(data):
    if data.strip().startswith("scanf"):
        if data[data.index("%")+1] == "d":
            f1.write(var_extractor()+"=int(input())")
            # print(data)
            temp = data.index(")")
            temp1 = data[4:temp+1]
            data = data.replace(temp1, "")
            print(data)
            return data
            # print(temp)
            # print(temp1)
            # print(data[data.index(";")+1])
    if data.strip().startswith("scanf"):
        if data[data.index("%")+1] == "f":
            f1.write(var_extractor()+"=float(input())")
            # print(data)
            temp = data.index(")")
            temp1 = data[4:temp+1]
            data = data.replace(temp1, "")
            print(data)
            return data
            # print(temp)
            # print(temp1)


def de_syntax(data):
    for words in list:
        data = data.replace(words, "")
        if "#" in data:
            data=""
        if "printf" in data:
            data = data.replace("printf", "print")
        if "scanf" in data:
            data = data.replace("scanf", "")
        if "int main()" in data:
            data = data.replace("int main()","")
        
    return data


def var_extractor():
    if data.strip().startswith("scanf"):
        b = data.index('&')
        d = data.index(')')
        var_name = data[b+1:d]
        return var_name
    if data.strip().startswith("int main()"):
        pass
    else:
        b = data.index('t')
        d = data.index(";")
        var_name = data[b+1:d]
        return var_name
    
#source file here
with open(filename) as f:
    a = 1
    for a in range(line_counter()):
        data = f.readline()
        if True:
            if data.strip().startswith("scanf"):
                if data[data.index("%")+1] == "d":
                    f1.write(var_extractor()+"=int(input())")
                    # print(data)
                    temp = data.index(")")
                    temp1 = data[4:temp+1]
                    data = data.replace(temp1, "")
                    print(data)
                    # print(temp)
                    # print(temp1)
                    # print(data[data.index(";")+1])
            if data.strip().startswith("scanf"):
                if data[data.index("%")+1] == "f":
                    f1.write(var_extractor()+"=float(input())")
                    # print(data)
                    temp = data.index(")")
                    temp1 = data[4:temp+1]
                    data = data.replace(temp1, "")
                    print(data)
                    # print(temp)
                    # print(temp1)
        if True:
            if data.strip().startswith("int"):
                if "=" in data:               
                    data = data.replace("int", "")
                else:
                    data = data.replace("int"+str(var_extractor()), "")
            if data.strip().startswith("float"):
                if "=" in data:               
                    data = data.replace("float", "")
                else:
                    data = data.replace("float"+str(var_extractor()), "")

            content = de_syntax(data)
            content = content.strip()
            if "%d" in content:
                content=content.replace("%d","")
            if "%f" in content:
                content=content.replace("%f","")
            if content.startswith("print"):
                if "\\n" in content:
                    content=content.replace("\\n","")
            f1.write(content+"\n")

print("VOILA! File converted successfully!!!")
f1.close()
with open("python.py") as f2:
     x=f2.read()
