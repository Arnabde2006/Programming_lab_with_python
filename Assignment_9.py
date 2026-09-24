import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset: UCI Automobile dataset -> imports-85.data (keep it in the same folder as this file)
# https://archive.ics.uci.edu/dataset/10/automobile

cols=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style",
      "drive-wheels","engine-location","wheel-base","length","width","height","curb-weight",
      "engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke",
      "compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]


#1
print("Q1 - Loading and Exploring the Dataset")

try:
    df=pd.read_csv("imports-85.data",header=None,names=cols)
except FileNotFoundError:
    df=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data",header=None,names=cols)

print("First five records:\n",df.head())
print("Last five records:\n",df.tail())
print("Number of rows and columns:",df.shape)
print("Column names:",list(df.columns))
print("Data types:\n",df.dtypes)


#2
print("Q2 - Dataset Information and Summary Statistics")

df.info()
print("Descriptive statistics (numerical columns):\n",df.describe())


#3
print("Q3 - Handling Missing Values")

df=df.replace("?",np.nan)
print("Missing values in each column:\n",df.isnull().sum())
print("Columns containing missing values:",list(df.columns[df.isnull().any()]))
print("Total missing values in dataset:",df.isnull().sum().sum())


#4
print("Q4 - Cleaning the Price Column")

df["price"]=pd.to_numeric(df["price"],errors="coerce")
print("Missing prices:",df["price"].isnull().sum())
df=df.dropna(subset=["price"])   # cars without a price are dropped
print("Minimum car price:",df["price"].min())
print("Maximum car price:",df["price"].max())
print("Average car price:",round(df["price"].mean(),2))
print("Median car price:",df["price"].median())


#5
print("Q5 - Frequency of Car Makes")

make_counts=df["make"].value_counts()
print("Cars per make:\n",make_counts)
print("Top 10 car manufacturers:\n",make_counts.head(10))


#6
print("Q6 - Body Style Analysis")

print(df["body-style"].value_counts().sort_values(ascending=False))


#7
print("Q7 - Fuel Type Analysis")

fuel_counts=df["fuel-type"].value_counts()
fuel_pct=(fuel_counts/fuel_counts.sum()*100).round(2)
print("Number of cars by fuel type:\n",fuel_counts)
print("Percentage of cars by fuel type:\n",fuel_pct)
plt.figure(figsize=(6,4))
plt.bar(fuel_counts.index,fuel_counts.values,color=["#4c72b0","#c44e52"])
plt.title("Number of Cars by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Number of Cars")
plt.grid(axis="y")
plt.show()


#8
print("Q8 - Car Price Distribution")

print(df["price"].describe())
plt.figure(figsize=(8,5))
plt.hist(df["price"],bins=20,color="teal",edgecolor="black")
plt.title("Distribution of Car Prices")
plt.xlabel("Price")
plt.ylabel("Number of Cars")
plt.grid(True)
plt.show()


#9
print("Q9 - Average Price by Car Make")

avg_make=df.groupby("make")["price"].mean().sort_values(ascending=False)
print("Average price by make (descending):\n",avg_make.round(2))
print("Five most expensive manufacturers:\n",avg_make.head(5).round(2))


#10
print("Q10 - Average Price by Body Style")

avg_body=df.groupby("body-style")["price"].mean().sort_values(ascending=False)
print(avg_body.round(2))
plt.figure(figsize=(8,5))
plt.bar(avg_body.index,avg_body.values,color="orange")
plt.title("Average Price by Body Style")
plt.xlabel("Body Style")
plt.ylabel("Average Price")
plt.grid(axis="y")
plt.show()


#11
print("Q11 - Horsepower Analysis")

df["horsepower"]=pd.to_numeric(df["horsepower"],errors="coerce")
hp=df["horsepower"]
print("Minimum horsepower:",hp.min())
print("Maximum horsepower:",hp.max())
print("Mean horsepower:",round(hp.mean(),2))
print("Median horsepower:",hp.median())
print("Standard deviation:",round(hp.std(),2))
plt.figure(figsize=(8,5))
plt.hist(hp.dropna(),bins=20,color="purple",edgecolor="black")
plt.title("Distribution of Horsepower")
plt.xlabel("Horsepower")
plt.ylabel("Number of Cars")
plt.grid(True)
plt.show()


#12
print("Q12 - Engine Size Analysis")

es=df["engine-size"]
print("Minimum engine size:",es.min())
print("Maximum engine size:",es.max())
print("Average engine size:",round(es.mean(),2))
print("Median engine size:",es.median())
plt.figure(figsize=(8,5))
plt.hist(es,bins=20,color="green",edgecolor="black")
plt.title("Distribution of Engine Sizes")
plt.xlabel("Engine Size")
plt.ylabel("Number of Cars")
plt.grid(True)
plt.show()


#13
print("Q13 - Horsepower vs Price")

plt.figure(figsize=(8,5))
plt.scatter(df["horsepower"],df["price"],color="blue",alpha=0.6)
plt.title("Horsepower vs Price")
plt.xlabel("Horsepower")
plt.ylabel("Price")
plt.grid(True)
plt.show()
r=df["horsepower"].corr(df["price"])
print(f"Correlation between horsepower and price: {r:.3f}")
print("Comment: there is a strong positive relationship - cars with more horsepower generally cost more." if r>0.5 else "Comment: the relationship between horsepower and price is weak.")


#14
print("Q14 - Engine Size vs Price")

plt.figure(figsize=(8,5))
plt.scatter(df["engine-size"],df["price"],color="red",alpha=0.6)
plt.title("Engine Size vs Price")
plt.xlabel("Engine Size")
plt.ylabel("Price")
plt.grid(True)
plt.show()
print("Correlation between engine size and price:",round(df["engine-size"].corr(df["price"]),3))


#15
print("Q15 - Curb Weight vs Price")

plt.figure(figsize=(8,5))
plt.scatter(df["curb-weight"],df["price"],color="brown",alpha=0.6)
plt.title("Curb Weight vs Price")
plt.xlabel("Curb Weight")
plt.ylabel("Price")
plt.grid(True)
plt.show()
print("Correlation between curb weight and price:",round(df["curb-weight"].corr(df["price"]),3))


#16
print("Q16 - Highway MPG Analysis")

h=df["highway-mpg"]
print("Minimum:",h.min())
print("Maximum:",h.max())
print("Mean:",round(h.mean(),2))
print("Median:",h.median())
plt.figure(figsize=(8,5))
plt.hist(h,bins=15,color="navy",edgecolor="black")
plt.title("Distribution of Highway Mileage")
plt.xlabel("Highway MPG")
plt.ylabel("Number of Cars")
plt.grid(True)
plt.show()


#17
print("Q17 - City MPG vs Highway MPG")

plt.figure(figsize=(8,5))
plt.scatter(df["city-mpg"],df["highway-mpg"],color="darkgreen",alpha=0.6)
plt.title("City MPG vs Highway MPG")
plt.xlabel("City MPG")
plt.ylabel("Highway MPG")
plt.grid(True)
plt.show()
r=df["city-mpg"].corr(df["highway-mpg"])
print("Correlation coefficient:",round(r,3))
if r>0.7:
    print("Yes - cars with higher city mileage generally also have higher highway mileage (strong positive correlation).")
else:
    print("There is no strong positive relationship between city and highway mileage.")


#18
print("Q18 - Number of Doors by Body Style")

door_table=pd.crosstab(df["body-style"],df["num-of-doors"])
print(door_table)
door_table.plot(kind="bar",figsize=(8,5))
plt.title("Number of Doors by Body Style")
plt.xlabel("Body Style")
plt.ylabel("Number of Cars")
plt.xticks(rotation=0)
plt.grid(axis="y")
plt.show()


#19
print("Q19 - Fuel Type and Average Price")

avg_fuel=df.groupby("fuel-type")["price"].mean()
print(avg_fuel.round(2))
plt.figure(figsize=(6,4))
plt.bar(avg_fuel.index,avg_fuel.values,color=["#4c72b0","#c44e52"])
plt.title("Average Price: Gasoline vs Diesel")
plt.xlabel("Fuel Type")
plt.ylabel("Average Price")
plt.grid(axis="y")
plt.show()


#20
print("Q20 - Drive Wheel Analysis")

dw=df["drive-wheels"].value_counts()
print("Front-wheel drive (fwd):",dw.get("fwd",0))
print("Rear-wheel drive (rwd):",dw.get("rwd",0))
print("Four-wheel drive (4wd):",dw.get("4wd",0))
plt.figure(figsize=(6,4))
plt.bar(dw.index,dw.values,color="steelblue")
plt.title("Distribution of Drive Wheels")
plt.xlabel("Drive Wheels")
plt.ylabel("Number of Cars")
plt.grid(axis="y")
plt.show()


#21
print("Q21 - Price Comparison by Drive Wheels")

avg_dw=df.groupby("drive-wheels")["price"].mean()
print(avg_dw.round(2))
plt.figure(figsize=(6,4))
plt.bar(avg_dw.index,avg_dw.values,color="darkorange")
plt.title("Average Price by Drive Wheels")
plt.xlabel("Drive Wheels")
plt.ylabel("Average Price")
plt.grid(axis="y")
plt.show()


#22
print("Q22 - Correlation Analysis of Numerical Variables")

num_cols=["price","engine-size","horsepower","curb-weight","city-mpg","highway-mpg"]
corr=df[num_cols].corr()
print("Correlation matrix:\n",corr.round(3))
price_corr=corr["price"].drop("price")
print("Most strongly positively correlated with price:",price_corr.idxmax(),round(price_corr.max(),3))
print("Most strongly negatively correlated with price:",price_corr.idxmin(),round(price_corr.min(),3))


#23
print("Q23 - Basic Car Price Analytics Report")

print("\n1. Dataset dimensions:",df.shape)
df.info()

print("\n2. Missing-value analysis:")
print(df.isnull().sum()[df.isnull().sum()>0])

print("\n3. Descriptive statistics:")
print(df[num_cols].describe().round(2))

top5=df.groupby("make")["price"].mean().sort_values(ascending=False).head(5)
print("\n4. Top five manufacturers by average price:\n",top5.round(2))

print("\n5. Most common body style:",df["body-style"].value_counts().idxmax())

print("\n6. Average price by fuel type:\n",df.groupby("fuel-type")["price"].mean().round(2))

print("\n7. Average price by drive wheels:\n",df.groupby("drive-wheels")["price"].mean().round(2))

plt.figure(figsize=(8,5))
plt.hist(df["price"],bins=20,color="teal",edgecolor="black")
plt.title("Histogram of Car Prices")
plt.xlabel("Price")
plt.ylabel("Number of Cars")
plt.grid(True)
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(df["horsepower"],df["price"],alpha=0.6)
plt.title("Horsepower vs Price")
plt.xlabel("Horsepower")
plt.ylabel("Price")
plt.grid(True)
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(df["engine-size"],df["price"],alpha=0.6,color="red")
plt.title("Engine Size vs Price")
plt.xlabel("Engine Size")
plt.ylabel("Price")
plt.grid(True)
plt.show()

print("\nConclusion:")
print(f"- The dataset has {df.shape[0]} cars (after dropping rows with missing price) and {df.shape[1]} columns; several columns (e.g. normalized-losses) contain missing values.")
print(f"- Average car price is about {df['price'].mean():.0f}; {top5.index[0]} is the most expensive manufacturer on average.")
print(f"- '{df['body-style'].value_counts().idxmax()}' is the most common body style.")
print(f"- Price is most strongly positively related to {price_corr.idxmax()} and most strongly negatively related to {price_corr.idxmin()}.")
print("- Larger engines and higher horsepower are associated with higher prices, while better fuel economy is associated with lower prices.")
