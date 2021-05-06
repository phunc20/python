
## `glob()` Non-Iteratively
`glob()` grabs only matched filenames in the specified directory **non-iteratively**. Cf. the following example.

`train_short_audio/` is a folder of the following structure, where each of its subfolders contains `*.ogg` files only `*.ogg` files only.
```
In [1]: !pwd
/home/phunc20/datasets/kaggle/birdclef-2021/train_short_audio

In [2]: ls
acafly/   bkhgro/   butsal1/  compot1/  gockin/   killde/   normoc/   rawwre1/  sancra/   tenwar/   whwbec1/
acowoo/   bkmtou1/  buwtea/   comrav/   gocspa/   labwoo/   norpar/   rcatan1/  sander/   thbeup1/  whwdov/
aldfly/   bknsti/   cacgoo1/  comyel/   goftyr1/  larspa/   norsho/   rebnut/   savspa/   thbkin/   wilfly/
ameavo/   blbgra1/  cacwre/   coohaw/   gohque1/  laufal1/  norwat/   rebsap/   saypho/   thswar1/  willet1/
amecro/   blbthr1/  calqua/   cotfly1/  goowoo1/  laugul/   nrwswa/   rebwoo/   scamac1/  towsol/   wilsni1/
...
```
If we let `folder` be the `Path` object pointing to this directory, then we have
```
In [3]: from pathlib import Path

In [4]: folder = Path.cwd()

In [5]: list(folder.glob("*.ogg"))
Out[5]: []

In [6]: list((folder / "westan").glob("*.ogg"))[:3]
Out[6]:
[PosixPath('/home/phunc20/datasets/kaggle/birdclef-2021/train_short_audio/westan/XC559251.ogg'),
 PosixPath('/home/phunc20/datasets/kaggle/birdclef-2021/train_short_audio/westan/XC441368.ogg'),
 PosixPath('/home/phunc20/datasets/kaggle/birdclef-2021/train_short_audio/westan/XC146191.ogg')]

```




## Regex in <code>glob()</code>
Regex in <code>glob()</code> is <b>different</b> from regex in <code>grep</code>, e.g. the dollar sign (<b><code>$</code></b>) does not represent <b>End Of Line</b>, neither does <code><b>^</b></code> represent <b>Begin Of Line</b>.

```
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

In [5]: gogi
Out[5]: PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi')

In [6]: gogi.glob("0$")
Out[6]: <generator object Path.glob at 0x7f3721d514d0>

In [7]: list(gogi.glob("0$"))
Out[7]: []

In [8]: list(gogi.glob("0\$"))
Out[8]: []


In [10]: list(gogi.glob("*0$"))
Out[10]: []

In [11]: list(gogi.glob(".*0$"))
Out[11]: []

In [12]: list(gogi.glob("mp4"))
Out[12]: []

In [13]: list(gogi.glob("mp4$"))
Out[13]: []

In [14]: list(gogi.glob("*mp4"))
Out[14]:
[PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002330000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002359000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002240000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002390000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002242000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002280000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002326000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002266000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002210000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002319000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002343000000.mp4')]

In [15]: list(gogi.glob("*0"))
Out[15]:
[PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002242000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002359000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002240000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002390000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002319000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002330000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002266000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002326000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002343000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002210000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002280000000')]

In [16]: list(gogi.glob("*0$"))
Out[16]: []

In [17]: list(gogi.glob("0*0"))
Out[17]:
[PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002242000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002359000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002240000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002390000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002319000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002330000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002266000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002326000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002343000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002210000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002280000000')]

In [18]: ls
00000002210000000/     00000002280000000/     00000002343000000/              03_test-corners.ipynb
00000002210000000.mp4  00000002280000000.mp4  00000002343000000.mp4           04_begin-crop.ipynb
00000002240000000/     00000002319000000/     00000002359000000/              __pycache__/
00000002240000000.mp4  00000002319000000.mp4  00000002359000000.mp4           table_corners.py
00000002242000000/     00000002326000000/     00000002390000000/              trash.py
00000002242000000.mp4  00000002326000000.mp4  00000002390000000.mp4
00000002266000000/     00000002330000000/     01_cut-frame.sh*
00000002266000000.mp4  00000002330000000.mp4  02_accidentally-delete-file.md

In [19]: list(gogi.glob("0[0-9]*0"))
Out[19]:
[PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002242000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002359000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002240000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002390000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002319000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002330000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002266000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002326000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002343000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002210000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002280000000')]

In [20]: list(gogi.glob("mp45"))
Out[20]: []

In [21]: list(gogi.glob("mp4$"))
Out[21]: []

In [22]: list(gogi.glob("0[0-9]*0"))
Out[22]:
[PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002242000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002359000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002240000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002390000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002319000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002330000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002266000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002326000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002343000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002210000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002280000000')]

In [23]: list(gogi.glob("000[0-9]*000"))
Out[23]:
[PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002242000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002359000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002240000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002390000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002319000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002330000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002266000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002326000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002343000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002210000000'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002280000000')]

In [24]: list(gogi.glob("000[0-9]*000."))
Out[24]: []

In [25]: list(gogi.glob("000[0-9]*000.mp4"))
Out[25]:
[PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002330000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002359000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002240000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002390000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002242000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002280000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002326000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002266000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002210000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002319000000.mp4'),
 PosixPath('/home/phunc20/samsung-SATA/datasets/food-on-table/gogi/00000002343000000.mp4')]
```
