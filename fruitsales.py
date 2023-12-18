import pandas as pd
fruit= pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                index=['2017 Sales', '2018 Sales'])
fruit.to_csv("fruit.csv")
