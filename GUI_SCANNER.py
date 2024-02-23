import cv2
from pyzbar.pyzbar import decode
import tkinter as tk
from PIL import Image, ImageTk
import pickle

def read_barcodes(frame):
    barcodes = decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_text = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)
        cv2.putText(frame, barcode_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        return barcode_text  # Return the barcode text if detected
    return None  # Return None if no barcode detected

def scan_barcodes():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting...")
            break
        
        barcode_text = read_barcodes(frame)
        if barcode_text:
            ide.set(barcode_text)  # Set the value of the barcode_text to ide
            break
        
        cv2.imshow('Barcode Scanner', frame)
        
        if cv2.waitKey(1) == 27:  # Exit when 'Esc' key is pressed
            break

    cap.release()
    cv2.destroyAllWindows()

def search_in_file():
    barcode_text = ide.get()
    with open("te.dat", "rb") as filee:
        ll = pickle.load(filee)
        for item in ll:
            if barcode_text == item[7]:
                team_info.set(f"Team Name: {item[1]}, Total Members: {item[3]}, Table Number: {item[5]}, Reg No: {item[7]}")
                break
        else:
            team_info.set("Team not found!")

# Create Tkinter window
root = tk.Tk()
root.title("Barcode Scanner")

# Create Tkinter variables
ide = tk.StringVar()
team_info = tk.StringVar()

# Create GUI elements
label = tk.Label(root, text="Scan Barcode:")
label.pack()

entry = tk.Entry(root, textvariable=ide)
entry.pack()

scan_button = tk.Button(root, text="Scan", command=scan_barcodes)
scan_button.pack()

search_button = tk.Button(root, text="Search", command=search_in_file)
search_button.pack()

info_label = tk.Label(root, textvariable=team_info)
info_label.pack()

root.mainloop()
