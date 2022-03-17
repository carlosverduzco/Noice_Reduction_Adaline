from tkinter.filedialog import askopenfilename
import csv

def getX():
    X = []
    try:
        file = askopenfilename()
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                X.append(float(row['X']))
    except:
        X = []
    return X
