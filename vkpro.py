# все обновления софта создаются автором: hussaroff | lzt: @runduk
import vk_api
import getpass
import time
print('''
    VVV     VVV  KKK   KKK  PPPPPPPPP   RRRRRRRRR   OOOOOOOOOOO
    VVV     VVV  KKK  KKK   PPPPPPPPPP  RRRRRRRRRR  OOOO   OOOO
    VVV     VVV  KKKKKK     PPP     PP  RRR     RR  OOO     OOO
     VVV   VVV   KKKKK      PPP    PP   RRR    RR   OOO     OOO
      VVV VVV    KKKKKK     PPPPPPPP    RRRRRRRRR   OOO     OOO
       VVVVV     KKK  KKK   PPP         RRR    RRR  OOOO   OOOO
        VVV      KKK   KKK  PPP         RRR     RRR OOOOOOOOOOO

                       AUTOR: VK.COM/ID388038821
                             VERSION: 0.3
''')

enter = input("Если вы согласны на обработку Ваших данных этим софтом, жмите Enter: ")
print("Данные с пометкой '*' автоматически будут запоминаться системой.")
login = input("Введите Ваш логин от страницы: ") # эти данные нужны для API
password = getpass.getpass("* Введите Ваш пароль от страницы(без отображения): ") # эти данные нужны для API
vk_session = vk_api.VkApi(login, password)
vk_session.auth()
vk = vk_session.get_api()

print("Данные введены верно, нет ошибок и мы готовы начать работать с вами!\n")

def body():
    print("\nИнформация по пользованию, методы и баги:\n post - Послать пост-сообщение на вашу стену\n statusname - Поменять статус\n onoff - Послать сайту информацию что вы online/offline")
    print(" spamtitle - Спам сменой названия беседы\n sendmsg - Отправить сообщение пользователю/беседе по ID\n profileinfo - Получить инофрмацию о своем профиле(полную) ")
    print(" friends - Информация о ваших друзьях\n ephoto - Сделать аватарку некликаберной\n cbuser - Вернуть пользователя в беседу")
    print(" textact - Бесконечно выводить статус набора сообщения или аудио в беседе/ЛС \n")
    info = input("Введите метод-значение: ")
    if info == 'post':
        message1 = input("Введите любое сообщение на вашу стену: ")
        print(vk.wall.post(message=message1), "\n")
        body()
    elif info == 'textact':
        print("Бесконечно выводить статус набора сообщения или аудио в беседе/ЛС")
        chatinfo = input("Беседа(1) это или ЛС(2): ")
        if chatinfo == '1':
            chatid1 = input("Введите chatid: ")
            chati = input("Аудио(1) или печатание(2): ")
            if chati == '1':
                print("Будет работать, пока работает программа!")
                while int(chati) < 10:
                    time.sleep(8)
                    print(vk.messages.setActivity(user_id=chatid1, type='audiomessage'))
            elif chati == '2':
                print("Будет работать, пока работает программа!")
                while int(chati) < 10:
                    time.sleep(8)
                    print(vk.messages.setActivity(user_id=chatid1, type='typing'))
            else:
                body()
        elif chatinfo == '2':
            chatid1 = input("Введите id пользователя: ")
            chati = input("Аудио(1) или печатание(2): ")
            if chati == '1':
                print("Будет работать, пока работает программа!")
                while int(chati) < 10:
                    time.sleep(8)
                    print(vk.messages.setActivity(user_id=chatid1, type='audiomessage'))
            elif chati == '2':
                print("Будет работать, пока работает программа!")
                while int(chati) < 10:
                    time.sleep(8)
                    print(vk.messages.setActivity(user_id=chatid1, type='typing'))
            else:
                body()
        else:
            print("Вы ввели некоректные данные и возвращены на главную страницу")
            body()
        body()
    elif info == 'statusname':
        statusi = input("Хотите ли вы посмотреть статус любого человека введя его id?(answer y/n): ")
        if statusi == 'y':
            userid = input("Введите ID профиля ВК(только цифры, без id): ")
            print(vk.status.get(user_id=userid), "\n")
            what = input("Идем дальше или хватит?(answer y/n): ")
        elif statusi == 'n':
            message1 = input("Введите любой желаемый статус: ")
            print(vk.status.set(text=message1))
            body()
        else:
            body()
        if what == 'y':
            message1 = input("Введите любой желаемый статус, если не надо жмите n: ")
            print(vk.status.set(text=message1))
        elif message1 == 'n':
            print("Отменено\n")
        else:
            print(vk.status.set(text=message1))
        body()
    elif info == 'onoff':
        print("Выберите, хотите вы онлайн(on) или оффлайн(off)?")
        onoff = input("Хочу быть on/off: ")
        if onoff == 'off':
            print(vk.account.setOffline())
            print("Вы больше не в сети.\n")
        elif onoff == 'on':
            print(vk.account.setOnline())
            print("Вы появились в сети.\n")
        else:
            print("Вы не выбрали допустимые параметры!\n")
        body()
    elif info == 'sendmsg':
        smgid = input("Вы хотите отправить сообщение человеку или в беседу? (answer m/c): ")
        if smgid == 'm':
            idmsg = input("Введите ID человека(без id): ")
            sendmsg = input("Введите ваше любое сообщение человеку: ")
            vk.messages.send(user_id=idmsg, message=sendmsg, random_id='12345')
        elif smgid == 'c':
            idmsg1 = input("Введите ID беседы: ")
            sendmsg1 = input("Введите ваше любое сообщение в беседу: ")
            vk.messages.send(chat_id=idmsg1, message=sendmsg1, random_id='445235')
        else:
            body()
        body()
    elif info == 'spamtitle':
        chatid = input("Введите номер беседы: ")
        spam = input("Введите новое название(вы можете спамить так): ")
        spam1 = input("Проспамить 5 раз сменой названия беседы? (answer y/n): ")
        if spam1 == 'y':
            print(vk.messages.editChat(chat_id=chatid, title=spam))
            print(vk.messages.editChat(chat_id=chatid, title=spam))
            print(vk.messages.editChat(chat_id=chatid, title=spam))
            print(vk.messages.editChat(chat_id=chatid, title=spam))
            print(vk.messages.editChat(chat_id=chatid, title=spam))
        elif spam1 == 'n':
            print(vk.messages.editChat(chat_id=chatid, title=spam))
        else:
            body()
        body()
    elif info == 'profileinfo':
        yn = input("Получить информацию о своем профиле(answer y/n):  ")
        if yn == 'n':
            body()
        elif yn == 'y':
            print(vk.account.getProfileInfo())
        else:
            body()
        body()
    elif info == 'cbuser':
        print("Вы должны быть админом беседы или быть пригласившим пользователя в беседу, он должен быть в друзьях у вас!")
        chat = input("Введите ID беседы: ")
        user = input("Введите ID пользователя, который сам вышел из беседы:  ")
        print(vk.messages.removeChatUser(chat_id=chat, user_id=user))
        print(vk.messages.addChatUser(chat_id=chat, user_id=user))
        print("Пользователь успешно возвращен!\n")
        body()
    elif info == 'friends':
        print(" add - добавить или отправить заявку в друзья по id\n arefriends - узнать информацию о заявке пользователя\n friendsdel - удалить или отклонить друга/заявку")
        print(" getmutual - получить список общих друзей между пользователями\n onlinefriends - получить список друзей, которые онлайн(не только ваших друзей)\n")
        yn = input("Введите значение: ")
        if yn == 'add':
            userid = input("Введите ID профиля для отправки или принятия заявки в друзья: ")
            text = input("Текст для отправки заявки(если не надо, оставьте поле пустым и жмите ENTER): ")
            print(vk.friends.add(user_id=userid, text=text))
        elif yn == 'arefriends':
            print("Выведет 0 - пользователь не является другом, 1 – отправлена заявка/подписка пользователю,\n2 – имеется входящая заявка/подписка от пользователя, 3 – пользователь является другом;,")
            userids = input("Введите ID или IDs пользователя(лей): ")
            print(vk.friends.areFriends(user_ids=userids))
        elif yn == 'friendsdel':
            delete = input("Удалить из друзей или отклонить заявку в друзья по ID(так-же отмена исходящей заявки в друзья): ")
            print(vk.friends.delete(user_id=delete))
        elif yn == 'getmutual':
            prof1 = input("Введите ID первого друга: ")
            prof2 = input("Введите ID второго друга: ")
            print(vk.friends.getMutual(source_uid=prof1, target_uid=prof2))
        elif yn == 'onlinefriends':
            online = input("Введите ID пользователя у которого вы хотите узнать онлайн друзей(если ваших друзей, то ничего не пишите): ")
            print(vk.friends.getOnline(user_id=online, list_id='1', online_mobile='bool 1'))
        else:
            print("Вы ввели неверное значение или нарошно вышли из категории")
            body()
    elif info == 'ephoto':
        yn = input("Надо удалить фото, и сделать аватарку некликабельной?(answer y/n): ")
        if yn == 'y':
            userid = input("Удалите все фотографии которые были на аватарке, кроме желаемой аватарки (press ENTER to continue)")
            text = print('''var photoget = API.photos.get({album_id: "profile", rev: 1, extented: 1});
var photoid = photoget.items[0].id;
var deletep = API.photos.delete({photo_id: photoid});
var restorep = API.photos.restore({photo_id: photoid});
var check = API.photos.get({album_id: "profile", rev: 1, extented: 1});
if(check.items.length == 0){
return "noclick";
} else {
return "click";
}
var photoget = API.photos.get({album_id: "profile", rev: 1, extented: 1});
var photoid = photoget.items[0].id;
var deletep = API.photos.delete({photo_id: photoid});
var restorep = API.photos.restore({photo_id: photoid});
var check = API.photos.get({album_id: "profile", rev: 1, extented: 1});
if(check.items.length == 0){
return "noclick";
} else {
return "click";
}''')
            print(vk.execute(code=text))
        elif yn == 'n':
            body()
        else:
            print("Вы ввели неверное значение или нарошно вышли из категории")
            body()
        body()
    else:
        print("\nПока в разработке!\nИли вы ошиблись в выборе!\n")
        body()
body()
