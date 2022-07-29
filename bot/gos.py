import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

main_token = "e4128d88581696f9382e18f3d1852b9b463041116389f16f0b27d6c055d1dd923514e1eab8a1586369746"
vk_session = vk_api.VkApi(token=main_token)

bot_id = 213622107

longpoll = VkBotLongPoll(vk_session, bot_id)

status = "main"

gsv = "@zhenya_bruna(ГСВ)"
gcv = "@zhenya_bruna(ГКВ)"
st = "@zhenya_bruna(СТ)"
judge = "@zhenya_bruna(Судья)"
gp = "@zhenya_bruna(ГП)"
guber = "@zhenya_bruna(Губернатор)"
gcl = "@zhenya_bruna(ГЦЛ)"
stk = "@zhenya_bruna(СтК)"
cb = "@zhenya_bruna(ЦБ)"
lspd = "@zhenya_bruna(ЛСПД)"
sfpd = "@zhenya_bruna(СФПД)"
swat = "@zhenya_bruna(СВАТ)"
rcsd = "@zhenya_bruna(РКШД)"
fbi = "@zhenya_bruna(ФБР)"
lsmc = "@zhenya_bruna(ЛСМЦ)"
sfmc = "@zhenya_bruna(СФМЦ)"
lvmc = "@zhenya_bruna(ЛВМЦ)"
lsa = "@zhenya_bruna(ЛСа)"
sfa = "@zhenya_bruna(ВМС)"
msp = "@zhenya_bruna(ТСР)"
rls = "@zhenya_bruna(СМИ ЛС)"
rsf = "@zhenya_bruna(СМИ СФ)"
rlv = "@zhenya_bruna(СМИ ЛВ)"


# ГС/ЗГС ГОС

access_full = ["489856771", "475362255", "342420933"]

# Government

access_full_government = ["608273181"]
access_spec_government = ["665664706"]

# Central Office

access_full_co = ["342420933", "471076385"]
access_spec_co = ["543775126", "547781950", "100437381"]

# Department of Justice

acceess_full_justice = ["360669127", "481698071"]
access_spec_justice = ["454427393", "435861554", "561978801", "30732603"]

# Department of Health

access_full_health = ["676100115"]
access_spec_health = ["466657339", "450908343", "482497386"]

# Departament of Defense

access_full_defense = ["341995691"]
access_spec_defense = ["709048695", "522188393"]

# Mass Media

access_full_media = ["454108081", "572994700"]
access_spec_media = ["482497386"]

statuses = ["main", "menu government", "menu co", "menu juctice", "menu health", "menu defense", "menu media"]

accesses = access_full + access_full_government + access_spec_government + access_full_co + access_spec_co + acceess_full_justice + access_spec_justice + access_full_health + access_spec_health + access_full_defense + access_spec_defense + access_full_media + access_spec_media

statuses_menu_organizations = ["menu gcl", "menu stk", "menu cb", "menu lspd", "menu sfpd", "menu swat", "menu fbi", "menu rcsd", "menu lsmc", "menu sfmc", "menu lvmc", "menu lsa", "menu sfa", "menu msp", "menu rls", "menu rsf", "menu rlv"]


def check_status(status):
    for string in statuses_menu_organizations:
        if string == str(status):
            return True
    return False

def check_access(user_id, list):
    for id in list:
        if str(id) == str(user_id):
            return True
    return False


def sender(text, id, keyboard=None):
    if keyboard != None:
        vk_session.method("messages.send",
                          {"user_id": id, "message": text, "random_id": 0, "keyboard": keyboard.get_keyboard()})
    else:
        vk_session.method("messages.send", {"user_id": id, "message": text, "random_id": 0})


def send_noaccess_message(id, isAuth=True):
    if isAuth:
        sender(
            "Отказано в доступе! Вы не являетесь следящим за данным министерством! Если это не так, то отпишите @id342420933(Жене Ветрову) для получения доступа!",
            int(id))
    else:
        sender(
            "Отказано в доступе! Если вы являетесь следящим за гос. структурой, то отпишите @id342420933(Жене Ветрову) для получения доступа!",
            int(id))


def chat_sender(text, id):
    vk_session.method("messages.send", {"chat_id": id, "message": text, "random_id": 0})


def getMainKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Меню Пра-Во", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню ЦА", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Меню МЮ", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню МЗ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Меню МО", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню СМИ", VkKeyboardColor.PRIMARY)
    return keyboard


def getGovernmentKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Меню предов", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Меню выговоров", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Позвать всех в игру!", VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard


def getGovernmentPredsKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Пред ГСВ", VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Пред ГКВ", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Пред СТ", VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Пред Судье", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Пред Губернатору", VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Пред ГП", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard

def getGovernmentVigsKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Выговор ГСВ", VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Выговор ГКВ", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Выговор СТ", VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Выговор Судье", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Выговор Губернатору", VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Выговор ГП", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard

def getCoKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Меню ГЦЛ", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню СтК", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Меню ЦБ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Позвать всех в игру!", VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard


def getJusticeKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Меню ЛСПД", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню СФПД", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Меню СВАТ", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню РКШД", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню ФБР", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Позвать всех в игру!", VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard


def getHealthKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Меню ЛСМЦ", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню СФМЦ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Меню ЛВМЦ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Позвать всех в игру!", VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard


def getDefenseKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Меню ЛСа", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню СФа", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Меню ТСР", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Позвать всех в игру!", VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard


def getMediaKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Меню СМИ ЛС", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню СМИ СФ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Меню СМИ ЛВ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Позвать всех в игру!", VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard

def getOrgKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Выдача преда", VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Выдача выговора", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Выдача нормы", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Выдача нормы дискорда", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Сообщение в орг. беседу", VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard

def getPunishKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard


def getKeyboardByStatus():
    if status == "main":
        return getMainKeyboard()
    elif status == "menu government":
        return getGovernmentKeyboard()
    elif status == "menu co":
        return getCoKeyboard()
    elif status == "menu justice":
        return getJusticeKeyboard()
    elif status == "menu health":
        return getHealthKeyboard()
    elif status == "menu defense":
        return getDefenseKeyboard()
    elif status == "menu media":
        return getMediaKeyboard()
    elif check_status(status):
        return getOrgKeyboard()
    elif status == "pred government":
        return getGovernmentPredsKeyboard()
    elif status == "vig government":
        return getGovernmentVigsKeyboard()
    elif status.startswith("pred") or status.startswith("vig"):
        return getPunishKeyboard()

def makePunish(in_status, isPred, msg, id):
    target = getTarget(in_status)
    if isPred:
        chat_sender(target + ", +предупреждение за " + msg, 1)
    else:
        chat_sender(target + ", +выговор за " + msg, 1)



def getTarget(status):
    target = ""
    if "gcv" in status:
        target = gcv
    elif "gsv" in status:
        target = gsv
    elif "stk" in status:
        target = stk
    elif "judge" in status:
        target = judge
    elif "guber" in status:
        target = guber
    elif "gp" in status:
        target = gp
    elif "gcl" in status:
        target = gcl
    elif "st" in status:
        target = st
    elif "cb" in status:
        target = cb
    elif "lspd" in status:
        target = lspd
    elif "sfpd" in status:
        target = sfpd
    elif "swat" in status:
        target = swat
    elif "rcsd" in status:
        target = rcsd
    elif "fbi" in status:
        target = fbi
    elif "lsmc" in status:
        target = lsmc
    elif "sfmc" in status:
        target = sfmc
    elif "lvmc" in status:
        target = lvmc
    elif "lsa" in status:
        target = lsa
    elif "sfa" in status:
        target = sfa
    elif "msp" in status:
        target = msp
    elif "rls" in status:
        target = rls
    elif "rsf" in status:
        target = rsf
    elif "rlv" in status:
        target = rlv
    return target

def saveVariables():
    text = "Вот тут твоя часть кода"

while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.from_chat:
                    id = event.chat_id
                    msg = event.object.message["text"]
                else:
                    id = event.object.message["from_id"]
                    message = event.object.message["text"]
                    msg = message.lower()

                    if check_access(id, accesses):
                        if msg == "откат":
                            status = "main"
                            sender("Работаем", id, getKeyboardByStatus())
                        if status == "main":
                            if msg == "меню пра-во":
                                if check_access(id, access_full_government) or check_access(id,
                                                                                            access_spec_government) or check_access(
                                        id, access_full):
                                    status = "menu government"
                                    sender("Перехожу в ваше меню", id, getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "меню ца":
                                if check_access(id, access_full_co) or check_access(id, access_spec_co) or check_access(
                                        id, access_full):
                                    status = "menu co"
                                    sender("Перехожу в ваше меню", id, getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "меню мю":
                                if check_access(id, acceess_full_justice) or check_access(id,
                                                                                          access_spec_justice) or check_access(
                                        id, access_full):
                                    status = "menu justice"
                                    sender("Перехожу в ваше меню", id, getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "меню мз":
                                if check_access(id, access_full_health) or check_access(id,
                                                                                        access_spec_health) or check_access(
                                        id, access_full):
                                    status = "menu health"
                                    sender("Перехожу в ваше меню", id, getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "меню мо":
                                if check_access(id, access_full_defense) or check_access(id,
                                                                                         access_spec_defense) or check_access(
                                        id, access_full):
                                    status = "menu defense"
                                    sender("Перехожу в ваше меню", id, getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "меню сми":
                                if check_access(id, access_full_media) or check_access(id,
                                                                                       access_spec_media) or check_access(
                                        id, access_full):
                                    status = "menu media"
                                    sender("Перехожу в ваше меню", id, getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            else:
                                sender("Начинаю свою работу", id, getKeyboardByStatus())
                        elif status == "menu government":
                            if msg == "обратно":
                                status = "main"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                            elif msg == "позвать всех в игру!":
                                chat_sender("@all, В ИГРУ!", 1)
                                sender("Позвал", id, getKeyboardByStatus())
                            elif msg == "меню предов":
                                status = "pred government"
                                sender("Перехожу в меню предов", id, getKeyboardByStatus())
                            elif msg == "меню выговоров":
                                status = "vig government"
                                sender("Перехожу в меню выговоров", id, getKeyboardByStatus())
                        elif status == "menu co":
                            if msg == "меню гцл":
                                status = "menu gcl"
                                sender("Переходим в меню ГЦЛ", id, getKeyboardByStatus())
                            elif msg == "меню стк":
                                status = "menu stk"
                                sender("Переходим в меню СтК", id, getKeyboardByStatus())
                            elif msg == "меню цб":
                                status = "menu cb"
                                sender("Переходим в меню ЦБ", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "main"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                            elif msg == "позвать всех в игру!":
                                chat_sender("@all, В ИГРУ!", 1)
                                sender("Позвал", id, getKeyboardByStatus())
                        elif status == "menu justice":
                            if msg == "меню лспд":
                                status = "menu lspd"
                                sender("Переходим в меню ЛСПД", id, getKeyboardByStatus())
                            elif msg == "меню сфпд":
                                status = "menu sfpd"
                                sender("Переходим в меню СФПД", id, getKeyboardByStatus())
                            elif msg == "меню сват":
                                status = "menu swat"
                                sender("Переходим в меню СВАТ", id, getKeyboardByStatus())
                            elif msg == "меню фбр":
                                status = "menu fbi"
                                sender("Переходим в меню ФБР", id, getKeyboardByStatus())
                            elif msg == "меню ркшд":
                                status = "menu rcsd"
                                sender("Переходим в меню РКШД", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "main"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            elif msg == "позвать всех в игру!":
                                chat_sender("@all, В ИГРУ!", 1)
                                sender("Позвал", id, getKeyboardByStatus())
                        elif status == "menu health":
                            if msg == "меню лсмц":
                                status = "menu lsmc"
                                sender("Переходим в меню ЛСМЦ!", id, getKeyboardByStatus())
                            elif msg == "меню сфмц":
                                status = "menu sfmc"
                                sender("Переходим в меню СФМЦ!", id, getKeyboardByStatus())
                            elif msg == "меню лвмц":
                                status = "menu lvmc"
                                sender("Переходим в меню ЛВМЦ", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "main"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            elif msg == "позвать всех в игру!":
                                chat_sender("@all, В ИГРУ!", 1)
                                sender("Позвал", id, getKeyboardByStatus())
                        elif status == "menu defense":
                            if msg == "меню лса":
                                status = "menu lsa"
                                sender("Переходим в меню ЛСа", id, getKeyboardByStatus())
                            elif msg == "меню сфа":
                                status = "menu sfa"
                                sender("Переходим в меню СФа", id, getKeyboardByStatus())
                            elif msg == "меню тср":
                                status = "menu msp"
                                sender("Переходим в меню ТСР", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "main"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            elif msg == "позвать всех в игру!":
                                chat_sender("@all, В ИГРУ!", 1)
                                sender("Позвал", id, getKeyboardByStatus())
                        elif status == "menu media":
                            if msg == "меню сми лс":
                                status = "menu rls"
                                sender("Переходим в меню СМИ ЛС", id, getKeyboardByStatus())
                            elif msg == "меню сми сф":
                                status = "menu rsf"
                                sender("Переходим в меню СМИ СФ", id, getKeyboardByStatus())
                            elif msg == "меню сми лв":
                                status = "menu rlv"
                                sender("Переходим в меню СМИ ЛВ", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "main"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            elif msg == "позвать всех в игру!":
                                chat_sender("@all, В ИГРУ!", 1)
                                sender("Позвал", id, getKeyboardByStatus())
                        elif status == "pred government":
                            if msg == "пред гсв":
                                status = "pred gsv"
                                sender("Идем давать пред ГСВ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "пред гкв":
                                status = "pred gcv"
                                sender("Идем давать пред ГКВ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "пред ст":
                                status = "pred st"
                                sender("Идем давать пред СТ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "пред судье":
                                status = "pred judge"
                                sender("Идем давать пред Судье", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "пред губернатору":
                                status = "pred guber"
                                sender("Идем давать пред Губернатору", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "пред гп":
                                status = "pred gp"
                                sender("Идем давать пред ГП", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu government"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                        elif status == "vig government":
                            if msg == "выговор гсв":
                                status = "vig gsv"
                                sender("Идем давать выговор ГСВ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выговор гкв":
                                status = "vig gcv"
                                sender("Идем давать выговор ГКВ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выговор ст":
                                status = "vig st"
                                sender("Идем давать выговор СТ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выговор судье":
                                status = "vig judge"
                                sender("Идем давать выговор Судье", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выговор губернатору":
                                status = "vig guber"
                                sender("Идем давать выговор Губернатору", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выговор гп":
                                status = "vig gp"
                                sender("Идем давать выговор ГП", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu government"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                        elif status == "menu gcl":
                            if msg == "выдача преда":
                                status = "pred gcl"
                                sender("Идем давать пред ГЦЛ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig gcl"
                                sender("Идем давать выговор ГЦЛ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(gcl + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС", 1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(gcl + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС", 1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg gcl"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu co"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu stk":
                            if msg == "выдача преда":
                                status = "pred stk"
                                sender("Идем давать пред СтК", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig stk"
                                sender("Идем давать выговор СтК", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(stk + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС", 1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(stk + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС", 1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg stk"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu co"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu cb":
                            if msg == "выдача преда":
                                status = "pred cb"
                                sender("Идем давать пред ЦБ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig cb"
                                sender("Идем давать выговор ЦБ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(cb + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС", 1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(cb + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС", 1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg cb"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu co"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu lspd":
                            if msg == "выдача преда":
                                status = "pred lspd"
                                sender("Идем давать пред ЛСПД", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig lspd"
                                sender("Идем давать выговор ЛСПД", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(lspd + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(lspd + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg lspd"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu justice"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu sfpd":
                            if msg == "выдача преда":
                                status = "pred sfpd"
                                sender("Идем давать пред СФПД", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig sfpd"
                                sender("Идем давать выговор СФПД", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(sfpd + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(sfpd + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg sfpd"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu justice"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu rcsd":
                            if msg == "выдача преда":
                                status = "pred rcsd"
                                sender("Идем давать пред РКШД", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig rcsd"
                                sender("Идем давать выговор РКШД", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(rcsd + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(rcsd + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg rcsd"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu justice"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu swat":
                            if msg == "выдача преда":
                                status = "pred swat"
                                sender("Идем давать пред СВАТ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig swat"
                                sender("Идем давать выговор СВАТ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(swat + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(swat + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg swat"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu justice"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu fbi":
                            if msg == "выдача преда":
                                status = "pred fbi"
                                sender("Идем давать пред ФБР", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig fbi"
                                sender("Идем давать выговор ФБР", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(fbi + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(fbi + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg fbi"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu justice"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu lsmc":
                            if msg == "выдача преда":
                                status = "pred lsmc"
                                sender("Идем давать пред ЛСМЦ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig lsmc"
                                sender("Идем давать выговор ЛСМЦ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(lsmc + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(lsmc + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg lsmc"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu health"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu sfmc":
                            if msg == "выдача преда":
                                status = "pred sfmc"
                                sender("Идем давать пред СФМЦ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig sfmc"
                                sender("Идем давать выговор СФМЦ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(sfmc + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(sfmc + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg sfmc"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu health"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu lvmc":
                            if msg == "выдача преда":
                                status = "pred lvmc"
                                sender("Идем давать пред ЛВМЦ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig lvmc"
                                sender("Идем давать выговор ЛВМЦ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(lvmc + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(lvmc + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg lvmc"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu health"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu lsa":
                            if msg == "выдача преда":
                                status = "pred lsa"
                                sender("Идем давать пред ЛСа", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig lsa"
                                sender("Идем давать выговор ЛСа", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(lsa + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(lsa + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg lsa"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu defense"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu sfa":
                            if msg == "выдача преда":
                                status = "pred sfa"
                                sender("Идем давать пред ВМС", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig sfa"
                                sender("Идем давать выговор ВМС", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(sfa + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(sfa + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg sfa"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu defense"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu msp":
                            if msg == "выдача преда":
                                status = "pred msp"
                                sender("Идем давать пред ТСР", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig msp"
                                sender("Идем давать выговор ТСР", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(msp + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(msp + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg lsa"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu defense"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu rls":
                            if msg == "выдача преда":
                                status = "pred rls"
                                sender("Идем давать пред СМИ ЛС", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig rls"
                                sender("Идем давать выговор СМИ ЛС", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(rls + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(rls + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg rls"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu media"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu rsf":
                            if msg == "выдача преда":
                                status = "pred rsf"
                                sender("Идем давать пред СМИ СФ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig rsf"
                                sender("Идем давать выговор СМИ СФ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(rsf + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(rsf + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg rsf"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu media"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu rlv":
                            if msg == "выдача преда":
                                status = "pred rlv"
                                sender("Идем давать пред СМИ ЛВ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig rlv"
                                sender("Идем давать выговор СМИ ЛВ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(rlv + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(rlv + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg rlv"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu media"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif "pred" in status:
                            if msg != "обратно":
                                makePunish(status, True, msg, id)
                                status = status.replace("pred", "menu").replace("gcv", "government").replace("gsv", "government").replace("judge", "government").replace("guber", "government").replace("gp", "government")
                                if not ("stk" in status) and "st" in status:
                                    status = status.replace("st", "government")
                                sender("Выдано!", id, getKeyboardByStatus())
                            else:
                                status = status.replace("pred", "menu").replace("gcv", "government").replace("gsv", "government").replace("judge", "government").replace("guber", "government").replace("gp", "government")
                                if not ("stk" in status) and "st" in status:
                                    status = status.replace("st", "government")
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif "vig" in status:
                            if msg != "обратно":
                                makePunish(status, False, msg, id)
                                status = status.replace("vig", "menu").replace("gcv", "government").replace("gsv", "government").replace("judge", "government").replace("guber", "government").replace("gp", "government")
                                if not ("stk" in status) and "st" in status:
                                    status = status.replace("st", "government")
                                sender("Выдано!", id, getKeyboardByStatus())
                            else:
                                status = status.replace("vig", "menu").replace("gcv", "government").replace("gsv", "government").replace("judge", "government").replace("guber", "government").replace("gp", "government")
                                if not ("stk" in status) and "st" in status:
                                    status = status.replace("st", "government")
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                    else:
                        send_noaccess_message(id, False)


    except Exception as e:
        print(e)
