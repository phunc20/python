<pre>
In [1]: from pathlib import Path

In [2]: !pwd
/home/phunc20/samsung-SATA/datasets/food-on-table/gogi

In [3]: ls
00000002210000000/     00000002280000000/     00000002343000000/              03_test-corners.ipynb
00000002210000000.mp4  00000002280000000.mp4  00000002343000000.mp4           04_begin-crop.ipynb
00000002240000000/     00000002319000000/     00000002359000000/              __pycache__/
00000002240000000.mp4  00000002319000000.mp4  00000002359000000.mp4           table_corners.py
00000002242000000/     00000002326000000/     00000002390000000/              trash.py
00000002242000000.mp4  00000002326000000.mp4  00000002390000000.mp4
00000002266000000/     00000002330000000/     01_cut-frame.sh*
00000002266000000.mp4  00000002330000000.mp4  02_accidentally-delete-file.md

In [4]: gogi = Path.cwd()

In [34]: gogi / "00000002319000000" / "T0"
Out[34]: PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002319000000/T0')

In [35]: Path.mkdir(gogi / "00000002319000000" / "T0")

In [36]: ls -d 00000002319000000/T0
00000002319000000/T0/

In [37]: Path.rmdir(gogi / "00000002319000000" / "T0")

In [38]: ls -d 00000002319000000/T0
ls: cannot access '00000002319000000/T0': No such file or directory

</pre>
