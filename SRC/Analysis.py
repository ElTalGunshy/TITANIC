import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/train.csv")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/train.csv")
print(df)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/train.csv")

print(df)
print("Número de pasajeros:", len(df))
print("Número de columnas:", len(df.columns))
print("Columnas:")
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
print("Duplicados:", df.duplicated().sum())
print(df.describe())
#----------------------------------------------
