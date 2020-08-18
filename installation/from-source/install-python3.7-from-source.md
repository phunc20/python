# As of 2020/07/25, The Default Python Versio on Arch Linux Is <code>3.8.2</code>
However, in some scenarios, one might be interested in having other python versions as well. For example, the other day I wanted to register in the exam of tensorflow developper certificate, which recommends <code>python3.7</code> for consistency.


- For <code>python3.6</code> One can easily install using the AUR
- But when it comes to installing  <code>python3.7</code>  using the AUR, I ran into some problems with pacman/gpg keys. I tried some commands to refresh keys, etc. <b>without success</b>.
- I then tried to install <code>python3.7</code> from source (using the tarball from [python's official website](https://www.python.org/downloads/source/)). It turned out to be a lot easier than I thought; here were the steps I followed (by referring to the <code>README.rst</code> inside the tarball):
<pre># Inside the directory of the uncompressed tarball
./configure<br/>
make<br/>
# A lot of testing will be printed to stdout; this part is the most time-consuming, more than all of `./configure`, `make` and `sudo make altinstall`, the last being amazingly fast.
make test<br/>
# In order not to mess up with the system's default python, which is python3.8, DO NOT `sudo make install`; instead, DO `sudo make altinstall` like suggested in README.rst
sudo make altinstall
</pre>


## Troubleshoot
- In some newly installed machine (e.g. I have experienced difficulties on my artix x200 tablet), the <code><b>make test</b></code> might take too long and <b>never succeed</b>. In my case, I found out that it was probably because I hadn't set <code><b>/etc/hosts</b></code>. I provided one example of this file in the present directory for reference.
- Oh, besides, I did <code><b>make clean</b></code> when the build failed and that I wantd to start all overagain.
