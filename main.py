import os 
import  openai
import utils.ayar as ayar 
import utils.funci as funci
from pyrogram import Client, filters
os.system('clear')
# Функции тут
def catxpt(textas):
    openai.api_key= 'insert openai api key'
    # promt ='Hello'
    
    # задаем модель и промпт
    model_engine = "text-davinci-003"
    prompt = "Hello"
    
    # задаем макс кол-во слов
    max_tokens = 128 
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=textas,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return completion.choices[0].text
# Переменные тут 

app = Client("azercelius", api_id=ayar.api_id, api_hash=ayar.api_hash)
# -----------------------------------------------------⇥
# Этот сниппет выведет отформатированный список всех сессий и дату их создания.
# Если вам нужна другая информация, обратитесь к соответствующей документации:
# https://docs.pyrogram.org/telegram/types/authorization
# with app:
#     auths = app.send(GetAuthorizations()).authorizations

#     # Sort list of Authorizations and give us the longest name+version combination
#     auths.sort(key=lambda x: x.date_created)
#     width = max(auths, key=lambda x: len(x.app_name + x.app_version))
#     width = len(width.app_name + width.app_version) + 1

#     for auth in auths:
#         print(f"{auth.app_name} {auth.app_version}".ljust(width), end=" - ")
#         #        print(datetime.fromtimestamp(auth.date_created))
# # -----------------------------------------------------⇥ Показывает сколько стикеров, у меня есть
# with app:
#     all_sets = app.send(functions.messages.GetAllStickers(hash=0)).sets
#     count = sum([x.count for x in all_sets])
#     print(
#         f"{count} stickers across {len(all_sets)} sets.\n"
#         f"Average of {count / len(all_sets):.2f} stickers per pack."
#     )


# -----------------------------------------------------⇥ Тело бота

# Фильтр на слово Кот
@app.on_message(filters.text & filters.regex('^Кот ') )
async def help(_, message):
    orig_text = message.text.split("Кот ", maxsplit=1)[1]
    await message.reply(f"<i>{catxpt(orig_text)}</i>", parse_mode=enums.ParseMode.HTML )
    await asyncio.sleep(15)    

# Ответ на слово .test
@app.on_message(filters.command("test", ".") )
async def help(_, message):
    await message.reply('i workd')
   
     
if __name__ == "__main__":
    app.run()
