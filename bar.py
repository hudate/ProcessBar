#!/usr/bin/python3 env/python3 /usr/bin/env python3
# -*- coding: utf-8 -*-

import time


class Bar(object):

    def __init__(self, running_char='*', mask_char='#'):
        self.func_name_list = []
        self.func_time_list = []
        self.running_char = running_char
        self.mask_char = mask_char

    def name_dict(self, app_name, model_name, func_name):
        return {
            'app_name': app_name,
            'model_name': model_name,
            'func_name': func_name
        }

    def set_func_list(self, app_name, model_name, func_name):
        name_dict = self.name_dict(app_name, model_name, func_name)

        if name_dict not in self.func_name_list:
            self.func_name_list.append(name_dict)
            time_dict = name_dict
            time_dict['start_time'] = time.time()
            self.func_time_list.append(time_dict)

    def run_timedelta(self, app_name=None, model_name=None, func_name=None):
        t = time.time()
        now_process = [
            e_name
            for e_name in self.func_time_list
                if app_name == e_name['app_name'] and model_name == e_name['model_name'] and func_name == e_name['func_name']
        ][0]
        ran_time = t - now_process['start_time']
        return ran_time

    def show_bar(self, app_name, model_name, func_name, ran_time, max_value, now_value, msg):
        name_list = []
        if app_name is not None:
            name_list.append('app_name: %s' % app_name)

        if model_name is not None:
            name_list.append('model_name: %s' % model_name)

        if func_name is not None:
            name_list.append('func_name: %s' % func_name)

        _percent = now_value / max_value

        if _percent == 0.0:
            _ran_time = '%.2f' % ran_time
            _running_chars_count = int(_percent * 100)
            _percent = '%.2f' % (_percent * 100) + '%'
            string = '\t'.join(name_list) + ' \t process: [%s    %s] \t 开始' % (
                _running_chars_count * self.running_char, _percent)
        else:
            if _percent != 1.0:
                '''clear some lines content, and reprint string'''
                pass
            _total_time = ran_time / _percent
            _ran_time = '%.2f' % ran_time
            _remaining_time = '%.2f' % (_total_time - ran_time)
            _running_chars_count = int(_percent * 100)
            _percent = '%.2f' % (_percent * 100) + '%'
            string = '' + '\t'.join(name_list) + ' \t process: [%s    %s] \t 已用时间：%s \t 剩余时间：%s' % (
                _running_chars_count * self.running_char, _percent, _ran_time, _remaining_time)
        print(string)


        if msg:
            time.sleep(0.01)
            print('\t'.join(name_list)+ '\t' + msg)


    def process(self, app_name=None, model_name=None, func_name=None, max_value=None, now_value=None, msg=None):
        self.set_func_list(app_name, model_name, func_name)
        ran_time = self.run_timedelta(app_name, model_name, func_name)
        self.show_bar(app_name, model_name, func_name, ran_time, max_value, now_value, msg)



