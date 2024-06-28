import sys
import re    

def clean_fasta(filename):
    '''Reads in a fasta file with extra whitespace or line numbers, 
    and reads the data into a string with just the header + newline + ACTG or actg characters'''
    with open(filename, 'r') as infile:
        # add the header unchanged
        header = infile.readline()
        cleanstring = header

        # cancel if not valid file
        if header[0] != '>' or filename.split('.')[1].lower() != 'fasta':
            print('Please input a .fasta file with a header.')
            return None

        # read all the sequence characters into a single line
        for line in infile:
            cleanline = re.sub('[^actgACTG]', '', line)
            cleanstring = cleanstring + cleanline
    return cleanstring
    

if __name__ == '__main__':    
    infile = sys.argv[1]
    data = clean_fasta(infile)
    if data:
        with open(infile, 'w') as outfile:
            outfile.write(data)