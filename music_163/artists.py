"""
获取所有的歌手信息
"""
import requests
import urllib3
from bs4 import BeautifulSoup
from music_163 import sql

cookies = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': '_ntes_nnid=fa9c8e543e36dd502ae9e6a226d4672f,1551751983384; _ntes_nuid=fa9c8e543e36dd502ae9e6a226d4672f; _ga=GA1.2.1199911014.1551751984; JSESSIONID-WYYY=Ao7VM8BP6rqM2cDCYo1iJGDdBJbvhy1ED%5CP%2FqoH7HvcUUPfp371GiSZY3DC2DBKUDRXHamMPCnvQNIedsxBm3T%5CeBGXNtFkyYYMTyu6ckHKZX7o4RJoJlwAllS4wOYaGEzexwTXMv7UD1i%2B1j%2BKZkD9B8T3lSTC%5Cfut2XT7ONvij82j0%3A1551867101251; _iuqxldmzr_=32; WM_NI=0EKDxL8xiD2HIKJQ7ai1Zxv84aGe9cq3HNuLnXbBCh%2BFmPB02zUGxYiMb%2FeZeZQrZT0skPN0uQJHPO1r%2Be4uHg2yZTedr5rZhzkjSjGhuFUW%2BfbufX3Sx1%2B5x9%2Bjfor%2Fb08%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed9dc6e969699dadc25a18e8aa2c15e978f8faaf27dab968686c852acf08395d32af0fea7c3b92af49b85a5fb48fca8a7a5b1448b9586b2b66babef9699f534f8bf8986bc69b3ed88aff848ae88aea3c264e99aa3b1c13cf2a69ba8fb53ab93aed0e852a7869f93d960f4ada5b1cd3cb78f86a9d345f3aee586b77f8cb9fe9ad960a7bcbed6f152aca6a58bd26285b8bba7d85de9baae96e554f18db8d2aa3fbce7e58be565b2f1aed1bb37e2a3; WM_TID=rI6kBwyYWb1BVUBEBBIohiZZeUdlldoL',
    'DNT': '1',
    'Host': 'music.163.com',
    'Pragma': 'no-cache',
    'Referer': 'http://music.163.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

def getUrl(type,url ,params):
    requests.packages.urllib3.disable_warnings()
    httprequuest = urllib3.PoolManager();
    httprespon = httprequuest.request(type, url,headers=cookies,fields=params)
    return httprespon.data.decode()






def save_artist(group_id, initial):
    params = {'id': group_id, 'initial': initial}
    content = getUrl('get','http://music.163.com/discover/artist/cat',params)

    # 网页解析
    soup = BeautifulSoup(content, 'html.parser')
    body = soup.body

    hot_artists = body.find_all('a', attrs={'class': 'msk'})
    artists = body.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'})

    for artist in hot_artists:
        artist_id = artist['href'].replace('/artist?id=', '').strip()
        artist_name = artist['title'].replace('的音乐', '')
        try:
            print(artist_id+"-hot-"+artist_name)
            # sql.insert_artist(artist_id, artist_name)
        except Exception as e:
            # 打印错误日志
            print(e)

    for artist in artists:
        artist_id = artist['href'].replace('/artist?id=', '').strip()
        artist_name = artist['title'].replace('的音乐', '')
        try:
            print(artist_id + "--" + artist_name)
            # sql.insert_artist(artist_id, artist_name)
        except Exception as e:
            # 打印错误日志
            print(e)



# for i in range(65, 91):
#     save_artist(1001, i)
if __name__ == '__main__':
    save_artist(1001,-1)
