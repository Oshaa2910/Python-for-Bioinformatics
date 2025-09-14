def translate(sequence):
  codon_table = {
      'UUU' : 'F', 'UUC' : 'F', 'UUA' : 'L', 'UUG' : 'L',
      'UCU' : 'S', 'UCC' : 'S', 'UCA' : 'S', 'UCG' : 'S',
      'UAU' : 'Y', 'UAC' : 'Y', 'UAA' : '*', 'UAG' : '*',
      'UGU' : 'C', 'UGC' : 'C', 'UGA' : '*', 'UGG' : 'W',
      'CUU' : 'L', 'CUC' : 'L', 'CUA' : 'L', 'CUG' : 'L',
      'CCU' : 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P',
      'CAU' : 'H', 'CAC' : 'H', 'CAA' : 'Q', 'CAG' : 'Q',
      'CGU' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R',
      'AUU' : 'l', 'AUC' : 'l', 'AUA' : 'l', 'AUG' : 'M',
      'ACU' : 'T', 'ACC' : 'T', 'ACA' : 'T', 'ACG' : 'T',
      'AAU' : 'N', 'AAC' : 'N', 'AAA' : 'K', 'AAG' : 'K',
      'AGU' : 'S', 'AGC' : 'S', 'AGA' : 'R', 'AGG' : 'R',
      'GUU' : 'V', 'GUC' : 'V', 'GUA' : 'V', 'GUG' : 'V',
      'GCU' : 'A', 'GCC' : 'A', 'GCA' : 'A', 'GCG' : 'A',
      'GAU' : 'P', 'GAC' : 'P', 'GAA' : 'E', 'GAG' : 'E',
      'GGU' : 'G', 'GGC' : 'G', 'GGA' : 'G', 'GGG' : 'G',
  }

  sequence = sequence.upper()
  if "T" in sequence:
    sequence = sequence.replace("T", "U")
  protein = ''
  if len(sequence) % 3 == 0:
    for i in range(0, len(sequence), 3):
      codon = sequence[i : i + 3]
      protein += codon_table[codon]
  return protein

dna = input("Enter a DNA/RNA sequence: ")
protein = translate(dna)
print("Protein sequence:", protein)