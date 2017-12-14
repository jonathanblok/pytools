import hashlib
import urllib2 as urllib


def hash_response(response):
    md5hashlib = hashlib.md5()
    md5hashlib.update(response)
    currenthash = md5hashlib.hexdigest()
    return currenthash


def get_html_response(url):
    response = urllib.request.urlopen(url)
    html_response = response.read()
    return html_response

#GET /huurwoningen/utrecht/0-1300 HTTP/1.1
#Host: www.pararius.nl
#Connection: keep-alive
#Cache-Control: max-age=0
#Upgrade-Insecure-Requests: 1
#User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36
#Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
#Accept-Encoding: gzip, deflate, br
#Accept-Language: en-US,en;q=0.9,nl;q=0.8,de;q=0.7,pl;q=0.6
#Cookie: D_SID=31.201.167.136:mrsrAs2Bc6tXG6PYqBfc3FOioTx3TbsIBFbBpQdfG/A; userAcceptedCookies=true; fuelfid=5FC70ZZ71s0IEClz1_TGQL3R7JCXruD5QpcqdOAn0rGm0rNvtTtCONRR8FJd_y4kCxwVAcazpg7Jo80Cti_oGV9uYTJQeXdrU0g1TFk5cjAwd3NmQVZwRmtQdUFjV1dhYlJvM2tkSFh3NW8; _ga=GA1.2.1909659599.1513258494; _gid=GA1.2.1283146770.1513258494; _gat=1; D_IID=F2320F0D-6702-3771-AA7B-4DD302719D13; D_UID=66518BB2-417E-379E-A050-1D37FD0C2E9E; D_ZID=C995E355-768B-3A72-9A85-C715E86ADE75; D_ZUID=C17B459E-CB1C-35FF-924C-189BA09E44DA; D_HID=5273ADA4-947E-3BC0-8495-A2B687EBE887



def get_html_response_as_firefox(url):
    opener = urllib.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    #opener.addheaders = [('Cookie', 'D_SID=31.201.167.136:mrsrAs2Bc6tXG6PYqBfc3FOioTx3TbsIBFbBpQdfG/A; userAcceptedCookies=true; fuelfid=5FC70ZZ71s0IEClz1_TGQL3R7JCXruD5QpcqdOAn0rGm0rNvtTtCONRR8FJd_y4kCxwVAcazpg7Jo80Cti_oGV9uYTJQeXdrU0g1TFk5cjAwd3NmQVZwRmtQdUFjV1dhYlJvM2tkSFh3NW8; _ga=GA1.2.1909659599.1513258494; _gid=GA1.2.1283146770.1513258494; _gat=1; D_IID=F2320F0D-6702-3771-AA7B-4DD302719D13; D_UID=66518BB2-417E-379E-A050-1D37FD0C2E9E; D_ZID=C995E355-768B-3A72-9A85-C715E86ADE75; D_ZUID=C17B459E-CB1C-35FF-924C-189BA09E44DA; D_HID=5273ADA4-947E-3BC0-8495-A2B687EBE887')]
    req = urllib.Request(url)
    return opener.open(req).info()


def test():
    url = 'https://www.google.com'
    print(get_html_response_as_firefox(url))
    url = 'https://www.pararius.nl/huurwoningen/utrecht/0-1300'
    print(get_html_response_as_firefox(url))


if __name__ == "__main__":
    test()