# JDC_Lambda_KOSIS_API_Route
JDC KOSIS API Route using AWS Lambda &amp; API Gateway @ JOBMAP

통계청 Open API를 간편하게 호출해서 사용할 수 있도록 제작한 API.

특수한 기능은 없고 단순히 apiKey와 파라미터로 받은 값을 실어서 통계청 API로 request를 보내고 받아서 출력해주는 소스이다. 통계청 API의 경우 return받는 json의 키값에 쌍따옴표(") 처리가 되어있지 않아 일부 환경에서 제대로 인식하지 못하는 문제가 있었다. 이를 파이썬의 demjson 모듈로 json decode한 후 API 응답을 해준다.

본 파이썬 코드는 AWS Lambda에 올려서 구동되며, API Gateway로 REST API 요청을 받아 처리한다.

실서비스에 활용할 용도로 제작된 코드라 apiKey와 api주소는 공개하지 않는다.
