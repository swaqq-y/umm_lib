
def create_emptyfile(name, extention):
    f = open("{}.{}".format(name, extention), "w+")
def create_filewithcontent(name, extention, content):
    f = open("{}.{}".format(name, extention), "w+")
    f.write(content)
def  create_filefromtemplate(name, extention, template):
    templates = {"Python calculator" : "def calculator(command, a, b): \n \t if command == '*':\n \t \t return a * b \n \t elif command == '/':\n \t \t return a/b\n \t elif command == '+':\n \t \t return a + b\n \t elif command == '-':\n \t \t return a-b"}
    f = open("{}.{}".format(name, extention), "w+")
    f.write(templates[template])

