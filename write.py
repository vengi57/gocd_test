import pandas as pd
df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
                   'mask': ['red', 'purple'],
                   'weapon': ['sai', 'bo staff']})
df.to_csv("./output/file_name_1.csv",index = False)
df.to_csv("./output/file_name_2.csv",index = False)
df.to_csv("./output/file_name_3.csv",index = False)
