import asyncio
from telebot.async_telebot import AsyncTeleBot
from telebot import types
import telebot
import csv




TOKEN = ''
bot = AsyncTeleBot(TOKEN)










weapons = {
    'Бастард': ['Огонь', 'Вода', 'Гроза', 'Лёд', 'Дракон', 'Без стихии'],
    'Двуручный меч': ['Огонь', 'Вода', 'Гроза', 'Лёд', 'Дракон', 'Без стихии'],
    'Меч и щит': ['Огонь', 'Вода', 'Гроза', 'Лёд', 'Дракон', 'Без стихии'],
    'Молот': ['Огонь', 'Вода', 'Гроза', 'Лёд', 'Дракон', 'Без стихии'],
    'Охотничий рог': ['Огонь', 'Вода', 'Гроза', 'Лёд', 'Дракон', 'Без стихии'],
    'Силовой клинок': ['Огонь', 'Вода', 'Гроза', 'Лёд', 'Дракон', 'Без стихии'],
    'Выкидной топор': ['Огонь', 'Вода', 'Гроза', 'Лёд', 'Дракон', 'Без стихии'],
    'Парные клинки': ['Огонь', 'Вода', 'Гроза', 'Лёд', 'Дракон', 'Без стихии'],
    'Глефа насекомых': ['Огонь', 'Вода', 'Гроза', 'Лёд', 'Дракон', 'Без стихии'],
    'Копьё': ['Огонь', 'Вода', 'Гроза', 'Лёд', 'Дракон', 'Без стихии'],
    'Копьепушка': ['Огонь', 'Вода', 'Гроза', 'Лёд', 'Дракон', 'Без стихии'],
    'Лук': ['Огонь', 'Вода', 'Гроза', 'Лёд', 'Дракон', 'Без стихии'],
    'ЛБГ': ['Огонь', 'Вода', 'Гроза', 'Лёд', 'Дракон', 'Без стихии'],
    'ХБГ': ['Огонь', 'Вода', 'Гроза', 'Лёд', 'Дракон', 'Без стихии'],
}






photos = {
    'Бастард': {
        'Огонь': 'https://ibb.co/qMLDmNS6',
        'Вода': 'https://drive.google.com/u/0/drive-viewer/AKGpihY45urB--yO3d_E0qetW_YakSH0hVBtLESKplP-uzOSCZky40s8f9CwzDqSshExTAzQriT4dLUkoySaXBsyQrt1h9bOKyG8bAE=s1600-rw-v1',
        'Гроза': 'https://drive.google.com/u/0/drive-viewer/AKGpihYD6k-icsSM_qcrOh9Lwl0lRTVRyCyK4kNvBapkAXuSyMl55HFADNueOusmCftDRn57P3i9yiE0LhOttPsufxYLIrfTsyJ_8Q=s1600-rw-v1',
        'Лёд': 'https://drive.google.com/u/0/drive-viewer/AKGpihbrdOYD1Z4Pw6PGNBnwDxpvU6TTAlYUuva58ImqQhJTGyTKoWGOQ1GCllpDENzZgBicyMYRJ4xBxAKpw86aAkP8lgMTYhvK-v4=s1600-rw-v1',
        'Дракон': 'https://drive.google.com/u/0/drive-viewer/AKGpihZ0KYCaIAgGqL55SDB7cUHLsqsJHp-OYsqGLxlKqouX_zG4UnM8JM4zp_0r_oyrQ81srTSIvt8IpPsRUL0y34eUsLtslUeI9BE=s1600-rw-v1',
        'Без стихии': 'https://ibb.co/JjBx1vTQ',
    },
    'Двуручный меч': {
        'Огонь': 'https://drive.google.com/u/0/drive-viewer/AKGpihawfzfswX8y5oaa5fmuytk3YQQZprjPVXAVKfi7XAOSYdWYy1QLEadQwqiw4ToABI6ipNToiUuNoeb_nhV9BoifRTsKjaH0V8I=s1600-rw-v1',
        'Вода':'https://drive.google.com/u/0/drive-viewer/AKGpihaR97jiScQ50851WzbBHtebkJCOkKch8XiCcYrZzLn11lKbAPjVjeRp0TQTpFxF8ROfD-Ojm7ZHCWTY_YNuHVtfJSTbO_1I2Q=s1600-rw-v1',
        'Гроза':'https://drive.google.com/u/0/drive-viewer/AKGpihbvqCnufzNSMCo3TXfs5_jun72ukW2TUYnlRfIH0bxa35SVGU7rv7qHpiu2wcx4Py-26fdKVKYFEeV9BrOEx-TUnud8bALRVg=s1600-rw-v1',
        'Лёд':'https://drive.google.com/u/0/drive-viewer/AKGpihY480k-bSa8Id3etgPW4Qp-fzbD0RuUy8-5a1XC0EHgAg48JGEJjjrIyc9BnZ2GcyahvgrqEiWQFFusVBkMVQhi6BGF7b_dAG0=s1600-rw-v1',
        'Дракон':'https://drive.google.com/u/0/drive-viewer/AKGpiha14wa2w97id1yIzcQr4Ohn6WBM4brXCRjvidk65Kt859WJdZSX48RNSypGJnoTGsTfcSpK-ZOA5GAY_cHVX2jnBYGkRtYywPM=s1600-rw-v1',
        'Без стихии':'https://drive.google.com/u/0/drive-viewer/AKGpihZHoiG27HcTC0qqcbCPPGd2_C2blF72KruaDYm6xZWwNfqb5DL5guFzlWBOcxmX1U7G0HUyRsbUYLSmRz2zWZQc_8RcRXCVwu8=s1600-rw-v1',
    },
    'Меч и щит':{
        'Огонь': 'https://drive.google.com/u/0/drive-viewer/AKGpihYVFdZp3wWy9UC74X-lNVNsQIiZ3Wh_pzhEbE_vJ1yse4sIw6m-_8BFdL0gokHgMfTRh6br3G5kzgxZNuP4qz9lMb2OPP9lCw=s1600-rw-v1',
        'Вода':'https://drive.google.com/u/0/drive-viewer/AKGpiha71nxT4F9fNUTFHlt4DFByxm7J5_oqNkuB1hPBQcio0AIKlP8C0_7SC1IrBgl1X28fkpw_fsH9rIcSuULGcO2q4bwcXyuLiw=s1600-rw-v1',
        'Гроза':'https://drive.google.com/u/0/drive-viewer/AKGpihYmMzgParmtnGHJQTfWxz3OxmlplhBh9Xwpbmim_0UDVZhZbzk_HeBNfYYlate8HTWpWIwkLD3VyW0QQF4uNcf3B25ydYHfDpU=s1600-rw-v1',
        'Лёд':'https://drive.google.com/u/0/drive-viewer/AKGpihaV00OUWuog4cQbs4RRspAYegKDBgj7xDCYQ0mTkTakZI9fg1Mq7hdpuigzkjkuUo_pzAtBMl4KqcqszXnpPhJ8pzezex6knUg=s1600-rw-v1',
        'Дракон':'https://drive.google.com/u/0/drive-viewer/AKGpihZz2tPxG-wKIxsqOD_5pix6QrCRHw664CXZxHw_8E48p-sYZoa183kE4scwhLiP1K70eyWm79_Hivh4s_M7LpSzHjzvE6VWhg=s1600-rw-v1',
        'Без стихии':'https://drive.google.com/u/0/drive-viewer/AKGpihbQ16OuBJErgYze0J51wptEiBhhCxIuXkyjXpkxgqoQPKPuIzrbgzKBU-54tVeMUvxDoXC7fO0-XqJftYz-CXR45EAh_hxF4Ds=s1600-rw-v1',
    },
    'Молот': {
        'Огонь': 'https://drive.google.com/u/0/drive-viewer/AKGpihbgHjQnxUhn6z7a8j0-xXZG5pcJllhusprHPxqfGqVbP_c8v2F1q5zzKc73sGcSkaPJza9dxNqTXDSgGJHAh-RXsUfn0W9i6w=s1600-rw-v1',
        'Вода':'https://drive.google.com/u/0/drive-viewer/AKGpihY6R1Eww28dI32lBRN_Jw4V6uRV826Ve2w5JAYloa55U_ssVatvkgjnb3ECzp-A3Vv6Do3aTWZx1i1NVaOt2ezHETnSrg_EqA=s1600-rw-v1',
        'Гроза':'https://drive.google.com/u/0/drive-viewer/AKGpihZoycHKJnh8JPPjgwtjF6lBY4aZbKsquvR7TzLjg9blkBp-X1LGpfTvr6HmiYwSp6cDCqyl5fwol8ifW7qVVvfShvoSr0TD6y0=s1600-rw-v1',
        'Лёд':'https://drive.google.com/u/0/drive-viewer/AKGpihbdLF-qtXk03LI3JJZ0TAO5kzZdSiJWeM_52c1ppR77yQxFfsf6fSf9Oi0IG0oaW50XaF0R7C-M7ie4w7J4cKtlLpMIMEwtQ2w=s1600-rw-v1',
        'Дракон':'https://drive.google.com/u/0/drive-viewer/AKGpihZbzTTmrrTXEI-xsz68p-KupdfOwhTcW46_Ndvs4DBmWCCaG8RoZ2yZgAnPTMCrLh2oh5kKBOVImQ756FIyCwgFyRCsI58lJA=s1600-rw-v1',
        'Без стихии':'https://drive.google.com/u/0/drive-viewer/AKGpihauewOQpL47s8W0MamN-ywAZ5dKNBZKUm8Kckkra1H3lYyExuSd2uzV8rbrQ5FPYwxLskP1mjRgLMG9v402RayTSPi5a3lpDrw=s1600-rw-v1',
    },
    'Охотничий рог': {
        'Огонь': 'https://drive.google.com/u/0/drive-viewer/AKGpihb5OYbf7-5QZsSt8KARjfbuvH5U7ptarUjy3SPvcWRbglKP_ew4NFQD_y5LGlGQZIMlmBHBC4kY81w2BVQjFk1y2ILq7vK9iSg=s1600-rw-v1',
        'Вода':'https://drive.google.com/u/0/drive-viewer/AKGpihbWhowWy7nXWslwtPNMCQ-0HtybzxNWQipECnERyyh0kyn0oy0nEtZgrS86dghZO-mrSzMxlJ1cZk8izWRtt-HSyT9-R5B3Aw=s1600-rw-v1',
        'Гроза':'https://drive.google.com/u/0/drive-viewer/AKGpihbXVm6E4UNB3x18guNon12sgOD4EHvOARV4HYnxnQnqXcC0ah-qoRKFtU-EkhfKeGRdrZYddbkFeOQkiv4BbAnH6DDnuWpukw=s1600-rw-v1',
        'Лёд':'https://drive.google.com/u/0/drive-viewer/AKGpihbh73VCaX9VBkvapiA8-wxJSEDmIT-avoT-g_eS3tuXwbw3MKeI3OyKzt5RaeEa70qdc2drStO28Oti-owka5DoPCovOUJehCQ=s1600-rw-v1',
        'Дракон':'https://drive.google.com/u/0/drive-viewer/AKGpihbo5nFxzhe0RNmAzB7NzKh4oE_I0VKPVb354Z8xdx1q-Db5x_ZEcSsOesymNZ01cAOs0CXcysAmHpkUDmiBrj8GY7N8EgkcPWA=s1600-rw-v1',
        'Без стихии':'https://drive.google.com/u/0/drive-viewer/AKGpihagJohe2KusNRN8cFfNkaQisGVMYQvVbFWHYTd1CmHhJExUvvqZUULsdkgoSzslqolFqAJJ_aFLDzySuQ9C1NllAxwegR6g8BM=s1600-rw-v1',
    },
    'Силовой клинок': {
        'Огонь': 'https://ibb.co/nNd7wPTF',
        'Вода':'https://ibb.co/S4mLm2bk',
        'Гроза':'https://ibb.co/C5wMJFLH',
        'Лёд':'https://ibb.co/jPCG6qDy',
        'Дракон':'https://ibb.co/KzBsBNMb',
        'Без стихии':'https://ibb.co/kgmWz39f',
    },
    'Выкидной топор': {
        'Огонь': 'https://drive.google.com/u/0/drive-viewer/AKGpihZQPH3XhmyW_sBi-aV3mW8j70SCpt6bPBGyrhDWw5JuudrAGKnu2LsS-B887ZYe9rYXwe_bf0O0XEaSdXZzF5G33cV9D4_H_k4=s1600-rw-v1',
        'Вода':'https://drive.google.com/u/0/drive-viewer/AKGpihaooeGB0kLYlnou6kItl-nuZr-Ke6htiHpUSBF4d7TRgIddYIlt-VET01_EXnLkADTYjMrH7bNJ_85nfCHD_L4nSdrRIOUdKQ=s1600-rw-v1',
        'Гроза':'https://drive.google.com/u/0/drive-viewer/AKGpihbo7EYC6gPn9__kI6SYSN9y-FmOY6Q823no30pfBOUaaHOjr-6LfOUQOc_3pW0m2ggavqcZYfvZYkgdsRzYtXcR6_yaEphYJnQ=s1600-rw-v1',
        'Лёд':'https://drive.google.com/u/0/drive-viewer/AKGpihbCuUXsKHMFqEvy2Me7uQLvY9HOswQchD_5RSEwvEuY_pjzYtaW7EBqt9yVZ4R4XmI32izmPBtiH2Pu3z2fl9-8mcGPd5Oesi0=s1600-rw-v1',
        'Дракон':'https://drive.google.com/u/0/drive-viewer/AKGpihbuOSpq3kYM1C7MpajBGjS12aFRW10vz4Viw9NK1Q2PULKr3W55_3iD5Toi9jIt8KO4fPcUi408u6kJKiaw2VbvZSVGF1p-tjM=s1600-rw-v1',
        'Без стихии':'https://drive.google.com/u/0/drive-viewer/AKGpihbVHS0SJGA8hBUuIzbw9_FnUbVvVWjL8k-bNaatuPZi4hLuVLrcaFMaL7u8Wtcr1zvGDBcGC0EsesGRh2BruD4Tmfd76amLdQ=s1600-rw-v1',
    },
    'Парные клинки': {
        'Огонь': 'https://ibb.co/35MBwhvg',
        'Вода':'https://ibb.co/Y4rvb9NH',
        'Гроза':'https://ibb.co/ynYD4QJg',
        'Лёд':'https://ibb.co/23r7f4pb',
        'Дракон':'https://ibb.co/twN4YzQV',
        'Без стихии':'https://ibb.co/G3pXYZWK',
    },
    'Глефа насекомых': {
        'Огонь': 'https://ibb.co/My7r9w48',
        'Вода':'https://ibb.co/mV0NyBz0',
        'Гроза':'https://ibb.co/s9tD7SLV',
        'Лёд':'https://ibb.co/2YyTfMDr',
        'Дракон':'https://ibb.co/9kc6btdK',
        'Без стихии':'https://ibb.co/YTdmCR1Y',
    },
    'Копьё': {
        'Огонь': 'https://ibb.co/21b9Mn0f',
        'Вода':'https://ibb.co/KjJ4vQ9V',
        'Гроза':'https://ibb.co/xS59Fj7N',
        'Лёд':'https://ibb.co/QjDMwpHy',
        'Дракон':'https://ibb.co/wrLxw49s',
        'Без стихии':'https://ibb.co/H5SgQrG',
    },
    'Копьепушка': {
        'Огонь': 'https://drive.google.com/u/0/drive-viewer/AKGpihYenloF2WnR5IkFPpJqbsymPDCGV73lqBCP1xLddhht04nWlcBjtwlZ-Xgu8uFKcj_XLtyJPrTzTk1QwfRymzV-sNc0rBQHQKQ=s1600-rw-v1',
        'Вода':'https://drive.google.com/u/0/drive-viewer/AKGpihZllYZGGn7edE7-pKYUNluXpxbTRkegvDiIL9-w8VFDaeVKQCMS7Ribzmt-5eT7ETjqleCoKhI-AEUZg7lgdIgj0QpQyAEeGjc=s1600-rw-v1',
        'Гроза':'https://drive.google.com/u/0/drive-viewer/AKGpihbPwN8IvGsFE9nqxXXnQXAncSS7FobXo1c5zkuF_21vTFJtfI4v-Sc24eFRrcfNWyDqbizPj4OMRsCdQbw_DulieBa9ZGjP2Q=s1600-rw-v1',
        'Лёд':'https://drive.google.com/u/0/drive-viewer/AKGpihZU9esjJjI01fV8HhIai3rwfPU1jS2eQEGhtPE6imFMNU7YRIyx1cXvtcUcQliBjQeO9yeBc9sXA108vLLUNLHc943UDW-jEaU=s1600-rw-v1',
        'Дракон':'https://drive.google.com/u/0/drive-viewer/AKGpiha7bAXSdiOSB2DvrfF2pV7nAoUcYDmw8SJTB47QggGmClFPhmazhvGT57cJB15o7e_3ebc_Yvh8vql2raAIREnUvJuZBrDgwkY=s1600-rw-v1',
        'Без стихии':'https://drive.google.com/u/0/drive-viewer/AKGpihb2Z8vpUpJvVP4d2DZ6TiwXVMP9vlSU5OmiopwdQHm7TsAr9liWI7B68xhDCJ5_zIvRle_RBnPzqGQdt3V2hIHvDHQIlStPZ6k=s1600-rw-v1',
    },
    'Лук': {
        'Огонь': 'https://ibb.co/Hfd7SBzJ',
        'Вода':'https://ibb.co/qM42ns4D',
        'Гроза':'https://ibb.co/ZpkHyTzn',
        'Лёд':'https://ibb.co/NgKXtJfB',
        'Дракон':'https://ibb.co/23hBq8DL',
        'Без стихии':'https://ibb.co/spd73KCT',
    },
    'ЛБГ': {
        'Огонь': 'https://ibb.co/F4rHZJWn',
        'Вода':'https://ibb.co/1fmdT5bF',
        'Гроза':'https://ibb.co/PvXSbYZ9',
        'Лёд':'https://ibb.co/VWTPFbX9',
        'Дракон':'https://ibb.co/8DJQ9pyx',
        'Без стихии':'https://ibb.co/35c4B0RW',
    },
    'ХБГ': {
        'Огонь': 'https://drive.google.com/u/0/drive-viewer/AKGpihZYemUQo-TH80vND5KMovRKbjLsbnEieVolKnPvSU-CctjMq6CjnVSYGRk-6RWGhqBJj8ZrI-QdCKQtAHtxNucbEVpg828GHKw=s1600-rw-v1',
        'Вода':'https://drive.google.com/u/0/drive-viewer/AKGpihZmUebGHIwD3XVo3FQEmSXvI5zhQopWuCtW3tbqEM2-HKAvEAHZkWvi8oiYeWNcryhOxrJpem1e8PbgQs34y-_Ur5tc-lLgKQ=s1600-rw-v1',
        'Гроза':'https://drive.google.com/u/0/drive-viewer/AKGpihZz06vOVQXVPNOZ7OMBLvxNbPJSvxNUGxexNLseUHHuJ5ygTkZC_8f8SM2zoEeB8OYMDCvVgOOZ7V8-4LZ6tt-onM4ljer40g=s1600-rw-v1',
        'Лёд':'https://drive.google.com/u/0/drive-viewer/AKGpihZit2I4Yz6lp0h-semMyZxzVX04gzR2VLgTixbHS5v-eepXtbYU5HR7nXd31KqYV1WQsSp_Fa6dRuBhRIbgCVvnVxpctRM72ng=s1600-rw-v1',
        'Дракон':'https://drive.google.com/u/0/drive-viewer/AKGpihZRDtR0tnRL3ibmEGrXB0geRB6q4calfKUsaXlPVIyW6mZEogG2QKq2Tdb9STUWKUl_hQMj9Gqsr8HPY43cssbESwZ6kBnpsk0=s1600-rw-v1',
        'Без стихии':'https://drive.google.com/u/0/drive-viewer/AKGpihayk9w4PcnEFcpCEXLiSpPwZvCQIvgQkf5f-eyM7EZa5pDW19jjcKnb-c3UvLSmsFXyVlJc7loVeW6WHSG5a2z8k9pIuKoLGg=s1600-rw-v1',
    },
}








choice = {}



# Выбор оружия


def weapon():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    buttons = [types.KeyboardButton(name) for name in weapons.keys()]
    buttons.append(types.KeyboardButton('Назад'))
    markup.add(*buttons)
    return markup




# выбор стихий


def element(weapon):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    elems = weapons.get(weapon, [])
    buttons = [types.KeyboardButton(e) for e in elems]
    buttons.append(types.KeyboardButton('Назад'))
    markup.add(*buttons)
    return markup

@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    with open("База.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            message.from_user.id,
            message.from_user.username
        ])
    await bot.send_message(message.chat.id,
        'Я - MonsterCardBot\nВыбери оружие с которым ты играешь а я покажу карточки стихий для него',
        
        

        
        reply_markup=weapon()
    
    )
    choice[message.chat.id] = None

    


@bot.message_handler(func=lambda m: m.text == 'Назад')
async def go_back(message):
    choice[message.chat.id] = None
    await bot.send_message(message.chat.id, 'Выбери оружие:', reply_markup=weapon())

@bot.message_handler(func=lambda m: m.text in weapons.keys())
async def choose_weapon(message):
    choice[message.chat.id] = message.text
    await bot.send_message(message.chat.id,
        f'Ты выбрал оружие: {message.text}\n Выбери стихию:',
        reply_markup=element(message.text)
    )

@bot.message_handler(func=lambda m: True)
async def choose_element(message):
    weapon = choice.get(message.chat.id)
    if not weapon:
        
        await bot.send_message(message.chat.id, 'Сначала выбери оружие', reply_markup=weapon())
        return


    elements = weapons.get(weapon, [])
    if message.text not in elements:
        await bot.send_message(message.chat.id, 'Выбери стихию из списка', reply_markup=element(weapon))
        return

    # отправка фотошек
    card = photos.get(weapon, {}).get(message.text)
    if card:
        await bot.send_photo(message.chat.id,card, caption=f'Оружие: {weapon}\nСтихия: {message.text}')
    else:
        await bot.send_message(message.chat.id, 'Изображение не добавлено')

   


asyncio.run(bot.polling())
