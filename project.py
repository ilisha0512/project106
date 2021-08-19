import plotly.express as px
import csv
import numpy as np
def getdatasource(datapath):
    marksinpercentage = []
    dayspresent = []
    with open(datapath) as f:
        csvreader = csv.DictReader(f)
        for i in csvreader:
            dayspresent.append(float(i["Days Present"]))
            marksinpercentage.append(float(i["Marks In Percentage"]))
    return {"x": dayspresent, "y": marksinpercentage}
def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource ["y"])
    print("correlation is ", correlation[0, 1])
def setup():
    datapath = "Student Marks vs Days Present_Project.csv"
    datasource = getdatasource(datapath)
    findcorrelation(datasource)
setup()