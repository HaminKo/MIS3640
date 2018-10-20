def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.
    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    fin = open(source, 'r')
    fout = open(dest, 'w')
    for line in fin:
        fout.write(line.replace(pattern, replace))
        # if pattern in line:
        #     fout.write(line.replace(pattern, replace))
        # else:
        #     fout.write(line)
    fin.close()
    fout.close()
    


pattern = 'man'
replace = 'woman'
source = 'output.txt'
dest = 'new_' + source
sed(pattern, replace, source, dest)