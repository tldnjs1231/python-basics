from bs4 import BeautifulSoup

st = """
<html id="a">
    <body class="b">
        <div id="hello1" here="jeju1">안녕1</div>
        <div class="hello2" here="jeju2">안녕2</div>
        <div id="c">
            <span class="d" here="jeju3">안녕3</span>
        </div>
        <span>안녕4</span>
        <a href="https://www.naver.com">NAVER로가기</a>
    </body>
</html>
"""


# soup = BeautifulSoup(st, 'html.parser')
# print(soup.select_one('#hello1').get('here')) # jeju1
# # 속성값을 따올 때는 .get('속성명') 사용
# # 지난 시간에 텍스트 따올 때는 .text 사용

# print(soup.select_one('.hello2').get('here')) # jeju2
# print(soup.select_one('.d').get('here')) # jeju3
# print(soup.select_one('a').get('href')) # 네이버 링크



# 바이너리 파일 열기, 저장
# 웹 상에서 바이너리 파일 링크 가져와서 파일로 저장

import requests

res = requests.get('https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2FMjAxNjEwMDNfMTI3%2FMDAxNDc1NDk0NjE5NTY2.Q1huwy8TyvU5eYNX9anp-0HA42g6lvfF-Xd_qYGv7vAg.A4XwZVC3jPK0uGEQW38mL2sSc4RBYMI0-YrzCm613cwg.GIF.rlaqudwls951%2Fi13991973333.gif&type=sc960_832_gif')


f = open('나보단못함.gif', 'wb')
f.write(res.content) # res.text: html 소스, res.content: 바이너리값








