import os
import sys
import math
import random
import numpy as np
import cv2

# Root directory of the project
ROOT_DIR = os.path.abspath("../../")

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn.config import Config
from mrcnn import utils

class BuildingDataset(utils.Dataset):
    def load_building(self, dataset_dir, subset):
        self.add_class('building',1,'building')
        assert subset in ['train','val','test']
        dataset_dir = os.path.join(dataset_dir,subset)
        self.img_dir = dataset_dir
        self.mask_dir =
        image_ids = os.listdir(dataset_dir)
        for image_id in image_ids:
            self.add_image('building',image_id,os.path.join(dataset_dir,image_id))
    def load_mask(self, image_id):
        info = self.image_info(image_id)
