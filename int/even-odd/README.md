### Parity Check Implementation Comparison
Experiments showed, maybe somewhat <b>surprisingly</b>, that
- on smaller integers (i.e. <code>Test01</code>), <code><b>modulo.py</b></code> seems to be <b>faster</b>
- on bigger integers (i.e. <code>Test02</code>), <code><b>bitwise_and.py</b></code> looks <b>faster</b>


<pre>
(tf2.2.0-py3.6) [phunc20@artichaut-X220 even-odd]$ python bitwise_and.py
Test01 took 0.2229928970336914 (sec)
Test02 took 2.8073081970214844 (sec)
(tf2.2.0-py3.6) [phunc20@artichaut-X220 even-odd]$ python bitwise_and.py
Test01 took 0.22194910049438477 (sec)
Test02 took 2.834136486053467 (sec)
(tf2.2.0-py3.6) [phunc20@artichaut-X220 even-odd]$ python bitwise_and.py
Test01 took 0.2531590461730957 (sec)
Test02 took 2.808337688446045 (sec)
(tf2.2.0-py3.6) [phunc20@artichaut-X220 even-odd]$ python modulo.py
Test01 took 0.19445252418518066 (sec)
Test02 took 2.9149699211120605 (sec)
(tf2.2.0-py3.6) [phunc20@artichaut-X220 even-odd]$ python modulo.py
Test01 took 0.19482183456420898 (sec)
Test02 took 2.952134132385254 (sec)
(tf2.2.0-py3.6) [phunc20@artichaut-X220 even-odd]$ python modulo.py
Test01 took 0.2371220588684082 (sec)
Test02 took 2.8577136993408203 (sec)
</pre>

