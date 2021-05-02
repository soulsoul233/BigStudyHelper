import json
import requests
from configparser import ConfigParser

def main():
    config = ConfigParser()
    config.read("setting.config", encoding="UTF-8")
    name = config['JXUFE']['name']
    url = config['JXUFE']['url']
    userID = url.split("userId")[1].split("name")[0][1:-1]
    headers = {'Host': 'onestop.jxufe.edu.cn', 'Connection': 'keep-alive', 'Accept': 'application/json, text/plain, */*',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66',
                'Content-Type': 'application/json;charset=UTF-8', 'Origin': 'http://onestop.jxufe.edu.cn',
                'Referer': "http://onestop.jxufe.edu.cn/eos/wx/youthStudy/studyList.jsp?userId=" + userID,
                'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh'}
    payload = {'orgid': '54', 'urlStr': 'http://def.yigao0792.com/1/jxufe/save.php',
                'openid': userID,
                'name': name, 'nickname': '', 'sex': '', 'province': '江西省', 'city': '南昌市', 'headimgurl': '',
                'sign': '',
                'timestamp': '', 'rectime': ''}
    requests.post("http://onestop.jxufe.edu.cn/eos/com.lantuo.bps.youthStudy.stwhttp.biz.ext", data=json.dumps(payload), headers=headers, cookies=dict(JSESSIONID=requests.get("http://onestop.jxufe.edu.cn/eos/wx/youthStudy/studyList.jsp?userId=" + userID).cookies['JSESSIONID']))


if __name__ == '__main__':
    main()

