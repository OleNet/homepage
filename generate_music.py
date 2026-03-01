#!/usr/bin/env python3
import html

# Read music list
with open('../my-music-list.txt', 'r', encoding='utf-8') as f:
    songs = [line.strip() for line in f if line.strip()]

# Generate song list HTML
song_items = []
for song in songs:
    if ' - ' in song:
        title, artist = song.split(' - ', 1)
    else:
        title, artist = song, ''
    title = html.escape(title)
    artist = html.escape(artist)
    song_items.append(f'      <li><span class="song-title">{title}</span><span class="song-artist">{artist}</span></li>')

songs_html = '\n'.join(song_items)

template = f'''<!DOCTYPE html>
<html lang="zh-Hans" class="zh">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Music · 刘佳祥</title>
  <link rel="stylesheet" href="style.css">
  <link rel="preconnect" href="https://fonts.loli.net" crossorigin />
  <link rel="preload" as="style" href="https://fonts.loli.net/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=DM+Sans:wght@300;400;500&family=Noto+Serif+SC:wght@300;400;500;600;700&display=swap" onload="this.onload=null;this.rel='stylesheet'" />
  <noscript><link rel="stylesheet" href="https://fonts.loli.net/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=DM+Sans:wght@300;400;500&family=Noto+Serif+SC:wght@300;400;500;600;700&display=swap" /></noscript>
</head>
<body>

<nav>
  <div class="container">
    <a href="index.html" class="site-name">刘 佳祥</a>
    <ul class="nav-links">
      <li><a href="index.html">About</a></li>
      <li><a href="music.html" class="active">Music</a></li>
      <li><a href="photography.html">Photography</a></li>
    </ul>
  </div>
</nav>

<main>
  <div class="container">
    <header class="section-header">
      <h1 class="section-title">Music</h1>
    </header>

    <ul class="music-list">
{songs_html}
    </ul>
  </div>
</main>

<footer>
  <div class="container">
    <p>&copy; 2025 刘佳祥</p>
  </div>
</footer>

</body>
</html>
'''

with open('music.html', 'w', encoding='utf-8') as f:
    f.write(template)

print(f'Generated music.html with {len(songs)} songs')
