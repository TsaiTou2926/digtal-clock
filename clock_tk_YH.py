import tkinter as tk
import datetime
import time

GMT = datetime.timezone(datetime.timedelta(hours=8))    # 設定所在時區 ( 台灣是 GMT+8 )

root = tk.Tk()                # 建立視窗物件
root.title('電子鐘 v2.0')     # 設定視窗標題
root.geometry('300x225')      # 設定視窗大小
root.configure(bg='#181818')

a = tk.StringVar()            # 建立文字變數
b = tk.StringVar()
c = tk.StringVar()

# 建立不斷改變文字變數的函式
def showTime():
    now = datetime.datetime.now(tz=GMT).strftime('%H點%M分%S秒')   # 取得目前的時間，格式使用 H點M分S秒
    a.set(now)                    # 設定變數內容
    root.after(10, showTime)    # 視窗每隔 10 毫秒再次執行一次 showTime()

def showDate():
    day = time.strftime('西元%Y年%m月%d日') # 取得目前的日期，格式使用西元年月日
    b.set(day)                      # 設定變數內容
    root.after(1000, showDate)

def showWeek():
    weeknow = time.strftime('%A') # 取得英文輸出的星期幾
    if weeknow == 'Sunday':
        c.set('星期日')
    elif weeknow == 'Monday':
        c.set('星期一')
    elif weeknow == 'Tuesday':
        c.set('星期二')
    elif weeknow == 'Wednesday':
        c.set('星期三')
    elif weeknow == 'Thursday':
        c.set('星期四')
    elif weeknow == 'Friday':
        c.set('星期五')
    elif weeknow == 'Saturday':
        c.set('星期六')
    root.after(1000, showWeek)

tk.Label(root, text='現在日期', font=('Microsoft YaHei',20,), bg='#181818', fg='SkyBlue').pack()   # 放入第一個 Label 標籤
tk.Label(root, textvariable=b, font=('Microsoft YaHei',20), bg='#181818', fg='white').pack()   # 放入第二個 Label 標籤，內容是 b 變數
tk.Label(root, textvariable=c, font=('Microsoft YaHei', 20), bg='#181818', fg='Orange').pack() # 放入第三個 Label 標籤，內容是 c 變數
tk.Label(root, text='現在時間', font=('Microsoft YaHei', 20), bg='#181818', fg='SkyBlue').pack() # 放入第四個 Label 標籤
tk.Label(root, textvariable=a, font=('Microsoft YaHei', 20), bg='#181818', fg='white').pack()  # 放入第五個 Label 標籤，內容是 a 變數

showTime()   # 執行函式
showDate()
showWeek()

root.mainloop()