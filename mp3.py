import subprocess
import youtube_dl
import os
import warnings
warnings.filterwarnings("ignore") 

os.system('clear')

#pkg install ffmpeg
# %%
print ("""
\033[1;36m^   ▒▀▀█▀▀  ▒█  ▒█  ▒▀▀█▀▀█  ▒█▀▀█  ▒▀█▀▒     \033[1;36m^
\033[1;36m^     ▒█    ▒█  ▒█    ▒█  █  ▒█  █    █       ^
\033[1;36m^   \033[1;37m  ▒█    ▒█  ▒█    ▒█▄▄█  ▒█▄▄█    █       \033[1;36m^
\033[1;36m^   \033[1;37m  ▒█    ▒█▄▄▒█    ▒█     ▒█ ▒█  ▒▄█▄▒     \033[1;36m^
\033[1;34m▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
\033[1;34m█\033[1;36mPEMBUAT  : \033[1;37mTupai\033[1;34m       █\033[1;36mYT: \033[1;37mPenghasil Gratisan\033[1;34m █
\033[1;34m█\033[1;36mHOBI     : \033[1;37mNyopet\033[1;34m      █\033[0;33m       Warning!!!      \033[1;34m█
\033[1;34m█\033[1;36mAQOUNT_ML: \033[1;37mAllmost.kill\033[1;34m█\033[0;33m  This script is free\033[1;34m  █
\033[1;34m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
\033[1;34m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█""")

#os.system('termux-open-url https://youtu.be/2E-K71-oKg4')

def run():
    # MINTA PENGGUNA UNTUK VIDEO YANG INGIN MEREKA UNDUH
    video_url = input("\033[0;32mMASUKKAN URL YOUTUBE: \033[0;33m") 
    # UNDUH DAN UBAH KE MP3 DAN SIMPAN DI FOLDER UNDUHAN
    print ("\033[1;36m")
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False)
    print ("\033[1;36m")
    video_title = video_info['title']
    filename = f"{video_title}.mp3"

    # TANYAKAN KEPADA PENGGUNA JALUR YANG MEREKA INGINKAN UNTUK MENYIMPAN FILE SETELAH DIUNDUH
    path_to_save = input("\r\033[0;32mMASUKKAN NAMA FOLDER BUAT MENYIMPAN MUSIC: \033[0;33m")

    where_to_save = os.getcwd()

    if path_to_save != "":
        where_to_save = f"{path_to_save}"

    filename = f"{video_info['title']}.mp3"
    output_path = os.path.join(where_to_save, filename)


    options = {
        # MENGURANGI BEBERAPA BARIS KELUARAN MENJADI MINIMAL DAN OLEH KARENA ITU, WAKTU
        'quiet': True,
        'noplaylist': True,
        'format': 'bestaudio/best',
        'keepvideo': True,
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    # MENGEMBALIKAN SISTEM OS MISALNYA. 'NT' UNTUK WINDOWS
    
    
    # BUKA FILE SETELAH DI UNDUH
    


if __name__ == '__main__':
    run()
    print ("\033[1;33mDownload Sucses Silahkan Cek")
  
  
    
    	
   
    
