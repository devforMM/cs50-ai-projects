import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
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


    return(labels[1:],evidence[1:])


def train_model(evidence, labels):
    model=KNeighborsClassifier(n=1)
    model.fit(evidence,labels)
    raise NotImplementedError


def evaluate(labels, predictions):
    sensivity=0
    specifity=0
    for i in range(len(labels)):
         if labels[i]==predictions[i]:
             sensivity+=1
         else:
             specifity+=1
    return((sensivity/len(labels),specifity/len(labels)))


if __name__ == "__main__":
    main()
