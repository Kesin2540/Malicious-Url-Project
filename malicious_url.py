import pandas as pd
import tldextract
import ipaddress
from datetime import datetime
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

SHORTENERS = [
    "bit.ly", "t.co", "tinyurl.com", "goo.gl", "ow.ly", "is.gd", "buff.ly", 
    "adf.ly", "shorte.st", "cutt.ly", "rb.gy", "rebrand.ly", "bl.ink", "tr.im",
    "tiny.cc", "s.coop", "mcaf.ee", "t2m.io", "v.gd", "qr.ae", "0rz.tw", "x.co",
    "soo.gd", "lnkd.in", "shrtco.de", "chilp.it", "clck.ru", "s.id", "u.nu",
    "qr.net", "shorturl.at", "aka.ms", "gph.is", "ht.ly", "safe.mn", "wp.me",
    "y2u.be", "fb.me", "4sq.com", "snip.ly", "flip.it", "cur.lv", "kutt.it",
    "tiny.pl", "short.cm", "gg.gg", "ouo.io", "bc.vc", "festyy.com", "zee.gl"
]

df = pd.read_csv('/home/kesin/Downloads/malicious_phish/malicious_phish.csv')

def isShortenedUrl(url):
    return urlparse(url).hostname in SHORTENERS

def IsIpAddress(url):
    hostname = urlparse(url).hostname
    try:
        ipaddress.ip_address(hostname)
        return True
    except ValueError:
        return False

def countNum(url):
    return sum(c.isdigit() for c in url)

def countLetter(url):
    return sum(c.isalpha() for c in url)

def fd_length(url):
    urlpath= urlparse(url).path
    try:
        return len(urlpath.split('/')[1])
    except:
        return 0

def appendingProcesses(url, type):
    data = {
        "Length of the Url": len(url),
        "Hostname": urlparse(url).netloc,
        "Hostname Length": len(urlparse(url).netloc),
        "Path": urlparse(url).path,
        "Path Length": len(urlparse(url).path),
        "First Directory Length": fd_length(url),
        "Top Level Domain": tldextract.extract(url).suffix,
        "TLD Length": len(tldextract.extract(url).suffix),
        "No. of -": url.count('-'),
        "No. of @": url.count('@'),
        "No. of ?": url.count('?'),
        "No. of %": url.count('%'),
        "No. of .": url.count('.'),
        "No. of =": url.count('='),
        "No. of https": url.count('https'),
        "No. of http": url.count('http'),
        "No. of www": url.count('www'),
        "No. of Numerical Values": countNum(url),
        "No. of Letters": countLetter(url),
        "No. of Directories": url.count('/') - 1,
        "IP address or not": 1 if IsIpAddress(url) else 0,
        "Shortened Url Used": 1 if isShortenedUrl(url) else 0,
        "Type": type
    }
    return data

print(datetime.now())

with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(appendingProcesses, df.iloc[:, 0], df.iloc[:, 1]))

df_processed = pd.DataFrame(results)

df_processed.to_csv('processed_url.csv')
