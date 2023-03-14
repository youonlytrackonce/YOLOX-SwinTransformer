#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]
        
        #  model config  #
        self.num_classes = 1
        self.depth = 1.00
        self.width = 1.00

        #  swin config #
        self.swin_embed_dim = 128
        self.swin_depths = [2, 2, 18, 2]
        self.swin_num_heads = [4, 8, 16, 32]
        self.swin_out_channels = [128, 256, 512, 1024]
        self.swin_drop_path_rate = 0.3
        self.swin_pretrained = True
        self.swin_pretrained_type = "COCO" 
        self.swin_pretrained_checkpoint = "./pretrained/cascade_mask_rcnn_swin_base_patch4_window7.pth"
    
        #  transform config  #
        self.degrees = 120.0
        #  dataloader config #
        self.data_num_workers = 2
        self.input_size = (640, 640)
        self.random_size = (20, 20)
        self.data_dir = "./datasets/trackeveryseason"
        self.train_ann = "train.json"
        self.val_ann = "val.json"

        # training config #
        self.basic_lr_per_img = 0.01 / 64.0
        self.eval_interval = 5

        # testing config #
        self.test_size = (640, 640)
        self.test_conf = 0.2
        self.nmsthre = 0.2
