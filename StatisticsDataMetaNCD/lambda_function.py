import json
import requests
import demjson

def lambda_handler(event, context):
    # SET Variables
    statCode = 200
    message = "성공"
    apiKey = ""
    parameters = event["queryStringParameters"]
    input_params = {}
    '''
    parameters = {
        "orgId": "",
        "tblId": "",
        "format": "",
        "prdSe": "" (선택)
    }
    '''
    
    # GET querystrings
    try:
        orgId = parameters["orgId"]
        tblId = parameters["tblId"]
        frmat = parameters["format"]
    except:
        return{
            'statusCode': 400,
            'body': "필수 인자가 전달되어야 합니다."
        }
    else:
        input_params['orgId'] = orgId
        input_params['tblId'] = tblId
        input_params['format'] = frmat
    
    if 'prdSe' in parameters:
        input_params['prdSe'] = parameters["prdSe"]
    
    input_params["apiKey"] = apiKey
    input_params["method"] = "getMeta"
    input_params["type"] = "NCD"
    try:
        target_url = "http://kosis.kr/openapi/statisticsData.do"
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
    