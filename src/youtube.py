import urllib.request
import urllib.parse
import re
import pafy
import vlc 


def get_url_result(video_to_search): 
    query_string = urllib.parse.urlencode({"search_query" : video_to_search})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    url = "http://www.youtube.com/watch?v=" + search_results[0]
    print(url)
    return url

def play_video(url):
    # Use VLC to play the video without any pause-play control
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(url)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
