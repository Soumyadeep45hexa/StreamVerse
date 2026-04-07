import urllib.request
import re

url = 'https://posterspy.com/posters/dune-poster-6/'
req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5'
    }
)

try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        match = re.search(r'<meta property="og:image" content="(.*?)"', html)
        if match:
            img_url = match.group(1)
            print('Found image URL:', img_url)
            
            img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(img_req) as img_res, open('c:/Snap Syntax/dune.jpg', 'wb') as out_file:
                out_file.write(img_res.read())
            print('Downloaded successfully!')
        else:
            print('Could not find image URL in HTML')
except Exception as e:
    print('Failed:', str(e))
