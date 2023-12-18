#imports
from telegram import Bot
from telegram.ext import Updater, CommandHandler
from credits import bot_token
from random import choice, randint
from playerdata import PlayerData

#telegram
bot = Bot(token = bot_token)
updater = Updater(bot_token, use_context = True)
dispatcher = updater.dispatcher

#dices
dice1 = ['Кролик','Кролик','Кролик','Кролик','Свинья','Свинья','Овца','Овца','Кролик','Кролик','Корова','Волк', 'Овчарка', 'х2', 'Стадо']
dice2 = ['Кролик','Кролик','Кролик','Кролик','Овца','Овца','Свинья','Свинья','Кролик','Кролик','Лошадь','Лиса', 'Собака', 'х2', 'Медведь']

#password
password = randint(100000, 999999)



#player's step, player's list
player = [1, PlayerData(rabbits=1), PlayerData(rabbits=1)]


#functions

def Winners() -> None or str:
    winner = player[player[0]].anim
    if (winner[0] and winner[1] and winner[2] and winner[3] and winner[4]) > 0:
        return f'Игрок {player[0]} победил'
    else:
        return None

#switch player's step
def SwitchPlayer() -> None:
    if player[0] == 1:
        player[0] = 2
    else:
        player[0] = 1
    return

#rolling dices
def Roll(step:int) -> str:
    updates = [0 for i in range(8)]
    values = [choice(dice1), choice(dice2)]
    if 'Лиса' in values:
        if player[step].anim[5] > 0:
            player[step].anim[5] -= 1
            updates[5] -= 1
        elif player[step].anim[7] > 0:
            pass
        else:
            buf = player[step].anim[0]
            player[step].anim[0] = 1
            updates[0] -= buf-1
    if 'Волк' in values:
        if player[step].anim[6] > 0:
            player[step].anim[6] -= 1
            updates[6] -= 1
        elif player[step].anim[7] > 0:
            pass
        else:
            updates[1] -= player[step].anim[1]
            updates[2] -= player[step].anim[2]
            updates[3] -= player[step].anim[3]
            player[step].anim[1] = 0
            player[step].anim[2] = 0
            player[step].anim[3] = 0
    if 'Собака' in values:
        player[step].anim[5] += 1
        updates[5] += 1
    if 'Овчарка' in values:
        player[step].anim[6] += 1
        updates[6] += 1
    if 'Медведь' in values:
        if player[step].anim[7] > 0:
            player[step].anim[7] -= 1
            updates[7] -= 1
        else:
            if player[step].anim[3] > 0:
                updates[3] -= player[step].anim[3]
                player[step].anim[3] = 0
            else:
                updates[2] -= player[step].anim[2]
                player[step].anim[2] = 0
    if 'Стадо' in values:
        player[step].anim[1] += 3
        player[step].anim[2] += 2
        updates[1] += 3
        updates[2] += 2
    if values[0] == values[1]:
        match values[0]:
            case 'Кролик':
                if player[step].anim[0] > 0:
                    player[step].anim[0] *= 2
                    updates[0] += player[step].anim[0]/2
                else:
                    player[step].anim[0] = 1
                    updates[0] += 1
            case 'Овца':
                if player[step].anim[1] == 0:
                    player[step].anim[1] = 1
                    updates[1] += 1
                else:
                    player[step].anim[1] *= 2
                    updates[1] += player[step].anim[1]/2
            case 'Свинья':
                if player[step].anim[2] == 0:
                    player[step].anim[2] = 1
                    updates[2] += 1
                else:
                    player[step].anim[2] *= 2
                    updates[2] += player[step].anim[2]/2
            # case 'Корова':
            #     if player[step].anim[3] == 0:
            #         player[step].anim[3] = 1
            #     else:
            #         player[step].anim[3] *= 2
            # case 'Лошадь':
            #     if player[step].anim[4] == 0:
            #         player[step].anim[4] = 1
            #     else:
            #         player[step].anim[4] *= 2
            case 'х2':
                player[step].anim[0] *= 3
                player[step].anim[1] *= 3
                player[step].anim[2] *= 3
                player[step].anim[3] *= 3
                player[step].anim[4] *= 3
                updates[0] += player[step].anim[0]*2/3
                updates[1] += player[step].anim[1]*2/3
                updates[2] += player[step].anim[2]*2/3
                updates[3] += player[step].anim[3]*2/3
                updates[4] += player[step].anim[4]*2/3

        values = [f'2 {values[0]}']
    else:
        for i in range(2):
            match values[i]:
                case 'Кролик':
                    buf = player[step].anim[0]
                    player[step].anim[0] *= 1.5
                    player[step].anim[0] = round(player[step].anim[0])
                    updates[0] += player[step].anim[0] - buf
                case 'Овца':
                    buf = player[step].anim[1]
                    player[step].anim[1] *= 1.5
                    player[step].anim[1] = round(player[step].anim[1])
                    updates[1] += player[step].anim[1] - buf
                case 'Свинья':
                    buf = player[step].anim[2]
                    player[step].anim[2] *= 1.5
                    player[step].anim[2] = round(player[step].anim[2])
                    updates[2] += player[step].anim[2] - buf
                case 'Корова':
                    buf = player[step].anim[3]
                    player[step].anim[3] *= 1.5
                    player[step].anim[3] = round(player[step].anim[3])
                    updates[3] += player[step].anim[3] - buf
                case 'Лошадь':
                    buf = player[step].anim[4]
                    player[step].anim[4] *= 1.5
                    player[step].anim[4] = round(player[step].anim[4])
                    updates[4] += player[step].anim[4] - buf
                case 'х2':
                    player[step].anim[0] *= 2
                    player[step].anim[1] *= 2
                    player[step].anim[2] *= 2
                    player[step].anim[3] *= 2
                    player[step].anim[4] *= 2
                    updates[0] += player[step].anim[0]/2
                    updates[1] += player[step].anim[1]/2
                    updates[2] += player[step].anim[2]/2
                    updates[3] += player[step].anim[3]/2
                    updates[4] += player[step].anim[4]/2
        values = [f'{values[0]} и {values[1]}']
    text_upd = str()
    anims = ['Кроликов: ','Овец: ','Свиней: ','Коров: ','Лошадей: ','Собак: ','Овчарок: ','Сторожей: ']
    for i in range(8):
        if updates[i] != 0:
            text_upd += anims[i] + str(player[step].anim[i]) + f'   ({int(updates[i])})\n\n'
    values.append(str(text_upd))
    return values


#bot functions

def Cheats(updater, context):
    player[player[0]].anim[0] = 100
    player[player[0]].anim[1] = 100
    player[player[0]].anim[2] = 100
    player[player[0]].anim[3] = 100
    player[player[0]].anim[4] = 100

    player[player[0]].anim[5] = 1
    player[player[0]].anim[6] = 1
    player[player[0]].anim[7] = 1
    return

def StartGame(updater, context):
    player[1].reset(1)
    player[2].reset(1)
    context.bot.send_message(updater.effective_chat.id, 'Игра началась')
    context.bot.send_message(updater.effective_chat.id, f'Ход игрока {player[0]}')
    return

def Start(updater, context):
    player[0] = 1
    context.bot.send_message(updater.effective_chat.id, 'Бот Суперфермер запущен\n\n/help для ознакомления с командами\n/rules для ознакомления с правилами\n/game для начала новой игры\n  ---> /howtoplay <---')
    return

def HowToPlay(updater, context):
    context.bot.send_message(updater.effective_chat.id, 'Перед началом игры игроки должны определиться, кто будет первый, а кто второй. Когда наступает ваш ход, вы обязаны кинуть кости, и только после этого можете совершить обмен. После того как вы завершите свой ход, напишите /next. Вы также можете играть в одиночку, в таком случае писать команду /next не нужно.')

def ShowRules(updater, context):
    context.bot.send_message(updater.effective_chat.id, 'Игра Суперфермер - это игра на 2 человека. Цель игры собрать на своей ферме всех животных. В течении игры вы будете кидать 2 кости, которые изображают произошедшее событие, также в свой ход вы можете обменять несколько своих животных на какое-то другое (подробнее на /trades). Если на кубике выпадает 2 одинаковых животных, то вы получаете 1 экземпляр себе на ферму. Если выпадает только 1 животное, то если оно у вас уже есть, то вы получаете еще половину от количества уже имеющихся (округление в большую сторону). Также на кубике может выпасть волк, лиса или медведь: когда приходит лиса, она съедает всех кроликов, кроме одного; когда приходит волк, он съедает всех животных кроме кроликов и лошадей; когда приходит медведь, он съедает всех коров, если у игрока нет ни одной коровы, то он съедает всех свиней. Когда вы закончите свой ход напишите /next. Для комфортной игры требуется доверие игроков друг другу, а также соблюдение правил и отсутствие шуллерства.\nПриятной игры!')
    return

def ShowCommands(updater, context):
    context.bot.send_message(updater.effective_chat.id, '''
/start - Вызвать бота
/game - Начать новую игру
/rules - Прочитать правила
/trades - Посмотреть возможные обмены
/roll - Кинуть кости
/farm - Просмотреть свою ферму
/next - Закончить ход''')
    return
    
def ShowTradeCommands(updater, context):
    context.bot.send_message(updater.effective_chat.id, '/sheep - Купить 1 овцу взамен на 6 кроликов\n\n/pig - Купить 1 свинью взамен на 2 овцы\n\n/cow - Купить 1 корову взамен на 3 свиньи\n\n/horse - Купить 1 лошадь взамен на 2 коровы\n\n/dog - Купить собаку взамен на 1 овцу (/infodog для справки)\n\n/sheepdog - Купить овчарку взамен на 1 корову (/infosheepdog для справки)\n\n/guard - Купить сторожа взамен на 1 лошадь (/infoguard для справки)')
    return

def NextPlayer(updater, context):
    SwitchPlayer()
    context.bot.send_message(updater.effective_chat.id, f'Ход игрока {player[0]}')
    return

def Dicing(updater, context):
    data = Roll(player[0])
    values = data[0]
    upd = data[1]
    context.bot.send_message(updater.effective_chat.id, f'Игроку {player[0]} выпало {values}')
    if upd != '':
        context.bot.send_message(updater.effective_chat.id, upd)
    win = Winners()
    if win != None:
        context.bot.send_message(updater.effective_chat.id, win)
    return

def SeeFarm(updater, context):
    context.bot.send_message(updater.effective_chat.id, f'У игрока {player[0]} на данный момент имеется:\n\n\n{player[player[0]].anim[0]} кроликов\n{player[player[0]].anim[1]} овец\n{player[player[0]].anim[2]} свиней\n{player[player[0]].anim[3]} коров\n{player[player[0]].anim[4]} лошадей\n\n{player[player[0]].anim[5]} собак\n{player[player[0]].anim[6]} овчарок\n{player[player[0]].anim[7]} сторожей')
    return

def DogInfo(updater, context):
    context.bot.send_message(updater.effective_chat.id, 'Если у вас на руках есть собака, то если на кубике выпадет лиса, то собака защитит вашу ферму. Важно! Собака уходит сразу после того как была использована.')
    return

def SheepDogInfo(updater, context):
    context.bot.send_message(updater.effective_chat.id, 'Если у вас на руках есть овчарка, то если на кубике выпадет волк, то овчарка защитит вашу ферму. Важно! Овчарка уходит сразу после того как была использована.')
    return

def GuardInfo(updater, context):
    context.bot.send_message(updater.effective_chat.id, 'Если у вас на руках есть сторож, то любые угрозы из леса вам не страшны. Важно! Сторож уходит после того, как защитит вас от медведя.')

def BuySheep(updater, context):
    if player[player[0]].anim[0] > 6:
        player[player[0]].anim[0] -= 6
        player[player[0]].anim[1] += 1
        context.bot.send_message(updater.effective_chat.id, f'Игрок {player[0]} купил овцу успешно\n\nОсталось кроликов: {player[player[0]].anim[0]}')
    else:
        context.bot.send_message(updater.effective_chat.id, 'Недостаточно кроликов.\nМинимальное количество: 7')
    win = Winners()
    if win != None:
        context.bot.send_message(updater.effective_chat.id, win)
    return

def BuyPig(updater, context):
    if player[player[0]].anim[1] >= 2:
        player[player[0]].anim[1] -= 2
        player[player[0]].anim[2] += 1
        context.bot.send_message(updater.effective_chat.id, f'Игрок {player[0]} купил свинью успешно\n\nОсталось овец: {player[player[0]].anim[1]}')
    else:
        context.bot.send_message(updater.effective_chat.id, 'Недостаточно овец.\nМинимальное количество: 2')
    win = Winners()
    if win != None:
        context.bot.send_message(updater.effective_chat.id, win)
    return

def BuyCow(updater, context):
    if player[player[0]].anim[2] >= 3:
        player[player[0]].anim[2] -= 3
        player[player[0]].anim[3] += 1
        context.bot.send_message(updater.effective_chat.id, f'Игрок {player[0]} купил корову успешно\n\nОсталось свиней: {player[player[0]].anim[2]}')
    else:
        context.bot.send_message(updater.effective_chat.id, 'Недостаточно свиней.\nМинимальное количество: 3')
    win = Winners()
    if win != None:
        context.bot.send_message(updater.effective_chat.id, win)
    return

def BuyHorse(updater, context):
    if player[player[0]].anim[3] >= 2:
        player[player[0]].anim[3] -= 2
        player[player[0]].anim[4] += 1
        context.bot.send_message(updater.effective_chat.id, f'Игрок {player[0]} купил лошадь успешно\n\nОсталось коров: {player[player[0]].anim[3]}')
    else:
        context.bot.send_message(updater.effective_chat.id, 'Недостаточно коров.\nМинимальное количество: 2')
    win = Winners()
    if win != None:
        context.bot.send_message(updater.effective_chat.id, win)
    return

def BuyDog(updater, context):
    if player[player[0]].anim[1] >= 1:
        player[player[0]].anim[1] -= 1
        player[player[0]].anim[5] += 1
        context.bot.send_message(updater.effective_chat.id, f'Игрок {player[0]} купил собаку успешно\n\nОсталось овец: {player[player[0]].anim[1]}')
    else:
        context.bot.send_message(updater.effective_chat.id, 'Недостаточно овец.\nМинимальное количество: 1')
    return

def BuySheepdog(updater, context):
    if player[player[0]].anim[3] >= 1:
        player[player[0]].anim[3] -= 1
        player[player[0]].anim[6] += 1
        context.bot.send_message(updater.effective_chat.id, f'Игрок {player[0]} купил овчарку успешно\n\nОсталось коров: {player[player[0]].anim[3]}')
    else:
        context.bot.send_message(updater.effective_chat.id, 'Недостаточно коров.\nМинимальное количество: 1')
    return

def BuyGuard(updater, context):
    if player[player[0]].anim[4] >= 1:
        player[player[0]].anim[4] -= 1
        player[player[0]].anim[7] += 1
        context.bot.send_message(updater.effective_chat.id, f'Игрок {player[0]} купил сторожа успешно\n\nОсталось лошадей: {player[player[0]].anim[4]}')
    else:
        context.bot.send_message(updater.effective_chat.id, 'Недостаточно лошадей.\nМинимальное количество: 1')
    return


#creating handlers
start_hand = CommandHandler('start', Start)
game_hand = CommandHandler('game', StartGame)
guide_hand = CommandHandler('howtoplay', HowToPlay)
rules_hand = CommandHandler('rules', ShowRules)
coms_hand = CommandHandler('help', ShowCommands)
trade_hand = CommandHandler('trades', ShowTradeCommands)
next_hand = CommandHandler('next', NextPlayer)
roll_hand = CommandHandler('roll', Dicing)
farm_hand = CommandHandler('farm', SeeFarm)
infodog_hand = CommandHandler('infodog', DogInfo)
infosheepdog_hand = CommandHandler('infosheepdog', SheepDogInfo)
infoguard_hand = CommandHandler('infoguard', GuardInfo)
sheep_hand = CommandHandler('sheep', BuySheep)
pig_hand = CommandHandler('pig', BuyPig)
cow_hand = CommandHandler('cow', BuyCow)
horse_hand = CommandHandler('horse', BuyHorse)
dog_hand = CommandHandler('dog', BuyDog)
sheepdog_hand = CommandHandler('sheepdog', BuySheepdog)
guard_hand = CommandHandler('guard', BuyGuard)
cheat_hand = CommandHandler(str(password), Cheats)

#adding handlers to dispatcher
dispatcher.add_handler(start_hand)
dispatcher.add_handler(game_hand)
dispatcher.add_handler(guide_hand)
dispatcher.add_handler(rules_hand)
dispatcher.add_handler(coms_hand)
dispatcher.add_handler(trade_hand)
dispatcher.add_handler(next_hand)
dispatcher.add_handler(roll_hand)
dispatcher.add_handler(farm_hand)
dispatcher.add_handler(infodog_hand)
dispatcher.add_handler(infosheepdog_hand)
dispatcher.add_handler(infoguard_hand)
dispatcher.add_handler(sheep_hand)
dispatcher.add_handler(pig_hand)
dispatcher.add_handler(cow_hand)
dispatcher.add_handler(horse_hand)
dispatcher.add_handler(dog_hand)
dispatcher.add_handler(sheepdog_hand)
dispatcher.add_handler(guard_hand)
dispatcher.add_handler(cheat_hand)

print(password)
#starting code
updater.start_polling()
updater.idle
