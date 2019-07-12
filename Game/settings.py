#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class Settings():
    """存储所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5