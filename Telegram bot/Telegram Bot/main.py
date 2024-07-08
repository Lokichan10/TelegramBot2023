from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

button_hi = KeyboardButton('Привет! 👋')
sumary_cost = 0
greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

API_TOKEN = '6186086068:AAFgq6nnPJgBwca2Z7XQja_PCZYBKugRLQw'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
'''
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="С пюрешкой")],
        [types.KeyboardButton(text="Без пюрешки")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)
    '''
def defoult(name,description,cost):
   @dp.message_handler()
   async def cmd_start(message: types.Message):
       await message.answer(f'''
**{name}**
__{description}__
**{cost}**
         ''')











@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('этот бот Belisimo pizza, всю информацию вы можете найти в официальном сайте https://bellissimo.uz/, создатель бота @yan_bragin_cs')

@dp.message_handler(commands="menu")
async def cmd_start(message: types.Message):
   kb = [
       [types.KeyboardButton(text="Пица🍕")],
       [types.KeyboardButton(text="Закуски🍟")],
       [types.KeyboardButton(text="Напитки🍹")],
       [types.KeyboardButton(text="Салаты🥬")],
       [types.KeyboardButton(text="Десерты🍧")],
       [types.KeyboardButton(text="Соусы🧂")]
   ]
   keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
   await message.answer("Что вы хотите?", reply_markup=keyboard)





########## PIZAS ##########




@dp.message_handler(text = 'Пица🍕') 
async def pizza(message: types.Message):
   kb = [
       [types.KeyboardButton(text="Донар Пица🍕")],
       [types.KeyboardButton(text="Салса🍕")],
       [types.KeyboardButton(text="Гурме🍕")],
       [types.KeyboardButton(text="Супер микс🍕")],
       [types.KeyboardButton(text="Куриный кари🍕")],
       [types.KeyboardButton(text="Курица с сыром🍕")],
       [types.KeyboardButton(text="Двойной пеперони🍕")],
       [types.KeyboardButton(text="Пица в виде сердечка🍕")],
       [types.KeyboardButton(text="Куриный ранч🍕")],
       [types.KeyboardButton(text="Халапено🍕")],
       [types.KeyboardButton(text="Пеперони🍕")],
       [types.KeyboardButton(text="Мексиканский🍕")],
       [types.KeyboardButton(text="Маргарита🍕")],
       [types.KeyboardButton(text="Курица Барбикью🍕")],
       [types.KeyboardButton(text="Курица и грибы🍕")],
       [types.KeyboardButton(text="Комбо🍕")],
       [types.KeyboardButton(text="Кебаб🍕")],
       [types.KeyboardButton(text="Гавайский🍕")], 
       [types.KeyboardButton(text="Вегетарианский🍕")],
       [types.KeyboardButton(text="Белисимо🍕")],
       [types.KeyboardButton(text="Алфредо🍕")],
       [types.KeyboardButton(text="Дабл чизбургер🍕")]
   ]
   keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
   await message.answer("Что вы хотите из списка", reply_markup=keyboard)


########## options of pizza ##########

##### Donar pizza #####

@dp.message_handler(text = 'Донар Пица🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\donnar-pizza.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Донар Пицца
Вкусная и сытная пицца с мясом донар и настоящим сыром моцарелла''', reply_markup=keyboard)
    @dp.message_handler(commands= 'buy') 
    async def pizza(message: types.Message):
        global sumary_cost
        sumary_cost = sumary_cost + 55_000
        return sumary_cost 
    

##### Salsa #####
@dp.message_handler(text = 'Салса🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\salsa.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Салса
Цыпленок, соус сальса, нежный сыр моцарелла, халапеньо, болгарский перец и помидоры''', reply_markup=keyboard)
    @dp.message_handler(commands= 'buy') 
    async def pizza(message: types.Message):
        global sumary_cost
        sumary_cost = sumary_cost + 60_000
        return sumary_cost
    
##### Гурме #####
@dp.message_handler(text = 'Гурме🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\Gurme.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Гурме
Соус для пиццы, зайтун, пепперони, козикорин, орегано''', reply_markup=keyboard)

##### Супер микс #####
@dp.message_handler(text = 'Супер микс🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\super-mix.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Супер микс
Пицца "супер микс" сочетание 4 разных любимых пицц в 1 пицце 😋 идеально подходит для тех, кто любит попробовать все и сразу 🙃''', reply_markup=keyboard)

##### Куриный кари #####
@dp.message_handler(text = 'Куриный кари🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\Chiken karri.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Куриный кари
Рулет из говядины и куриное филе с сыром моцарелла, ананасом и соусом карри''', reply_markup=keyboard)
    
##### Халапено #####
@dp.message_handler(text = 'Халапено🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\halapeno.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Халапено
Филе индейки, нежная говядина, лук, помидоры, острый перец халапеньо, сыр моцарелла и соус барбекю''', reply_markup=keyboard)
    
##### Курица с сыром #####
@dp.message_handler(text = 'Курица с сыром🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\cheese chicken.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Курица с сыром
Мягкое куриное филе, сыр моцарелла, помидоры и сырный соус''', reply_markup=keyboard)
    
##### Двойной пеперони #####
@dp.message_handler(text = 'Двойной пеперони🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\double peperoni.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Двойной пеперони
Две порции пепперони с сыром моцарелла и томатным соусом''', reply_markup=keyboard)

##### Пица в виде сердечка🍕 #####
@dp.message_handler(text = 'Пица в виде сердечка🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\love_pizz.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Пица в виде сердечка
Удивите любимого необычной пиццей ❤ ️ колбасы пепперони, мягкий сыр моцарелла и томатный соус''', reply_markup=keyboard)
    
##### Халапено🍕 #####
@dp.message_handler(text = 'Халапено🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\halapeno.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Халапено
Филе индейки, нежная говядина, лук, помидоры, острый перец халапеньо, сыр моцарелла и соус барбекю  ''', reply_markup=keyboard)
    
##### Пеперони🍕 #####
@dp.message_handler(text = 'Пеперони🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\peperoni.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Пепперони   
Пепперони, сыр моцарелла с томатным соусом''', reply_markup=keyboard)

##### Мексиканский🍕 #####
@dp.message_handler(text = 'Мексиканский🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\meksikan.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Мексиканский   
Говядина, колбаса пепперони, нежный сыр моцарелла, халапеньо, соус барбекю, сладкий перец, лук и помидоры''', reply_markup=keyboard)

##### Курица Барбикью🍕 #####
@dp.message_handler(text = 'Курица Барбикью🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\barbekyu chicken.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Курица Барбикью   
Куриное филе, лук, эластичный сыр моцарелла с барбекю и томатным соусом''', reply_markup=keyboard)

##### Курица и грибы🍕 #####
@dp.message_handler(text = 'Курица и грибы🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\chicken and mushrooms.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Курица и грибы 
Куриное филе, сыр моцарелла, грибы и орегано с соусом для пиццы''', reply_markup=keyboard)
    
##### Комбо🍕 #####
@dp.message_handler(text = 'Комбо🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\kombo.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Комбо
Филе индейки, пепперони, куриное филе и сыр моцарелла с томатным соусом''', reply_markup=keyboard)
    
##### Кебаб🍕 #####
@dp.message_handler(text = 'Кебаб🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\kebab.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Кебаб
Шашлык, хрустящий болгарский перец, помидоры и лук с томатным соусом''', reply_markup=keyboard)
    
##### Дабл чизбургер🍕 #####
@dp.message_handler(text = 'Дабл чизбургер🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\double chizeburger.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Дабл чизбургер
Мягкая говядина и сыр моцарелла с луком, помидорами и соусом для гамбургеров''', reply_markup=keyboard)

##### Вегетарианский🍕 #####
@dp.message_handler(text = 'Вегетарианский🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\vegetarian.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Вегетарианский
С помидорами, хрустящим болгарским перцем, орегано, грибами, маслинами, сыром моцарелла и луковым томатным соусом''', reply_markup=keyboard)

##### Дабл чизбургер🍕 #####
@dp.message_handler(text = 'Дабл чизбургер🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\double chizeburger.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Дабл чизбургер
Мягкая говядина и сыр моцарелла с луком, помидорами и соусом для гамбургеров''', reply_markup=keyboard)
    
##### Белисимо🍕 #####
@dp.message_handler(text = 'Белисимо🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\bellissimo.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Белисимо
Филе индейки с сыром моцарелла, хрустящим болгарским перцем, грибами, маслинами, пепперони и луковым томатным соусом''', reply_markup=keyboard)

    
##### Алфредо🍕 #####
@dp.message_handler(text = 'Алфредо🍕') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\pizza\afredo.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    kb = [
        [types.KeyboardButton(text="Маленькая")],
        [types.KeyboardButton(text="Большая")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('''
Алфредо
Соус Альфредо, шпинат, сыр моцарелла, мягкое куриное филе, грибы''', reply_markup=keyboard)


#######################################################################################################

# @dp.message_handler(text = 'Донар Пица🍕') 
# async def pizza(message: types.Message):
#    photo = open(r"C:\Users\Stanislav Boduen\OneDrive\Рабочий стол\Telegram Bot\images\pizza\donnar-pizza.jpg", 'rb')
#    await bot.send_photo(chat_id=message.chat.id, photo=photo)
#    kb = [
#        [types.KeyboardButton(text="Маленькая")],
#        [types.KeyboardButton(text="Большая")]
#    ]
#    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
#    @dp.message_handler(text = 'Маленькая') 
#    async def pizza(message: types.Message):
#       await message.answer("55 000 сум💴")
#       await message.answer('Напишите /buy если хотите купить')
#       @dp.message_handler(commands='buy') 
#       async def pizza(message: types.Message):
#          await message.answer('Успешно добавлено ')
#          global sumary_cost
#          sumary_cost = sumary_cost + 55000
# 
# 
# 
#    @dp.message_handler(text = 'Большая') 
#    async def pizza(message: types.Message):
#       await message.answer('82 000 сум💴')
#       await message.answer('Напишите /buy если хотите купить')
#       @dp.message_handler(commands='buy') 
#       async def pizza(message: types.Message):
#          await message.answer('Успешно добавлено ')
#          global sumary_cost
#          sumary_cost = sumary_cost + 82000
#          global sumary_cost
# 
# 
# 
# ########################################################################################################
# 
# 
# #######################################################################################################
# 
# @dp.message_handler(text = 'Салса🍕') 
# async def pizza(message: types.Message):
#    photo = open(r"C:\Users\Stanislav Boduen\OneDrive\Рабочий стол\Telegram Bot\images\pizza\donnar-pizza.jpg", 'rb')
#    await bot.send_photo(chat_id=message.chat.id, photo=photo)
#    kb = [
#        [types.KeyboardButton(text="Маленькая")],
#        [types.KeyboardButton(text="Большая")]
#    ]
#    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
#    await message.answer('''
# Салса
# Курица, соус сальса, мягкий сыр моцарелла, халапеньо, болгарский перец и помидоры''', reply_markup=keyboard)
#    @dp.message_handler(text = 'Маленькая') 
#    async def pizza(message: types.Message):
#       await message.answer("55 000 сум💴")
#       await message.answer('Напишите /buy если хотите купить')
#       @dp.message_handler(commands='buy') 
#       async def pizza(message: types.Message):
#          await message.answer('Успешно добавлено ')
#          sumary_cost = sumary_cost + 55000
# 
# 
# 
#       @dp.message_handler(text = 'Большая') 
#       async def pizza(message: types.Message):
#          await message.answer('82 000 сум💴')
#          await message.answer('Напишите /buy если хотите купить')
#          @dp.message_handler(commands='buy') 
#          async def pizza(message: types.Message):
#             await message.answer('Успешно добавлено ')
#             sumary_cost = sumary_cost + 82000
# 
# 
# 
# @dp.message_handler(text = 'Салса🍕') 
# async def pizza(message: types.Message):
#    photo = open(r"C:\Users\Stanislav Boduen\OneDrive\Рабочий стол\Telegram Bot\images\pizza\donnar-pizza.jpg", 'rb')
#    await bot.send_photo(chat_id=message.chat.id, photo=photo)
#    kb = [
#        [types.KeyboardButton(text="Маленькая")],
#        [types.KeyboardButton(text="Большая")]
#    ]
#    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
#    await message.answer('''
# Салса
# Курица, соус сальса, мягкий сыр моцарелла, халапеньо, болгарский перец и помидоры''', reply_markup=keyboard)
#    @dp.message_handler(text = 'Маленькая') 
#    async def pizza(message: types.Message):
#       await message.answer("55 000 сум💴")
#       await message.answer('Напишите /buy если хотите купить')
#       @dp.message_handler(commands='buy') 
#       async def pizza(message: types.Message):
#          await message.answer('Успешно добавлено ')
#          sumary_cost = sumary_cost + 55000
# @dp.message_handler(text = 'Салса🍕') 
# async def pizza(message: types.Message):
#    photo = open(r"C:\Users\Stanislav Boduen\OneDrive\Рабочий стол\Telegram Bot\images\pizza\donnar-pizza.jpg", 'rb')
#    await bot.send_photo(chat_id=message.chat.id, photo=photo)
#    kb = [
#        [types.KeyboardButton(text="Маленькая")],
#        [types.KeyboardButton(text="Большая")]
#    ]
#    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
#    await message.answer('''
# Салса
# Курица, соус сальса, мягкий сыр моцарелла, халапеньо, болгарский перец и помидоры''', reply_markup=keyboard)
#    @dp.message_handler(text = 'Маленькая') 
#    async def pizza(message: types.Message):
#       await message.answer("55 000 сум💴")
#       await message.answer('Напишите /buy если хотите купить')
#       @dp.message_handler(commands='buy') 
#       async def pizza(message: types.Message):
#          await message.answer('Успешно добавлено ')
#          sumary_cost = sumary_cost + 55000
########################################################################################################



@dp.message_handler(text = 'Закуски🍟') 
async def zakus(message: types.Message):
   kb = [
       [types.KeyboardButton(text="Картошка фри🍟")],
       [types.KeyboardButton(text='Картошка "По деревенский"🍟')],
       [types.KeyboardButton(text="8 пеперони ролы🍟")],
       [types.KeyboardButton(text="4 пеперони ролы🍟")],
       [types.KeyboardButton(text="Паста Альфредо🍟")],
       [types.KeyboardButton(text="Бредстик🍟")],
       [types.KeyboardButton(text="Куриный Белистр🍟")],
       [types.KeyboardButton(text="Мясной Белистр🍟")],
       [types.KeyboardButton(text="Куриные поперсы🍟")]
   ]
   keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
   await message.answer("Что вы хотите из списка", reply_markup=keyboard)

##### Картошка фри🍟 #####
@dp.message_handler(text = 'Картошка фри🍟') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\snack\kartoshka fri.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Картошка фри
Свежесрезанный Хрустящий картофель фри из духовки''')
    
##### Картошка "По деревенский"🍟 #####
@dp.message_handler(text = 'Картошка "По деревенский"🍟') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\snack\po derevenski.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Картошка "По деревенский"
Картофель "по-деревенский" с хрустящей корочкой, только что вынутый из духовки''')

##### 8 пеперони ролы🍟 #####
@dp.message_handler(text = '8 пеперони ролы🍟') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\snack\peperoni roli(8).jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
8 пеперони ролы
Хрустящее тесто, нежный соус ранчо, пепперони и много сыра''')
    
##### 4 пеперони ролы🍟 #####
@dp.message_handler(text = '4 пеперони ролы🍟') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\snack\peperoni roli(4).jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
4 пеперони ролы
Хрустящее тесто, нежный соус ранчо, пепперони и много сыра''')
    
##### Паста Альфредо🍟 #####
@dp.message_handler(text = 'Паста Альфредо🍟') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\snack\alfredo.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Паста Альфредо
Индейка, нежный сыр моцарелла и шампиньоны в сочетании с пастой фузилли''')

##### Куриный Белистр🍟 #####
@dp.message_handler(text = 'Куриный Белистр🍟') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\snack\chicken bellisster.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Куриный Белистр
Вкусная курица в мягкой лепешке с настоящим сыром моцарелла, помидорами и соусом ранчо''')
    
##### Мясной Белистр🍟 #####
@dp.message_handler(text = 'Мясной Белистр🍟') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\snack\meat bellisster.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Мясной Белистр
Вкусное донарное мясо в мягкой лепешке с настоящим сыром моцарелла, помидорами, луком и соусом барбекю.''')

##### Куриные поперсы🍟 #####
@dp.message_handler(text = 'Куриные поперсы🍟') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\snack\chicken poppers.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Куриные поперсы
Qarsildoq tovuq bo'lakchalari 100% tovuq filesidan tayyorlangan va barbekyu sousi bilan qoplangan.''')
    



























@dp.message_handler(text = 'Напитки🍹') 
async def drinks(message: types.Message):
   kb = [
       [types.KeyboardButton(text="Coca-Cola 0,5 l🍹")],
       [types.KeyboardButton(text="Coca-Cola разливная🍹")],
       [types.KeyboardButton(text="Кола 0.25 баночная🍹")],
       [types.KeyboardButton(text="Coca-Cola 1 l🍹")],
       [types.KeyboardButton(text="Fanta разливная🍹")],
       [types.KeyboardButton(text="Coca-Cola 1,5 l🍹")],
       [types.KeyboardButton(text="Sprite разливной🍹")],
       [types.KeyboardButton(text="Fanta 0,5 l🍹")],
       [types.KeyboardButton(text="Fanta 1 l🍹")],
       [types.KeyboardButton(text="Fanta 1,5 l🍹")],
       [types.KeyboardButton(text="Sprite 0,5 l🍹")],
       [types.KeyboardButton(text="Sprite 1 l🍹")],
       [types.KeyboardButton(text="Sprite 1,5 l🍹")],
       [types.KeyboardButton(text="Обрикосовый сок🍹")],
       [types.KeyboardButton(text="Вода 1 l🍹")],
       [types.KeyboardButton(text="Ананасовый сок🍹")],
       [types.KeyboardButton(text="Апельсиновый сок🍹")], 
       [types.KeyboardButton(text="Вишнёвый сок🍹")],
       [types.KeyboardButton(text="Мультифруктовый сок🍹")],
       [types.KeyboardButton(text="Персиковый сок🍹")],
       [types.KeyboardButton(text="яблочный сок🍹")],
       [types.KeyboardButton(text="Американо☕️")],
       [types.KeyboardButton(text="Латте☕️")],
       [types.KeyboardButton(text="Капучино☕️")]
   ]
   keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
   await message.answer("Что вы хотите из списка", reply_markup=keyboard)


@dp.message_handler(text = 'Coca-Cola 0,5 l🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\cola(0.5).jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Coca-Cola 0,5 l''')


@dp.message_handler(text = 'Coca-Cola разливная🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\coca cola(dish).jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Coca-Cola разливная''')


@dp.message_handler(text = 'Кола 0.25 баночная🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\cola(0.25(free)).jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Кола 0.25 баночная''')

@dp.message_handler(text = 'Coca-Cola 1 l🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\cola(1).jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Coca-Cola 1 l''')

@dp.message_handler(text = 'Fanta разливная🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\fanta(dish).jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Fanta разливная''')
    
@dp.message_handler(text = 'Coca-Cola 1,5 l🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\cola(1.5).jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Coca-Cola 1,5 l''')
        
@dp.message_handler(text = 'Fanta разливная🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\fanta(dish).jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Fanta разливная''')

@dp.message_handler(text = 'Sprite разливной🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\sprite(dish).jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Sprite разливной''')

@dp.message_handler(text = 'Fanta 0,5 l🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\fanta(0.5).jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Fanta 0,5 l''')

@dp.message_handler(text = 'Fanta 1 l🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\fanta(1).jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Fanta 1 l''')

@dp.message_handler(text = 'Fanta 1,5 l🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\fanta(1,5).jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Fanta 1.5 l''')

@dp.message_handler(text = 'Sprite 0,5 l🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\sprite(0.5).jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Sprite 0,5 l''')

@dp.message_handler(text = 'Sprite 1 l🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\sprite(1).jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Sprite 1 l''')

@dp.message_handler(text = 'Sprite 1,5 l🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\sprite(1.5).jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Sprite 1,5 l''')

@dp.message_handler(text = 'Обрикосовый сок🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\обрикосовый.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Обрикосовый сок''')

@dp.message_handler(text = 'Вода 1 l🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\вода.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Вода 1 l''')

@dp.message_handler(text = 'Ананасовый сок🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\ананас.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Ананасовый сок''')

@dp.message_handler(text = 'Апельсиновый сок🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\апельсин.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Апельсиновый сок''')

@dp.message_handler(text = 'Вишнёвый сок🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\вышня.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Вишнёвый сок''')

@dp.message_handler(text = 'Мультифруктовый сок🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\мультифрукт.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Мультифруктовый сок''')

@dp.message_handler(text = 'Персиковый сок🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\персик.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Персиковый сок''')

@dp.message_handler(text = 'яблочный сок🍹') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\яблоко.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
яблочный сок''')

@dp.message_handler(text = 'Американо☕️') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\американо.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Американо☕️''')

@dp.message_handler(text = 'Латте☕️') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\лате.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Латте''')

@dp.message_handler(text = 'Капучино☕️') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\drinks\капучино.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Капучино''')











@dp.message_handler(text = 'Салаты🥬') 
async def salat(message: types.Message):
   kb = [
       [types.KeyboardButton(text="Греческий🥬")],
       [types.KeyboardButton(text="Цезарь🥬")]
   ]
   keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
   await message.answer("Что вы хотите из списка", reply_markup=keyboard)

##### Греческий🥬 #####
@dp.message_handler(text = 'Греческий🥬') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\salat\грецкий.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Греческий''')
    
##### Цезарь🥬 #####
@dp.message_handler(text = 'Цезарь🥬') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\salat\цезарь.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Цезарь''')


@dp.message_handler(text = 'Десерты🍧') 
async def salat(message: types.Message):
   kb = [
       [types.KeyboardButton(text="Эклеры 8 штук🍧")],
       [types.KeyboardButton(text="Эклеры 16 штук🍧")],
       [types.KeyboardButton(text="Шоколадный фонтан🍧")]
       
   ]
   keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
   await message.answer("Что вы хотите из списка", reply_markup=keyboard)

@dp.message_handler(text = 'Эклеры 8 штук🍧') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\disert\sinamon roll(8).jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Sinnamon Rollar 8 ta''')

@dp.message_handler(text = 'Эклеры 16 штук🍧') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\disert\sinamon roll(16).jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Sinnamon Rollar 16 ta''')

@dp.message_handler(text = 'Шоколадный фонтан🍧') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\disert\shokoladli fondan.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Шоколадный фонтан''')




@dp.message_handler(text = 'Соусы🧂') 
async def salat(message: types.Message):
   kb = [
      [types.KeyboardButton(text="Фирменный🧂")],
       [types.KeyboardButton(text="Сырный соус🧂")],
       [types.KeyboardButton(text="Барбикью соус🧂")]
       
   ]
   keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
   await message.answer("Что вы хотите из списка", reply_markup=keyboard)
    
@dp.message_handler(text = 'Фирменный🧂') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\sous\firmenniy.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Фирменный''')
    
@dp.message_handler(text = 'Сырный соус🧂') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\sous\cheese.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Сырный соус''')

@dp.message_handler(text = 'Барбикью соус🧂') 
async def pizza(message: types.Message):
    photo = open(r"C:\Users\user\Desktop\Telegram Bot\images\sous\barbekyu.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('''
Барбикью соус''')


@dp.message_handler(commands=['basket'])
async def cmd_start(message: types.Message):
   await message.answer(f'У вас заказ на {sumary_cost} сум')
   await message.answer('Напишите /rb что-бы отменить заказ')
   @dp.message_handler(commands=['rb'])
   async def cmd_start(message: types.Message):
      global sumary_cost
      sumary_cost = 0
      await message.answer('Заказ обнулен!')

@dp.message_handler(commands=['info'])
async def cmd_start(message: types.Message):
   await message.answer('''
ru: Bellissimo Pizza можно сытно и вкусно покушать большой компаний на раз, два, три! 
Встречайте наше новое комбо — «Три за 99»: это три пиццы из пяти на ваш выбор с общей 
скидкой в 35% Для всей семьи, коллег или друзей — попробуйте, вам обязательно понравится. 
Bellissimo Pizza — повод объединиться. 
uz: Bellissimo Pizza’da ko‘pchilik bo‘lib mazali va 
to‘yimli ovqatlanish uchun bir, ikki, uch desangiz bas! Yangi komboni kutib oling — 
«99 ga uchta»: beshta pitsa orasidan xohlagan uchtasini tanlab oling va 35% chegirmaga
ega bo‘ling. Katta oila, hamkasblar yoki do‘stlar uchun — tatib ko‘ring, sizga albatta 
yoqib tushadi. Bellissimo Pizza — birlashish uchun sabab.''')

@dp.message_handler(commands=['portfolio'])
async def cmd_start(message: types.Message):
   await message.answer('''
Тимур Усманов ⭐️⭐️⭐️⭐️:
Четыре звезды - это хорошая оценка, поэтому я даю этому месту хорошую оценку. Большинство пиццерий в Ташкенте, 
вроде Чопар, Московской пиццы, Додо и т.п. рядом с Белиссимо тянут лишь на три звезды. Есть конечно Рони, 
Крафт-пицца, Стуззико, Итальянская пицца, которые рядом с Белиссимо достойны 5 звёзд, но там ценник повыше. 
Белиссимо - идеальный вариант, чтобы заказать и забрать домой, а не кушать на месте. Да, и заказывайте на тонком тесте. 
Пирог вы можете поесть и в других заведениях.

Николай Лукьяненко ⭐️⭐️⭐️⭐️⭐️:
На мой взгляд самая хорошая доставка пиццы.
1. Она вкусная
2. Персонал очень вежливый особенно когда они поднимают рубку и называют ваше имя))

Yuri Reynsberg ⭐️⭐️⭐️⭐️⭐️:
Отличная пицца, всё есть, цена адекватная. Можно собрать свой набор по вкусу. За раз можно съесть более половины 
большой в один присест, на одного. Ибо вкусно.

Александр ⭐️⭐️⭐️⭐️⭐️:
Быстро. Вкусно. Обычно не съедаю корочки у пиццы, а тут тесто очень вкусное, так что ничего не осталось.
Пробовал Фирменную и Альфредо. Обе годные!
''')
   

@dp.message_handler(commands=['help'])
async def cmd_start(message: types.Message):
   await message.answer('''
Это бот сделанный (не професиональным) програмистом @yan_bragin_cs посвещенный обучению создания
тг ботов и это бот Bellissimo pizza, здесь вы можете выбрать
вашу любимаю пиццу но не заказать, потому-что это еще не готово
это всего лишь Beta-test.''')
   
@dp.message_handler(commands=['about'])
async def cmd_start(message: types.Message):
   await message.answer('''
Мы пиццерия Bellissimo pizza, у нас много вкусняшек
вы можете заказать у нас какие нибудь пиццы, сладости,
соусы, напитки, у нас есть почти всё! ну не почти, у нас есть много чего!''')
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
