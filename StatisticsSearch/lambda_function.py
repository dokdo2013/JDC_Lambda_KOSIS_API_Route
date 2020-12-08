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
        "searchNm": "",
        "sort": "", (선택)
        "startCount": "", (선택)
        "resultCount": "", (선택)
        "format": ""
    }
    '''
    
    # GET querystrings
    try:
        searchNm = parameters["searchNm"]
        frmat = parameters["format"]
    except:
        return{
            'statusCode': 400,
            'body': "필수 인자가 전달되어야 합니다."
        }
    else:
        input_params['searchNm'] = searchNm
        input_params['format'] = frmat
    
    if 'sort' in parameters:
        input_params['sort'] = parameters["sort"]
    if 'startCount' in parameters:
        input_params['startCount'] = parameters["startCount"]
    if 'resultCount' in parameters:
        input_params['resultCount'] = parameters["resultCount"]
    
    input_params["apiKey"] = apiKey
    input_params["method"] = "getList"
    try:
        target_url = "http://kosis.kr/openapi/statisticsSearch.do"
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
    