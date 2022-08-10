# USAGE
# python explore_dims.py --conf conf/cars.json

# import the necessary packages
from __future__ import print_function
from custom_library.utils import Conf
from scipy import io
import numpy as np
import glob

# load the configuration file and initialize the list of widths and heights
conf    = Conf('/home/damian/Workspace/GitHub_Repos/pyimagegurus_course/02__Object_Detectors/02.04_05_and_beyond/preparing_experiment/conf/cars.json')
widths  = []
heights = []

# loop over all annotations paths
for p in glob.glob(conf["image_annotations"] + "/*.mat"):
	# load the bounding box associated with the path and update the width and height lists
	(y, h, x, w) = io.loadmat(p)["box_coord"][0]
	widths.append(  w - x)
	heights.append( h - y)

# compute the average of both the width and height lists
(avgWidth, avgHeight) = (np.mean(widths), np.mean(heights))
print(f'''[INFO] avg. width:   {avgWidth:.2f}''')
print(f'''[INFO] avg. height:  {avgHeight:.2f}''')
print(f'''[INFO] aspect ratio: {(avgWidth / avgHeight):.2f}''')