import cv2
from pyzbar.pyzbar import decode

def read_barcodes(frame):
    barcodes = decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_text = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)
        cv2.putText(frame, barcode_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        return barcode_text  # Return the barcode text if detected
    return None  # Return None if no barcode detected

def main():
    # Access the default camera (usually index 0)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting...")
            break
        
        barcode_text = read_barcodes(frame)
        if barcode_text:
            global ide
            ide=barcode_text  # Print the barcode text here
            
            break
        
        cv2.imshow('Barcode Scanner', frame)
        
        if cv2.waitKey(1) == 27:  # Exit when 'Esc' key is pressed
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
    


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
    li=["team Name:",rows[c][0],"Total Members: ",rows[c][1],"table number:",table[c],"regno: ",rows[c][2]]
    l.append(li)
pickle.dump(l,file)
file.close()

filee=open("te.dat","rb")
ll=pickle.load(filee)
for inde in range(len_file):
    
    if ide==ll[inde][7]:
        
        for i in range(len_file):
            print("-------------------")
            if ll[i][7]==ide:
                print(ll[i][0],ll[i][1])
                print(ll[i][2],ll[i][3])
                print(ll[i][4],ll[i][5])
                print(ll[i][6],ll[i][7])
                print("-------------------")
                break
    
    
#ADD JARVIS CODE IN IT.
