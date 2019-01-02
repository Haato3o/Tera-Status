'''
					SLS websites
	NA: http://sls.service.enmasse.com:8080/servers/list.en
	EU: http://web-sls.tera.gameforge.com:4566/servers/list.uk
	RU: http://launcher.tera-online.ru/launcher/sls/
	TW: http://tera.mangot5.com/game/tera/serverList.xml
'''

from bs4 import BeautifulSoup
import requests

def check_server(url):
	'''
		Function to check TERA server status
		:param url: SLS website
		:return: dict
	'''
	readUrl = requests.request('get', url).text
	bs = BeautifulSoup(readUrl, 'html.parser')
	serverNames = bs.find_all('name')
	serverStatus = bs.find_all('permission_mask')
	sStatus = {}

	for name in serverNames:
		sStatus[name['raw_name'].strip('\n')] = None
	for status in range(len(serverStatus)):
		if serverStatus[status].get_text() == '0x00000000':
			sStatus[serverNames[status]['raw_name'].strip('\n')] = 'up'
		else:
			sStatus[serverNames[status]['raw_name'].strip('\n')] = 'down'

	return sStatus

if __name__ == '__main__':
	na_sls = 'http://sls.service.enmasse.com:8080/servers/list.en'
	results = check_server(na_sls)
	for server in results:
		print(f'{server} is {results[server]}')
	
