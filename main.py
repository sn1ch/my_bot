from vk_api.longpoll import VkLongPoll, VkChatEventType
import vk_api
from vk_api.utils import get_random_id
import time
import random

token = '513cfaa4f335106331513b4363ba62682eb72516230204c1c1c72ed28be7aeee4253953ed5413aa8e91f2'
vk_session = vk_api.VkApi(token=token)
# session_api = vk_session.get_api()
# longpoll = VkLongPoll(vk_session)
while True:
    messages = vk_session.method('messages.getConversations', {'offset': 0, 'count': 20, 'filter': 'unread'})
    if messages['count'] >= 1:
        id1 = messages['items'][0]['last_message']['from_id']
        body = messages['items'][0]['last_message']['text']
        if body.lower() == 'привет':
            vk_session.method('messages.send', {'peer_id': id1, 'random_id': get_random_id(),
                                                'message': 'Привет! Отправь "котик" если хочешь котика!'})
        elif body.lower() == 'котик':
            # x = random.choice(cats)
            vk_session.method('messages.send',
                              {'peer_id': id1, 'random_id': get_random_id(), 'message': 'Вот держи :)',
                               'attachment': 'photo-180875568_456239018'})
        else:
            vk_session.method('messages.send',
                              {'peer_id': id1, 'random_id': get_random_id(), 'message': 'Я не понял тебя!'})
    time.sleep(1)
