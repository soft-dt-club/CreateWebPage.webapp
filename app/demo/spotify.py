import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import os
from dotenv import load_dotenv
load_dotenv()


def search(keyword):
    
    # Oath2
    # client_id = os.getenv('CLIENT_ID')
    # client_secret = os.getenv('CLIENT_SECRET')
    # sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    #     client_id=client_id, client_secret=client_secret), language='ja')
    # 検索
    # result = sp.search(q=keyword, limit=10, market='JP')
    # print(result)

    # ダミー用jsonファイルを読み込む
    # NOTE: 絶対パスを指定する
    dummy = open(os.getcwd()+r"\demo\dummy_data.json", 'r', encoding="utf-8")
    json_load = json.load(dummy)

    result_list = []
    for track in json_load['tracks']['items']:
    # for track in result['tracks']['items']:
        target = {}
        # 曲名
        target['name'] = track['name']
        if track['is_playable'] is True:
            # 試聴リンク
            target['preview_url'] = track['preview_url']
        # ジャケット画像
        target['images'] = track['album']['images'][1]['url']
        # アーティスト名
        target['artist'] = track['album']['artists'][0]['name']
        # リリースタイプ(single or album)
        target['album_type'] = track['album']['album_type']
        # アルバム名
        target['album_title'] = track['album']['name']
        # リリース日
        target['release_date'] = track['album']['release_date']
        result_list.append(target)

    return result_list
