import PyPDF2 as pd
import os

merger = pd.PdfFileMerger()

list1 = []

i= 1

for items in os.listdir():
    if items.endswith('.pdf'):
        list1.append(items)
        print(i,"-",items)
        i=i+1


def number():
    n = list(map(int,input("Serial number of pdf separated by space and in proper sequence").split()))
    print(n)
    for i in n:
        try:
            e= list1[i-1]
            merger.append(e)
        except:
            print("Please enter a number in range.")
            number()

number()


merger.write("Final.pdf")
merger.close()
