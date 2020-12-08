import json
#import requests

def lambda_handler(event, context):
    return event
    # SET Variables
    statCode = 200
    message = "성공"
    apiKey = ""
    parameters = event["queryStringParameters"]
    input_params = {}
    input_params["apiKey"] = apiKey
    input_params["method"] = "getList"
    '''
    parameters = {
        "orgId" : "101",
        "tblId" : "DT_1YL20631",
        "objL1" : "11010",
        "itmId" : "T10",
        "loadGubun" : "1",
        "prdSe" : "Y",
        "format" : "json",
        "newEstPrdCnt" : "1000"
    }
    '''
    
    # GET querystrings
    try:
        orgId = parameters["orgId"]
        tblId = parameters["tblId"]
        objL1 = parameters["objL1"]
        itmId = parameters["itmId"]
        loadGubun = parameters["loadGubun"]
        prdSe = parameters["prdSe"]
        frmat = parameters["format"]
    except:
        statCode = 400
        message = "필수 인자가 전달되어야 합니다."
    else:
        input_params['orgId'] = orgId
        input_params['tblId'] = tblId
        input_params['objL1'] = objL1
        input_params['itmId'] = itmId
        input_params['loadGubun'] = loadGubun
        input_params['prdSe'] = prdSe
        input_params['format'] = frmat
    
    objNumbers = 1
    
    if 'objL2' in parameters:
        input_params["objL2"] = objL2 = parameters["objL2"]
        objNumbers += 1
    if 'objL3' in parameters:
        input_params["objL3"] = objL3 = parameters["objL3"]
        objNumbers += 1
    if 'objL4' in parameters:
        input_params["objL4"] = objL4 = parameters["objL4"]
        objNumbers += 1
    if 'objL5' in parameters:
        input_params["objL5"] = objL5 = parameters["objL5"]
        objNumbers += 1
    if 'objL6' in parameters:
        input_params["objL6"] = objL6 = parameters["objL6"]
        objNumbers += 1
    if 'objL7' in parameters:
        input_params["objL7"] = objL7 = parameters["objL7"]
        objNumbers += 1
    if 'objL8' in parameters:
        input_params["objL8"] = objL8 = parameters["objL8"]
        objNumbers += 1
    
    prdType = 0
    
    if 'startPrdDe' in parameters:
        if 'endPrdDe' in parameters:
            prdType = 1
            input_params["startPrdDe"] = parameters["startPrdDe"]
            input_params["endPrdDe"] = parameters["endPrdDe"]
    elif 'newEstPrdCnt' in parameters:
        if 'prdInterval' in parameters:
            prdType = 2
            input_params["newEstPrdCnt"] = parameters["newEstPrdCnt"]
            input_params["prdInterval"] = parameters["prdInterval"]
        else:
            prdType = 2
            input_params["newEstPrdCnt"] = parameters["newEstPrdCnt"]
    if prdType == 0:
        prdType = 2
        input_params["newEstPrdCnt"] = 100000
    input_params["apiKey"] = apiKey
    input_params["method"] = "getList"
    try:
        target_url = "http://kosis.kr/openapi/Param/statisticsParameterData.do"
        res = requests.get(target_url, params = input_params)
        ans = res.text
    except:
        statCode = 400
        message = "KOSIS API가 응답하지 않습니다."
    # return
    return {
        'statusCode': statCode,
        'message': message,
        'body': json.dumps(event)
    }