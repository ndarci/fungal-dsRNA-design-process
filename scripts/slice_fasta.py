import sys
from clean_fasta import clean_fasta

def slice_fasta(start, length, infilename, outfilename):
    '''Read in an input fasta file, select a slice from start -> start + length, 
    and write a new fasta file to outfile with a matching header'''
    # select the sequence data only
    indata = clean_fasta(infilename).split('\n')[1]

    # correct for zero indexing
    start -= 1 

    # check index error
    if start + length > len(indata) or start < 0:
        print('Slice out of range of input sequence.')
        return None
    
    # get a slice of length bases starting at start
    slice = indata[start:start+length]
    sliced_fasta = '>' + outfilename.split('.')[0] + '\n' + slice

    return sliced_fasta

if __name__ == '__main__':
    seqstart, seqlength, input_filename, output_filename = sys.argv[1:5]
    seqstart = int(seqstart)
    seqlength = int(seqlength)
    new_file_data = slice_fasta(seqstart, seqlength, input_filename, output_filename)
    with open(output_filename, 'w') as outfile:
        outfile.write(new_file_data)

