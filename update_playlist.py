# update_playlist.py

import requests

# Güncel IPTV kanallarının bulunduğu güvenilir bir kaynaktan veri çekin
# Örneğin: response = requests.get('https://example.com/iptv_channels.json')
# channels = response.json()

channels = [
    {
        "name": "BBC News",
        "url": "http://example.com/stream/bbc.m3u8",
        "group": "News",
        "tvg_id": "bbc"
    },
    {
        "name": "CNN",
        "url": "http://example.com/stream/cnn.m3u8",
        "group": "News",
        "tvg_id": "cnn"
    }
]

with open("playlist.m3u", "w") as f:
    f.write("#EXTM3U\n")
    for ch in channels:
        f.write(f'#EXTINF:-1 tvg-id="{ch["tvg_id"]}" tvg-name="{ch["name"]}" group-title="{ch["group"]}",{ch["name"]}\n')
        f.write(f'{ch["url"]}\n')
