import cv2
import numpy as np
from pathlib import Path
from tqdm.auto import tqdm


#image_dir = Path("../valid/")
#image_suffixes = [
#    ".png",
#    ".jpg",
#]
#
#image_paths = []
#for suffix in image_suffixes:
#    image_paths.extend(image_dir.glob(f"*{suffix}"))
#
##print(f"{image_paths = }")
#h_distinct = np.array([], dtype=np.uint8)
#for p in tqdm(image_paths):
#    bgr = cv2.imread(str(p))
#    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
#    h = hsv[..., 0]
#    h_distinct = np.concatenate((h_distinct, np.unique(h)))
#    h_distinct = np.unique(h_distinct)
#    #print(f"{h_distinct = }")
#    #import ipdb; ipdb.set_trace()
#print(f"{h_distinct = }")
#print(f"{h_distinct.shape = }")


n_intensities = 2**8
all_uint8_bgr = np.empty((1, n_intensities**3, 3), dtype=np.uint8)
print("Building the array of all colors (uint8)")
for b in tqdm(range(n_intensities)):
    for g in range(n_intensities):
        for r in range(n_intensities):
            i = (n_intensities**2)*b + n_intensities*g + r
            all_uint8_bgr[0, i] = np.array([[[b,g,r]]], dtype=np.uint8)
#plt.matshow(all_uint8_bgr)
#plt.show()
import ipdb; ipdb.set_trace()
hsv = cv2.cvtColor(all_uint8_bgr, cv2.COLOR_BGR2HSV)
h = hsv[..., 0]
h_distinct = np.unique(h)
print(f"{h_distinct = }")
print(f"{h_distinct.shape = }")


