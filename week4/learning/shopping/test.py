import csv
from sklearn.neighbors import KNeighborsClassifier

def convert_month(month):
    months = {
        "jan": 1, "feb": 2, "mars": 3, "apr": 4, "may": 5, "jun": 6,
        "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12
    }
    return months[month]
rows=[]
evidence=[]
labels=[]
with open("./test.csv",mode="r",encoding="utf-8") as file:
    reader=csv.reader(file)
    for row in reader:
        rows.append(row)
    titres=rows[0]
    for row in reader:
        
        for t in titres:
            if t in ["Administrative", "Informational", "ProductRelated", "Month", 
         "OperatingSystems", "Browser", "Region", "TrafficType", "VisitorType", "Weekend"]:
                int(row[t])

            elif t in ["Administrative_Duration", "Informational_Duration", "ProductRelated_Duration", 
           "BounceRates", "ExitRates", "PageValues", "SpecialDay"]:
                float(row[t])  # J'imagine que ces valeurs sont des nombres décimaux ?

            elif t=="MOnth":
                row[t]=convert_month(row[t])
            elif t=="VisitorType":
                if row[t]=="returning":
                    row[t]==1
                else:
                    row[t]==0
            elif t=="weekned":
                if row[t]=="weekend":
                    row[t]=1
                else:
                    row[t]=0    
        if row[-1]=='TRUE':
            labels.append(1)
        elif row[-1]=="FALSE":
            labels.append(0)
    evidence.append(row)

labels=labels[1:]
evidence=evidence[1:]

        



def evaluate(labels,predictions):
     sensivity=0
     specifity=0
     for i in range(len(labels)):
         if labels[i]==predictions[i]:
             sensivity+=1
         else:
             specifity+=1
     return((sensivity/len(labels),specifity/len(labels)))
 
     

def train_model(evidence,labels):
    model=KNeighborsClassifier(n=1)
    model.fit(evidence,labels)