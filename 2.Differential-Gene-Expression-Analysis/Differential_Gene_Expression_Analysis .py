import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_ind

file_name = input("Enter the name of the CSV file (only .csv extension): ")
a = pd.read_csv(file_name) 

#cleaning data

a = a.dropna()
a = a.head(100)

# defining conditions
control_cols = ['SRR1039508', 'SRR1039509']  # Untreated
treated_cols = ['SRR1039512', 'SRR1039513']  # Trted

'''variable = a[mean_control] & a[mean_treated]
select control column = a[control_cols]
select treated column = a[treated_cols]
calculate verage = .mean(axis=1)'''

#calculate mean

a['mean_control'] = a[control_cols].mean(axis=1)
a['mean_treated'] = a[treated_cols].mean(axis=1)

#Compute log2 Fold Change

'''a['log2_fold_change'] => creates a new column
np.log2(...) => numpy function. it calculates logarithm base 2
a['mean_treated'] + 1 => This adds 1 to each value in the 'mean_treated' column. To avoid log2(0)
np.log2(a['mean_treated'] + 1) =?This gives you a new Series where each element is: 
log2(mean_treated expression + 1)
showing how much expression exists in treated condition (on log scale).'''

a['log2_fold_change'] = np.log2(a['mean_treated']+ 1) - np.log2(a['mean_control'] + 1)

#Calculate p-value

p_values = []
for i, row in a.iterrows():
    try:
        control_vals = row[control_cols].astype(float)
        treated_vals = row[treated_cols].astype(float)
        stat, p = ttest_ind(control_vals, treated_vals)
        p_values.append(p)
    except:
        p_values.append(1.0)  # if something fails, assign non-significant
a['p_value'] = p_values

#Upregulated / Downregulated / Not significant

p_thresh = 0.05
fc_thresh = 1  # change this based on how strong a fold change you want to detect

a['Significance'] = 'Not significant'
a.loc[(a['p_value'] < p_thresh) & (a['log2_fold_change'] > fc_thresh), 'Significance'] = 'Upregulated'
a.loc[(a['p_value'] < p_thresh) & (a['log2_fold_change'] < -fc_thresh), 'Significance'] = 'Downregulated'

# volcano plot
a['color'] = a['Significance'].map({
    'Upregulated': 'red',
    'Downregulated': 'blue',
    'Not significant': 'gray'
})

plt.figure(figsize=(10, 6))
plt.scatter(a['log2_fold_change'], -np.log10(a['p_value']), c=a['color'], alpha=0.7)
plt.axhline(-np.log10(p_thresh), color='black', linestyle='--')
plt.axvline(fc_thresh, color='black', linestyle='--')
plt.axvline(-fc_thresh, color='black', linestyle='--')
plt.xlabel('log2(Fold Change)')
plt.ylabel('-log10(p-value)')
plt.title('Volcano Plot')
plt.grid(True)
plt.tight_layout()
plt.show()

# save the results

a.to_csv('airway_dge_results.csv', index=False)
a[a['Significance'] == 'Upregulated'].to_csv('airway_upregulated.csv', index=False)
a[a['Significance'] == 'Downregulated'].to_csv('airway_downregulated.csv', index=False)