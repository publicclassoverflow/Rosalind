# http://rosalind.info/problems/ba1e/
# Given integers L and t, a string Pattern forms an (L, t)-clump inside
# a (larger) string Genome if there is an interval of Genome of length
# L in which Pattern appears at least t times. For example, TGCATGCA forms
# a (25,3)-clump in the following Genome: gatcagcataagggtcccTGCAATGCATGACAAGCCTGCAgttgttttacgatcagcataagggtcccTGCAATGCATGACAAGCCTGCAgttgttttac.

# Clump Finding Problem
# Find patterns forming clumps in a string.
# Given: A string Genome, and integers k, L, and t.
# Return: All distinct k-mers forming (L, t)-clumps in Genome.


def count_clumps(sequence, k, L, t):
    clumps = set()
    for i in range(len(sequence) - (L - 1)):
        kmers = {}
        for j in range(L - (k - 1)):
            kmer = sequence[(i + j):(i + j + k)]
            kmers[kmer] = kmers.get(kmer, 0) + 1
            if kmers[kmer] >= t:
                clumps.add(kmer)
    return clumps


def run(filename):
    with open(filename, "r") as infile:
        dna_sequence = infile.readline().strip()
        parameters = infile.readline().strip().split()
        k = int(parameters[0])
        L = int(parameters[1])
        t = int(parameters[2])
        clumps = count_clumps(dna_sequence, k, L, t)
        print(" ".join(clumps))


if __name__ == "__main__":
    print("The result from sample data:")
    run("sample.txt")
    print("The result from the dataset:")
    run("rosalind_ba1e.txt")

