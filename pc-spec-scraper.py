import requests
from bs4 import BeautifulSoup 


pc_url = "https://www.newegg.com/ibuypower-element-9-white-gaming-desktop-pcs-geforce-rtx-5070-ti-amd-ryzen-7-7800x3d-32gb-ddr5-1-tb-ssd-pb-ewa7n57t-01/p/3D5-0007-00J37?item=3D5-0007-00J37&source=region&utm_source=google&utm_medium=paid+shopping&utm_campaign=knc-googleadwords-pc-_-pla-_-gaming+desktop+pcs-_-3D5-0007-00J37&id0=Google&id1=22893743459&id2=180748030541&id3=&id4=&id5=pla-2430368789735&id6=&id7=9002074&id8=&id9=g&id10=c&id11=&id12=Cj0KCQjwh5vFBhCyARIsAHBx2wyOKdStHnsn8vSBQyJPVLa-ufDBVFx0cy0OvdtLSrr9Feon1C50ejYaAsuyEALw_wcB&id13=&id14=Y&id15=&id16=769254148021&id17=&id18=&id19=&id20=&id21=pla&id22=8438988&id23=online&id24=3D5-0007-00J37&id25=US&id26=2430368789735&id27=Y&id28=&id29=&id30=15136430808029116850&id31=en&id32=&id33=DA&id34=US&gad_source=1&gad_campaignid=22893743459&gclid=Cj0KCQjwh5vFBhCyARIsAHBx2wyOKdStHnsn8vSBQyJPVLa-ufDBVFx0cy0OvdtLSrr9Feon1C50ejYaAsuyEALw_wcB"
#print(pc_url)

url_request = requests.get(pc_url)
soup = BeautifulSoup(url_request.text, 'html.parser')

price_div = soup.find('div', {"class":'price-current'})
price = price_div.get_text()
print(price)

table_rows = soup.find_all('tr')
print(table_rows)


# Motherboard
# CPU
    #CPU Name
# Graphics
# Memory
    # Memory Capacity
    # Memory Speed
# Power Supply
# Storage
# Case
# Cooling System
#----------------------#
# <span class="price-current-label"></span>
# <tr><th>Case<!-- --> </th><td>Element 9 White</td></tr>

#quick_info_div = soup.find('table', {"class":"table-horizontal", "caption":"Quick Info"})
#print(price)
