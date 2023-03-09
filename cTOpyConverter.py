import os
filename = input("Enter File name: ")+".c"

def line_counter():
    content = True
    i = 1
    with open(filename) as f:
        while content:
            content = f.readline()
            if content.endswith("}"):
                pass
            i += 1
    return i-2

def rename_final_file():
    with open("python.py") as y1:
        content = y1.read()
    with open(new_name+".py", "w") as y2:
        y2.write(content)
    os.remove("python.py")

f1 = open("py.py", "w")
f1.write("#Disclaimer: This is a machine generated code.")

list = ["void main()", "int main()", "return 0;", ";", "}", "main()"]

def datatype_extractor(data):
    pass
    if data.strip().startswith("scanf"):
        if data[data.index("%")+1] == "d":
            f1.write(var_extractor()+"=int(input())")
            temp = data.index(")")
            temp1 = data[4:temp+1]
            data = data.replace(temp1[0:-1], "")
            print(data)
            return data
        
    if data.strip().startswith("scanf"):
        if data[data.index("%")+1] == "f":
            f1.write(var_extractor()+"=float(input())")
            temp = data.index(")")
            temp1 = data[4:temp+1]
            data = data.replace(temp1, "")
            print(data)
            return data

def de_syntax(data):
    for words in list:
        data = data.replace(words, "")
        if "#" in data:
            data = ""
        if "printf" in data:
            data = data.replace("printf", "print")
        if "scanf" in data:
            data = data.replace("scanf", "")
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

# source file here
with open(filename) as f:
    a = 1
    for a in range(line_counter()):
        data = f.readline()
        if True:
            if data.strip().startswith("scanf"):
                p = data.index("scanf")
                if data[data.index("%")+1] == "d":
                    f1.write(var_extractor()+"=int(input())")
                    temp = data.index(")")
                    temp1 = data[p:temp+1]
                    data = data.replace(temp1, "")
            if data.strip().startswith("scanf"):
                if data[data.index("%")+1] == "f":
                    f1.write(var_extractor()+"=float(input())")
                    temp = data.index(")")
                    temp1 = data[4:temp+1]
                    data = data.replace(temp1, "")
        if True:
            if "," in data:
                if "print" not in data:
                    data=data.replace(",","\n")
            if data.strip().startswith("int"):
                if "=" in data:
                    data = data.replace("int", "")
            if data.strip().startswith("unsigned int"):
                if "=" in data:
                    data = data.replace("unsigned int", "")                  
            if data.strip().startswith("int"):
                data = data.replace("int"+str(var_extractor()), "")
            if data.strip().startswith("float"):
                if "=" in data:
                    data = data.replace("float", "")
                else:
                    data = data.replace("float"+str(var_extractor()), "")

            content = de_syntax(data)
            if content.strip().startswith("{"):
                content=content.replace("{","")

            content = content.strip()

            if "%d" in content:
                content = content.replace("%d", "")

            if "%f" in content:
                content = content.replace("%f", "")

            if content.strip().startswith("print"):
                if "\\n" in content:
                    content = content.replace("\\n", "no")

            f1.write(content.strip()+"\n")

print("VOILA! File converted successfully!!!")
f1.close()
with open("py.py") as f2:
    x = f2.read()
if "i++" in x:
    x=x.replace("i++","\ti+=1")
    
if "{" in x:
    x=x.replace("{",":")
if "if" in x:
    a=x.index("):")
    x=x[:a+3]+"\t"+x[a+3:]
    f=x.rindex("):")
    x=x[:f+3]+"\t"+x[f+3:]

if "else" in x:
    b=x.index("e:")
    x=x[:b+3]+"\t"+x[b+3:]

with open("python.py", "w") as f3:
    f3.write(x.strip())

os.remove("py.py")
new_name = input("\nRename your Python File: ")
rename_final_file()
