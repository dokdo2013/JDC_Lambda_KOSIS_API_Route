import json
import requests
import demjson

def lambda_handler(event, context):
    #return event
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
        "orgId": "",
        "tblId": "",
        "metaItm": ""
    }
    '''
    
    # GET querystrings
    try:
        orgId = parameters["orgId"]
        tblId = parameters["tblId"]
        metaItm = parameters["metaItm"]
        frmat = parameters["format"]
    except:
        return{
            'statusCode': 400,
            'body': "필수 인자가 전달되어야 합니다."
        }
    else:
        input_params['orgId'] = orgId
        input_params['tblId'] = tblId
        input_params['metaItm'] = metaItm
        input_params['format'] = frmat
    
    
    input_params["apiKey"] = apiKey
    input_params["method"] = "getList"
    try:
        target_url = "http://kosis.kr/openapi/statisticsExplData.do"
        res = requests.get(target_url, params = input_params)
        ans = res.text
        ans = demjson.decode(ans)
    except:
        return{
            'statusCode': 400,
            'body': "KOSIS API가 응답하지 않습니다."
        }
    # return
    return {
        'statusCode': statCode,
        'body': json.dumps(ans)
    }
    