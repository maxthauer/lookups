from bs4 import BeautifulSoup
import requests, argparse, time

parser = argparse.ArgumentParser()
parser.add_argument('query')
args = parser.parse_args()
query = args.query

headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

url = 'https://spur.us/context/'+query
r = requests.get(url, headers=headers)
url = r.text
soup = BeautifulSoup(url, features="lxml")
result = soup.find('div', {'class': 'col-lg-10 col-xl-8 white-card'})
content = result.select('h1')
verdict = content[0].text

if "Not Anonymous" in verdict:
	print ("{} | Not Anonymous".format(query))
else:
	verdict = verdict.split('-')
	v = verdict[1].replace("\n", "")
	final = v.replace(" ", "")
	print ("{} | {}".format(query,final))
time.sleep(10) 
