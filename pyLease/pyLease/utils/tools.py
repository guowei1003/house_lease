# coding:utf-8

# author: Guo wei Cao
import time


def dateFormat(d_time, spider='data_58', time_type='p'):
    """
    格式化时间
    :param d_time: 输入时间
    :param spider: 爬虫:data_58
    :param time_type: 格式化类型:p:public,u:update
    :return: 标准时间
    """
    now_time = time.time()
    r_time = None
    if spider == 'data_58' and time_type == 'p':
        if ""
    elif spider == 'data_58' and time_type == 'u':
        pass
    elif spider == 'data_anjuke' and time_type == 'p':
        pass
    elif spider == 'data_anjuke' and time_type == 'u':
        pass
    else:
        r_time = '未知时间'

    return r_time
