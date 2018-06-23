from bs4 import BeautifulSoup
import urllib.request

url = 'http://sls.service.enmasse.com:8080/servers/list.en'
readUrl = urllib.request.urlopen(url).read()
readUrl = readUrl.decode('utf-8')
bs = BeautifulSoup(readUrl, 'html.parser')
serverNames = bs.find_all('name')
serverStatus = bs.find_all('permission_mask')
sStatus = []

for y in range(len(serverStatus)):
	status = serverStatus[y].get_text()
	if status == '0x00000000':
		serverStatus[y] = 'up'
	else:
		serverStatus[y] = 'down'
for x in range(len(serverNames)):
	sStatus.append("{} is {}".format(serverNames[x].get_text().strip('\n'), serverStatus[x]))
for server in sStatus:
	print(server, end='\n')