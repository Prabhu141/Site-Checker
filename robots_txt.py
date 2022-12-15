import urllib.request
import io

def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib.request.urlopen(path + "robots.txt", data=None)
    data = io.TextIOWrapper(req, encoding='utf-8')
    return data.read()

print(get_robots_txt('https://www.google.com/'))
# print(get_robots_txt('https://www.amazon.com/'))























#
# import urllib.robotparser
# import requests
#
# rp = urllib.robotparser.RobotFileParser()
# rp.set_url("http://www.musi-cal.com/robots.txt")
# rp.read()
# rrate = rp.request_rate("*")
#
# rrate.requests
#
# rrate.seconds
#
# rp.crawl_delay("*")
#
# rp.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco")
#
# rp.can_fetch("*", "http://www.musi-cal.com/")













