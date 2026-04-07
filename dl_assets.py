import urllib.request
import re

# Download Poster
poster_url = 'https://images.timesnowhindi.com/photo/msid-153551516,width-1080,height-1350,resizemode-3/153551516.jpg'
req1 = urllib.request.Request(poster_url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req1) as res, open('c:/Snap Syntax/dhurandhar2-poster.jpg', 'wb') as f:
        f.write(res.read())
    print('Poster downloaded')
except Exception as e:
    print('Poster failed:', e)

# Download Pinterest Background
pin_url = 'https://in.pinterest.com/pin/188306828165260865/'
req2 = urllib.request.Request(pin_url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req2) as res:
        html = res.read().decode('utf-8')
        match = re.search(r'<meta property="og:image" name="og:image" content="(.*?)"', html)
        if not match:
            # fallback
            match = re.search(r'<meta property="og:image" content="(.*?)"', html)
        if match:
            bg_url = match.group(1)
            bg_req = urllib.request.Request(bg_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(bg_req) as b_res, open('c:/Snap Syntax/hero-bg.jpg', 'wb') as f:
                f.write(b_res.read())
            print('Background downloaded:', bg_url)
        else:
            print('Could not extract image from Pinterest link')
except Exception as e:
    print('Background failed:', e)
