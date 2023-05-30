import pandas as pd
data = pd.read_csv("feedback.csv")

def getfeedback(student):
    data = pd.read_csv("feedback.csv")
    fb = data[data["Student Name"]==student].iloc[0]["Feedback"] 
    return fb
     
if __name__=="__main__":
    fb = getfeedback("Agarwal, Shrey")
    print(fb)
