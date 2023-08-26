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
