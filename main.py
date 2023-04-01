import time

import telebot
from telebot import types
import bs4 as b
from  bs4 import  BeautifulSoup
import requests
Token = open("venv/token.txt", 'r')
bot = telebot.TeleBot(Token.read())



@bot.message_handler(commands=['start'])
def start (message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    help = types.InlineKeyboardButton('help')
    markup1.add(help)
    bot.send_message(message.chat.id, '''Привет!
Я бот, который поможет научиться основам трейдинга в простой форме''', reply_markup=markup1)
    markup = types.InlineKeyboardMarkup(row_width=2)

    go = types.InlineKeyboardButton('Go', callback_data='go')
    markup.add(go)

    photo1 = 'https://i.pinimg.com/564x/f2/ea/dc/f2eadce93e391d7a67c1550ffbc73167.jpg'
    bot.send_photo(message.chat.id, photo1 , reply_markup=markup)





@bot.callback_query_handler(lambda c: c.data == 'go')
def go (call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.delete_message(call.message.chat.id, call.message.message_id - 1)
    bot.delete_message(call.message.chat.id, call.message.message_id -2)
    markup = types.InlineKeyboardMarkup(row_width=2)
    trade = types.InlineKeyboardButton('Биржа', callback_data='trd')
    howstart = types.InlineKeyboardButton('Как начать', callback_data='hws')
    informa = types.InlineKeyboardButton(' Информация', callback_data='info')
    markup.add(trade, howstart,informa)
    photo1 = 'https://rusvest.ru/wp-content/uploads/2017/08/Crypto-exchange.jpg'
    bot.send_photo(call.message.chat.id,photo1, '', reply_markup= markup)

@bot.callback_query_handler(lambda c: c.data == 'trd')
def answer1 (call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    game = types.InlineKeyboardButton('Симулятор', callback_data='play')
    study = types.InlineKeyboardButton('Обучение', callback_data='ycheba')
    back = types.InlineKeyboardButton('Назад', callback_data='backtostart')
    markup.add(game, study, back)
    photo1 = 'https://miro.medium.com/max/3202/1*aGT1oTkxqPLVYWgXCSOSgw.png'

    bot.send_photo(call.message.chat.id, photo1, reply_markup= markup)

@bot.callback_query_handler(lambda c: c.data == 'backtostart')
def answer1 (call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    trade = types.InlineKeyboardButton('Биржа', callback_data='trd')
    howstart = types.InlineKeyboardButton('Как начать', callback_data='hws')
    info = types.InlineKeyboardButton('Информация', callback_data='info')
    markup.add(trade, howstart, info)
    photo1 = 'https://rusvest.ru/wp-content/uploads/2017/08/Crypto-exchange.jpg'
    bot.send_photo(call.message.chat.id, photo1, '', reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'hws')
def answer2 (call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    beg = types.InlineKeyboardButton(text='Посмотреть',url= 'https://www.tinkoff.ru/invest/education/courses/')
    backtotrade = types.InlineKeyboardButton('Назад', callback_data='backtt')
    markup.add(beg, backtotrade)
    photo1 ='https://img.freepik.com/premium-photo/printed-question-mark-covering-a-magnifying-glass_124595-67.jpg'

    bot.send_photo(call.message.chat.id,photo1, 'Ссылка на обучение',reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'backtt')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    trade = types.InlineKeyboardButton('Биржа', callback_data='trd')
    howstart = types.InlineKeyboardButton('Как начать', callback_data='hws')
    informa = types.InlineKeyboardButton('Иформация', callback_data='info')
    markup.add(trade, howstart, informa)
    photo1 = 'https://rusvest.ru/wp-content/uploads/2017/08/Crypto-exchange.jpg'
    bot.send_photo(call.message.chat.id, photo1, '', reply_markup=markup)



@bot.callback_query_handler(lambda c: c.data == 'ycheba')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    veb = types.InlineKeyboardButton('Статьи', callback_data='veb')
    howstart = types.InlineKeyboardButton('Видео', callback_data='mp4')
    backtotrd = types.InlineKeyboardButton('Назад', callback_data='bttrade')
    markup.add(veb, howstart,backtotrd)
    photo1 = 'https://i.pinimg.com/564x/9a/b3/7f/9ab37fdc8e5a22cffd0868ff75b21b08.jpg'
    bot.send_photo(call.message.chat.id, photo1, '', reply_markup=markup)



@bot.callback_query_handler(lambda c: c.data == 'mp4')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=1)
    howstart = types.InlineKeyboardButton('Blockchain', callback_data='vid1')
    u = types.InlineKeyboardButton('Криптовалюты', callback_data='n2')
    m = types.InlineKeyboardButton('От чего зависит курс биткойна?',callback_data='n9' )
    backtotrd = types.InlineKeyboardButton('Назад', callback_data='ycheba')
    markup.add( howstart,u,m,backtotrd)
    photo1 = 'https://i.pinimg.com/564x/9a/b3/7f/9ab37fdc8e5a22cffd0868ff75b21b08.jpg'
    bot.send_photo(call.message.chat.id, photo1, '', reply_markup=markup)

@bot.callback_query_handler(lambda c: c.data == 'n9')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup()
    backtotrd = types.InlineKeyboardButton('Назад', callback_data='mp4')
    markup.add(backtotrd)
    bot.send_message(call.message.chat.id, 'https://youtu.be/Ptym81b0prI', reply_markup=markup)



@bot.callback_query_handler(lambda c: c.data == 'n2')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    backtotrd = types.InlineKeyboardButton('Назад', callback_data='mp4')
    markup.add(backtotrd)
    bot.send_message(call.message.chat.id, 'https://youtu.be/-RWCJ8NqZmA', reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'vid1')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    backtotrd = types.InlineKeyboardButton('Назад', callback_data='mp4')
    markup.add(backtotrd)
    bot.send_message(call.message.chat.id, 'https://youtu.be/ttEkY4Owd1c', reply_markup=markup)




@bot.callback_query_handler(lambda c: c.data == 'veb')      ########################
def state (call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = types.InlineKeyboardMarkup(row_width=1)
        st = types.InlineKeyboardButton('Краткая история биткойна', callback_data='abzac1')
        stt = types.InlineKeyboardButton('Blockchain', callback_data='blockchain1')
        backtoychoba = types.InlineKeyboardButton('Назад', callback_data='ycheba')
        kript = types.InlineKeyboardButton('Биткойн', callback_data='kripta1')
        hiw1 = types.InlineKeyboardButton('Как это работает?', callback_data='HowItWork1' )
        markup.add(st,stt,kript,hiw1,backtoychoba)
        photo1 = 'https://staging.ifamagazine.com/wp-content/uploads/2021/03/rsz_adobestock_408057388-scaled.jpg'
        bot.send_photo(call.message.chat.id, photo1, reply_markup=markup)

@bot.callback_query_handler(lambda c: c.data == 'kripta1')
def state1 (call):
    bot.delete_message(call.message.chat.id, call.message.message_id )

    markup = types.InlineKeyboardMarkup()
    st = types.InlineKeyboardButton('вперёд', callback_data='kripta2')
    markup.add(st)
    bot.send_message(call.message.chat.id,'Биткойны могут использоваться для обмена на товары или услуги у продавцов, которые согласны их принимать. Обмен на обычные валюты происходит через онлайн-сервисы обмена цифровых валют, другие платёжные системы, обменные пункты или непосредственно между заинтересованными сторонами. Котировка биткойна зависит исключительно от баланса спроса и предложения, она никем не регулируется и не сдерживается. При этом никто не обязан принимать биткойны, то есть не существует механизма получить за них хоть что-нибудь, если по какой-то причине их откажутся покупать или принимать в оплату.', reply_markup=markup)



@bot.callback_query_handler(lambda c: c.data == 'kripta2')
def state2 (call):
    markup = types.InlineKeyboardMarkup()
    st = types.InlineKeyboardButton('вперёд', callback_data='kripta3')
    markup.add(st)
    bot.send_message(call.message.chat.id,'Комиссия за проведение операций назначается отправителем добровольно. Размер комиссии влияет на приоритет при обработке транзакции. Обычно программа-клиент подсказывает рекомендуемый размер комиссии. Транзакции без комиссии возможны и также обрабатываются, однако не рекомендуются, поскольку время их обработки неизвестно и может быть довольно велико.',reply_markup=markup )


@bot.callback_query_handler(lambda c: c.data == 'kripta3')
def state3 (call):
    markup = types.InlineKeyboardMarkup()
    st = types.InlineKeyboardButton('вперёд', callback_data='kripta4')
    markup.add(st)
    bot.send_message(call.message.chat.id, 'Для прогноза курса обращайте внимание на следующие вещи: 1. Изучите историю криптовалюты и ее основные принципы. Это поможет вам понять, как работает рынок и какие факторы влияют на цены.', reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'kripta4')
def state4 (call):
    markup = types.InlineKeyboardMarkup()
    st = types.InlineKeyboardButton('вперёд', callback_data='kripta5')
    markup.add(st)
    bot.send_message(call.message.chat.id,  '2. Следите за новостями и событиями в мире криптовалют. Это может быть выход новых криптовалют на рынок, изменения законодательства в разных странах, взломы бирж и т.д.',reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'kripta5')
def state5 (call):
    markup = types.InlineKeyboardMarkup()
    st = types.InlineKeyboardButton('вперёд', callback_data='kripta6')
    markup.add(st)
    bot.send_message(call.message.chat.id, '3. Анализируйте графики цен на криптовалюты. Вы можете использовать различные инструменты и платформы для анализа цен, такие как TradingView или CoinMarketCap.',reply_markup=markup)




@bot.callback_query_handler(lambda c: c.data == 'kripta6')
def state6 (call):
    markup = types.InlineKeyboardMarkup()
    sty = types.InlineKeyboardButton('вперёд', callback_data='kripta7')
    markup.add(sty)
    bot.send_message(call.message.chat.id, '4. Изучайте отзывы и мнения экспертов в области криптовалют. Существует множество блогеров, журналистов и трейдеров, которые делятся своим опытом и знаниями о рынке.',reply_markup=markup)




@bot.callback_query_handler(lambda c: c.data == 'kripta7')
def state7 (call):
    markup = types.InlineKeyboardMarkup()
    stt = types.InlineKeyboardButton('Круто! А теперь к инвестициям', callback_data='nazadkinvestic')
    markup.add(stt)
    bot.send_message(call.message.chat.id, '5. Участвуйте в сообществах и форумах, связанных с криптовалютами. Это поможет вам получить информацию из первых рук и общаться с другими участниками рынка.', reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'blockchain1')      ########################
def state1 (call):
        bot.delete_message(call.message.chat.id, call.message.message_id )

        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('вперёд', callback_data='blockchain2')
        markup.add(st)
        bot.send_message(call.message.chat.id,'Криптовалюту сегодня рассматривают как инвестиции, возможный защитный актив и даже как зарплату в метавселенных — цифровых мирах, в которых можно создавать аватаров, играть, ходить в магазины и общаться. Работоспособность всех этих систем поддерживает технология блокчейна.',reply_markup=markup)



@bot.callback_query_handler(lambda c: c.data == 'blockchain2')      ########################
def state2 (call):
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('вперёд', callback_data='blockchain3')
        markup.add(st)
        bot.send_message(call.message.chat.id,'Блокчейн — это база данных с транзакциями, состоящая из последовательно выстроенной цепочки цифровых блоков, в каждом из которых хранится информация о предыдущем и следующем блоках.',reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'blockchain3')      ########################
def state3 (call):
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('вперёд', callback_data='blockchain4')
        markup.add(st)
        bot.send_message(call.message.chat.id, 'Это своеобразная цифровая тетрадь, в которой записи неизменны благодаря механизму хеширования — уникальному набор буквенных и цифровых символов, где изменение одного символа влечет изменение в других блоках. ',reply_markup=markup)



@bot.callback_query_handler(lambda c: c.data == 'blockchain4')      ########################
def state5 (call):
        markup = types.InlineKeyboardMarkup()
        stt = types.InlineKeyboardButton('Круто! А теперь к инвестициям', callback_data='back')
        st = types.InlineKeyboardButton('А как был создан блокчейн?', callback_data='blockchain5')
        markup.add(st, stt)
        bot.send_message(call.message.chat.id, 'Главное преимущество блокчейна в его прозрачности, потому что каждый может ознакомиться с информацией внутри блоков, но никто не в силах ее изменить или уничтожить.',reply_markup=markup)




@bot.callback_query_handler(lambda c: c.data == 'blockchain5')      ########################
def state4 (call):
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('вперёд', callback_data='blockchain6')
        markup.add(st)
        bot.send_message(call.message.chat.id,  'Официально история «блоков и цепей» начинается 31 октября 2008 года, когда некто под псевдонимом Сатоши Накамото упомянул блокчейн в white paper (базовом документе) про сеть первой криптовалюты — биткоина. ',reply_markup=markup)




@bot.callback_query_handler(lambda c: c.data == 'blockchain6')  ########################
def state6(call):
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('вперёд', callback_data='blockchain7')
        markup.add(st)
        bot.send_message(call.message.chat.id, 'Основополагающие принципы применения децентрализации и неизменности для учета документов были заложены еще в 1960-1970 годах, но ближе всего к ним можно отнести работы ученых Стюарта Хабера и У. Скотта Сторнетта, которые в 1991 году описали схему последовательного создания блоков, в которых находится хеш.',reply_markup=markup)




@bot.callback_query_handler(lambda c: c.data == 'blockchain7')      ########################
def state7(call):
        markup = types.InlineKeyboardMarkup()
        stt = types.InlineKeyboardButton('Круто! А теперь к инвестициям', callback_data='nazadkinvestic')
        markup.add(stt)
        bot.send_message(call.message.chat.id, 'Технология была даже запатентована, но стала для своего времени вертолетом Да Винчи — технической возможности для реализации идеи не было, и интерес к ней пропал. Срок патента истек в 2004 году, всего за четыре года до появления Сатоши и его white paper.',reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'back')
def state(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        bot.delete_message(call.message.chat.id, call.message.message_id - 2)
        bot.delete_message(call.message.chat.id, call.message.message_id - 3)
        markup = types.InlineKeyboardMarkup(row_width=1)
        st = types.InlineKeyboardButton('Краткая история биткойна', callback_data='abzac1')
        stt = types.InlineKeyboardButton('Blockchain', callback_data='blockchain1')
        kript = types.InlineKeyboardButton('Биткойн', callback_data='kripta1')
        hiw1 = types.InlineKeyboardButton('Как это работает?', callback_data='HowItWork1' )
        backtoychoba = types.InlineKeyboardButton('Назад', callback_data='ycheba')
        markup.add(st,stt,kript,hiw1,backtoychoba)
        photo1 = 'https://staging.ifamagazine.com/wp-content/uploads/2021/03/rsz_adobestock_408057388-scaled.jpg'
        bot.send_photo(call.message.chat.id, photo1, reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'HowItWork1')      ########################
def state1(call):
        bot.delete_message(call.message.chat.id, call.message.message_id )
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('вперёд', callback_data='HowItWork2')
        markup.add(st)
        bot.send_message(call.message.chat.id,'Блокчейн — это система распределенного реестра данных, доступная каждому участнику этой сети. Например, цифровая валюта, в основе работы которой лежит блокчейн, может создаваться, перемещаться и храниться вне компетенции любого правительства, финансового учреждения или личного юриста, но тем не менее каждая транзакция записывается в блокчейн и публична. Это своеобразная нить Ариадны, хлебные крошки и навигатор, которые ведут любого желающего проверить информацию по транзакциям.',reply_markup=markup)



@bot.callback_query_handler(lambda c: c.data == 'HowItWork2')      ########################
def state2 (call):
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('вперёд', callback_data='HowItWork3')
        markup.add(st)
        bot.send_message(call.message.chat.id,'Блоки в сети добавляются с помощью процедуры майнинга. За каждый новый блок майнер получает вознаграждение, которое составляет финансовую основу его деятельности.',reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'HowItWork3')      ########################
def state3 (call):
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('вперёд', callback_data='HowItWork4')
        markup.add(st)
        bot.send_message(call.message.chat.id, 'После того как совершена первая транзакция, она должна быть подтверждена несколькими участниками сети — в этом и состоит суть децентрализации блокчейна без конкретных посредников. Это означает еще одно преимущество блокчейна перед классической финансовой системой — в отличие от банков блокчейн работает круглосуточно и не зависит от центрального банка конкретной страны.',reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'HowItWork4')      ########################
def state4 (call):
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('вперёд', callback_data='HowItWork5')
        markup.add(st)
        bot.send_message(call.message.chat.id,  'В 2014 году, по свидетельствам, можно было намайнить вплоть до 1-2 биткоинов просто на обычном компьютере дома, но чтобы добыть то же количество биткоинов сейчас, нужно приручить сложную математику и найти сотни видеокарт, расположенные в одном дата-центре, которые еще называют майнинговыми фермами.',reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'HowItWork5')      ########################
def state5 (call):
        markup = types.InlineKeyboardMarkup()
        g = types.InlineKeyboardButton('Вперед', callback_data='HowItWork6')
        markup.add(g)
        bot.send_message(call.message.chat.id, 'Первый алгоритм работы майнеров, в том числе и биткоина, называли Proof-of-Work (доказательство работы). Он требовал большой вычислительной мощности, которую обеспечивали компьютеры. Поэтому сейчас стали появляться блокчейны с алгоритмом Proof-of-Stake (доказательство ставки), на котором правят бал не машины, а валидаторы — участники сети, отвечающие за ее целостность и подтверждение всех происходящих в блокчейне транзакций. ',reply_markup=markup)




@bot.callback_query_handler(lambda c: c.data == 'HowItWork6')
def state6 (call):
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('вперёд', callback_data='HowItWork7')
        markup.add(st)
        bot.send_message(call.message.chat.id, 'P-o-W требует много электроэнергии, дорогого и редкого специализированного оборудования. Чтобы стать валидатором P-o-S, надо иметь некоторое количество монет этой сети, заложить их, то есть «создать stake» и поставить специальное программное обеспечение. Подтверждая транзакции, валидаторы получают вознаграждение.',reply_markup=markup)




@bot.callback_query_handler(lambda c: c.data == 'HowItWork7')      ########################
def state8 (call):
        markup = types.InlineKeyboardMarkup()
        stt = types.InlineKeyboardButton('Круто! А теперь к инвестициям', callback_data='nazadkinvestic')
        markup.add(stt)
        bot.send_message(call.message.chat.id, ' Самым ярким примером использования алгоритма P-o-W является сеть биткоина, а альтернативой можно считать сеть Ethereum, которая хоть и начиналась с использования алгоритма P-o-W, но находится в стадии перехода на алгоритм P-o-S.',reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'abzac1')
def state1(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('Вперёд', callback_data='abzac2')
        g = types.InlineKeyboardButton('Назад к статьям', callback_data='veb')
        markup.add(st,g)
        bot.send_message(call.message.chat.id, 'История главной мировой криптовалюты началась 31 октября 2008 года, когда никому не известный человек под псевдонимом Сатоши Накамото опубликовал статью «Биткойн: P2P электронные деньги». В этой статье он описал будущий протокол биткоина – свод правил, по которым должна была работать создаваемая система.',reply_markup=markup)



@bot.callback_query_handler(lambda c: c.data == 'abzac2')
def state2(call):
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('Вперёд', callback_data='abzac3')
        markup.add(st)
        bot.send_message(call.message.chat.id, 'Все части системы были известны и до Накамото. Криптографические алгоритмы, заложенные в основу биткоина, уже существовали. Распределенное хранение данных в децентрализованных сетях также использовалось.',reply_markup=markup)

@bot.callback_query_handler(lambda c: c.data == 'abzac3')
def state3(call):
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('Вперёд', callback_data='abzac4')
        markup.add(st)
        bot.send_message(call.message.chat.id, 'Гениальность Накамото была в том, что именно он собрал отдельные куски в целое, выстроил систему и заставил ее работать. Предлагаемая система была действительно революционной, ничего подобного ранее не существовало.',reply_markup=markup)



@bot.callback_query_handler(lambda c: c.data == 'abzac4')
def state4(call):
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('Вперёд', callback_data='abzac5')
        markup.add(st)
        bot.send_message(call.message.chat.id, 'Вскоре после публикации протокола, 3 января 2009 года, Сатоши был сгенерирован первый блок в цепочке блокчейна. В этот момент были намайнены первые 50 биткоинов.',reply_markup=markup)



@bot.callback_query_handler(lambda c: c.data == 'abzac5')
def state5(call):
        markup = types.InlineKeyboardMarkup()
        stt = types.InlineKeyboardButton('Круто! А теперь к инвестициям', callback_data='ven')
        st = types.InlineKeyboardButton('А что было дальше?', callback_data='abzac6')
        markup.add(st, stt)
        bot.send_message(call.message.chat.id, '''
Последнее сообщение от «Сатоши» — кто бы ни скрывался за этим псевдонимом – было получено 12 декабря 2010 года. После этого он исчез из Cети и больше не участвовал ни в дальнейшем развитии биткоина, ни вообще в какой-либо деятельности…
Такова история появления биткоина.''',reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'ven')
def state(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        bot.delete_message(call.message.chat.id, call.message.message_id - 2)
        bot.delete_message(call.message.chat.id, call.message.message_id - 3)
        bot.delete_message(call.message.chat.id, call.message.message_id - 4)
        markup = types.InlineKeyboardMarkup(row_width=1)
        st = types.InlineKeyboardButton('Краткая история биткойна', callback_data='abzac1')
        stt = types.InlineKeyboardButton('Blockchain', callback_data='blockchain1')
        kript = types.InlineKeyboardButton('Биткойн',callback_data='kripta1')
        hiw1 = types.InlineKeyboardButton('Как это работает?', callback_data='HowItWork1' )
        backtoychoba = types.InlineKeyboardButton('Назад',callback_data='ycheba')
        markup.add(st,stt,kript,hiw1,backtoychoba)
        photo1 = 'https://staging.ifamagazine.com/wp-content/uploads/2021/03/rsz_adobestock_408057388-scaled.jpg'
        bot.send_photo(call.message.chat.id, photo1, reply_markup=markup)



@bot.callback_query_handler(lambda c: c.data == 'abzac6')
def state6 (call):
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('вперёд', callback_data='abzac7')
        markup.add(st)
        bot.send_message(call.message.chat.id,'Сразу после появления биткоина началось его активное развитие.Уже через 9 месяцев, 5 октября 2009 года, был впервые установлен обменный курс биткоина. На ресурсе New Liberty Standart можно было обменять 1 доллар на 1 309,03 биткоинов. То есть, за 1 цент можно было купить 13 биткоинов! Вы можете сопоставить эту цифру с сегодняшним курсом и понять, каков был рост у биткоина за все время.',reply_markup=markup)

@bot.callback_query_handler(lambda c: c.data == 'abzac7')
def state8 (call):
        markup = types.InlineKeyboardMarkup()
        stt = types.InlineKeyboardButton('Круто! А теперь к инвестициям', callback_data='nazadkinvestic')
        markup.add(stt)
        bot.send_message(call.message.chat.id,'22 мая 2010 года состоялся настоящий прорыв! Впервые биткоины были обменены на реальный товар.Американец Ласло Ханеч за 10 000 биткоинов получил две пиццы. Это было по-настоящему революционным событием. Биткоин перестал быть сугубо виртуальным феноменом и проник в реальный мир.',reply_markup=markup)

@bot.callback_query_handler(lambda c: c.data == 'nazadkinvestic')
def state (call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        bot.delete_message(call.message.chat.id, call.message.message_id - 2)
        bot.delete_message(call.message.chat.id, call.message.message_id - 3)
        bot.delete_message(call.message.chat.id, call.message.message_id - 4)
        bot.delete_message(call.message.chat.id, call.message.message_id - 5)
        bot.delete_message(call.message.chat.id, call.message.message_id - 6)


        markup = types.InlineKeyboardMarkup(row_width=1)
        st = types.InlineKeyboardButton('Краткая история биткойна', callback_data='abzac1')
        stt = types.InlineKeyboardButton('Blockchain', callback_data='blockchain1')
        backtoychoba = types.InlineKeyboardButton('Назад', callback_data='ycheba')
        kript = types.InlineKeyboardButton('Биткойн',callback_data='kripta1')
        hiw1 = types.InlineKeyboardButton('Как это работает?', callback_data='HowItWork1' )
        markup.add(st,stt,kript,hiw1,backtoychoba)
        photo1 = 'https://staging.ifamagazine.com/wp-content/uploads/2021/03/rsz_adobestock_408057388-scaled.jpg'
        bot.send_photo(call.message.chat.id, photo1, reply_markup=markup)




















@bot.callback_query_handler(lambda c: c.data == 'bttrade')
def answer1 (call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    game = types.InlineKeyboardButton('Симулятор', callback_data='play')
    study = types.InlineKeyboardButton('Обучение', callback_data='ycheba')
    back = types.InlineKeyboardButton('Назад', callback_data='backtostart')
    markup.add(game, study, back)
    photo1 = 'https://miro.medium.com/max/3202/1*aGT1oTkxqPLVYWgXCSOSgw.png'

    bot.send_photo(call.message.chat.id, photo1, reply_markup= markup)




@bot.callback_query_handler(lambda c: c.data == 'mp4')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    howstart = types.InlineKeyboardButton('Blockchain', callback_data='vid1')
    backtotrd = types.InlineKeyboardButton('Назад', callback_data='ycheba')
    markup.add( howstart,backtotrd)
    photo1 = 'https://i.pinimg.com/564x/9a/b3/7f/9ab37fdc8e5a22cffd0868ff75b21b08.jpg'
    bot.send_photo(call.message.chat.id, photo1, '', reply_markup=markup)

@bot.callback_query_handler(lambda c: c.data == 'vid1')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    backtotrd = types.InlineKeyboardButton('Назад', callback_data='mp4')
    markup.add(backtotrd)
    vide = 'https://youtu.be/Ptym81b0prI'
    bot.send_video(call.message.chat.id, vide,reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'info')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=1)
    mast = types.InlineKeyboardButton('Владельцы', callback_data='mybot')
    backtosta = types.InlineKeyboardButton('Назад', callback_data='btt')
    markup.add(mast, backtosta)
    photo1 = 'https://resh.edu.ru/uploads/lesson_extract/7316/20200113122314/OEBPS/objects/m_info_7_2_1/5df618b1e2002477581035db.jpg'
    bot.send_photo(call.message.chat.id, photo1, '', reply_markup=markup)

@bot.callback_query_handler(lambda c: c.data == 'btt')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    trade = types.InlineKeyboardButton('Биржа', callback_data='trd')
    howstart = types.InlineKeyboardButton('Как начать', callback_data='hws')
    informa = types.InlineKeyboardButton('Иформация', callback_data='info')
    markup.add(trade, howstart, informa)
    photo1 = 'https://rusvest.ru/wp-content/uploads/2017/08/Crypto-exchange.jpg'
    bot.send_photo(call.message.chat.id, photo1, '', reply_markup=markup)
















@bot.callback_query_handler(lambda c: c.data == 'play')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    mast = types.InlineKeyboardButton('Играть', callback_data='play2')
    passport = types.InlineKeyboardButton('Об игре', callback_data='infof')
    backtosta = types.InlineKeyboardButton('Назад', callback_data='trd')
    markup.add(mast, passport, backtosta)
    photo1 = 'https://i.pinimg.com/564x/f8/e9/bc/f8e9bc430a5926eed3e166f8f2c6697c.jpg'
    bot.send_photo(call.message.chat.id, photo1, '', reply_markup=markup)

@bot.callback_query_handler(lambda c: c.data == 'play2')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=1)
    mast1 = types.InlineKeyboardButton('Играть', callback_data='play3')
    backtosta = types.InlineKeyboardButton('Назад', callback_data='trd')
    markup.add(mast1, backtosta)
    photo1 = 'https://i.pinimg.com/564x/f8/e9/bc/f8e9bc430a5926eed3e166f8f2c6697c.jpg'
    bot.send_photo(call.message.chat.id, photo1, 'В этой игре вам нужно угадать, вырастет значение акции, или упадет', reply_markup=markup)

@bot.callback_query_handler(lambda c: c.data == 'play3')
def play(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    fallin = types.InlineKeyboardButton('Уменьшится', callback_data='falin')
    rising = types.InlineKeyboardButton('Увеличится', callback_data='rising2')
    m = types.InlineKeyboardButton('Назад',callback_data='play2')
    markup.add(fallin, rising,m)
    photo1 = 'https://i.pinimg.com/564x/f8/e9/bc/f8e9bc430a5926eed3e166f8f2c6697c.jpg'
    bot.send_photo(call.message.chat.id, photo1,
    '', reply_markup=markup)
    def get_bitcoin_rate():
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        if response.status_code == 200:
            return response.json()['bpi']['USD']['rate_float']
        else:
            return None

    bitcoin_rate = get_bitcoin_rate()
    if bitcoin_rate is not None:
        bot.send_message(call.message.chat.id,f'Курс биткоина: {bitcoin_rate} долларов США')


@bot.callback_query_handler(lambda c: c.data == 'falin')
def answer1(call):
    def get_bitcoin_rate():
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        if response.status_code == 200:
            return response.json()['bpi']['USD']['rate_float']
        else:
            return None
    a = get_bitcoin_rate()
    t = 20
    import time
    for i in range(1,t+1):
        bot.send_message(call.message.chat.id,i)
        time.sleep(1)
    time.sleep(1)
    b = get_bitcoin_rate()
    if a > b:
        bot.send_message(call.message.chat.id, 'Вы выиграли')
    else:
        bot.send_message(call.message.chat.id, 'Вы проигралии')
    time.sleep(1)
    bot.delete_message(call.message.chat.id, call.message.message_id )
    markup = types.InlineKeyboardMarkup(row_width=1)
    w = types.InlineKeyboardButton('Назад', callback_data='play3')
    markup.add(w)
    photo1 = 'https://staging.ifamagazine.com/wp-content/uploads/2021/03/rsz_adobestock_408057388-scaled.jpg'
    bot.send_photo(call.message.chat.id, photo1, reply_markup=markup)

@bot.callback_query_handler(lambda c: c.data == 'rising2')
def answer1(call):
    def get_bitcoin_rate():
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        if response.status_code == 200:
            return response.json()['bpi']['USD']['rate_float']
        else:
            return None
    a = get_bitcoin_rate()
    t = 20
    import time
    for i in range(1,t+1):
        bot.send_message(call.message.chat.id,i)
        time.sleep(1)
    time.sleep(1)
    b = get_bitcoin_rate()
    if a < b:
        bot.send_message(call.message.chat.id, 'Вы выиграли')

    else:
        bot.send_message(call.message.chat.id, 'Вы проиграли')

    time.sleep(1)
    markup = types.InlineKeyboardMarkup(row_width=1)
    w = types.InlineKeyboardButton('Назад', callback_data='play3')
    markup.add(w)
    photo1 = 'https://staging.ifamagazine.com/wp-content/uploads/2021/03/rsz_adobestock_408057388-scaled.jpg'
    bot.send_photo(call.message.chat.id, photo1, reply_markup=markup)

@bot.callback_query_handler(lambda c: c.data == 'mybot')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    backtosta = types.InlineKeyboardButton('Назад', callback_data='info')
    markup.add(backtosta)
    photo1 = 'https://resh.edu.ru/uploads/lesson_extract/7316/20200113122314/OEBPS/objects/m_info_7_2_1/5df618b1e2002477581035db.jpg'
    bot.send_photo(call.message.chat.id, photo1, '''
Владельцы:
======================
https://t.me/ss_We_can
======================
https://t.me/lagovdp
======================
https://t.me/arthurphotographer
======================
https://t.me/Mr_SaZaN
======================''', reply_markup=markup)









bot.polling(none_stop=True)















bot.polling(none_stop=True)