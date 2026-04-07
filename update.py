import re

with open('c:/Snap Syntax/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Hero Section
# We are currently on Inception
if '<h1 class="hero-title">INCEPTION</h1>' in html:
    html = re.sub(
        r'<h1 class="hero-title">INCEPTION</h1>.*?&#9654; VIEW DETAILS</a>',
        '''<h1 class="hero-title">Dhurandhar 2</h1>
                    <div class="hero-meta">
                        <span class="hero-rating">&#11088; 7.5</span>
                        <span>2025</span>
                        <span class="hero-badge">Action / Thriller</span>
                    </div>
                    <p class="hero-desc">Power. Revenge. No way back.</p>
                    <a href="#modal-dhurandhar2" class="hero-btn">&#9654; VIEW DETAILS</a>''',
        html,
        flags=re.DOTALL
    )

# 2. Add to Trending Now inside <div class="trending-row">...</div>
trend_addition = '''                <a href="#modal-matrix" class="trend-card">
                    <img src="https://image.tmdb.org/t/p/w300/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg" alt="The Matrix">
                    <div class="trend-overlay">
                        <div class="trend-title">The Matrix</div>
                        <div class="trend-rating">&#11088; 8.7</div>
                    </div>
                </a>
                <a href="#modal-dhurandhar2" class="trend-card">
                    <img src="dhurandhar2-poster.jpg" alt="Dhurandhar 2">
                    <div class="trend-overlay">
                        <div class="trend-title">Dhurandhar 2</div>
                        <div class="trend-rating">&#11088; 7.5</div>
                    </div>
                </a>'''

if 'alt="Dhurandhar 2"' not in html:
    html = re.sub(
        r'                <a href="#modal-matrix" class="trend-card">\s*<img src="https://image.tmdb.org/t/p/w300/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg" alt="The Matrix">\s*<div class="trend-overlay">\s*<div class="trend-title">The Matrix</div>\s*<div class="trend-rating">&#11088; 8.7</div>\s*</div>\s*</a>',
        trend_addition,
        html,
        flags=re.DOTALL
    )

# 3. Add to Movies Section (End of grid)
movie_addition = '''                <!-- Movie: Oppenheimer -->
                <a href="#modal-oppenheimer" class="media-card genre-drama">
                    <div class="card-poster-wrap">
                        <img src="https://image.tmdb.org/t/p/w300/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg" alt="Oppenheimer">
                        <div class="hover-play"></div>
                    </div>
                    <div class="card-info">
                        <h3 class="card-title">Oppenheimer</h3>
                        <div class="card-meta"><span>2023</span><span class="c-rating">&#11088;  8.3</span></div>
                        <div class="card-tags"><span class="c-tag tag-genre">Drama</span><span class="c-tag">3h 0m</span></div>
                    </div>
                </a>

                <!-- Movie: Dhurandhar 2 -->
                <a href="#modal-dhurandhar2" class="media-card genre-thriller genre-action">
                    <div class="card-poster-wrap">
                        <img src="dhurandhar2-poster.jpg" alt="Dhurandhar 2">
                        <div class="hover-play"></div>
                    </div>
                    <div class="card-info">
                        <h3 class="card-title">Dhurandhar 2</h3>
                        <div class="card-meta"><span>2025</span><span class="c-rating">&#11088; 7.5</span></div>
                        <div class="card-tags"><span class="c-tag tag-genre">Action/Thriller</span></div>
                    </div>
                </a>'''

html = re.sub(
    r'                <!-- Movie: Oppenheimer -->.*?</a>',
    movie_addition,
    html,
    flags=re.DOTALL
)


# 4. Add Modal
modal_addition = '''
    <!-- Dhurandhar 2 -->
    <div id="modal-dhurandhar2" class="modal-overlay">
        <div class="modal-content">
            <a href="#close" class="modal-close">&#10005;</a>
            <div class="modal-left"><img src="dhurandhar2-poster.jpg" alt="Dhurandhar 2"></div>
            <div class="modal-right">
                <h2 class="m-title">Dhurandhar 2</h2>
                <div class="m-meta"><span class="m-rating">&#11088; 7.5</span><span>2025</span><span>Action / Thriller</span><span>2h 20m</span></div>
                <p class="m-plot">A high-stakes action thriller involving power struggles and revenge.</p>
            </div>
        </div>
    </div>
</body>'''

html = html.replace('</body>', modal_addition)


with open('c:/Snap Syntax/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html fully updated.')
