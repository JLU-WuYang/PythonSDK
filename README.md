# PythonSDK
- YouDao
  youdaofanyi sdk for python
  - transferWord
    transfer Chinese word to English word  or English word  to Chinese word 
    request:
          - app_name(got from youdao)
          - app_key
          - word
    return:
          - dic
            - 释义(List)(if have)
            - 英式英语(prounction in UK)(if have)
            - 美式英语(if have)
            - 翻译(List)
            - 网络释义(List)(if have)
  - transferSentence
    transfer English, Japanese, Korean, French, Russian.. to Chinese or Chinese to English
    request:
          - app_name
          - app_key
          - sentence
    return:
          - dic
            - 翻译(List)
            - 网络释义(List)(if have)
