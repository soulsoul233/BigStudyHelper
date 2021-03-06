import json
import requests as r

def Ding(key, secret, content):
    import time
    import hmac
    import hashlib
    import base64
    import urllib.parse
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    url = "https://oapi.dingtalk.com/robot/send?access_token=" + key + "&timestamp=" + timestamp + "&sign=" + sign
    head = {'Content-Type': 'application/json'}
    r.encoding = 'utf-8'
    tmp = "{\"msgtype\": \"text\", \"text\": {\"content\": \"" + content + "\"}}"
    r.post(url, data=json.dumps(eval(tmp)), headers=head)

def DoIt(name, userID):

    url2 = "http://onestop.jxufe.edu.cn/eos/wx/youthStudy/studyList.jsp?userId=" + userID
    api2 = "http://onestop.jxufe.edu.cn/eos/com.lantuo.bps.youthStudy.stwhttp.biz.ext"
    headers2 = {'Host': 'onestop.jxufe.edu.cn', 'Connection': 'keep-alive', 'Accept': 'application/json, text/plain, */*',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66',
                'Content-Type': 'application/json;charset=UTF-8', 'Origin': 'http://onestop.jxufe.edu.cn',
                'Referer': url2,
                'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh'}
    payload2 = {'orgid': '54', 'urlStr': 'http://def.yigao0792.com/1/jxufe/save.php',
                'openid': userID,
                'name': name, 'nickname': '', 'sex': '', 'province': '江西省', 'city': '南昌市', 'headimgurl': '',
                'sign': '',
                'timestamp': '', 'rectime': ''}
    r2 = r.get(url2)

    try:
        cs2 = dict(JSESSIONID=r2.cookies['JSESSIONID'])
    except:
        print("所填信息有误,无法登录!")
        exit()
    final2 = r.post(api2, data=json.dumps(payload2), headers=headers2, cookies=cs2)
    CON = final2.json()['result']
    I = 0
    Flag = 0
    result = ""
    for i in str(CON):
        if Flag:
            result = result + i
        if i == '"':
            I = I + 1
        if I == 5:
                Flag = 1
        elif I == 6:
            break
    return result


def main():
    key = "xxxxxxxxxxxxxxxxxxxxxxxxx"
    secret = "xxxxxxxxxxxxxxxxxxxxxxxxx"

    name = [
        ("张三", "xxxxxxxxxxxxxxxxxxxxxxxxx"),
        ("李四", "xxxxxxxxxxxxxxxxxxxxxxxxx"),
    ]

    for i in range(len(name)):
        result = DoIt(name[i][0],name[i][1])


    try:
        Ding(key,secret, result[:-1])
        print("钉钉通知成功!")
    except:
        print("未填写钉钉群机器人S/K, 采用本地通知")
        print(result[:-1])


if __name__ == '__main__':
    main()

def main_handler(event, context):
    main()
