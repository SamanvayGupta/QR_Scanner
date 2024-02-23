import csv
r=open("Testing.csv","r")
re=csv.reader(r)
ro1 = []
for row in re:
    ro1.append(row)
r.close()
rows=[]
for li in ro1:
    if li!=[]:
        rows.append(li)
    else:
        continue
len_file=len(rows)
print(rows)

# upper is for csv file reading

#lower is for taking the lenght of 
l=[]
for i in range(1,len_file+1):
    l.append(i)
table=[]
try:
    import random
    for j in reversed(range(1,len_file+1)):
        count=random.randrange(1,j+1)

        if len(l)>count:
            b=l.pop(count)
    
            table.append(b)
        else:
            count-=1
            b=l.pop(count)
        
            table.append(b)
except:
    print("DONE")
import pickle

file=open("te.dat","wb")
l=[]
ele=["TEAM_NAME","TEAM_TABLE","TEAM_MEMBERS"]
for c in range(0,len_file):
    li=["team Name:",rows[c][0],"Total Members: ",rows[c][1],"table number:",table[c]]
    l.append(li)
pickle.dump(l,file)

file.close()
filee=open("te.dat","rb")
ll=pickle.load(filee)
while True:
    print("-------------------")
    a=input("Enter: ")
    if a=="n" or a=="N":
        break
    else:
        for x in ll:
            if x[1]==a:
                print(x[0],x[1])
                print(x[2],x[3])
                print(x[4],x[5])
                print("-------------------")
                break
            else:
                continue
#ADD JARVIS CODE IN IT.