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
print(df[["Age", "Cabin", "Embarked"]].isnull().sum())
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["HasCabin"] = df["Cabin"].notnull()
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["Alone"] = df["FamilySize"] == 1
def categoria_edad(edad):
    if edad < 13:
        return "Niño"
    elif edad < 18:
        return "Joven"
    elif edad < 60:
        return "Adulto"
    else:
        return "Adulto mayor"
df["AgeGroup"] = df["Age"].apply(categoria_edad)

supervivencia = df["Survived"].mean() * 100
print("Porcentaje de supervivencia:", supervivencia)
print(df.groupby("Sex")["Survived"].mean() * 100)
print(df.groupby("Pclass")["Survived"].mean() * 100)
print(df.groupby("Alone")["Survived"].mean() * 100)
#----------------------------------------------
sns.barplot(data=df, x="Sex", y="Survived")

plt.title("Supervivencia según el sexo")
plt.ylabel("Porcentaje de supervivencia")
plt.xlabel("Sexo")

plt.show()
sns.barplot(data=df, x="Pclass", y="Survived")

plt.title("Supervivencia según la clase")
plt.ylabel("Porcentaje de supervivencia")
plt.xlabel("Clase")

plt.show()

sns.barplot(data=df, x="AgeGroup", y="Survived")

plt.title("Supervivencia según grupo de edad")
plt.ylabel("Porcentaje de supervivencia")
plt.xlabel("Grupo de edad")

plt.show()
