https://docs.opencv.org/4.x/de/d25/imgproc_color_conversions.html#color_convert_rgb_hsv


<p><a class="anchor" id="color_convert_rgb_hsv"></a></p><h2>RGB \(\leftrightarrow\) HSV </h2>
<p>In case of 8-bit and 16-bit images, R, G, and B are converted to the floating-point format and scaled to fit the 0 to 1 range.</p>
<p class="formulaDsp">
\[V \leftarrow max(R,G,B)\]
</p>
 <p class="formulaDsp">
\[S \leftarrow \fork{\frac{V-min(R,G,B)}{V}}{if \(V \neq 0\)}{0}{otherwise}\]
</p>
 <p class="formulaDsp">
\[H \leftarrow \forkfour{{60(G - B)}/{(V-min(R,G,B))}}{if \(V=R\)} {{120+60(B - R)}/{(V-min(R,G,B))}}{if \(V=G\)} {{240+60(R - G)}/{(V-min(R,G,B))}}{if \(V=B\)} {0}{if \(R=G=B\)}\]
</p>
<p> If \(H&lt;0\) then \(H \leftarrow H+360\) . On output \(0 \leq V \leq 1\), \(0 \leq S \leq 1\), \(0 \leq H \leq 360\) .</p>
<p>The values are then converted to the destination data type:</p><ul>
<li>8-bit images: \(V \leftarrow 255 V, S \leftarrow 255 S, H \leftarrow H/2 \text{(to fit to 0 to 255)}\)</li>
<li>16-bit images: (currently not supported) \(V &lt;- 65535 V, S &lt;- 65535 S, H &lt;- H\)</li>
<li>32-bit images: H, S, and V are left as is</li>
</ul>
