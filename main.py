#pip install googletrans==3.1.0a0
#pip install vk_api
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from tokens import main_token
from googletrans import Translator

translator = Translator()
vk_session = vk_api.VkApi(token=main_token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def sender(id, text):
    vk_session.method('messages.send',{'user_id':id, 'message':text,'random_id':0})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text
            id = event.user_id
            print("ИД: "+ str(id)+ " сообщение: "+ msg)
            answer = ""
            if translator.detect(msg).lang=='ru':
                answer = translator.translate(msg, dest='en')
                sender(id, answer.text + '\nопределено: ' + answer.src)
            else:
                answer = translator.translate(msg, dest='ru')
                sender(id, answer.text+'\nопределено: '+answer.src)
            print(answer.text)
