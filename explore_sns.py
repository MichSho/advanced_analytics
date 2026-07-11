import pandas as pd
import seaborn as sns
sns.get_dataset_names()
tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")
titanic = sns.load_dataset("titanic")
penguins = sns.load_dataset("penguins")

"""
"tips" (regression / customer behavior)
"flights" (time series)
"penguins" (EDA + classification)
"titanic" (classification / survival prediction)

"""

df = tips
df.info()
df.describe()
df["tip_pct"] = df["tip"] / df["total_bill"]

df['time'].unique()
df['time'].nunique()
df['day'].value_counts()

#grouping to see how a quantitative variable (tip) changes across a qualitative variable
df.groupby('sex')['tip'].mean()

#cross tabulation is perfect for comparing two qualitative variables
#(e.g., smoker (yes/no) vs time (lunch/dinner)) 
#it creates a contingency table that shows the frequency distribution of the qualitative variables,
#allowing us to see how they relate to each other.
pd.crosstab(df['smoker'], df['time'])
