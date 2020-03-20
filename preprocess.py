import pandas as pd, numpy as np

# Read recipe inputs
new_cases_processed_df = pd.read_csv('/corona-virus-complete-dataset/new_cases.csv')

cols = list(new_cases_processed_df.columns)
col_length = len(new_cases_processed_df.columns)
row_length = len(new_cases_processed_df)

df_duplicate = pd.concat([new_cases_processed_df]*(col_length-1), ignore_index=True)
filterd = df_duplicate.filter(['date'])
filterd['country'] = ""
vv = []
cols.remove('date')

for ctry in cols:
    for i in range(1, (row_length+1)):
        vv.append(ctry)

filterd['country'] = vv
filterd['cases'] = ""
cc = []
for ctry in cols:
    cc.append(pd.Series(new_cases_processed_df[ctry].values))
cc = pd.concat(cc, ignore_index=True)
filterd['cases'] = cc

new_cases_new_format_df = filterd


# Write recipe outputs
new_cases_new_format_df.to_csv('new_cases_processed.csv', sep=',')