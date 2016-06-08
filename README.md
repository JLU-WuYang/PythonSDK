# PythonSDK
- YouDao<br>
  youdaofanyi sdk for python
  - transferWord<br>
    transfer Chinese word to English word  or English word  to Chinese word <br><br>
      request:
          <ul>
          <li>app_name(got from youdao)</li>
          <li>app_key</li>
          <li>word</li>
          </ul>
            <br>
      return:<br>
          dic
          <ul>
            <li>释义(List)(if have)</li>
            <li>英式英语(prounction in UK)(if have)</li>
            <li>美式英语(if have)</li>
            <li>翻译(List)</li>
            <li>网络释义(List)(if have)</li>
          </ul>
  - transferSentence<br>
    transfer English, Japanese, Korean, French, Russian.. to Chinese or Chinese to English<br><br>
      request:<br>
          <ul>
          <li>app_name</li>
          <li>app_key</li>
          <li>sentence</li>
          </ul>
      <br>
      return:<br>
          dic
            <ul>
            <li>翻译(List)</li>
            <li>网络释义(List)(if have)</li>
            </ul>
