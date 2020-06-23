import requests
url = 'https://www.douban.com'
session = requests.session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Cookie': 'll="108090"; bid=s6UeOkk_HVo; _pk_ses.100001.8cb4=*; __utma=30149280.1668536889.1590162315.1590162315.1590162315.1; __utmc=30149280; __utmz=30149280.1590162315.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); push_noty_num=0; push_doumail_num=0; ap_v=0,6.0; __utmv=30149280.21713; dbcl2="217131254:uANDA7DxuB4"; ck=6Txg; _pk_id.100001.8cb4=005a23f4529d84aa.1590162314.1.1590162887.1590162314.; __utmb=30149280.11.10.1590162315'
}

comment = '笨赖谁？'
data = {
    'ck': '6Txg',
    'comment': comment,
    'privacy_and_reply_limit': 'P,'
}
session.post(url, headers = headers, data = data)