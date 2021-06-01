import csv
from collections import Counter
with open('./data.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    file_data.pop(0)
    new_data = []
    for i in range (len(file_data)):
        n_num = file_data[i][2]
        new_data.append(float(n_num))
n = len(new_data)
total_num = 0
for j in new_data:
    total_num+=j
mean = total_num/n
print("Mean : "+str(mean))
median_data=new_data
median_data.sort()
if n % 2 == 0:
    median1 = float(median_data[n//2])
    median2 = float(median_data[n//2-1])
    median = (median1+median2)/2
else : 
    median = median_data[n//2]
print("Median : "+str(median))
mode_data = Counter(new_data)
mode_data_for_range = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
}
for height,mode_occurrence in mode_data.items():
    if 75 < float(height) < 85 :
        mode_data_for_range["75-85"]+=mode_occurrence
    elif 85 < float(height) < 95 :
        mode_data_for_range["85-95"]+=mode_occurrence
    elif 95 < float(height) < 105 :
        mode_data_for_range["95-105"]+=mode_occurrence
    elif 105 < float(height) < 115 :
        mode_data_for_range["105-115"]+=mode_occurrence
    elif 115 < float(height) < 125 :
        mode_data_for_range["115-125"]+=mode_occurrence
    elif 125 < float(height) < 135 :
        mode_data_for_range["125-135"]+=mode_occurrence
    elif 135 < float(height) < 145 :
        mode_data_for_range["135-145"]+=mode_occurrence
    elif 145 < float(height) < 155 :
        mode_data_for_range["145-155"]+=mode_occurrence
    elif 155 < float(height) < 165 :
        mode_data_for_range["155-165"]+=mode_occurrence
    elif 165 < float(height) < 175 :
        mode_data_for_range["165-175"]+=mode_occurrence
mode_range , mode_mode_occurrence = 0,0
for range,mode_occurrence in mode_data_for_range.items():
    if mode_occurrence > mode_mode_occurrence :
        mode_range,mode_mode_occurrence = [int(range.split("-")[0]),int(range.split("-")[1])],mode_occurrence
mode = float ((mode_range[0]+mode_range[1])/2)
print(f"Mode is {mode:2f}")