from difflib import restore
from glob import glob
import time
from datetime import datetime
from importlib import reload
from pickle import NONE
from sqlite3 import Time
from bs4 import BeautifulSoup
import telebot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# import emailSenha

# Por informações do seu bot.########
api_key = ''  # TOKEN DO SEU BOT
chat_id =''  # ID DO CANAL pladix
#####################################
bot = telebot.TeleBot(token=api_key)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
nav = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), chrome_options=options)

nav.get('https://blaze.com/pt/games/double')

analisar = 0
analisar2 = 0
analisar3 = 0
analisar4 = 0
analisar5 = 0
gale_atual = 0
gale_atual2 = 0
gale_atual3 = 0
gale_atual4 = 0
gale_atual5 = 0
analisar_open = 0
resultsDouble = []
possivelsinal = 0
possivelsinal2 = 0
possivelsinal3 = 0
possivelsinal4 = 0
possivelsinal5 = 0
wins = 0
loss = 0
brancos = 0
assertividade = 0
# resto = 0

# round((wins + brancos) / (wins + loss + brancos) * 100, 2)
#
# hora = datetime.today().strftime('%H:%M')


while True:
    def qualnum(x):
        if x == '0':
            return 0

        if x == '1':
            return 1

        if x == '2':
            return 2

        if x == '3':
            return 3

        if x == '4':
            return 4

        if x == '5':
            return 5

        if x == '6':
            return 6

        if x == '7':
            return 7

        if x == '8':
            return 8

        if x == '9':
            return 9

        if x == '10':
            return 10

        if x == '11':
            return 11

        if x == '12':
            return 12

        if x == '13':
            return 13

        if x == '14':
            return 14


    def qualcor(x):
        if x == '0':
            return 'B'

        if x == '1':
            return 'V'

        if x == '2':
            return 'V'

        if x == '3':
            return 'V'

        if x == '4':
            return 'V'

        if x == '5':
            return 'V'

        if x == '6':
            return 'V'

        if x == '7':
            return 'V'

        if x == '8':
            return 'P'

        if x == '9':
            return 'P'

        if x == '10':
            return 'P'

        if x == '11':
            return 'P'

        if x == '12':
            return 'P'

        if x == '13':
            return 'P'

        if x == '14':
            return 'P'


    def qualsimb(x):
        if x == '0':
            return '⚪️'

        if x == '1':
            return '🔴️'

        if x == '2':
            return '🔴️'

        if x == '3':
            return '🔴️'

        if x == '4':
            return '🔴️'

        if x == '5':
            return '🔴️'

        if x == '6':
            return '🔴️'

        if x == '7':
            return '🔴️'

        if x == '8':
            return '⚫️'

        if x == '9':
            return '⚫️'

        if x == '10':
            return '⚫️'

        if x == '11':
            return '⚫️'

        if x == '12':
            return '⚫️'

        if x == '13':
            return '⚫️'

        if x == '14':
            return '⚫️'


    try:
        resulROOL = nav.find_element(
            By.XPATH, '//*[@id="roulette-timer"]/div[1]').text
    except NameError as erro:
        print(erro)
        print('ERRO 403')
    except Exception as erro:
        print('ERRO 404')

    analisar_open = 0
    if resulROOL == 'Girando...':
        analisar_open = 1
        print('Analisando')
        time.sleep(13)
        c = nav.page_source
        resultsDouble.clear()

        soup = BeautifulSoup(c, 'html.parser')
        go = soup.find('div', class_="entries main")
        for i in go:
            if i.getText():
                resultsDouble.append(i.getText())
            else:
                resultsDouble.append('0')

        resultsDouble = resultsDouble[:-1]

        if analisar_open == 1:

            default = resultsDouble[0:4]

            mapeando = map(qualnum, default)
            mapeando2 = map(qualcor, default)
            finalnum = list(mapeando)
            finalcor = list(mapeando2)


            def CHECK_VERSION(num):
                global possivelsinal
                # global possivelsinal2
                global possivelsinal3
                global possivelsinal4
                global possivelsinal5
                global analisar
                # global analisar2
                global analisar3
                global analisar4
                global analisar5
                global gale_atual
                # global gale_atual2
                global gale_atual3
                global gale_atual4
                global gale_atual5
                global wins
                global loss
                global brancos
                global assertividade
                # global resto

                if possivelsinal == 0:
                    if num == ['V', 'V', 'V', 'P']:
                        possivelsinal = 1
                        bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                        print("send msg")
                        return
                    if num == ['P', 'P', 'P', 'V']:
                        possivelsinal = 1
                        bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                        print("send msg")
                        return

                if analisar == 0:
                    if num == ['V', 'V', 'V', 'V']:
                        analisar = 1
                        analisar2 = 7
                        possivelsinal2 = 7
                        analisar3 = 7
                        possivelsinal3 = 7
                        analisar4 = 7
                        possivelsinal4 = 7
                        analisar5 = 7
                        possivelsinal5 = 7
                        bot.send_message(chat_id=chat_id, text='''
🎲️ Oportunidade Encontrada

🎯️ Apostar em PRETO ⚫️

🎳️ Opcional: Cobrir no BRANCO ⚪️

🎰️ Blaze Double
                        ''')
                        print("send msg")
                        return
                    if num == ['P', 'P', 'P', 'P']:
                        analisar = 1
                        analisar2 = 7
                        possivelsinal2 = 7
                        analisar3 = 7
                        possivelsinal3 = 7
                        analisar4 = 7
                        possivelsinal4 = 7
                        analisar5 = 7
                        possivelsinal5 = 7
                        bot.send_message(chat_id=chat_id, text='''
🎲️ Oportunidade Encontrada

🎯️ Apostar em VERMELHO 🔴️️

🎳️ Opcional: Cobrir no BRANCO ⚪️

🎰️ Blaze Double
                        ''')
                        print("send msg")
                        return

                elif analisar == 1:

                    if gale_atual == 0:
                        # WIN    #['X','V', 'V']: manda sinal
                        if num == ['P', 'V', 'V', 'V']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar = 0
                            gale_atual = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['V', 'P', 'P', 'P']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar = 0
                            gale_atual = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'V', 'V', 'V']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar = 0
                            gale_atual = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'P', 'P', 'P']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar = 0
                            gale_atual = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return

                        if num == ['V', 'V', 'V', 'V']:
                            gale_atual = gale_atual + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 1ª PROTEÇÃO''')
                            print("send msg")
                            return
                        if num == ['P', 'P', 'P', 'P']:
                            gale_atual = gale_atual + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 1ª PROTEÇÃO''')
                            print("send msg")
                            return

                    if gale_atual == 1:
                        if num == ['P', 'V', 'V', 'V']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar = 0
                            gale_atual = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['V', 'P', 'P', 'P']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar = 0
                            gale_atual = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'V', 'V', 'V']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar = 0
                            gale_atual = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'P', 'P', 'P']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar = 0
                            gale_atual = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return

                        if num == ['V', 'V', 'V', 'V']:
                            gale_atual = gale_atual + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 2ª PROTEÇÃO''')
                            print("send msg")
                            return
                        if num == ['P', 'P', 'P', 'P']:
                            gale_atual = gale_atual + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 2ª PROTEÇÃO''')
                            print("send msg")
                            return

                    if gale_atual == 2:
                        if num == ['P', 'V', 'V', 'V']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar = 0
                            gale_atual = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['V', 'P', 'P', 'P']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar = 0
                            gale_atual = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'V', 'V', 'V']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar = 0
                            gale_atual = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'P', 'P', 'P']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar = 0
                            gale_atual = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return

                        if num == ['V', 'V', 'V', 'V']:
                            loss = loss + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''❌️ LOSS 😓️''')
                            bot.send_message(chat_id=chat_id, text='''⚠️ ATENÇÃO AO GERENCIAMENTO''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar = 0
                            gale_atual = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['P', 'P', 'P', 'P']:
                            loss = loss + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''❌️ LOSS 😓️''')
                            bot.send_message(chat_id=chat_id, text='''⚠️ ATENÇÃO AO GERENCIAMENTO''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar = 0
                            gale_atual = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return

                    if analisar == 0 and gale_atual == 0:
                        possivelsinal = 0
                        return

                #################################################
                # if possivelsinal2 == 0:
                #     if num == ['V', 'P', 'V', 'V']:
                #         possivelsinal2 = 1
                #         bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                #         print("send msg")
                #         return
                #     if num == ['P', 'V', 'P', 'P']:
                #         possivelsinal2 = 1
                #         bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                #         print("send msg")
                #         return
                #     if num == ['V', 'P', 'V', 'B']:
                #         possivelsinal2 = 1
                #         bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                #         print("send msg")
                #         return
                #     if num == ['P', 'V', 'P', 'B']:
                #         possivelsinal2 = 1
                #         bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                #         print("send msg")
                #         return

                if analisar2 == 0:
                    if num == ['P', 'V', 'V', 'B']:
                        analisar2 = 1
                        analisar = 7
                        possivelsinal = 7
                        analisar3 = 7
                        possivelsinal3 = 7
                        analisar4 = 7
                        possivelsinal4 = 7
                        analisar5 = 7
                        possivelsinal5 = 7
                        bot.send_message(chat_id=chat_id, text='''
🎲️ Oportunidade Encontrada

🎯️ Apostar em PRETO ⚫️

🎳️ Opcional: Cobrir no BRANCO ⚪️

🎰️ Blaze Double
                        ''')
                        print("send msg")
                        return
                    if num == ['V', 'P', 'P', 'B']:
                        analisar2 = 1
                        analisar = 7
                        possivelsinal = 7
                        analisar3 = 7
                        possivelsinal3 = 7
                        analisar4 = 7
                        possivelsinal4 = 7
                        analisar5 = 7
                        possivelsinal5 = 7
                        bot.send_message(chat_id=chat_id, text='''
🎲️ Oportunidade Encontrada

🎯️ Apostar em VERMELHO 🔴️️

🎳️ Opcional: Cobrir no BRANCO ⚪️

🎰️ Blaze Double
                        ''')
                        print("send msg")
                        return

                elif analisar2 == 1:

                    if gale_atual2 == 0:
                        # WIN    #['X','V', 'V']: manda sinal
                        if num == ['P', 'P', 'V', 'V']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar2 = 0
                            gale_atual2 = 0
                            possivelsinal2 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['V', 'V', 'P', 'P']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar2 = 0
                            gale_atual2 = 0
                            possivelsinal2 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'P', 'V', 'V']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar2 = 0
                            gale_atual2 = 0
                            possivelsinal2 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'V', 'P', 'P']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar2 = 0
                            gale_atual2 = 0
                            possivelsinal2 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['V', 'P', 'V', 'V']:
                            gale_atual2 = gale_atual2 + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 1ª PROTEÇÃO''')
                            print("send msg")
                            return
                        if num == ['P', 'V', 'P', 'P']:
                            gale_atual2 = gale_atual2 + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 1ª PROTEÇÃO''')
                            print("send msg")
                            return

                    if gale_atual2 == 1:
                        if num == ['P', 'V', 'P', 'V']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar2 = 0
                            gale_atual2 = 0
                            possivelsinal2 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['V', 'P', 'V', 'P']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar2 = 0
                            gale_atual2 = 0
                            possivelsinal2 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'V', 'P', 'V']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar2 = 0
                            gale_atual2 = 0
                            possivelsinal2 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'P', 'V', 'P']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar2 = 0
                            gale_atual2 = 0
                            possivelsinal2 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return

                        if num == ['V', 'V', 'P', 'V']:
                            gale_atual2 = gale_atual2 + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 2ª PROTEÇÃO''')
                            print("send msg")
                            return
                        if num == ['P', 'P', 'V', 'P']:
                            gale_atual2 = gale_atual2 + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 2ª PROTEÇÃO''')
                            print("send msg")
                            return

                    if gale_atual2 == 2:
                        if num == ['P', 'V', 'V', 'P']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar2 = 0
                            gale_atual2 = 0
                            possivelsinal2 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['V', 'P', 'P', 'V']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar2 = 0
                            gale_atual2 = 0
                            possivelsinal2 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'V', 'V', 'P']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar2 = 0
                            gale_atual2 = 0
                            possivelsinal2 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'P', 'P', 'V']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar2 = 0
                            gale_atual2 = 0
                            possivelsinal2 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return

                        if num == ['V', 'V', 'V', 'P']:
                            loss = loss + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''❌️ LOSS 😓️''')
                            bot.send_message(chat_id=chat_id, text='''⚠️ ATENÇÃO AO GERENCIAMENTO''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar2 = 0
                            gale_atual2 = 0
                            possivelsinal2 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['P', 'P', 'P', 'V']:
                            loss = loss + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''❌️ LOSS 😓️''')
                            bot.send_message(chat_id=chat_id, text='''⚠️ ATENÇÃO AO GERENCIAMENTO''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar2 = 0
                            gale_atual2 = 0
                            possivelsinal2 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return

                    if analisar2 == 0 and gale_atual2 == 0:
                        possivelsinal2 = 0
                        return

                #################################################
                if possivelsinal3 == 0:
                    if num == ['P', 'V', 'B', 'P']:
                        possivelsinal3 = 1
                        bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                        print("send msg")
                        return
                    if num == ['P', 'V', 'B', 'V']:
                        possivelsinal3 = 1
                        bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                        print("send msg")
                        return
                    if num == ['V', 'P', 'B', 'P']:
                        possivelsinal3 = 1
                        bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                        print("send msg")
                        return
                    if num == ['V', 'P', 'B', 'V']:
                        possivelsinal3 = 1
                        bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                        print("send msg")
                        return
                    if num == ['V', 'P', 'B', 'B']:
                        possivelsinal3 = 1
                        bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                        print("send msg")
                        return
                    if num == ['P', 'V', 'B', 'B']:
                        possivelsinal3 = 1
                        bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                        print("send msg")
                        return

                if analisar3 == 0:
                    if num == ['P', 'P', 'V', 'B']:
                        analisar3 = 1
                        analisar = 7
                        possivelsinal = 7
                        analisar2 = 7
                        possivelsinal2 = 7
                        analisar4 = 7
                        possivelsinal4 = 7
                        analisar5 = 7
                        possivelsinal5 = 7
                        bot.send_message(chat_id=chat_id, text='''
🎲️ Oportunidade Encontrada

🎯️ Apostar em VERMELHO 🔴️️️

🎳️ Opcional: Cobrir no BRANCO ⚪️

🎰️ Blaze Double                      
                        ''')
                        print("send msg")
                        return
                    if num == ['V', 'V', 'P', 'B']:
                        analisar3 = 1
                        analisar = 7
                        possivelsinal = 7
                        analisar2 = 7
                        possivelsinal2 = 7
                        analisar4 = 7
                        possivelsinal4 = 7
                        analisar5 = 7
                        possivelsinal5 = 7
                        bot.send_message(chat_id=chat_id, text='''
🎲️ Oportunidade Encontrada

🎯️ Apostar em PRETO ⚫️

🎳️ Opcional: Cobrir no BRANCO ⚪️

🎰️ Blaze Double
                        ''')
                        print("send msg")
                        return

                elif analisar3 == 1:

                    if gale_atual3 == 0:
                        # WIN    #['X','V', 'V']: manda sinal
                        if num == ['V', 'P', 'P', 'V']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar3 = 0
                            gale_atual3 = 0
                            possivelsinal3 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['P', 'V', 'V', 'P']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar3 = 0
                            gale_atual3 = 0
                            possivelsinal3 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'P', 'P', 'V']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar3 = 0
                            gale_atual3 = 0
                            possivelsinal3 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'V', 'V', 'P']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar3 = 0
                            gale_atual3 = 0
                            possivelsinal3 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return

                        if num == ['P', 'P', 'P', 'V']:
                            gale_atual3 = gale_atual3 + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 1ª PROTEÇÃO''')
                            print("send msg")
                            return
                        if num == ['V', 'V', 'V', 'P']:
                            gale_atual3 = gale_atual3 + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 1ª PROTEÇÃO''')
                            print("send msg")
                            return

                    if gale_atual3 == 1:
                        if num == ['V', 'P', 'P', 'P']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar3 = 0
                            gale_atual3 = 0
                            possivelsinal3 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['P', 'V', 'V', 'V']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar3 = 0
                            gale_atual3 = 0
                            possivelsinal3 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'P', 'P', 'P']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar3 = 0
                            gale_atual3 = 0
                            possivelsinal3 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'V', 'V', 'V']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar3 = 0
                            gale_atual3 = 0
                            possivelsinal3 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return

                        if num == ['P', 'P', 'P', 'P']:
                            gale_atual3 = gale_atual3 + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 2ª PROTEÇÃO''')
                            print("send msg")
                            return
                        if num == ['V', 'V', 'V', 'V']:
                            gale_atual3 = gale_atual3 + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 2ª PROTEÇÃO''')
                            print("send msg")
                            return

                    if gale_atual3 == 2:
                        if num == ['V', 'P', 'P', 'P']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar3 = 0
                            gale_atual3 = 0
                            possivelsinal3 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['P', 'V', 'V', 'V']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar3 = 0
                            gale_atual3 = 0
                            possivelsinal3 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'P', 'P', 'P']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar3 = 0
                            gale_atual3 = 0
                            possivelsinal3 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'V', 'V', 'V']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar3 = 0
                            gale_atual3 = 0
                            possivelsinal3 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return

                        if num == ['P', 'P', 'P', 'P']:
                            loss = loss + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''❌️ LOSS 😓️''')
                            bot.send_message(chat_id=chat_id, text='''⚠️ ATENÇÃO AO GERENCIAMENTO''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar3 = 0
                            gale_atual3 = 0
                            possivelsinal3 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['V', 'V', 'V', 'V']:
                            loss = loss + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''❌️ LOSS 😓️''')
                            bot.send_message(chat_id=chat_id, text='''⚠️ ATENÇÃO AO GERENCIAMENTO''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar3 = 0
                            gale_atual3 = 0
                            possivelsinal3 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return

                    if analisar3 == 0 and gale_atual3 == 0:
                        possivelsinal3 = 0
                        return

                #################################################
                if possivelsinal4 == 0:
                    if num == ['V', 'V', 'B', 'P']:
                        possivelsinal4 = 1
                        bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                        print("send msg")
                        return
                    if num == ['V', 'V', 'B', 'V']:
                        possivelsinal4 = 1
                        bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                        print("send msg")
                        return
                    if num == ['P', 'P', 'B', 'P']:
                        possivelsinal4 = 1
                        bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                        print("send msg")
                        return
                    if num == ['P', 'P', 'B', 'V']:
                        possivelsinal4 = 1
                        bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                        print("send msg")
                        return
                    if num == ['V', 'V', 'B', 'B']:
                        possivelsinal4 = 1
                        bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                        print("send msg")
                        return
                    if num == ['P', 'P', 'B', 'B']:
                        possivelsinal4 = 1
                        bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                        print("send msg")
                        return

                if analisar4 == 0:
                    if num == ['V', 'V', 'V', 'B']:
                        analisar4 = 1
                        analisar = 7
                        possivelsinal = 7
                        analisar2 = 7
                        possivelsinal2 = 7
                        analisar3 = 7
                        possivelsinal3 = 7
                        analisar5 = 7
                        possivelsinal5 = 7
                        bot.send_message(chat_id=chat_id, text='''
🎲️ Oportunidade Encontrada

🎯️ Apostar em PRETO ⚫️️️️

🎳️ Opcional: Cobrir no BRANCO ⚪️

🎰️ Blaze Double                      
                        ''')
                        print("send msg")
                        return
                    if num == ['P', 'P', 'P', 'B']:
                        analisar4 = 1
                        analisar = 7
                        possivelsinal = 7
                        analisar2 = 7
                        possivelsinal2 = 7
                        analisar3 = 7
                        possivelsinal3 = 7
                        analisar5 = 7
                        possivelsinal5 = 7
                        bot.send_message(chat_id=chat_id, text='''
🎲️ Oportunidade Encontrada

🎯️ Apostar em VERMELHO 🔴️️️️

🎳️ Opcional: Cobrir no BRANCO ⚪️

🎰️ Blaze Double
                        ''')
                        print("send msg")
                        return

                elif analisar4 == 1:

                    if gale_atual4 == 0:
                        # WIN    #['X','V', 'V']: manda sinal
                        if num == ['P', 'V', 'V', 'V']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar4 = 0
                            gale_atual4 = 0
                            possivelsinal4 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['V', 'P', 'P', 'P']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar4 = 0
                            gale_atual4 = 0
                            possivelsinal4 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'V', 'V', 'V']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar4 = 0
                            gale_atual4 = 0
                            possivelsinal4 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'P', 'P', 'P']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar4 = 0
                            gale_atual4 = 0
                            possivelsinal4 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return

                        if num == ['V', 'V', 'V', 'V']:
                            gale_atual4 = gale_atual4 + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 1ª PROTEÇÃO''')
                            print("send msg")
                            return
                        if num == ['P', 'P', 'P', 'P']:
                            gale_atual4 = gale_atual4 + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 1ª PROTEÇÃO''')
                            print("send msg")
                            return

                    if gale_atual4 == 1:
                        if num == ['P', 'V', 'V', 'V']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar4 = 0
                            gale_atual4 = 0
                            possivelsinal4 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['V', 'P', 'P', 'P']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar4 = 0
                            gale_atual4 = 0
                            possivelsinal4 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'V', 'V', 'V']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar4 = 0
                            gale_atual4 = 0
                            possivelsinal4 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'P', 'P', 'P']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar4 = 0
                            gale_atual4 = 0
                            possivelsinal4 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return

                        if num == ['V', 'V', 'V', 'V']:
                            gale_atual4 = gale_atual4 + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 2ª PROTEÇÃO''')
                            print("send msg")
                            return
                        if num == ['P', 'P', 'P', 'P']:
                            gale_atual4 = gale_atual4 + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 2ª PROTEÇÃO''')
                            print("send msg")
                            return

                    if gale_atual4 == 2:
                        if num == ['P', 'V', 'V', 'V']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar4 = 0
                            gale_atual4 = 0
                            possivelsinal4 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['V', 'P', 'P', 'P']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar4 = 0
                            gale_atual4 = 0
                            possivelsinal4 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'V', 'V', 'V']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar4 = 0
                            gale_atual4 = 0
                            possivelsinal4 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['B', 'P', 'P', 'P']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar4 = 0
                            gale_atual4 = 0
                            possivelsinal4 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return

                        if num == ['V', 'V', 'V', 'V']:
                            loss = loss + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''❌️ LOSS 😓️''')
                            bot.send_message(chat_id=chat_id, text='''⚠️ ATENÇÃO AO GERENCIAMENTO''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar4 = 0
                            gale_atual4 = 0
                            possivelsinal4 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return
                        if num == ['P', 'P', 'P', 'P']:
                            loss = loss + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''❌️ LOSS 😓️''')
                            bot.send_message(chat_id=chat_id, text='''⚠️ ATENÇÃO AO GERENCIAMENTO''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar4 = 0
                            gale_atual4 = 0
                            possivelsinal4 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar5 = 0
                            possivelsinal5 = 0
                            return

                    if analisar4 == 0 and gale_atual4 == 0:
                        possivelsinal4 = 0
                        return

                #################################################
                # if possivelsinal5 == 0:
                #     if num == ['P', 'V', 'B', 'P']:
                #         possivelsinal5 = 1
                #         bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                #         print("send msg")
                #         return
                #     if num == ['P', 'V', 'B', 'V']:
                #         possivelsinal5 = 1
                #         bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                #         print("send msg")
                #         return
                #     if num == ['V', 'P', 'B', 'P']:
                #         possivelsinal5 = 1
                #         bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                #         print("send msg")
                #         return
                #     if num == ['V', 'P', 'B', 'V']:
                #         possivelsinal5 = 1
                #         bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                #         print("send msg")
                #         return
                #     if num == ['P', 'V', 'B', 'B']:
                #         possivelsinal5 = 1
                #         bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                #         print("send msg")
                #         return
                #     if num == ['V', 'P', 'B', 'B']:
                #         possivelsinal5 = 1
                #         bot.send_message(chat_id=chat_id, text="🥁️ Possível Oportunidade ")
                #         print("send msg")
                #         return

                if analisar5 == 0:
                    if num == ['V', 'P', 'V', 'B']:
                        analisar5 = 1
                        analisar = 7
                        possivelsinal = 7
                        analisar2 = 7
                        possivelsinal2 = 7
                        analisar3 = 7
                        possivelsinal3 = 7
                        analisar4 = 7
                        possivelsinal4 = 7
                        bot.send_message(chat_id=chat_id, text='''
🎲️ Oportunidade Encontrada

🎯️ Apostar em VERMELHO 🔴️️️

🎳️ Opcional: Cobrir no BRANCO ⚪️

🎰️ Blaze Double                      
                        ''')
                        print("send msg")
                        return
                    if num == ['P', 'V', 'P', 'B']:
                        analisar5 = 1
                        analisar = 7
                        possivelsinal = 7
                        analisar2 = 7
                        possivelsinal2 = 7
                        analisar3 = 7
                        possivelsinal3 = 7
                        analisar4 = 7
                        possivelsinal4 = 7
                        bot.send_message(chat_id=chat_id, text='''
🎲️ Oportunidade Encontrada

🎯️ Apostar em  PRETO ⚫️

🎳️ Opcional: Cobrir no BRANCO ⚪️

🎰️ Blaze Double
                        ''')
                        print("send msg")
                        return

                elif analisar5 == 1:

                    if gale_atual5 == 0:
                        # WIN    #['X','V', 'V']: manda sinal
                        if num == ['V', 'V', 'P', 'V']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar5 = 0
                            gale_atual5 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            return
                        if num == ['P', 'P', 'V', 'P']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar5 = 0
                            gale_atual5 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            return
                        if num == ['B', 'V', 'P', 'V']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar5 = 0
                            gale_atual5 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            return
                        if num == ['B', 'P', 'V', 'P']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar5 = 0
                            gale_atual5 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            return

                        if num == ['P', 'V', 'P', 'V']:
                            gale_atual5 = gale_atual5 + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 1ª PROTEÇÃO''')
                            print("send msg")
                            return
                        if num == ['V', 'P', 'V', 'P']:
                            gale_atual5 = gale_atual5 + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 1ª PROTEÇÃO''')
                            print("send msg")
                            return

                    if gale_atual5 == 1:
                        if num == ['V', 'P', 'V', 'P']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar5 = 0
                            gale_atual5 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            return
                        if num == ['P', 'V', 'P', 'V']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar5 = 0
                            gale_atual5 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            return
                        if num == ['B', 'P', 'V', 'P']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar5 = 0
                            gale_atual5 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            return
                        if num == ['B', 'V', 'P', 'V']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar5 = 0
                            gale_atual5 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            return

                        if num == ['P', 'P', 'V', 'P']:
                            gale_atual5 = gale_atual5 + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 2ª PROTEÇÃO''')
                            print("send msg")
                            return
                        if num == ['V', 'V', 'P', 'V']:
                            gale_atual5 = gale_atual5 + 1
                            bot.send_message(chat_id=chat_id, text='''🤞️ VAMOS PARA A 2ª PROTEÇÃO''')
                            print("send msg")
                            return

                    if gale_atual5 == 2:
                        if num == ['V', 'P', 'P', 'V']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar5 = 0
                            gale_atual5 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            return
                        if num == ['P', 'V', 'V', 'P']:
                            wins = wins + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''✅️✅️✅️ WIIIIN ✅️✅️✅️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar5 = 0
                            gale_atual5 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            return
                        if num == ['B', 'P', 'P', 'V']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar5 = 0
                            gale_atual5 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            return
                        if num == ['B', 'V', 'V', 'P']:
                            brancos = brancos + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''⚪️⚪️⚪️ BRANCOOOOOOO ⚪️⚪️⚪️️''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar5 = 0
                            gale_atual5 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            return

                        if num == ['P', 'P', 'P', 'V']:
                            loss = loss + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''❌️ LOSS 😓️''')
                            bot.send_message(chat_id=chat_id, text='''⚠️ ATENÇÃO AO GERENCIAMENTO''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar5 = 0
                            gale_atual5 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            return
                        if num == ['V', 'V', 'V', 'P']:
                            loss = loss + 1
                            if (wins + brancos + loss) != 0:
                                assertividade = round(((wins + brancos) / (wins + loss + brancos)) * 100, 2)
                            else:
                                assertividade = 0
                            bot.send_message(chat_id=chat_id, text='''❌️ LOSS 😓️''')
                            bot.send_message(chat_id=chat_id, text='''⚠️ ATENÇÃO AO GERENCIAMENTO''')
                            bot.send_message(chat_id=chat_id, text=(
                                f''' ✅️ {wins} | ⚪️ {brancos} | 🚫️ {loss} ️ \n\n 🏆️  {assertividade}% de Acertos '''))
                            print("send msg")
                            time.sleep(16)
                            analisar5 = 0
                            gale_atual5 = 0
                            analisar = 0
                            possivelsinal = 0
                            analisar2 = 0
                            possivelsinal2 = 0
                            analisar3 = 0
                            possivelsinal3 = 0
                            analisar4 = 0
                            possivelsinal4 = 0
                            return

                    if analisar5 == 0 and gale_atual5 == 0:
                        possivelsinal5 = 0
                        return


            #################################################

            checkVersion = CHECK_VERSION(finalcor)
            print(checkVersion)
            print(finalcor)
            # time.sleep(3)