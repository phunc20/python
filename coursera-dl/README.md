## `coursera-dl` not working out of the box
One cannot download coursera courses right after installing `pip install coursera-dl`. Instead,
some configurations are needed:
- Find the file `cookies.py` in the site package folder of your installed virtualenv for `coursera-dl`
  ```bash
  [phunc20@homography-x220t coursera-dl]$ workon coursera
  (coursera) [phunc20@homography-x220t coursera-dl]$ which python
  /home/phunc20/.virtualenvs/coursera/bin/python
  (coursera) [phunc20@homography-x220t coursera-dl]$ find /home/phunc20/.virtualenvs/coursera/lib/python3.7/site-packages/coursera/ -type f -iname "cookies.py"
  /home/phunc20/.virtualenvs/coursera/lib/python3.7/site-packages/coursera/cookies.py
  (coursera) [phunc20@homography-x220t coursera-dl]$
  ```
- Change the content of the function `login()` in `cookies.py` to a **one-line code**.
  ```python
  def login(session, username, password, class_name=None):
      session.cookies.set('CAUTH', '[YOUR CAUTH COOKIE VALUE]')
  ```
  - Find the **newest cauth cookie** using your web browser
  - The original content of `login()` contains a lot of lines of code. Just comment them all out.
- Download the content of a coursera course using the command syntax below
  - `coursera-dl -u <email> -p <password> <coursename>`
    - e.g. `coursera-dl -u tungnv15@gmail.com -p passCuaTung julia-programming`
    - Don't use the course's url, i.e. don't `coursera-dl -u tungnv15@gmail.com -p passCuaTung https://www.coursera.org/learn/julia-programming`. Just the course name.
- cf. [https://github.com/coursera-dl/coursera-dl/issues/702](https://github.com/coursera-dl/coursera-dl/issues/702) for more info.
