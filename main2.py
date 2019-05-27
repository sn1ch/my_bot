from vk_api.longpoll import VkLongPoll, VkChatEventType, VkEventType
import vk_api
from vk_api.utils import get_random_id
import time
import random
import get_pictures
from datetime import datetime

# token = '513cfaa4f335106331513b4363ba62682eb72516230204c1c1c72ed28be7aeee4253953ed5413aa8e91f2'
token2 = '108bcadc8fe20b7a867b86e5f1950b977575d91c921a550a56d1b2cb035d72dab8d30589a17bffff512d7'

vk_session = vk_api.VkApi(token=token2)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

# def get1(vk_session, id_group, vk):
#     try:
#         attachment = ''
#         max_num = vk.photos.get(owner_id=id_group, album_id='262105112', count=0)['count']
#         print(max_num)
#         num = random.randint(1, max_num)
#         pictures = vk.photos.get(owner_id=str(id_group), album_id='262105112', count=2, offset=num)[
#             'items']
#         buff = []
#         for element in pictures:
#             buff.append('photo' + str(id_group) + '_' + str(element['id']))
#         print(buff)
#         attachment = ','.join(buff)
#         # attachment = str(buff[0])
#         return attachment
#     except:
#         return get1(vk_session, id_group, vk)


while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение: ' + str(event.text))
            print(event.user_id, 'Время: ' + str(datetime.strftime(datetime.now(), '%H:%M:%S')))
            response = event.text.lower()
            if response == 'привет':
                vk_session.method('messages.send', {'peer_id': event.user_id, 'random_id': get_random_id(),
                                                    'message': 'Привет! Отправь "котик" если хочешь котика!'})
            elif response == 'котик':
                # attachment = get_pictures.get(vk_session, -180875568, session_api)
                # print(attachment)
                vk_session.method('messages.send',
                                  {'peer_id': event.user_id, 'random_id': get_random_id(), 'message': 'пидарк',
                                   'attachment': 'photo-180875568_456239022'})
