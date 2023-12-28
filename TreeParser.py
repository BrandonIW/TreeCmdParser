import re


def main(outputfile, inputfile):
    File_Counter = 0
    Dir_Counter = 0
    with open(outputfile, 'a') as outputcsv:
        outputcsv.write("File or Directory Name,Extension (File Only)\n")  # Write Header

        with open(inputfile, 'r') as TPList:
            for line in TPList:
                line = line.rstrip("\n")
                Filecount, Dircount, Ext, Name = parser(line)

                if Name:
                    Name = Name.replace(',', ' ')  # Get rid of commas in the filename or dir to avoid issues with csv

                if not Filecount and not Dircount:
                    continue
                if Filecount:
                    File_Counter += 1
                else:
                    Dir_Counter += 1

                outputcsv.write(
                    f'{Name},{Ext}\n')

        outputcsv.write(f"Total Directories: {Dir_Counter},Total Files: {File_Counter}")


def parser(line):
    """ Detect if directory or file based on existence of an extension """
    ext_regex = re.compile(r'\.\w+$')  # Regex to capture the existence of an extension
    name_regex = re.compile(
        r'\w.*')  # Regex to capture the file or dir's name and separate it from all the noise characters

    file_match = ext_regex.search(line)
    name_match = name_regex.search(line)

    if file_match:
        extension = file_match.group()
        file_name = name_match.group()
        return True, False, extension, file_name
    elif name_match:
        file_name = name_match.group()
        return False, True, "Directory", file_name
    else:
        return False, False, None, None


if __name__ == "__main__":
    main('C:\\Users\\BW\\Documents\\output.csv',
         'C:\\Users\\BW\\Documents\\list.txt\\list.txt')
