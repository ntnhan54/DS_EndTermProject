import requests
import json
import spotipy
import pandas as pd
from typing import List, Dict


import spotipy.util as util


# username = "Chrisnguyen"
# client_id= "ac6f1d431d774310a0761aef45b2160a"
# client_secret = "b967f892029e4a21a5f187a5d5b6c784"
# redirect_uri  = "http://localhost:7777/callback"

username = 'ntnhan54'
client_id = '30852d0a0cbe4c978fd66b78c48a82a5'
client_secret = 'a1d544ff27cd41ceb3912352abab2109'
redirect_uri  = "http://localhost:7777/callback"

scope = 'playlist-read-collaborative'

token = util.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=client_id,   
                                   client_secret=client_secret,     
                                   redirect_uri=redirect_uri)


print(token)


def get_id(track_name: str, token: str) -> str:
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer ' + token,
    }
    params = [
        ('q', track_name),
        ('type', 'track'),
    ]
    try:
        response = requests.get('https://api.spotify.com/v1/search', 
                    headers = headers, params = params, timeout = 5)
        json = response.json()
        first_result = json['tracks']['items'][0]
        track_id = first_result['id']
        return track_id
    except:
        return None


def get_features(track_id: str, token: str) -> dict:
    sp = spotipy.Spotify(auth=token)
    try:
        features = sp.audio_features([track_id])
        return features[0]
    except:
        return None


def get_all_playlist(username: str, token: str) -> List[Dict]:
    headers = {
        'Accept': 'application/json',\
        'Content-Type': 'application/json',\
        'Authorization': f'Bearer ' + token,\
    }
    
    offset   = 0
    limit    = 50
    total    = 100000 #max offset in spotify
    playlist = []
    
    while offset < total:
        params = [("limit", limit), ("offset", offset)]
        
        response = requests.get(f"https://api.spotify.com/v1/users/{username}/playlists", headers = headers, params=params)
        json_obj = response.json()
        
        if response.status_code get_ipython().getoutput("= 200:")
            print(response)
            continue
        
        playlist.extend(json_obj["items"])
        n = offset + len(json_obj["items"])

        print(f"Successfully get from playlist {offset} to {n}")
        offset = n
        
        if json_obj["total"] < total:
            total = json_obj["total"]
            
        if not "next" in json_obj or json_obj["next"] == "":
            break

    return playlist


spotify_playlist = get_all_playlist("spotify", token)


playlist_id = [s["id"] for s in spotify_playlist]    


with open("playlist.txt", "w") as f:
    for ids in playlist_id:
        f.write(ids + "\n")


len(playlist_id)


def getItemByPlaylist(ids: str, token: str) -> dict:

    headers = {
            'Accept': 'application/json',\
            'Content-Type': 'application/json',\
            'Authorization': f'Bearer ' + token,\
        }
    playListDetail = {
        'track_ids': set(),
        'artist_ids': set()
    }
    response = requests.get(f"https://api.spotify.com/v1/playlists/{ids}/tracks", headers = headers)
    json_obj = response.json()
    for item in json_obj['items']:
        try:
            playListDetail['track_ids'].add(item["track"]['id'])
            playListDetail['artist_ids'].add(item["track"]["artists"][0]['id'])
        except:
            pass
    return playListDetail


with open('playlist.txt') as f:
    playList_ids = f.read()
playList_ids = playList_ids.split('\n')[:-1]


playListDetails = getItemByPlaylist(playList_ids[0], token)
for i, ids in enumerate(playList_ids[1:]):
    print(i, ids)
    detail = getItemByPlaylist(ids, token)
    playListDetails['track_ids'] |= detail['track_ids']
    playListDetails['artist_ids'] |= detail['artist_ids']
try:
    playListDetails['track_ids'].remove(None)
    playListDetails['artist_ids'].remove(None)
except:
    pass


len(playListDetails['track_ids']), len(playListDetails['artist_ids'])


with open("tracks.txt", "w") as f:
    for ids in playListDetails['track_ids']:
        f.write(ids + "\n")


with open("artists.txt", "w") as f:
    for ids in playListDetails['artist_ids']:
        f.write(ids + "\n")
