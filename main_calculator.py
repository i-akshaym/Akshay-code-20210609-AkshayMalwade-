import json

data = '''[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
"HeightCm": 167, "WeightKg": 82}]
'''

class BMI_index:
    def __init__(self,gender,height,weight):
        self.h = height
        self.w = weight
        self.g = gender

    def Calculate(self):
        ret = self.w /((self.h/100)**2)
        self.ret = ret 
        return ret 

    def Category(self,dict1):
        for i,j in dict1.items():
            if j < 18.4:
                dictCAT.update({"BMI Category":"Underwight","Health Risk":"Malnutrition risk"})
            elif j > 18.5 and j <24.9:
                dictCAT.update({"BMI Category":"normal","Health Risk":"Low risk"})
            elif j > 25 and j <29.9:
                dictCAT.update({"BMI Category":"Overweight","Health Risk":"Enhanced risk"})
            elif j > 30 and j <34.9:
                dictCAT.update({"BMI Category":"Moderately obese","Health Risk":"Medium risk"})
            elif j > 30 and j <34.9:
                dictCAT.update({"BMI Category":"Severely obese","Health Risk":"High risk"})
            elif j > 30 and j <34.9:
                dictCAT.update({"BMI Category":"Very Severely obese","Health Risk":"Very High risk"})
            
            return(dictCAT)
    
    def merge(self,d1,d2):
        res = {**d1,**d2}
        return res
    
obj = json.loads(data)

dict1 = dict()
dictCAT = dict()

for i in range(len(obj)):
    
    gen=(obj[i].get("Gender"))
    heightt=(obj[i].get("HeightCm"))
    weightt=(obj[i].get("WeightKg"))
    bobj = BMI_index(gen,heightt,weightt)
    res = bobj.Calculate()   #Calculating the BMI index 
    
    dict1['BMI'] = res
    bobj.Category(dict1)
    
    dictADD = bobj.merge(dict1,dictCAT)
        
    finalDict={}
    for j in (obj[i],dictADD):
        finalDict.update(j)
    print (finalDict)

#count of Overweight people in list
arr = []
for f in finalDict.values():
    if f == 'Overweight':
        arr.append(f)
print("The Count of Overweight people",len(arr))
    
