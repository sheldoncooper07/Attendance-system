#id= int(input('Enter your id:'))
id=0
from sklearn import metrics
from sklearn.metrics import confusion_matrix

while(True):

    l=len(pred)
    test=[]
    i=0
    for i in range(l):
        test.append(id)
        i+=1
    len(test)
    # lst = []
    cm=confusion_matrix(test,pred)
    if(metrics.accuracy_score(test,pred)>.5):
        print("accuracy",metrics.accuracy_score(test,pred))
        print(id)
        # lst.append(id)
        break
    else:
        id+=1

# print(lst)
#print("confusion_matrix- ",cm)