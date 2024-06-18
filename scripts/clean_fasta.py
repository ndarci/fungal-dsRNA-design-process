import sys    

def clean_fasta(filename):
    '''Reads in a fasta file with extra whitespace, 
    and reads the data into a string with no whitespace'''
    with open(filename, 'r') as infile:
        # add the header unchanged
        header = infile.readline()

        # cancel if not valid file
        if header[0] != '>' or filename.split('.')[1].lower() != 'fasta':
            print('Please input a .fasta file with a header.')
            return None

        cleanstring = header
        # read all the sequence characters into a single line
        for line in infile:
            cleanstring = cleanstring + line.strip()
    return cleanstring
    

if __name__ == '__main__':    
    infile = sys.argv[1]
    data = clean_fasta(infile)
    if data:
        with open(infile, 'w') as outfile:
            outfile.write(data)