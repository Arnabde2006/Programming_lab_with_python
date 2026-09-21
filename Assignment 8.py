import array as arr
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ================= Part A - Arrays in Python =================

#1
print("Q1 - Create and Access an Array")

a=arr.array('i',[10,20,30,40,50,60,70,80,90,100])
print("Array elements:",a.tolist())
print("First element:",a[0])
print("Last element:",a[-1])
print("Middle element:",a[len(a)//2])


#2
print("Q2 - Array Operations")

a=arr.array('i',[12,45,7,23,56,89,34,21,67,90])
print("Array:",a.tolist())
print("Sum:",sum(a))
print("Average:",sum(a)/len(a))
print("Maximum:",max(a))
print("Minimum:",min(a))
print("Length:",len(a))


#3
print("Q3 - Insert and Delete Elements")

a=arr.array('i',range(1,11))
print("Original:",a.tolist())
a.insert(3,99)
print("After inserting 99 at position 3:",a.tolist())
a.append(100)
print("After appending 100:",a.tolist())
a.remove(5)
print("After removing 5:",a.tolist())
print("Updated array:",a.tolist())


#4
print("Q4 - Reverse and Sort an Array")

a=arr.array('i',[random.randint(1,100) for _ in range(10)])
print("Original:",a.tolist())
print("Ascending:",sorted(a))
print("Descending:",sorted(a,reverse=True))
a.reverse()
print("Reversed:",a.tolist())


#5
print("Q5 - Search and Count Elements")

a=arr.array('i',[5,12,7,12,9,3,12,8])
target=12
print("Array:",a.tolist())
if target in a:
    print(f"{target} found at index {a.index(target)}")
    print(f"{target} occurs {a.count(target)} time(s)")
else:
    print(f"{target} not found in the array")
target=100
if target in a:
    print(f"{target} found at index {a.index(target)}")
else:
    print(f"{target} not found in the array")


# ================= Part B - NumPy =================

#6
print("Q6 - Creating NumPy Arrays")

one_d=np.array([1,2,3,4,5])
two_d=np.array([[1,2,3],[4,5,6]])
zeros=np.zeros((3,3))
ones=np.ones((2,4))
rng=np.arange(1,11)
for name,x in [("1-D",one_d),("2-D",two_d),("Zeros",zeros),("Ones",ones),("Range",rng)]:
    print(f"{name} array:\n{x}\nShape: {x.shape}\n")


#7
print("Q7 - Array Indexing and Slicing")

a=np.arange(1,21)
print("Array:",a)
print("Positive indexing a[3]:",a[3])
print("Negative indexing a[-2]:",a[-2])
print("First five elements:",a[:5])
print("Last five elements:",a[-5:])
print("Alternate elements:",a[::2])


#8
print("Q8 - NumPy Array Arithmetic")

x=np.array([10,20,30,40,50])
y=np.array([3,4,5,6,7])
print("x:",x)
print("y:",y)
print("Addition:",x+y)
print("Subtraction:",x-y)
print("Multiplication:",x*y)
print("Division:",x/y)
print("Modulus:",x%y)
print("Exponentiation:",x**y)


#9
print("Q9 - Statistical Operations Using NumPy")

marks=np.array([78,85,92,67,74,88,95,59,81,70])
print("Marks:",marks)
print("Mean:",np.mean(marks))
print("Median:",np.median(marks))
print("Standard deviation:",np.std(marks))
print("Variance:",np.var(marks))
print("Maximum marks:",np.max(marks))
print("Minimum marks:",np.min(marks))


#10
print("Q10 - Reshaping NumPy Arrays")

a=np.arange(1,25)
for r,c in [(2,12),(3,8),(4,6),(6,4)]:
    b=a.reshape(r,c)
    print(f"{r} x {c} matrix:\n{b}\nShape: {b.shape}\n")


#11
print("Q11 - Matrix Operations")

m1=np.array([[1,2,3],[4,5,6],[7,8,9]])
m2=np.array([[9,8,7],[6,5,4],[3,2,1]])
print("Matrix 1:\n",m1)
print("Matrix 2:\n",m2)
print("Addition:\n",m1+m2)
print("Subtraction:\n",m1-m2)
print("Element-wise multiplication:\n",m1*m2)
print("Matrix multiplication:\n",np.dot(m1,m2))
print("Transpose of Matrix 1:\n",m1.T)
print("Transpose of Matrix 2:\n",m2.T)


#12
print("Q12 - Finding Elements Using NumPy Conditions")

a=np.array([12,45,67,23,88,54,31,90,15,62,77,40,29,51,66,8,99,34,57,21])
print("Array:",a)
print("Even numbers:",a[a%2==0])
print("Odd numbers:",a[a%2!=0])
print("Numbers greater than 50:",a[a>50])
print("Numbers between 20 and 60:",a[(a>=20)&(a<=60)])


#13
print("Q13 - NumPy Mathematical Functions")

angles=np.array([0,30,45,60,90])
rad=np.deg2rad(angles)
print("Angles (degrees):",angles)
print("Sine:",np.round(np.sin(rad),4))
print("Cosine:",np.round(np.cos(rad),4))
print("Tangent (90 is undefined/very large):",np.round(np.tan(rad[:-1]),4))
b=np.array([1,4,9,16,25])
print("Array:",b)
print("sqrt:",np.sqrt(b))
print("log:",np.round(np.log(b),4))
print("exp:",np.round(np.exp(np.array([1,2,3])),4))


#14
print("Q14 - Combining and Splitting Arrays")

p=np.array([1,2,3])
q=np.array([4,5,6])
print("p:",p,"q:",q)
print("concatenate:",np.concatenate((p,q)))
print("vstack:\n",np.vstack((p,q)))
print("hstack:",np.hstack((p,q)))
big=np.arange(1,10)
print("split into 3:",np.split(big,3))


#15
print("Q15 - Handling Missing and Invalid Values in NumPy")

a=np.array([10,20,np.nan,40,np.nan,60])
print("Array:",a)
print("NaN positions:",np.isnan(a))
print("Count of NaN values:",np.isnan(a).sum())
mean_val=np.nanmean(a)
print("Mean ignoring NaN:",mean_val)
a[np.isnan(a)]=mean_val
print("After replacing NaN with mean:",a)


# ================= Part C - Pandas =================

#16
print("Q16 - Creating a Pandas Series")

s=pd.Series([78,85,92,67,74,88,95,59,81,70])
print("Series:\n",s)
print("Index:",s.index)
print("Values:",s.values)
print("First five:\n",s.head())
print("Last three:\n",s.tail(3))
print("Maximum:",s.max())
print("Minimum:",s.min())


#17
print("Q17 - Creating and Accessing a DataFrame")

df=pd.DataFrame({
    "Roll Number":[101,102,103,104,105,106,107,108,109,110],
    "Name":["Arnab","Rahul","Priya","Amit","Neha","Sourav","Ritika","Karan","Sneha","Vikram"],
    "Department":["BCA","BCA","BBA","BCA","BBA","BCA","BBA","BCA","BBA","BCA"],
    "Marks":[85,72,90,64,78,55,88,69,81,93],
    "Attendance":[92,78,85,70,88,65,95,74,82,90]
})
print("Complete DataFrame:\n",df)
print("First five records:\n",df.head())
print("Last five records:\n",df.tail())
print("Selected columns:\n",df[["Name","Marks"]])
print("Record of a particular student (Roll 103):\n",df[df["Roll Number"]==103])


#18
print("Q18 - DataFrame Filtering")

print("Marks > 75:\n",df[df["Marks"]>75])
print("Attendance > 80%:\n",df[df["Attendance"]>80])
print("Marks > 60 and Attendance > 75%:\n",df[(df["Marks"]>60)&(df["Attendance"]>75)])
print("Department BCA:\n",df[df["Department"]=="BCA"])


#19
print("Q19 - Sorting and Ranking Data")

emp=pd.DataFrame({
    "Employee ID":[1,2,3,4,5,6],
    "Name":["Amit","Neha","Rahul","Priya","Karan","Sneha"],
    "Department":["IT","HR","IT","Finance","HR","Finance"],
    "Salary":[55000,48000,72000,61000,45000,66000]
})
print("Ascending by salary:\n",emp.sort_values("Salary"))
print("Descending by salary:\n",emp.sort_values("Salary",ascending=False))
print("Highest paid:\n",emp.loc[emp["Salary"].idxmax()])
print("Lowest paid:\n",emp.loc[emp["Salary"].idxmin()])
emp["Rank"]=emp["Salary"].rank(ascending=False).astype(int)
print("Ranking by salary:\n",emp.sort_values("Rank"))


#20
print("Q20 - Handling Missing Data in Pandas")

sd=pd.DataFrame({
    "Name":["Arnab","Rahul","Priya","Amit","Neha","Sourav"],
    "Marks":[85,np.nan,90,64,np.nan,55],
    "Attendance":[92,78,np.nan,70,88,65],
    "Department":["BCA","BCA",None,"BCA","BBA",None]
})
print("Data:\n",sd)
print("Missing values (True = missing):\n",sd.isnull())
print("Missing values per column:\n",sd.isnull().sum())
print("Rows after removing missing values:\n",sd.dropna())
filled=sd.copy()
filled["Marks"]=filled["Marks"].fillna(filled["Marks"].mean())
filled["Attendance"]=filled["Attendance"].fillna(filled["Attendance"].mean())
print("After replacing numeric missing values with column mean:\n",filled)


#21
print("Q21 - Grouping and Aggregation")

e=pd.DataFrame({
    "Department":["IT","HR","IT","Finance","HR","Finance","IT"],
    "Employee Name":["Amit","Neha","Rahul","Priya","Karan","Sneha","Arnab"],
    "Salary":[55000,48000,72000,61000,45000,66000,60000],
    "Experience":[3,2,7,5,1,6,4]
})
g=e.groupby("Department")["Salary"]
print("Average salary:\n",g.mean())
print("Maximum salary:\n",g.max())
print("Minimum salary:\n",g.min())
print("Number of employees:\n",e.groupby("Department")["Employee Name"].count())


# ================= Part D - Matplotlib =================

#22
print("Q22 - Line Plot")

months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
sales=[25000,27000,30000,28000,32000,35000,38000,36000,40000,42000,45000,50000]
plt.figure(figsize=(9,5))
plt.plot(months,sales,marker="o",color="blue")
plt.title("Monthly Sales of a Company")
plt.xlabel("Month")
plt.ylabel("Sales (Rs.)")
plt.grid(True)
plt.show()


#23
print("Q23 - Bar Chart")

students=["Arnab","Rahul","Priya","Amit","Neha"]
subjects=["Maths","Physics","Chemistry","English","CS"]
marks=[[85,78,82,75,90],[72,68,74,80,70],[90,88,85,92,95],[64,70,60,68,72],[78,82,80,76,85]]
x=np.arange(len(subjects))
w=0.15
plt.figure(figsize=(11,6))
for i,stu in enumerate(students):
    bars=plt.bar(x+i*w,marks[i],w,label=stu)
    for b in bars:
        plt.text(b.get_x()+b.get_width()/2,b.get_height()+1,str(int(b.get_height())),ha="center",fontsize=8)
plt.xticks(x+2*w,subjects)
plt.title("Marks Obtained by Five Students in Five Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()
plt.show()


#24
print("Q24 - Multiple Plots and Subplots")

temp=[15,18,23,28,33,36,32,31,30,27,21,16]
fig,ax=plt.subplots(1,3,figsize=(16,5))
ax[0].plot(months,temp,marker="o",color="red")
ax[0].set_title("Line Plot - Monthly Temperature")
ax[0].set_xlabel("Month")
ax[0].set_ylabel("Temperature (°C)")
ax[1].bar(months,temp,color="orange")
ax[1].set_title("Bar Chart - Monthly Temperature")
ax[1].set_xlabel("Month")
ax[1].set_ylabel("Temperature (°C)")
ax[2].scatter(months,temp,color="green")
ax[2].set_title("Scatter Plot - Temperature Distribution")
ax[2].set_xlabel("Month")
ax[2].set_ylabel("Temperature (°C)")
for a_ in ax:
    a_.tick_params(axis="x",rotation=45)
plt.tight_layout()
plt.show()


#25
print("Q25 - Pandas + NumPy + Matplotlib Data Visualization")

data=pd.DataFrame({
    "Student Name":["Arnab","Rahul","Priya","Amit","Neha","Sourav","Ritika","Karan","Sneha","Vikram"],
    "Mathematics":[85,72,90,64,78,55,88,69,81,93],
    "Physics":[78,68,88,70,82,60,85,65,79,90],
    "Chemistry":[82,74,85,60,80,58,90,72,76,92],
    "Computer Science":[90,70,95,68,84,62,92,75,83,96]
})
subjects=["Mathematics","Physics","Chemistry","Computer Science"]
avg=data[subjects].mean()
print("Average marks of each subject:\n",avg)
data["Total"]=np.sum(data[subjects].values,axis=1)
data["Average"]=np.round(data["Total"]/len(subjects),2)
print(data)

plt.figure(figsize=(8,5))
plt.bar(avg.index,avg.values,color=["#4c72b0","#55a868","#c44e52","#8172b2"],label="Average Marks")
plt.title("Average Marks in Each Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.legend()
plt.grid(axis="y")
plt.show()

plt.figure(figsize=(10,6))
for sub in subjects:
    plt.plot(data["Student Name"],data[sub],marker="o",label=sub)
plt.title("Marks of Individual Students")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8,5))
plt.hist(data["Average"],bins=5,color="teal",edgecolor="black",label="Average Marks")
plt.title("Distribution of Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.legend()
plt.grid(True)
plt.show()
