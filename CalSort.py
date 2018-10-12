from bipartiteMatch import bipartiteMatch

import pandas as pd


df= pd.read_csv('SampleData.csv', index_col=0, squeeze=True).to_dict()



df = bipartiteMatch(df)

print(df)
