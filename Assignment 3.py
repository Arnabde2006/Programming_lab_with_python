#1
print("Q1")

a1=[10,20,29,87,66,99,77,98,90,56]
print("the max no of student is ", max(a1))
print("the min no of student is ", min(a1))
print("the total no of student is ", sum(a1))
print("the avg no of student is ", ((sum(a1))/10))

#2
print("Q2")

a2=["Rice", "Milk","Bread","Egg","Butter"]
a2.append("Orange_Juice")
a2.remove("Rice")
print(a2)


#3
print("Q3")
a3=[34,11,50,33,45,75,63]
day=["Monday","Tuesday","Wednesday", "Thursday","Friday","Saturday","Sunday"]
ht=max(a3)
lt=min(a3)
hd=day[a3.index(ht)]
ld=day[a3.index(lt)]
print(f"Maximum Temp is {ht} which was recorded on {hd}")
print(f"Minimum Temp is {lt} which was recorded on {ld}" )


#4
print("Q4")

roll=[23,54,23,45,67]
u_roll=list(set(roll))
print(u_roll)


#5
print("Q5")

list34=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
odds=[]
evens=[]
for num in list34:
    if num%2==0:
        evens.append(num)
    else:
        odds.append(num)
print(f"Even list is {evens} \n and \nodd is {odds}")


#6
print("Q6")

stud=[["studentram", 63, 64 ,96 ],["ramana",85,75,15],["anshui",86,69,72],["anshuvi",69,96,67]]
for i in stud:
    name=i[0]
    total=sum(i[1:])
    print(f"\nName of student {name}, and total is {total}")


#7
print("Q7")
num67=[23,25,64,75,69]
sl=max(set(num67)- {max(num67)})
print("The 2nd largest number is ",sl)


#8
print("Q8")

listu=[10,20,30,40]
rotated = listu[-1:]+listu[:-1]
print(rotated)



#9
print("Q9")

a1=(10,20,29,87,66,99,77,98,90,56)
print("the max no of student is ", max(a1))
print("the min no of student is ", min(a1))
print("the total no of student is ", sum(a1))
print("the avg no of student is ", ((sum(a1))/10))


#10
print("Q10")

import math
p1=(float(input("Enter x1:")),float(input("Enter y1:")))
p2=(float(input("Enter x2:")),float(input("Enter y2:")))
distance=math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
print(f"Distance between two points is {distance:.2f}")

#11
print("Q11")
emp=(1001,"Andu","CEO",6245987)
print(f"EMP id {emp[0]}, name {emp[1]}, dep {emp[2]}, salary {emp[3]}")


#12
print("Q12")
a56=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
read = int(input("enter the no "))

if read in a56:
    print("In tuple")
else:
    print("Not present")


#13
print("Q13")

s56=(1,2,3,4,5,6,7,8,9,10)
print("max no is: ",max(s56),"\nmin no is: ",min(s56),"\navg no is: ",(sum(s56)/10),"\ntotal no is: ",sum(s56))



#14
print("Q14")

book= (" jadu","Ashu",600 ),("meloni","Asu",900 ),("kie","Ahu",200 ),("loninau","shu",100),("gytygh","ghf",700)

for title,author,price in book:
    print(f"Title:{title} | Author:{author}| price:{price} "  )


#15
print("Q15")
stu={"Andh":85,"Bishal":90,"Campak": 80}
hs=max(stu, key=stu.get)
print(f"Highest marks of student:{hs} {stu[hs]}")


#16
print("Q16")
con={"Andh":8000000005,"Bishal":9000000000,"Campak": 8000000000,"Adh":8000040005,"Bial":9070000000}
name=input("Name do:")
print("phone:",con.get(name,"Not found"))



#17
print("Q17")
pro={"Apple":85,"musabi":90,"cucumber": 85,"Adhi":85,"Bial":97}
pro["egg"]=40
pro["Apple"]=60
pro.pop("musabi", None)
print("Updated inventory\n",pro)


#18
print("Q18")
sentance=input("Enter sentance:")
word=sentance.split()
freq={}
for wod in word:
    freq[wod]=freq.get(wod,0)+1
print("Word Frequency",freq)



#19
print("Q19")
text=input("String :")
fre={}
for char in text:
    fre[char]=fre.get(char,0)+1
print("Character Frequency", fre)


#20
print("Q20")
emp1= {" jaduAshu":600 ,"meloniAsu":900 ,"kieAhu":200,"lonishu":100}
avg78=sum(emp1.values())/len(emp1)
print("Average sal", avg78)
print("Emp earning more than avg")
for name,sal in emp1.items():
    if sal>avg78:
        print(f"{name} and {sal}")


#21
print("Q21")
studwe={"Math":85,"pyhton":95, "DBMS":78, "CN":88}
toal=sum(studwe.values())
avg76= toal/4
if avg76>=90: grade="Distinction"
elif avg76>=75:grade="1st class"
elif avg76>=40:grade="Pass"
else:grade="fail"
print(f"Total:{toal}, Average : {avg76}, Grade:{grade}")

#22
print("Q22")

stud96={"Anshu":99, "Arnab":86, "Akita":54, "Jano":27}
for name,marks in stud96.items():
        if marks>=90:result="Distinction"
        elif marks>=75:result="1st class"
        elif marks>=40:result="Pass"
        else:result="fail"
        print(f"Name:{name} and Result:{result}")
