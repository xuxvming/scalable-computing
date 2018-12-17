


ls = [];

def format_file (filename):
        with open(filename, 'r') as file :
                filedata = file.read()
                if(len(filedata) < 8):
                        ls.append(filedata)
        # Replace the target string
        #filedata = filedata.replace(':', ' ')

        # Write the file out again
        with open('newrockyou.txt', 'w') as file:
                file.write(filedata)

format_file("rockyou.txt")
print(ls)