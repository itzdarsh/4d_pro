from sys import argv
import json,re
from collections import defaultdict
from operator import getitem

script,input_file = argv

def flatten_command(dictKey):
    for newK in dictKey:
        if(type(dictKey[newK]) is dict):
            flatten_command(dictKey[newK])
        else:
            dictKey[newK]='*'
    return(dictKey)

queryArr=[]
json1={}
entry_fin=defaultdict(int)

for line in open(input_file,'r'):
    try:
        entry = json.loads(line)
    except ValueError as e:  # catches subclass JSONDecodeError
        print(line)
    if ((entry["msg"] == "Slow query") and not(re.search("\$cmd",entry["attr"]["ns"]))):
        if(entry["attr"]["type"] == "command"):
            if ("find" in entry["attr"]["command"]):
                json1=entry["attr"]["command"]['filter']
                entry["attr"]["typeOp"]="find"
            elif("aggregate" in entry["attr"]["command"]):
                json1={'pipeline':{}}
                for i in entry["attr"]["command"]['pipeline']:
                    json1['pipeline'].update(i)
                entry["attr"]["typeOp"]="aggregate"
            elif("distinct" in entry["attr"]["command"]):
                json1=entry["attr"]["command"]['query']
                entry["attr"]["typeOp"]="distinct"
            elif("findAndModify" in entry['attr']["command"]):
                json1=entry["attr"]["command"]['query']
                entry["attr"]["typeOp"]="findAndModify"

            elif("getMore" in entry["attr"]["command"]):
                if ("find" in entry["attr"]["originatingCommand"]):
                    json1=entry["attr"]["originatingCommand"]['filter']
                    entry["attr"]["typeOp"]="getMoreFind"
                elif("aggregate" in entry["attr"]["originatingCommand"] ):
                    json1={'pipeline':{}}
                    for i in entry["attr"]["originatingCommand"]['pipeline']:
                        json1['pipeline'].update(i)
                    entry["attr"]["typeOp"]="getMoreAggr"
            else:
                continue
               
        elif(entry["attr"]["type"] == "update" ):
            json1=entry["attr"]["command"]
            entry["attr"]["typeOp"]="update"
        elif(entry["attr"]["type"] == "remove"):
            json1=entry["attr"]["command"]
            entry["attr"]["typeOp"]="remove"
        else:
            continue
        for key in json1:
            if(type(json1[key]) is dict):
                flatten_command(json1[key])
            else:
                json1[key]="1"

        #entry['surprise']=json1

        if not json1 in queryArr or entry_fin[str(json1)] is 0:
            entry_fin[str(json1)]= {'count':1}
            entry_fin[str(json1)].update({'ns':entry['attr']['ns'],'typeOp':entry["attr"]["typeOp"],'minTime':entry['attr']['durationMillis'],'totalTime':entry['attr']['durationMillis'],'maxTime':entry['attr']['durationMillis']})
            queryArr.append(json1)
        else:
            entry_fin[str(json1)]['count']+= 1
            if (entry['attr']['durationMillis'] > entry_fin[str(json1)]['maxTime'] ):
                entry_fin[str(json1)]['maxTime'] = entry['attr']['durationMillis']
                entry_fin[str(json1)]['totalTime'] += entry['attr']['durationMillis']
            elif (entry['attr']['durationMillis'] < entry_fin[str(json1)]['minTime']):
                entry_fin[str(json1)]['minTime'] = entry['attr']['durationMillis'] 
                entry_fin[str(json1)]['totalTime'] += entry['attr']['durationMillis']
            else:
                entry_fin[str(json1)]['totalTime'] += entry['attr']['durationMillis']        

sort_key=input("Please enter sort key: \n1. minTime\n2. maxTime\n3. count\n4. Namespace\n5. Operation\n") or 3
while(int(sort_key) not in range(1,6)):
    print("please enter 1 to 5\n")
    sort_key=input("Please enter sort key: \n1. minTime\n2. maxTime\n3. count\n4. Namespace\n5. Operation\n") or 3
sa=[0,"minTime","maxTime","count","ns","typeOp"]

print("{:80} {:15} {:100} {:6} {:10} {:8} {:8}".format("Namespace","Operation","Pattern","Count","totalTime(ms)","minTime(ms)","maxTime(ms)"))
for key, val in sorted(entry_fin.items(), key = lambda x: getitem(x[1],sa[int(sort_key)]),reverse=True):
    print("{:80} {:15} {:100} {:6} {:10} {:8} {:8}".format(val['ns'],val['typeOp'],key,val['count'],val['totalTime'],val['minTime'],val['maxTime']))
