import requests
import openpyxl
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'songs_mayday'
column_name = ['歌曲名', '所属专辑', '播放时长', '播放链接']
for x in range(0, 3):
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'sizer.yqq.song_next',
        'searchid': '64405487069162918',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(x + 1),
        'n': '20',
        'w': '五月天',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }
    res_music = requests.get(url, params = params)
    json_music = res_music.json()
    list_music = json_music['data']['song']['list']
    for music in list_music:
        name = music['name']
        album = music['album']['name']
        time = music['interval']
        link = 'https://y.qq.com/n/yqq/song/' + str(music['file']['media_mid']) + '.html\n\n'
        sheet.append([name, album, time, link])
        wb.save('mayday.xlsx')
        wb.close()