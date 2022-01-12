# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 下午5:59
# @Author  : Aydar
# @FileName: helpers.py
# @Software: PyCharm
# @Telegram   ：aydardev
import json
from uuid import UUID




class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)