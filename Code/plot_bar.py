import numpy as np
import pandas
import matplotlib.pyplot as plt


file_name = 'MCF10AUnique.xlsx'
n_measurements = 6
xl = pandas.ExcelFile(file_name)



# values = df['Arm_id'].values
#get a data frame with selected columns
# FORMAT = ['Arm_id', 'DSPName', 'Pincode']
# df_selected = df[FORMAT]


index = np.arange(n_measurements)
total_rows = xl.book.sheet_by_index(0).nrows
df = xl.parse()
# print df.columns
# print df[df.columns[0]]
gene_list = [[] for i in range(total_rows-1)]
counter = 0
gene_names = df[df.columns[0]].values
for i in np.arange(0,n_measurements):
  start = counter
  a = np.array(df[df.columns[start+1:start+4]].values)

  for r in np.arange(a.shape[0]):
    std_val = np.std(a[r])
    mean_val = np.mean(a[r])
    gene_list[r].append({ 'mean':mean_val, 'std':std_val})


  counter +=3

print "done"



index = np.arange(n_measurements)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

for i in np.arange(total_rows-1):
  data = gene_list[i]
  means = [data[k]['mean'] for k in np.arange(len(data))]
  stds = [data[k]['std'] for k in np.arange(len(data))]
  fig, ax = plt.subplots()
  plt.bar(index, means, bar_width,
                   alpha=opacity,
                   color='b',
                   yerr=stds,
                   error_kw=error_config)

  save_file = gene_names[i] + '.png'
  plt.savefig(save_file)
  plt.close(fig)
  # plt.show()
  print i