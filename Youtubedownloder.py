#ライブラリの設定
from tkinter import*
from tkinter import ttk
import tkinter.ttk as ttk
from yt_dlp import YoutubeDL

#ダウンロードコマンド
def installmp3():
    option = {
        'outtmpl' : '%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  
            'preferredcodec': 'mp3', 
            'preferredquality': '192'
        }]
    }
    ydl = YoutubeDL(option)
    result = ydl.download([entry1.get()])

def installm4a():
    option = {
        'outtmpl' : '%(title)s.%(ext)s',
        'format' : 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  
            'preferredcodec': 'm4a', 
            'preferredquality': '192'
        }]
    }
    ydl = YoutubeDL(option)
    result = ydl.download([entry1.get()])

def installmp4_best():
    option = {
        'outtmpl' : '%(title)s.%(ext)s',
        'format' : 'bestvideo[ext=mp4]+bestaudio[ext=mp3]/best[ext=mp4]'
    }
    ydl = YoutubeDL(option)
    result = ydl.download([entry1.get()])

def installmp4_middle():
    option = {
        'outtmpl' : '%(title)s.%(ext)s',
        'format' : 'best[ext=mp4]'
    }
    ydl = YoutubeDL(option)
    result = ydl.download([entry1.get()])

def installmp4_worst():
    option = {
        'outtmpl' : '%(title)s.%(ext)s',
        'format' : 'worst[ext=mp4]'
    }
    ydl = YoutubeDL(option)
    result = ydl.download([entry1.get()])

#メインウィンドウの設定
root = Tk()
root.title('Youtube downloder')#ここにアプリの名前を入力
root.geometry("356x173")#アプリのウィンドウの大きさ
root.resizable(False, False)
frame1 = ttk.Frame(root, width=200, height=100, relief='solid')
frame2 = ttk.Frame(root, width=200, height=200, borderwidth=2, relief='solid')
frame3 = ttk.Frame(root, width=100, height=300, borderwidth=2, relief='solid')
label1 = ttk.Label(frame2, text = 'URLを入力')
label3 = ttk.Label(frame1, text = 'Youtube downloder')
label4 = ttk.Label(frame1, text = 'Youtubeの動画をダウンロードする')
t = StringVar()
entry1 = ttk.Entry(frame2)
button1 = ttk.Button(frame3, text='download mp3', command=installmp3)
button4 = ttk.Button(frame3, text='download m4a', command=installm4a)
button2 = ttk.Button(frame3, text='download 最高品質mp4', command=installmp4_best)
button3 = ttk.Button(frame3, text='download 中品質mp4', command=installmp4_middle)
button5 = ttk.Button(frame3, text='download 最低品質mp4', command=installmp4_worst)
label2 = ttk.Label(frame3, text = 'ファイル形式を選択してダウンロード')
frame1.grid(row=0, column=0)#ここからはボタン等の配置
frame2.grid(row=1, column=0)
frame3.grid(row=0, column=1)
label3.pack(side=TOP)
label4.pack(side=TOP)
label1.pack(side=LEFT)
entry1.pack(side=LEFT)
button1.pack(side=BOTTOM)
button4.pack(side=BOTTOM)
button2.pack(side=BOTTOM)
button3.pack(side=BOTTOM)
button5.pack(side=BOTTOM)
label2.pack(side=BOTTOM)
root.mainloop()