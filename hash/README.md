- Hash randomization
  ```bash
  (py3.10) $ python -c "print(hash('Lorem'))"
  -2768474445891358110
  (py3.10) $ python -c "print(hash('Lorem'))"
  -8389030602155432467
  (py3.10) $ python -c "print(hash('Lorem'))"
  5606515980006570896
  (py3.10) $ export PYTHONHASHSEED=42
  (py3.10) $ python -c "print(hash('Lorem'))"
  -5730733714012086837
  (py3.10) $ python -c "print(hash('Lorem'))"
  -5730733714012086837
  (py3.10) $ python -c "print(hash('Lorem'))"
  -5730733714012086837
  (py3.10) $ unset PYTHONHASHSEED
  (py3.10) $ python -c "print(hash('Lorem'))"
  789397106792935266
  (py3.10) $ python -c "print(hash('Lorem'))"
  4868574452902325336
  (py3.10) $ python -c "print(hash('Lorem'))"
  6657707266505423509
  (py3.10) $
  ```
  Aside from using `export`, one could achieve the same by
  ```bash
  (py3.10) $ PYTHONHASHSEED=42 python -c "print(hash('Lorem'))"
  -5730733714012086837
  (py3.10) $ PYTHONHASHSEED=42 python -c "print(hash('Lorem'))"
  -5730733714012086837
  (py3.10) $ PYTHONHASHSEED=42 python -c "print(hash('Lorem'))"
  -5730733714012086837
  (py3.10) $ python -c "print(hash('Lorem'))"
  -611984041169765746
  (py3.10) $ python -c "print(hash('Lorem'))"
  -5728486443295551611
  (py3.10) $ python -c "print(hash('Lorem'))"
  773670319942648720
  ```
