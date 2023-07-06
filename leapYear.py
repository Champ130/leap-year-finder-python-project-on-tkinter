import tkinter as tk
print(dir(tk))


t = tk.Tk()
t.title('Leap Year Checker')
t.geometry('400x400+400+100')
t.resizable(0,0)

def leap_func():
    year2 = int(years.get("1.0",'end'))
    #length = len(str(year2))
    try:
        #if length>=4 and str(year2)[-1] == '0' and str(year2)[-2] == '0':
        if (year2 % 400 == 0) and (year2 % 4 == 0):
                result.delete("1.0", 'end')
                result.insert("1.0", f'{year2} ''is a leap year!')

        else:
                result.delete("1.0", 'end')
                result.insert("1.0", f'{year2} is not a leap year!')
    except :
        result.insert("1.0")

frame_top = tk.Frame(t, height=400, width=400, bg='yellow')
frame_top.pack(expand=True, fill=tk.BOTH)
years = tk.Text(frame_top, width=20, height=1, font='arial 10 bold')
years.place(x=90, y=40)

btn = tk.Button(frame_top, text='Check It Out', width = 10,  bg='white', font='arial 10 bold', command=leap_func)
btn.place(x=250, y=38)
result = tk.Text(frame_top, width=44, height=12, wrap='word')
result.place(x=20, y=85)

t.mainloop()