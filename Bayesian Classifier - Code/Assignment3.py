__author__ = 'Pramod'
#!/usr/bin/python
import sys
import itertools
import copy

#Solution to First Problem
def problemOne(symptomTrueFalseList, diseaseDict):
    #This method takes Symptoms true or false list and disease dictionary containing all the data corresponding to one disease
    num = 1
    den = 1
    innerList = []
    patientDict = {}
    for i in range(0,len(symptomTrueFalseList)):
        #innerList = listOfDiseases[sysCount]
        innerList = diseaseDict
        print "****innerList****",innerList
        if symptomTrueFalseList[i] == 'T':
            num = num * float(innerList['probabilityOfDiseaseMapped'][i])
            den = den * float(innerList['notProbabilityOfDiseaseMapped'][i])
        if symptomTrueFalseList[i] == 'F':
            num = num * (1 - float(innerList['probabilityOfDiseaseMapped'][i]))
            den = den * (1 - float(innerList['notProbabilityOfDiseaseMapped'][i]))
        #sysCount = sysCount +1

    num = num * float(innerList['probabilityofdisease'])
    den = den * (1 - float(innerList['probabilityofdisease']))
    result = num/(num+den)
    #print "result:", result
    patientDict[innerList['diseaseName']] = format(result, '.4f')
    print "patientDict", patientDict
    return patientDict

#Solution to Second Problem
def problemTwo(symptomTrueFalseList, diseaseDict):
    #This method takes Symptoms true or false list and disease dictionary containing all the data corresponding to one disease
    dictMaxMinMain = {}
    dictionaryMaxMinForDiesease = {}
    dictMaxMin = {}
    minMaxList = []
    #var = symptomTrueList
    symptomTrueList2 = []
    symptomTrueList2 = copy.deepcopy(symptomTrueFalseList)
    tupleList = []
    print symptomTrueList2
    countVal = symptomTrueFalseList.count('U')
    for i in itertools.product(['T','F'],repeat=countVal):
        tupleList.append(i)

    tupleCounter = 0
    listCounter = 0


    while(listCounter<len(tupleList)):
        for n,i in enumerate(symptomTrueList2):
            if i == 'U':
                symptomTrueList2[n] = tupleList[listCounter][tupleCounter]
                tupleCounter = tupleCounter+1
        print "diseaseDict", diseaseDict
        dictMaxMin = problemOne(symptomTrueList2, diseaseDict)
        var5 = dictMaxMin.values()
        minMaxList.append(var5[0])

        symptomTrueList2 = copy.deepcopy(symptomTrueFalseList)
        listCounter=listCounter+1
        tupleCounter = 0
    finalMinMaxList = []
    finalMinMaxList.append(min(minMaxList))
    finalMinMaxList.append(max(minMaxList))
    print "finalMinMaxList", finalMinMaxList
    dictionaryMaxMinForDiesease[str(dictMaxMin.keys()[0])]=finalMinMaxList
    print  dictionaryMaxMinForDiesease
    return dictionaryMaxMinForDiesease

#solution to Third Problem
#def problemThree(diseaseName, diseaseSymptoms, symptomTrueList):
def problemThree(symptomTrueFalseList, diseaseDict):
    #This method takes Symptoms true or false list and disease dictionary containing all the data corresponding to one disease
    #print "symptomTrueList", symptomTrueList
    #print "diseaseName", diseaseDict['diseaseName']
    #print "diseaseSymptoms", diseaseDict['symptoms']
    diseaseName = diseaseDict['diseaseName']
    diseaseSymp = diseaseDict['symptoms']
    originalValue = problemOne(symptomTrueFalseList,diseaseDict)
    originalValue1 = originalValue.values()
    originalValue11 = originalValue1[0]
    d1 ={}
    d2 ={}
    symptom2TrueList = []
    for i in range(len(symptomTrueFalseList)):
        symptom2TrueList = copy.deepcopy(symptomTrueFalseList)
        if symptom2TrueList[i] == 'U':
            symptom2TrueList[i] = 'T'
            res1 = problemOne(symptom2TrueList, diseaseDict)
            varKey1 = diseaseSymp[i]
            varValue1 = res1.values()
            d1[str([varKey1, 'T'])] = varValue1[0]
            symptom2TrueList[i] = 'F'
            res2 = problemOne(symptom2TrueList, diseaseDict)
            varKey2 = diseaseSymp[i]
            varValue2 = res2.values()
            d1[str([varKey2, 'F'])] = varValue2[0]
    d3 = []
    if len(d1)>0:

        minimum = min(d1, key=d1.get)
        maximum = max(d1, key=d1.get)
        if d1[maximum] > originalValue11:
            d3 = eval(maximum)
        else:
            d3 = ['none', 'N']
        if d1[minimum] < originalValue11:
            d3 += eval(minimum)
        else:
            d3 += ['none', 'N']
        #d3 = eval(maximum) + eval(minimum)
        #d2[diseaseName] = eval(maximum)
        #d2[diseaseName] = eval(minimum)
        print "d3",d3
    else:
        d3 = ['none', 'N','none', 'N']
    return {diseaseName : d3}

# Main Block of Code
filename = sys.argv[2]
fileobjectOpen = open(filename, "r")
#fileobjectWrite = open("sample_input_inference.txt", "w")
lines = fileobjectOpen.read().split('\n') #lines is a list
firstElement = lines[0].split(' ')
numberOfDiseases = eval(firstElement[0])
numberOfPatients = eval(firstElement[1])
numberOfLinesOfDiseases = int(numberOfDiseases) * 4
listOfDiseases = []
"""print "lines:", lines
print "firstElement:", firstElement
print "numberOfDiseases:", numberOfDiseases
print "numberOfPatients:", numberOfPatients
print "numberOfLinesOfDiseases:", numberOfLinesOfDiseases"""
lineNumber = 4
for number in range(1,numberOfLinesOfDiseases+1, lineNumber):
    resultDictionary  = {}
    probabilityDictionary1 = {}
    probabilityDictionary2 = {}
    lineInside = lines[number].split(' ') #First 20 lines after the first line
    var1 = eval(lines[number+1])
    var2 = eval(lines[number+2])
    var3 = eval(lines[number+3])
    diseaseName = lineInside[0]
    diseaseSymptoms = lineInside[1]
    diseaseProbability = lineInside[2]

    """for index in range(int(diseaseSymptoms)):
        resultDictionary[index] = [var2[index],var3[index],1-var2[index],1-var3[index]]
        print "!!!!resultDictionary!!!!", resultDictionary"""

    for index in range(int(diseaseSymptoms)):
        probabilityDictionary1[index] = var2[index]
        #print "!!!!probabilityDictionary1!!!!", probabilityDictionary1

    for index in range(int(diseaseSymptoms)):
        probabilityDictionary2[index] = var3[index]
        #print "!!!!probabilityDictionary2!!!!", probabilityDictionary2

    resultDictionary["diseaseName"] = diseaseName
    resultDictionary["symptoms"] = var1
    resultDictionary["probabilityofdisease"] = diseaseProbability
    resultDictionary["probabilityOfDiseaseMapped"] = probabilityDictionary1
    resultDictionary["notProbabilityOfDiseaseMapped"] = probabilityDictionary2
    listOfDiseases.append(resultDictionary)

""" print "lineInside:", lineInside
    print "diseaseName:", diseaseName
    print "diseaseSymptoms:", diseaseSymptoms
    print "diseaseProbability:", diseaseProbability
    print "var1:", var1
    print "var2:", var2
    print "var3:", var3 """

print "***listOfDiseases***", listOfDiseases
patientLineStarts = numberOfLinesOfDiseases+1
patientCount = 0
filename1 = filename.split(".")
filename2 = filename1[0]
suffix = "_inference.txt"
outputFileName = filename2+suffix
print "*****outputFileName******", outputFileName
filehandler=open(outputFileName,'w')
patientDictMinMax = {} #Second Problem
patientDictMinMaxUnknown = {} #Third Problem

#sysCount = 0
"""patientDict1 = {}
patientDictMinMax = {}
patientDictMinMaxUnknown = {}
patient_starting_line = linecount
global count
handler=open('output','w')"""
#for patientNumber in range(0, numberOfPatients):

while(patientCount < numberOfPatients):
    count = 0     #First program
    systemCount = 0  #First program
    symptomTrueOrFalseList = []  #First program
    patientDictMinMaxList = []   #Second Program
    patientDictMinMaxUnknownList = []
    patientList = {}
    mainDict = {}
    mainDictMinMax = {}
    mainDictMinMaxUnknown = {}
    patientSecondList = {}
    patientThirdList = {}

    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    #for countOfDiseases in range (0, numberOfDiseases):
    while(count < numberOfDiseases):
         symptomTrueOrFalseList = eval(lines[patientLineStarts])
         print "**symptomTrueOrFalseList**", symptomTrueOrFalseList

         #************Related to First problem************
         diseaseDict = listOfDiseases[systemCount]
         firstProblemSolution = problemOne(symptomTrueOrFalseList, diseaseDict)
         print firstProblemSolution
         key1 = firstProblemSolution.keys()
         value1 = firstProblemSolution.values()
         print "key1",key1[0]
         print "value1",value1[0]
         list1.append(key1[0])
         list2.append(value1[0])
         patientList = dict(zip(list1, list2)) #actual solution (for 1 patient)
         print "*patientList*", patientList

         #*********************Related to Second Problem********************
         patientDictionaryMinMaxProb = problemTwo(symptomTrueOrFalseList,diseaseDict)
         print "patientDictionaryMinMaxProb", patientDictionaryMinMaxProb
         key2 = patientDictionaryMinMaxProb.keys()
         value2 = patientDictionaryMinMaxProb.values()
         list3.append(key2[0])
         list4.append(value2[0])
         patientSecondList = dict(zip(list3,list4))
         print "patientSecondList", patientSecondList

         #*********************Related to Third Problem********************
         #patientDictMinMaxUnknown = problemThree(listOfDiseases[count]['diseaseName'],listOfDiseases[count]['symptoms'],symptomTrueOrFalseList)
         patientDictMinMaxUnknown = problemThree(symptomTrueOrFalseList, diseaseDict)
         print "*patientDictMinMaxUnknown*", patientDictMinMaxUnknown
         key3 = patientDictMinMaxUnknown.keys()
         value3 = patientDictMinMaxUnknown.values()
         list5.append(key3[0])
         list6.append(value3[0])
         patientThirdList = dict(zip(list5, list6))
         print patientThirdList

         patientLineStarts = patientLineStarts + 1
         count = count+1
         systemCount = systemCount+1
         print "patientLineStarts", patientLineStarts


    filehandler.write("Patient-"+str(patientCount+1)+":\n")
    filehandler.write(str(patientList) + "\n")
    filehandler.write(str(patientSecondList) + "\n")
    filehandler.write(str(patientThirdList)+ "\n")
    patientCount=patientCount+1
print outputFileName
filehandler.close()
fileobjectOpen.close()

