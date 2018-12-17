




def format_file (filename):
        with open(filename, 'r') as file :
                filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(':', ' ')

        # Write the file out again
        with open('xiux.broken', 'w') as file:
                file.write(filedata)

format_file("john.pot")