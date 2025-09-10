import pandas as pd
import matplotlib.pyplot as plt

#task 1: import excel file
file_path='/content/gene_expression_file.xlsx'
a = pd.read_excel(file_path)

#task 2: overview of dataset
print("Overview of dataset:")
print("1. Number of rows -> genes:", a.shape[0])
print("2. Number of columns (including gene names) -> samples:", a.shape[1])
print("3. Number of columns (excluding gene names) -> samples:", a.shape[1]-1)

#first few rows
print(a.head(2))

#task 3: clean rows
a_clean = a.dropna()

#task 4: key statistics
stats_a=a_clean.copy()
num=stats_a.iloc[:, 1:]
stats_a['Mean']=num.mean(axis=1)
stats_a['Media']=num.median(axis=1)
stats_a['Std']=num.std(axis=1)

#task 5: top 3 genes by mean
top_genes_mean=stats_a.sort_values(by='Mean', ascending=False).head(3)
print("Top three genes:")
print(top_genes_mean)

#task 6: prompt user
gene_name = input("Enter a gene name for detailed analysis: ")

#checking if the gene exist
if gene_name in a_clean.iloc[:,0].values:
  gene_row=a_clean[a_clean.iloc[:, 0]==gene_name].iloc[0, 1:]
  print(gene_row)

  #plotting the graph
  plt.figure(figsize=(10, 5))
  plt.plot(gene_row.index, gene_row.values)
  plt.title(f'Expression profile of {gene_name}')
  plt.xlabel('Samples')
  plt.ylabel('Expression level')
  plt.grid(True)
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()
else:
  print("Gene not found in the dataset.")