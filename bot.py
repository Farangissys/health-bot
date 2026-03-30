from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import random
import os
API_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

WARNING_TEXT = (
    "\n\n⚠️ Bu bot umumiy ma’lumot beradi. "
    "Aniq tashxis, dori tanlash va davolash uchun shifokorga murojaat qiling."
)

user_state = {}

# =========================
# UMUMIY BO'LIMLAR
# =========================

general_sections = {
    "Ovqatlanish": {
        "Sog‘lom ovqatlanish asoslari": (
            "Sog‘lom ovqatlanish organizmning normal ishlashi uchun juda muhim.\n\n"
            "Asosiy tamoyillar:\n"
            "• ratsionda sabzavot, meva, dukkaklilar, to‘liq don va oqsil manbalari bo‘lishi kerak;\n"
            "• juda sho‘r, juda shirin va chuqur qayta ishlangan ovqatlarni kamaytirish lozim;\n"
            "• ovqatlanish tartibini saqlash foydali;\n"
            "• porsiya nazorati ortiqcha vaznning oldini olishga yordam beradi."
        ),
        "Meva va sabzavot": (
            "Meva va sabzavotlar vitamin, mineral, antioksidant va tolaga boy.\n\n"
            "Ularning foydasi:\n"
            "• hazm tizimiga yordam beradi;\n"
            "• immunitetni qo‘llab-quvvatlaydi;\n"
            "• yurak-qon tomir tizimi uchun foydali;\n"
            "• ratsionni muvozanatlashtiradi."
        ),
        "Tuz, shakar va yog‘lar": (
            "Ortiqcha tuz qon bosimiga, ortiqcha shakar esa vazn va modda almashinuvi muammolariga salbiy ta’sir qilishi mumkin.\n\n"
            "Tavsiya:\n"
            "• juda sho‘r mahsulotlarni kamaytiring;\n"
            "• gazli va shirin ichimliklarni cheklang;\n"
            "• qovurilgan ovqat o‘rniga qaynatilgan, bug‘da yoki pechda tayyorlangan ovqatlarni tanlang."
        ),
        "Suv ichish odati": (
            "Suv modda almashinuvi, tana harorati va umumiy holat uchun muhim.\n\n"
            "Amaliy tavsiyalar:\n"
            "• suvni kun davomida bo‘lib-bo‘lib iching;\n"
            "• issiq havo va jismoniy faollik paytida ehtiyoj oshishi mumkin;\n"
            "• shirin ichimliklar o‘rniga oddiy suvni afzal ko‘ring."
        ),
    },
    "Homiladorlik": {
        "1-trimestr": (
            "Birinchi trimestr homila organlari shakllanishi boshlanadigan muhim davr.\n\n"
            "Muhim jihatlar:\n"
            "• erta prenatal nazorat;\n"
            "• dori vositalarini o‘zboshimchalik bilan qabul qilmaslik;\n"
            "• dam olish va ovqatlanishga e’tibor;\n"
            "• folat va shifokor tavsiyalariga amal qilish."
        ),
        "2-trimestr": (
            "Ikkinchi trimestr ko‘pincha nisbatan yengilroq o‘tadi.\n\n"
            "Bu davrda:\n"
            "• temir va kalsiyga e’tibor;\n"
            "• muvozanatli ovqatlanish;\n"
            "• muntazam tekshiruvlar;\n"
            "• xavfsiz yengil jismoniy faollik foydali."
        ),
        "3-trimestr": (
            "Uchinchi trimestrda charchoq va jismoniy noqulaylik ko‘payishi mumkin.\n\n"
            "Muhim tavsiyalar:\n"
            "• dam olishga e’tibor berish;\n"
            "• shifokor nazoratini davom ettirish;\n"
            "• oyoq shishi, bosh og‘rig‘i yoki noodatiy alomatlarda mutaxassisga murojaat qilish;\n"
            "• tug‘ruqqa tayyorgarlik."
        ),
        "Prenatal nazorat": (
            "Prenatal nazorat ona va homila holatini kuzatishga yordam beradi.\n\n"
            "Vazifalari:\n"
            "• asoratlarni erta aniqlash;\n"
            "• kerakli tekshiruvlarni vaqtida o‘tkazish;\n"
            "• ovqatlanish va turmush tarzi bo‘yicha tavsiyalar berish."
        ),
    },
    "Sport": {
        "Jismoniy faollik foydasi": (
            "Muntazam jismoniy faollik yurak, mushaklar, bo‘g‘imlar va ruhiy holat uchun foydali.\n\n"
            "Asosiy foydalar:\n"
            "• chidamlilik oshadi;\n"
            "• vazn nazoratiga yordam beradi;\n"
            "• stress kamayishi mumkin;\n"
            "• uyqu sifati yaxshilanishi mumkin."
        ),
        "Haftalik tavsiya": (
            "Doimiy jismoniy faollik sog‘liq uchun foydali.\n\n"
            "Muhim yondashuv:\n"
            "• haftalik rejani saqlash;\n"
            "• faollikni asta-sekin oshirish;\n"
            "• uzoq vaqt qimirlamay o‘tirishni kamaytirish."
        ),
        "Uy sharoitida mashq": (
            "Uyda ham samarali mashq qilish mumkin.\n\n"
            "Misollar:\n"
            "• cho‘zilish mashqlari;\n"
            "• plank;\n"
            "• o‘tirib-turish;\n"
            "• joyda yurish;\n"
            "• yengil kardio mashqlar."
        ),
        "Mashq xavfsizligi": (
            "Mashqni xavfsiz bajarish muhim.\n\n"
            "Qoidalar:\n"
            "• oldin qizish mashqlari;\n"
            "• ortiqcha zo‘riqmaslik;\n"
            "• og‘riq yoki bosh aylanishi bo‘lsa to‘xtash;\n"
            "• suv ichishni unutmaslik."
        ),
    },
    "Vitaminlar": {
        "A vitamini": (
            "A vitamini ko‘rish, teri va immun tizimi uchun muhim.\n\n"
            "Manbalari:\n"
            "• sabzi;\n"
            "• tuxum;\n"
            "• jigar;\n"
            "• sut mahsulotlari."
        ),
        "B guruhi vitaminlari": (
            "B vitaminlari asab tizimi, energiya almashinuvi va qon hosil bo‘lishida ishtirok etadi.\n\n"
            "Manbalari:\n"
            "• go‘sht;\n"
            "• tuxum;\n"
            "• dukkaklilar;\n"
            "• don mahsulotlari."
        ),
        "C vitamini": (
            "C vitamini immunitetni qo‘llab-quvvatlashda ishtirok etadi.\n\n"
            "Manbalari:\n"
            "• limon;\n"
            "• apelsin;\n"
            "• qulupnay;\n"
            "• bulg‘or qalampiri."
        ),
        "D vitamini": (
            "D vitamini suyaklar va tishlar uchun muhim.\n\n"
            "Manbalari:\n"
            "• quyosh nuri;\n"
            "• ayrim baliqlar;\n"
            "• boyitilgan mahsulotlar."
        ),
        "Vitamin yetishmovchiligi": (
            "Vitamin yetishmovchiligi holsizlik, umumiy darmonsizlik, teri o‘zgarishlari yoki boshqa belgilar bilan namoyon bo‘lishi mumkin.\n\n"
            "Bunday holatda:\n"
            "• sababni aniqlash muhim;\n"
            "• o‘zboshimchalik bilan ko‘p qo‘shimcha qabul qilish to‘g‘ri emas;\n"
            "• mutaxassis bilan maslahatlashish kerak."
        ),
    }
}

# =========================
# KASALLIKLAR
# Har birida 6 ta ichki bo'lim
# =========================

diseases = {
    "Gipertoniya": {
        "Ta’rif": (
            "Gipertoniya — qon bosimining doimiy ravishda yuqori bo‘lib yurishi bilan tavsiflanadigan holat. "
            "Qon bosimi yuqori bo‘lsa, yurak va qon tomirlari ko‘proq yuklama ostida ishlaydi."
        ),
        "Belgilar": (
            "Ko‘pincha uzoq vaqt alomatsiz kechishi mumkin. "
            "Ba’zi odamlarda bosh og‘rig‘i, bosh aylanishi, ko‘rishdagi noqulaylik, charchoq yoki ko‘krakdagi noxushlik sezilishi mumkin."
        ),
        "Xavf omillari": (
            "• ortiqcha tuz iste’moli\n"
            "• jismoniy faollikning kamligi\n"
            "• ortiqcha vazn\n"
            "• tamaki va spirtli ichimliklar\n"
            "• yoshning kattalashishi\n"
            "• oilaviy moyillik"
        ),
        "Nega muhim": (
            "Nazorat qilinmasa, insult, yurak xuruji, buyrak va boshqa qon tomir asoratlari xavfini oshiradi."
        ),
        "Oldini olish va nazorat": (
            "• tuzni kamaytirish\n"
            "• sog‘lom ovqatlanish\n"
            "• vaznni me’yorda saqlash\n"
            "• muntazam jismoniy faollik\n"
            "• qon bosimini tekshirtirib turish"
        ),
        "Qachon shifokorga murojaat qilish kerak": (
            "Agar qon bosimi tez-tez yuqori chiqsa, kuchli bosh og‘rig‘i, ko‘krak og‘rig‘i, nafas qisilishi yoki ko‘rish o‘zgarishi bo‘lsa, mutaxassisga murojaat qiling."
        ),
    },
    "Qandli diabet": {
        "Ta’rif": (
            "Qandli diabet — qondagi glyukoza miqdori yuqori bo‘lib turadigan surunkali holat."
        ),
        "Belgilar": (
            "• kuchli chanqash\n"
            "• tez-tez siyish\n"
            "• holsizlik\n"
            "• ko‘rishning xiralashishi\n"
            "• sababsiz ozish"
        ),
        "Xavf omillari": (
            "• ortiqcha vazn\n"
            "• kam jismoniy faollik\n"
            "• noto‘g‘ri ovqatlanish\n"
            "• oilaviy moyillik"
        ),
        "Nega muhim": (
            "Nazorat qilinmasa, yurak, buyrak, ko‘z va oyoq bilan bog‘liq asoratlarga olib kelishi mumkin."
        ),
        "Oldini olish va nazorat": (
            "• sog‘lom ratsion\n"
            "• vazn nazorati\n"
            "• muntazam faollik\n"
            "• tekshiruvdan o‘tib turish\n"
            "• shifokor tavsiyalariga rioya qilish"
        ),
        "Qachon shifokorga murojaat qilish kerak": (
            "Chanqash, tez siyish, ko‘rish yomonlashuvi yoki kuchli holsizlik kuzatilsa, tekshiruv zarur."
        ),
    },
    "Astma": {
        "Ta’rif": (
            "Astma — havo yo‘llarining surunkali yallig‘lanishi bilan bog‘liq kasallik."
        ),
        "Belgilar": (
            "• yo‘tal\n"
            "• xirillash\n"
            "• nafas qisilishi\n"
            "• ko‘krakda siqilish hissi"
        ),
        "Xavf omillari": (
            "• allergenlar\n"
            "• tutun\n"
            "• havo ifloslanishi\n"
            "• infeksiyalar\n"
            "• sovuq havo"
        ),
        "Nega muhim": (
            "Nazorat qilinmasa, kundalik hayot sifatini pasaytiradi va xurujlar xavfini oshiradi."
        ),
        "Oldini olish va nazorat": (
            "• qo‘zg‘atuvchi omillardan saqlanish\n"
            "• shifokor tavsiya qilgan davoga rioya qilish\n"
            "• simptomlarni kuzatib borish"
        ),
        "Qachon shifokorga murojaat qilish kerak": (
            "Agar nafas olish qiyinlashsa, tez-tez xirillash yoki xurujlar takrorlansa, mutaxassisga murojaat qiling."
        ),
    },
    "Anemiya": {
        "Ta’rif": (
            "Anemiya — qonda gemoglobin miqdori kamayib ketadigan holat."
        ),
        "Belgilar": (
            "• tez charchash\n"
            "• holsizlik\n"
            "• bosh aylanishi\n"
            "• nafas qisishi\n"
            "• terining oqarishi"
        ),
        "Xavf omillari": (
            "• temir tanqisligi\n"
            "• noto‘g‘ri ovqatlanish\n"
            "• qon yo‘qotish\n"
            "• homiladorlik\n"
            "• ayrim surunkali kasalliklar"
        ),
        "Nega muhim": (
            "To‘qimalarga kislorod yetkazilishi yomonlashadi, bu esa umumiy holatni susaytiradi."
        ),
        "Oldini olish va nazorat": (
            "• temirga boy mahsulotlar\n"
            "• zarurat bo‘lsa tekshiruv\n"
            "• shifokor tavsiyasi bilan qo‘shimchalar\n"
            "• sababni aniqlash"
        ),
        "Qachon shifokorga murojaat qilish kerak": (
            "Doimiy holsizlik, bosh aylanishi yoki nafas qisishi kuzatilsa, tekshiruv zarur."
        ),
    },
    "Ortiqcha vazn va semirish": {
        "Ta’rif": (
            "Ortiqcha vazn va semirish — organizmda me’yordan ortiq yog‘ to‘planishi bilan bog‘liq holat."
        ),
        "Belgilar": (
            "Asosiy belgi — vaznning me’yordan ortishi. Ba’zan tez charchash, nafas qisilishi va bo‘g‘imlarda zo‘riqish kuzatiladi."
        ),
        "Xavf omillari": (
            "• yuqori kaloriyali ovqatlar\n"
            "• kam harakatlilik\n"
            "• uzoq o‘tirish\n"
            "• noto‘g‘ri ovqatlanish odatlari\n"
            "• uyqu tartibining buzilishi"
        ),
        "Nega muhim": (
            "Yurak kasalliklari, insult, 2-tur diabet va bo‘g‘im muammolari xavfini oshiradi."
        ),
        "Oldini olish va nazorat": (
            "• ovqatlanishni yaxshilash\n"
            "• shirin ichimliklarni kamaytirish\n"
            "• muntazam jismoniy faollik\n"
            "• vaznni bosqichma-bosqich nazorat qilish"
        ),
        "Qachon shifokorga murojaat qilish kerak": (
            "Agar vazn bilan birga bosim, qand, bo‘g‘im og‘rig‘i yoki kundalik hayotda qiyinchiliklar bo‘lsa, shifokorga murojaat qiling."
        ),
    },
    "Sil (TB)": {
        "Ta’rif": (
            "Sil — asosan o‘pkani zararlaydigan, havo orqali yuqadigan yuqumli kasallik."
        ),
        "Belgilar": (
            "• 2 haftadan uzoq davom etuvchi yo‘tal\n"
            "• holsizlik\n"
            "• vazn yo‘qotish\n"
            "• isitma\n"
            "• kechasi terlash"
        ),
        "Xavf omillari": (
            "• immunitet pasayishi\n"
            "• yaqin aloqada bo‘lish\n"
            "• to‘yib ovqatlanmaslik\n"
            "• ayrim surunkali kasalliklar"
        ),
        "Nega muhim": (
            "Davolanmasa, og‘ir asoratlar va boshqalarga yuqish xavfi bo‘ladi."
        ),
        "Oldini olish va nazorat": (
            "• erta aniqlash\n"
            "• tibbiy tekshiruv\n"
            "• davolashni to‘liq yakunlash\n"
            "• shifokor tavsiyalariga qat’iy rioya qilish"
        ),
        "Qachon shifokorga murojaat qilish kerak": (
            "Agar yo‘tal uzoq davom etsa, vazn tushsa, isitma va kechasi terlash bo‘lsa, tekshiruv zarur."
        ),
    },
    "Gepatit B va C": {
        "Ta’rif": (
            "Gepatit B va C — jigarni zararlovchi virusli infeksiyalar."
        ),
        "Belgilar": (
            "Ba’zan umuman belgisiz kechadi. Ayrim hollarda:\n"
            "• holsizlik\n"
            "• ko‘ngil aynishi\n"
            "• qorinda noqulaylik\n"
            "• teri va ko‘z sarg‘ayishi"
        ),
        "Xavf omillari": (
            "• zararlangan qon bilan aloqa\n"
            "• steril bo‘lmagan asboblar\n"
            "• xavfli tibbiy yoki kosmetik muolajalar"
        ),
        "Nega muhim": (
            "Uzoq davom etsa, jigar shikastlanishi, sirroz yoki boshqa jiddiy muammolarga olib kelishi mumkin."
        ),
        "Oldini olish va nazorat": (
            "• xavfsiz tibbiy amaliyotlar\n"
            "• steril asboblardan foydalanish\n"
            "• gepatit B uchun emlash\n"
            "• zarur bo‘lsa skrining va tekshiruv"
        ),
        "Qachon shifokorga murojaat qilish kerak": (
            "Agar sarg‘ayish, holsizlik yoki xavfli kontakt bo‘lgan bo‘lsa, tekshiruvdan o‘tish kerak."
        ),
    },
    "OITS (HIV/AIDS)": {
        "Ta’rif": (
            "HIV immun tizimiga hujum qiluvchi virus. Davolanmagan holatda u immunitetni kuchsizlantirib, OITS bosqichiga olib borishi mumkin."
        ),
        "Belgilar": (
            "Dastlab ayrim odamlarda isitma, tomoq og‘rig‘i, limfa tugunlari kattalashishi yoki holsizlik bo‘lishi mumkin. "
            "Keyinchalik uzoq vaqt alomatsiz kechishi ham mumkin."
        ),
        "Xavf omillari": (
            "• himoyalanmagan jinsiy aloqa\n"
            "• zararlangan qon bilan aloqa\n"
            "• steril bo‘lmagan ignalar\n"
            "• ona-bolaga yuqish"
        ),
        "Nega muhim": (
            "Davolanmasa, immunitet zaiflashadi va organizm boshqa infeksiya hamda asoratlarga sezgir bo‘lib qoladi."
        ),
        "Oldini olish va nazorat": (
            "• xavfsiz jinsiy xulq\n"
            "• steril asboblardan foydalanish\n"
            "• test topshirish\n"
            "• aniqlansa, davoni erta boshlash va muntazam davom ettirish"
        ),
        "Qachon shifokorga murojaat qilish kerak": (
            "Agar xavfli kontakt bo‘lgan bo‘lsa yoki HIV bo‘yicha shubha bo‘lsa, test va maslahat uchun mutaxassisga murojaat qiling."
        ),
    },
    "COVID-19": {
        "Ta’rif": (
            "COVID-19 — SARS-CoV-2 virusi chaqiradigan infeksion kasallik."
        ),
        "Belgilar": (
            "• isitma\n"
            "• yo‘tal\n"
            "• tomoq og‘rig‘i\n"
            "• holsizlik\n"
            "• nafas qisilishi\n"
            "• hid yoki ta’m sezishdagi o‘zgarish"
        ),
        "Xavf omillari": (
            "• yoshi katta bo‘lish\n"
            "• surunkali kasalliklar\n"
            "• immunitetning pasayishi\n"
            "• yaqin aloqa va yopiq joylarda yuqori xavf"
        ),
        "Nega muhim": (
            "Ayrim odamlarda og‘ir kechishi, nafas tizimi va boshqa organlarga ta’sir qilishi mumkin."
        ),
        "Oldini olish va nazorat": (
            "• gigiyena qoidalari\n"
            "• kerak bo‘lganda izolyatsiya\n"
            "• xavfli holatda tibbiy maslahat\n"
            "• tavsiya etilgan profilaktika choralariga rioya qilish"
        ),
        "Qachon shifokorga murojaat qilish kerak": (
            "Agar nafas qisilishi, ko‘krak og‘rig‘i, yuqori isitma yoki og‘ir holat bo‘lsa, darhol tibbiy yordamga murojaat qiling."
        ),
    },
}

faq_data = {
    "Bot qanday ishlaydi?": "Bo‘limni tanlaysiz, keyin ichki mavzuni bosasiz. Kasalliklar bo‘limida esa kasallikni tanlab, ichki 6 bo‘limdan birini ochasiz.",
    "Bu bot tashxis qo‘yadimi?": "Yo‘q, bu bot faqat umumiy ma’lumot beradi.",
    "Dori tavsiya qiladimi?": "Yo‘q, dori va davolash bo‘yicha shifokor bilan maslahatlashish kerak.",
}

daily_tips = [
    "Kun davomida muntazam suv iching.",
    "Ratsionga ko‘proq sabzavot qo‘shing.",
    "Har kuni oz bo‘lsa ham jismoniy faollik qiling.",
    "Uyqu tartibini saqlashga harakat qiling.",
    "Tuz va shakarni me’yoridan oshirmang.",
]

# =========================
# KLAVIATURALAR
# =========================

def main_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add("Ovqatlanish", "Homiladorlik")
    kb.add("Sport", "Vitaminlar")
    kb.add("Kasalliklar", "Kalkulyatorlar")
    kb.add("Kun maslahati", "FAQ")
    kb.add("Bot haqida", "Yana savol bering")
    return kb

def nav_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add("Orqaga", "Bosh menyu")
    kb.add("Yana savol bering")
    return kb

def section_menu(section_name):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for topic in general_sections[section_name].keys():
        kb.add(topic)
    kb.add("Orqaga", "Bosh menyu")
    kb.add("Yana savol bering")
    return kb

def disease_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for disease_name in diseases.keys():
        kb.add(disease_name)
    kb.add("Orqaga", "Bosh menyu")
    kb.add("Yana savol bering")
    return kb

def disease_detail_menu(disease_name):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for part in diseases[disease_name].keys():
        kb.add(part)
    kb.add("Orqaga", "Bosh menyu")
    kb.add("Yana savol bering")
    return kb

def faq_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for q in faq_data.keys():
        kb.add(q)
    kb.add("Orqaga", "Bosh menyu")
    kb.add("Yana savol bering")
    return kb

def calculators_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    kb.add("BMI kalkulyator")
    kb.add("Kunlik suv ehtiyoji")
    kb.add("Yoshga qarab sport tavsiyasi")
    kb.add("Orqaga", "Bosh menyu")
    return kb

# =========================
# STATE
# =========================

def reset_user(user_id):
    user_state[user_id] = {
        "mode": "main",
        "current_section": None,
        "current_disease": None
    }

def ensure_user(user_id):
    if user_id not in user_state:
        reset_user(user_id)

def search_content(query):
    q = query.lower().strip()
    results = []

    for section, topics in general_sections.items():
        for topic, content in topics.items():
            text = f"{section} {topic} {content}".lower()
            if q in text:
                results.append((section, topic, content))

    for disease_name, parts in diseases.items():
        for part_name, content in parts.items():
            text = f"{disease_name} {part_name} {content}".lower()
            if q in text:
                results.append(("Kasalliklar", f"{disease_name} → {part_name}", content))

    return results[:5]

# =========================
# KALKULYATOR FUNKSIYALARI
# =========================

def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)

    if bmi < 18.5:
        category = "vazn yetishmovchiligi"
    elif bmi < 25:
        category = "me’yoriy vazn"
    elif bmi < 30:
        category = "ortiqcha vazn"
    else:
        category = "semirish"

    return round(bmi, 1), category

def calculate_water_need(weight_kg):
    liters = weight_kg * 0.03
    return round(liters, 2)

def sport_advice_by_age(age):
    if age < 5:
        return (
            "Bu yoshdagi bolalarda faol o‘yinlar, yugurish, sakrash va harakatli mashg‘ulotlar foydali. "
            "Mashg‘ulotlar o‘yin ko‘rinishida bo‘lishi kerak."
        )
    elif 5 <= age <= 17:
        return (
            "Bu yoshda yugurish, velosiped, suzish, sport o‘yinlari va umumiy jismoniy rivojlantiruvchi mashqlar foydali. "
            "Muntazam harakat va xavfsiz texnika muhim."
        )
    elif 18 <= age <= 39:
        return (
            "Bu yoshda kardio mashqlar, yugurish, fitnes, kuch mashqlari va moslashuvchanlik mashqlari tavsiya etiladi. "
            "Haftalik rejani saqlash foydali."
        )
    elif 40 <= age <= 59:
        return (
            "Bu yoshda yurish, yengil yugurish, suzish, velotrenajyor, cho‘zilish va o‘rtacha kuch mashqlari foydali. "
            "Yuklama asta-sekin oshirilishi kerak."
        )
    else:
        return (
            "60 yoshdan keyin piyoda yurish, yengil gimnastika, muvozanat mashqlari, cho‘zilish va shifokor ruxsat bergan yengil mashqlar foydali. "
            "Ortiqcha yuklamadan saqlanish kerak."
        )

# =========================
# START / HELP
# =========================

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    reset_user(message.from_user.id)
    await message.answer(
        "Assalomu alaykum.\nKerakli bo‘limni tanlang:",
        reply_markup=main_menu()
    )

@dp.message_handler(commands=["help"])
async def help_handler(message: types.Message):
    await message.answer(
        "Yo‘riqnoma:\n"
        "• Bo‘lim tanlang\n"
        "• Ichki mavzuni tanlang\n"
        "• Kasalliklar bo‘limida kasallikni tanlagach, ichki 6 bo‘lim chiqadi\n"
        "• Kalkulyatorlar bo‘limida hisob-kitob funksiyalari bor\n"
        "• Orqaga bir pog‘ona ortga qaytaradi\n"
        "• Bosh menyu bosh sahifaga olib boradi",
        reply_markup=main_menu()
    )

# =========================
# ASOSIY BO'LIMLAR
# =========================

@dp.message_handler(lambda m: m.text in general_sections.keys())
async def open_general_section(message: types.Message):
    user_id = message.from_user.id
    ensure_user(user_id)

    section = message.text
    user_state[user_id]["mode"] = "section"
    user_state[user_id]["current_section"] = section
    user_state[user_id]["current_disease"] = None

    await message.answer(
        f"{section} bo‘limi ochildi.\nMavzuni tanlang:",
        reply_markup=section_menu(section)
    )

@dp.message_handler(lambda m: m.text == "Kasalliklar")
async def open_diseases(message: types.Message):
    user_id = message.from_user.id
    ensure_user(user_id)

    user_state[user_id]["mode"] = "disease_menu"
    user_state[user_id]["current_section"] = "Kasalliklar"
    user_state[user_id]["current_disease"] = None

    await message.answer(
        "Kasalliklar bo‘limi ochildi.\nKasallikni tanlang:",
        reply_markup=disease_menu()
    )

@dp.message_handler(lambda m: m.text == "Kalkulyatorlar")
async def open_calculators(message: types.Message):
    user_id = message.from_user.id
    ensure_user(user_id)
    user_state[user_id]["mode"] = "calculators"

    await message.answer(
        "Kalkulyatorlardan birini tanlang:",
        reply_markup=calculators_menu()
    )

# =========================
# ODDIY BO'LIM MAVZULARI
# =========================

@dp.message_handler(lambda m: any(m.text in topics for topics in general_sections.values()))
async def general_topic_handler(message: types.Message):
    user_id = message.from_user.id
    ensure_user(user_id)

    found_section = None
    for section_name, topics in general_sections.items():
        if message.text in topics:
            found_section = section_name
            break

    if not found_section:
        await message.answer("Mavzu topilmadi.", reply_markup=main_menu())
        return

    user_state[user_id]["mode"] = "topic"
    user_state[user_id]["current_section"] = found_section
    user_state[user_id]["current_disease"] = None

    content = general_sections[found_section][message.text]

    await message.answer(
        f"{message.text}\n\n{content}{WARNING_TEXT}",
        reply_markup=nav_menu()
    )

# =========================
# KASALLIKLAR
# =========================

@dp.message_handler(lambda m: m.text in diseases.keys())
async def disease_handler(message: types.Message):
    user_id = message.from_user.id
    ensure_user(user_id)

    disease_name = message.text
    user_state[user_id]["mode"] = "disease_detail_menu"
    user_state[user_id]["current_section"] = "Kasalliklar"
    user_state[user_id]["current_disease"] = disease_name

    await message.answer(
        f"{disease_name} bo‘limi.\nKerakli qismni tanlang:",
        reply_markup=disease_detail_menu(disease_name)
    )

@dp.message_handler(lambda m: m.text in [
    "Ta’rif", "Belgilar", "Xavf omillari",
    "Nega muhim", "Oldini olish va nazorat",
    "Qachon shifokorga murojaat qilish kerak"
])
async def disease_part_handler(message: types.Message):
    user_id = message.from_user.id
    ensure_user(user_id)

    disease_name = user_state[user_id].get("current_disease")

    if not disease_name or disease_name not in diseases:
        await message.answer(
            "Avval kasallikni tanlang.",
            reply_markup=disease_menu()
        )
        return

    user_state[user_id]["mode"] = "disease_part"

    part_name = message.text
    content = diseases[disease_name][part_name]

    await message.answer(
        f"{disease_name}\n\n{part_name}:\n{content}{WARNING_TEXT}",
        reply_markup=nav_menu()
    )

# =========================
# FAQ / ABOUT / TIP
# =========================

@dp.message_handler(lambda m: m.text == "FAQ")
async def faq_handler(message: types.Message):
    user_id = message.from_user.id
    ensure_user(user_id)
    user_state[user_id]["mode"] = "faq"

    await message.answer(
        "Tez-tez so‘raladigan savollardan birini tanlang:",
        reply_markup=faq_menu()
    )

@dp.message_handler(lambda m: m.text in faq_data.keys())
async def faq_answer_handler(message: types.Message):
    user_id = message.from_user.id
    ensure_user(user_id)
    user_state[user_id]["mode"] = "faq_answer"

    await message.answer(
        faq_data[message.text],
        reply_markup=nav_menu()
    )

@dp.message_handler(lambda m: m.text == "Bot haqida")
async def about_handler(message: types.Message):
    user_id = message.from_user.id
    ensure_user(user_id)
    user_state[user_id]["mode"] = "about"

    await message.answer(
        "HealthInfo — sog‘liq bo‘yicha umumiy ma’lumot beruvchi Telegram bot.\n\n"
        "Imkoniyatlari:\n"
        "• Ovqatlanish\n"
        "• Homiladorlik\n"
        "• Sport\n"
        "• Vitaminlar\n"
        "• Kasalliklar\n"
        "• BMI kalkulyator\n"
        "• Suv ehtiyoji kalkulyatori\n"
        "• Yoshga qarab sport tavsiyasi\n"
        "• Qidiruv\n\n"
        "Bot tashxis qo‘ymaydi.",
        reply_markup=nav_menu()
    )

@dp.message_handler(lambda m: m.text == "Kun maslahati")
async def daily_tip_handler(message: types.Message):
    user_id = message.from_user.id
    ensure_user(user_id)
    user_state[user_id]["mode"] = "tip"

    tip = random.choice(daily_tips)
    await message.answer(
        f"💡 Kun maslahati:\n\n{tip}",
        reply_markup=nav_menu()
    )

# =========================
# KALKULYATORLAR
# =========================

@dp.message_handler(lambda m: m.text == "BMI kalkulyator")
async def bmi_start_handler(message: types.Message):
    user_id = message.from_user.id
    ensure_user(user_id)
    user_state[user_id]["mode"] = "bmi_input"

    await message.answer(
        "Bo‘yingiz va vazningizni kiriting.\n\n"
        "Format:\n170 65\n\n"
        "Bu yerda 170 = bo‘y (sm), 65 = vazn (kg)",
        reply_markup=nav_menu()
    )

@dp.message_handler(lambda m: m.text == "Kunlik suv ehtiyoji")
async def water_start_handler(message: types.Message):
    user_id = message.from_user.id
    ensure_user(user_id)
    user_state[user_id]["mode"] = "water_input"

    await message.answer(
        "Vazningizni kiriting.\n\n"
        "Format:\n65\n\n"
        "Bu yerda 65 = vazn (kg)",
        reply_markup=nav_menu()
    )

@dp.message_handler(lambda m: m.text == "Yoshga qarab sport tavsiyasi")
async def sport_age_start_handler(message: types.Message):
    user_id = message.from_user.id
    ensure_user(user_id)
    user_state[user_id]["mode"] = "age_input"

    await message.answer(
        "Yoshingizni kiriting.\n\n"
        "Format:\n21",
        reply_markup=nav_menu()
    )

@dp.message_handler(lambda m: m.from_user.id in user_state and user_state[m.from_user.id].get("mode") == "bmi_input" and m.text not in ["Orqaga", "Bosh menyu", "Yana savol bering"])
async def bmi_input_handler(message: types.Message):
    user_id = message.from_user.id
    text = message.text.strip().replace(",", ".")

    try:
        parts = text.split()
        if len(parts) != 2:
            raise ValueError

        height_cm = float(parts[0])
        weight_kg = float(parts[1])

        bmi, category = calculate_bmi(height_cm, weight_kg)
        user_state[user_id]["mode"] = "calculators"

        await message.answer(
            f"Natija:\n"
            f"• BMI: {bmi}\n"
            f"• Holat: {category}\n\n"
            f"Eslatma: BMI umumiy ko‘rsatkich bo‘lib, aniq baholash uchun mutaxassis tavsiyasi foydali.{WARNING_TEXT}",
            reply_markup=calculators_menu()
        )
    except Exception:
        await message.answer(
            "Noto‘g‘ri format.\nIltimos, quyidagicha kiriting:\n170 65",
            reply_markup=nav_menu()
        )

@dp.message_handler(lambda m: m.from_user.id in user_state and user_state[m.from_user.id].get("mode") == "water_input" and m.text not in ["Orqaga", "Bosh menyu", "Yana savol bering"])
async def water_input_handler(message: types.Message):
    user_id = message.from_user.id
    text = message.text.strip().replace(",", ".")

    try:
        weight_kg = float(text)
        liters = calculate_water_need(weight_kg)
        user_state[user_id]["mode"] = "calculators"

        await message.answer(
            f"Siz uchun taxminiy kunlik suv ehtiyoji: {liters} litr.\n\n"
            f"Eslatma: bu umumiy hisob. Issiq havo, sport, isitma yoki ayrim sog‘liq holatlarida ehtiyoj o‘zgarishi mumkin.",
            reply_markup=calculators_menu()
        )
    except Exception:
        await message.answer(
            "Noto‘g‘ri format.\nFaqat vaznni kiriting.\nMasalan:\n65",
            reply_markup=nav_menu()
        )

@dp.message_handler(lambda m: m.from_user.id in user_state and user_state[m.from_user.id].get("mode") == "age_input" and m.text not in ["Orqaga", "Bosh menyu", "Yana savol bering"])
async def age_input_handler(message: types.Message):
    user_id = message.from_user.id
    text = message.text.strip()

    try:
        age = int(text)
        advice = sport_advice_by_age(age)
        user_state[user_id]["mode"] = "calculators"

        await message.answer(
            f"Yoshga qarab sport tavsiyasi:\n\n{advice}{WARNING_TEXT}",
            reply_markup=calculators_menu()
        )
    except Exception:
        await message.answer(
            "Noto‘g‘ri format.\nFaqat yoshni kiriting.\nMasalan:\n21",
            reply_markup=nav_menu()
        )

# =========================
# QIDIRUV
# =========================

@dp.message_handler(lambda m: m.text == "Yana savol bering")
async def search_mode_handler(message: types.Message):
    user_id = message.from_user.id
    ensure_user(user_id)
    user_state[user_id]["mode"] = "search"

    await message.answer(
        "Qidiruv rejimi yoqildi.\nSavol yoki kalit so‘z yozing.\nMasalan: bosim, diabet, HIV, covid, sil, suv, vitamin",
        reply_markup=nav_menu()
    )

@dp.message_handler(lambda m: m.from_user.id in user_state and user_state[m.from_user.id].get("mode") == "search" and m.text not in ["Orqaga", "Bosh menyu", "Yana savol bering"])
async def search_handler(message: types.Message):
    results = search_content(message.text)

    if not results:
        await message.answer(
            "Bu so‘z bo‘yicha mos ma’lumot topilmadi.",
            reply_markup=nav_menu()
        )
        return

    parts = []
    for section, topic, content in results[:3]:
        parts.append(f"📌 {section} → {topic}\n{content}")

    await message.answer(
        "\n\n".join(parts) + WARNING_TEXT,
        reply_markup=nav_menu()
    )

# =========================
# NAVIGATSIYA
# =========================

@dp.message_handler(lambda m: m.text == "Orqaga")
async def back_handler(message: types.Message):
    user_id = message.from_user.id
    ensure_user(user_id)

    mode = user_state[user_id].get("mode")
    current_section = user_state[user_id].get("current_section")
    current_disease = user_state[user_id].get("current_disease")

    if mode == "topic" and current_section in general_sections:
        user_state[user_id]["mode"] = "section"
        await message.answer(
            f"{current_section} bo‘limiga qaytdingiz.\nMavzuni tanlang:",
            reply_markup=section_menu(current_section)
        )
        return

    if mode == "section":
        reset_user(user_id)
        await message.answer("Bosh sahifa:", reply_markup=main_menu())
        return

    if mode == "disease_part" and current_disease in diseases:
        user_state[user_id]["mode"] = "disease_detail_menu"
        await message.answer(
            f"{current_disease} bo‘limiga qaytdingiz.\nKerakli qismni tanlang:",
            reply_markup=disease_detail_menu(current_disease)
        )
        return

    if mode == "disease_detail_menu":
        user_state[user_id]["mode"] = "disease_menu"
        user_state[user_id]["current_disease"] = None
        await message.answer(
            "Kasalliklar ro‘yxatiga qaytdingiz.\nKasallikni tanlang:",
            reply_markup=disease_menu()
        )
        return

    if mode == "disease_menu":
        reset_user(user_id)
        await message.answer("Bosh sahifa:", reply_markup=main_menu())
        return

    if mode in ["faq", "faq_answer", "about", "tip", "search", "calculators"]:
        reset_user(user_id)
        await message.answer("Bosh sahifa:", reply_markup=main_menu())
        return

    if mode in ["bmi_input", "water_input", "age_input"]:
        user_state[user_id]["mode"] = "calculators"
        await message.answer(
            "Kalkulyatorlar bo‘limiga qaytdingiz:",
            reply_markup=calculators_menu()
        )
        return

    reset_user(user_id)
    await message.answer("Bosh sahifa:", reply_markup=main_menu())

@dp.message_handler(lambda m: m.text == "Bosh menyu")
async def home_handler(message: types.Message):
    reset_user(message.from_user.id)
    await message.answer("Bosh sahifa:", reply_markup=main_menu())

# =========================
# NOANIQ XABAR
# =========================

@dp.message_handler()
async def fallback_handler(message: types.Message):
    await message.answer(
        "Iltimos, menyudagi tugmalardan foydalaning.",
        reply_markup=main_menu()
    )

# =========================
# RUN
# =========================

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Bot is running')

def run_web():
    server = HTTPServer(('0.0.0.0', 10000), Handler)
    server.serve_forever()

threading.Thread(target=run_web).start()