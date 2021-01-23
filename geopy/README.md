## Range of latitude, longitud and altitude
- **latitude**: floating point value in **degrees** $\;\in [-90, 90]\;$
- **longitude**: floating point value in **degrees** $\;\in [-180, 180]\;$
- **altitude**: floating point value in **kilometers** $\;\in [-\infty, \infty]\;$ (Default to `0`)


```python
In [1]: import geopy

In [2]: p1 = geopy.point.Point(30, -181, 0)

In [3]: p1
Out[3]: Point(30.0, 179.0, 0.0)

In [4]: p1 = geopy.point.Point(30, 180, 0)

In [5]: p1
Out[5]: Point(30.0, 180.0, 0.0)

In [6]: p1 = geopy.point.Point(30, -180, 0)

In [7]: p1
Out[7]: Point(30.0, -180.0, 0.0)

In [8]: p1 = geopy.point.Point(30, 181, 0)

In [9]: p1
Out[9]: Point(30.0, -179.0, 0.0)

In [10]: p1 = geopy.point.Point(91, 0 , 0)
/home/phunc20/.virtualenvs/rtree-py3.7/bin/ipython:1: UserWarning: Latitude normalization has been prohibited in the newer versions of geopy, because the normalized value happened to be on a different pole, which is probably not what was meant. If you pass coordinates as positional args, please make sure that the order is (latitude, longitude) or (y, x) in Cartesian terms.
  #!/home/phunc20/.virtualenvs/rtree-py3.7/bin/python
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-10-a78df9ddf36d> in <module>
----> 1 p1 = geopy.point.Point(91, 0 , 0)

~/.virtualenvs/rtree-py3.7/lib/python3.7/site-packages/geopy/point.py in __new__(cls, latitude, longitude, altitude)
    185
    186         latitude, longitude, altitude = \
--> 187             _normalize_coordinates(latitude, longitude, altitude)
    188
    189         self = super().__new__(cls)

~/.virtualenvs/rtree-py3.7/lib/python3.7/site-packages/geopy/point.py in _normalize_coordinates(latitude, longitude, altitude)
     72                       '(latitude, longitude) or (y, x) in Cartesian terms.',
     73                       UserWarning, stacklevel=3)
---> 74         raise ValueError('Latitude must be in the [-90; 90] range.')
     75
     76     if abs(longitude) > 180:

ValueError: Latitude must be in the [-90; 90] range.

In [11]: p1 = geopy.point.Point(0, 0 , -1)

In [12]: p1
Out[12]: Point(0.0, 0.0, -1.0)

In [13]: p1 = geopy.point.Point(0, 0 , 1e100)

In [14]: p1
Out[14]: Point(0.0, 0.0, 1e+100)

```
