import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Cookie': 'anonymid=kai1a1r8-2we4bv; depovince=XG; _r01_=1; JSESSIONID=abcM5Ky39za_Pct-_07ix; ick_login=c3d5c45b-9ccc-450f-b30a-f8834cf4194c; taihe_bi_sdk_uid=e1a148401cd5586ad24b9352b0cdeedd; taihe_bi_sdk_session=abe5a21744208cf4d5b6438f90f182d5; first_login_flag=1; ln_uact=15012525590; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebecookies=350ef199-3e6d-4044-93de-cf071f8343e9|||||; _de=E038C89196EEF3C58E49A581F847F522; p=f1825d05c17ff824b4dd7db85a2b14630; ap=974484840; t=eeacb74418a8c053ad145bfdf47209470; societyguester=eeacb74418a8c053ad145bfdf47209470; id=974484840; xnsid=c301143a; ver=7.0; loginfrom=null; wp_fold=0'
}

url_in = 'http://www.renren.com/974484840'
res = requests.get(url_in, headers = headers)

soup = BeautifulSoup(res.text, 'html.parser')
rp = soup.find('span', class_="total")
print(rp.text)
