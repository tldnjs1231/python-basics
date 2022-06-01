import requests
from bs4 import BeautifulSoup


st = """<html>
    <body>
        <div id="champs">
            <div class="name">Kennen</div>
            <div class="hp">1000</div>
            <div class="mp">300</div>
        </div>
        <div id="champs">
            <div class="name">Teemo</div>
            <div class="hp">800</div>
            <div class="mp">100</div>
        </div>
        <div id="champs">
            <div class="name">Veigar</div>
            <div class="hp">500</div>
            <div class="mp">3000</div>
        </div>
    </body>
</html>"""


soup = BeautifulSoup(st, 'html.parser')

for i in soup.select('#champs'):
    print(i.select_one('.name'))
    print(i.select_one('.hp'))
    print(i.select_one('.mp'))

# .select()를 iter로 갖는 for문 안에 .select나 .select_one으로
# 마저 자를 수 있음
# #champs 안에 서로 다른 클래스 세 개 있는 경우 for문 세 번 돌려야 함
# 번거로우므로 마저 자르기 사용





