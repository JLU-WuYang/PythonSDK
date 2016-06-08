import requests
error={0:"正常",
           20:"要翻译的文本过长",
           30:"无法进行有效的翻译",
           40:"不支持的语言类型",
           50:"无效的key",
           60:"无词典结果"}

def transferWord(app_name,app_key,word):
    dic={}
    
    try:
        html=requests.get("http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%d&type=data&doctype=json&version=1.1&q=%s"%(app_name,app_key,word))
        s=html.json()
    except:
        print error[s["errorCode"]]
    if s.has_key('basic'):
        dic["释义"]=s['basic']['explains']
        dic["英式英语"]="['"+s['basic']['uk-phonetic']+"']"
        dic["美式英语"]="['"+s['basic']['us-phonetic']+"']" 
    if s.has_key('translation'):
        dic["翻译"]=s['translation']
    if s.has_key('web'):
        dic['网络释义']=s['web']
    return dic
    

def transferSentence(app_name,app_key,sentence):
    dic={}
    try:
        html=requests.get("http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%d&type=data&doctype=json&version=1.1&q=%s"%(app_name,app_key,sentence))
        s=html.json()
    except:
        print error[s["errorCode"]]
    if s.has_key('translation'):
        dic["翻译"]=s['translation']
    if s.has_key('web'):
        dic['网络释义']=s['web']
    return dic
