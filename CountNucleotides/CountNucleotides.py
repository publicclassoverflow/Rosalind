# http://rosalind.info/problems/dna/
# A string is simply an ordered collection of symbols selected from some
# alphabet and formed into a word; the length of
# a string is the number of symbols that it contains.

# An example of a length 21 DNA string (whose alphabet contains the symbols
# 'A', 'C', 'G', and 'T')
# is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA string ss of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of
# times that the symbols 'A', 'C', 'G',
# and 'T' occur in ss.


def count_nucleotides(dna_sequence):
    result = {}
    # for base in dna_sequence:
    #     result[base] = dna_sequence.count(base)
    # The method above has a complexity of O(4N)
    # The one below is O(N)
    for i in range(len(dna_sequence)):
        result[dna_sequence[i]] = result.get(dna_sequence[i], 0) + 1
    return result


def run(filename):
    with open(filename, 'r') as infile:
        sequence = infile.readline().strip()
        base_count = count_nucleotides(sequence)
        print(" ".join(str(base_count[base]) for base in ["A", "C", "G", "T"]))


if __name__ == "__main__":
    print("The result of sample sequence:")
    run("sample.txt")
    print("The result of the sequence in the dataset:")
    run("rosalind_dna.txt")

