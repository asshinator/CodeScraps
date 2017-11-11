import json
from pprint import pprint

def filter_depth(jsn,depth:int):
    if depth == 0:
        if type(jsn) is not list and type(jsn) is not dict:
            return jsn
        else:
            return ""
    elif type(jsn) is list:
        ret = []
        for item in jsn:
            ret += [filter_depth(item,depth-1)]
        return ret
    elif type(jsn) is dict:
        ret = {}
        for item in jsn:
            ret[filter_depth(item,depth-1)]=filter_depth(jsn[item],depth-1)
        return ret
    else:
        return jsn
    
    if jsn.has_key('children'):
        return 1 +  ([0] + map(depth, jsn['children']))
    else:
        return 1

def main():
    fileName ='C:\Personal\Courses\wharton-entrepreneurship-opportunity-syllabus-parsed.json' 
    with open(fileName) as data_file:    
        data = json.load(data_file)
    pprint(filter_depth(data,6))

    
if __name__ == "__main__":
    if 'isNullRun' in globals():
        True
    else:
        main()
    