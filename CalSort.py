from bipartiteMatch import bipartiteMatch
import csv
import pandas as pd

reader = csv.DictReader(open('myfile.csv'))

bipartiteMatch(reader)

    
