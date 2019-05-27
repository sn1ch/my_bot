import random
import vk_api
from datetime import datetime
import time


def get(vk_session, id_group, vk):
    # print('xyu')
    try:
        attachment = ''
        print('До всего:' + str(time.ctime(time.time())))
        max_num = vk.photos.get(owner_id='-180875568', album_id='wall', count=0)['count']
        print('Время после полученя всех картинок: ' + str(time.ctime(time.time())))
        print(max_num)
        num = random.randint(1, max_num)
        pictures = vk.photos.get(owner_id=str(id_group), album_id='wall', count=2, offset=num)[
            'items']
        buff = []
        for element in pictures:
            buff.append('photo' + str(id_group) + '_' + str(element['id']))
        print(buff)
        attachment = ','.join(buff)
        return attachment
    except:
        return get(vk_session, id_group, vk)
