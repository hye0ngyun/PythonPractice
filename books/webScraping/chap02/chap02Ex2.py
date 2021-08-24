from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
# 자식과 자손
print(bs.div.findAll('img'))    # 문서의 첫 번째 div 태그를 찾고, 그 div 태그의 자손인 모든 img 태그의 목록을 가져옵니다.

for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)
print('-'*37)
# 형제 다루기 next_siblings()
for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)
print('-'*37)
# 부모 다루기 .parent, .parents
print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())
'''
<tr id="gift1" class="gift"><td>
---
</td><td>
---
</td><td>
$15.00
</td><td>
<img src="../img/gifts/img1.jpg">
</td></tr>

1. 먼저 sre="../img/gifts/img1.jpg"에 해당하는 이미지를 선택한다.
2. 부모 태그(이 경우 <td>태그)를 선택한다.
3. 2에서 선택한 <td>의 previous_sibling(이 경우 제품 가격이 들어 있는 <td> 태그)을 선택합니다.
4. 태그에 들어 있는 텍스트인 $15.00를 선택합니다.
'''
