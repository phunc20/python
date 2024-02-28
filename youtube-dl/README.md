## Usage
- Video/audio quality: `-f best`
- With thumbnail: `--write-thumbnail`
- Specify video id to download that video
  ```bash
  $ # Full-blown
  $ youtube-dl https://youtube.com/watch?v=R8_veQiYBjI
  $ # Shorthand
  $ youtube-dl R8_veQiYBjI
  ```
- Download all videos of an entire channel
  ```bash
  $ # Say, we want to download all videos on @TheJuliaLanguage
  $ youtube-dl https://youtube.com/@TheJuliaLanguage
  ```
  
  Note that no shorthand is allowed. That is, it is not allowed to
  `youtube-dl @TheJuliaLanguage`


## Troubleshoot
- Breakdown around 2023/02/24 for `youtube-dl==2021.12.17`
    - One possible fix: <https://github.com/ytdl-org/youtube-dl/issues/31530#issuecomment-1433470254>  
      works like a charm!
    - Another fix is to install from github (which still works on 2023/05/03)
      ```sh
      $ pip install --upgrade "git+https://github.com/ytdl-org/youtube-dl.git"
      ```
- (2024/02/28) Python 3.12.1 still with `youtube-dl==2021.12.17`.  
  Solution found at <https://github.com/yt-dlp/yt-dlp/issues/6247#issuecomment-1433096554>.  
  That is, make the following modification to the file at
  `miniconda3/lib/python3.12/site-packages/youtube_dl/extractor/youtube.py`
  ```python
  # The original line
  #'uploader_id': self._search_regex(r'/(?:channel|user)/([^/?&#]+)', owner_profile_url, 'uploader id') if owner_profile_url else None,
  # Modified into this should work.
  'uploader_id': self._search_regex(r'/(?:channel/|user/|(?=@))([^/?&#]+)', owner_profile_url, 'uploader id', default=None),
  ```
