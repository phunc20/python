
- Breakdown around 2023/02/24 for `youtube-dl==2021.12.17`
    - One possible fix: <https://github.com/ytdl-org/youtube-dl/issues/31530#issuecomment-1433470254>  
      works like a charm!
    - Another fix is to install from github (which still works on 2023/05/03)
      ```sh
      $ pip install --upgrade "git+https://github.com/ytdl-org/youtube-dl.git"
      ```
