from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import socket
import mysql.connector
from datetime import date, datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1031))
s.listen(5)

clt, adr = s.accept()

mydb = mysql.connector.connect(user="root", password="123456", host="127.0.0.1", database="restaurants")
erp = mydb.cursor()

rt=Tk()
rt.geometry("1550x800")
# rt.configure(background="black")

starters=(("Pakode", 65),("Idli-Sambhar", 70),("Momos",30), ("Honey Chilli Potato", 50),("Paranthe", 60),("Sandwhich", 30),("Samose", 10))
main_course=(("Panner-Tikka", 120),("Mini-Thali", 100),("Rajma-Chawal", 60),("Cholle Chawal", 60),("Dal Tadka with Roti", 80))
chinese_food=(("Chowmein", 30),("Paneer Chilli", 60),("Manchurian", 60),("Fried Rice", 40),("Choupsey", 80))
bevrages=(("Tea", 10),("Coffee", 15),("Mineral Water", "20"),("Soft Drinks", "MRP"),("Lassi", 30),("Beer", 120))

cn=Canvas(rt, width=1550, height=800)
cn.pack()

cn.create_line(700, 125, 700, 750)

l0=Label(rt,text="Pappu Dhaba -Unofficial Restaurant", font=("bold", 40))
l0.place(x=30, y=30)

l1=Label(rt, text="ORDER", font=("bold", 22))
l1.place(x=850, y=200)

l1=Label(rt, text="AMOUNT", font=("bold", 22))
l1.place(x=1275, y=200)

lbx1=Listbox(rt, font=(22), width=30, height=20)
lbx1.place(x=750, y=250)

lbx2=Listbox(rt, font=(22), width=25, height=10)
lbx2.place(x=1200, y=250)

l2=Label(rt, text="Starters", font=("bold", 22))
l2.place(x=290, y=200)

cn.create_line(20, 300, 690, 300)

l2=Label(rt, text="Main Course", font=("bold", 22))
l2.place(x=260, y=320)

cn.create_line(20, 420, 690, 420)

l2=Label(rt, text="Chinese Food", font=("bold", 22))
l2.place(x=260, y=440)

cn.create_line(20, 530, 690, 530)

l2=Label(rt, text="Bevrages", font=("bold", 22))
l2.place(x=280, y=550)

food_items=[]
price=[]
total_price=0

def order(x):
    c=x
    food_items.append(c[0])
    lbx1.insert(ACTIVE, c[0])
    price.append(c[1])
    # print(price)
    lbx2.insert(ACTIVE, c[1])
    return price, food_items

bt1=Button(rt, text="pakode", command=lambda:order(starters[0]))
bt2=Button(rt, text="idli sambhar", command=lambda:order(starters[1]))
bt3=Button(rt, text="momos", command=lambda:order(starters[2]))
bt4=Button(rt, text="honey chiili potato", command=lambda:order(starters[3]))
bt5=Button(rt, text="paranthe", command=lambda:order(starters[4]))
bt6=Button(rt, text="sandwhich", command=lambda:order(starters[5]))
bt7=Button(rt, text="samose", command=lambda:order(starters[6]))
bt8=Button(rt, text="panner tikka", command=lambda:order(main_course[0]))
bt9=Button(rt, text="mini thali", command=lambda:order(main_course[1]))
bt10=Button(rt, text="rajma chawal", command=lambda:order(main_course[2]))
bt11=Button(rt, text="cholle chawal", command=lambda:order(main_course[3]))
bt12=Button(rt, text="dal tadka with roti", command=lambda:order(main_course[4]))
bt13=Button(rt, text="chowmein", command=lambda:order(chinese_food[0]))
bt14=Button(rt, text="panner chilli", command=lambda:order(chinese_food[1]))
bt15=Button(rt, text="manchurian", command=lambda:order(chinese_food[2]))
bt16=Button(rt, text="fried rice", command=lambda:order(chinese_food[3]))
bt17=Button(rt, text="choupsey", command=lambda:order(chinese_food[4]))
bt18=Button(rt, text="tea", command=lambda:order(bevrages[0]))
bt19=Button(rt, text="coffee", command=lambda:order(bevrages[1]))
bt20=Button(rt, text="mineral water", command=lambda:order(bevrages[2]))
bt21=Button(rt, text="soft drinks", command=lambda:order(bevrages[3]))
bt22=Button(rt, text="lassi", command=lambda:order(bevrages[4]))
bt23=Button(rt, text="beer", command=lambda:order(bevrages[5]))


bt1.place(x=30, y=250)
bt2.place(x=120, y=250)
bt3.place(x=210, y=250)
bt4.place(x=300, y=250)
bt5.place(x=420, y=250)
bt6.place(x=510, y=250)
bt7.place(x=600, y=250)
bt8.place(x=30, y=370)
bt9.place(x=120, y=370)
bt10.place(x=210, y=370)
bt11.place(x=300, y=370)
bt12.place(x=390, y=370)
bt13.place(x=30, y=480)
bt14.place(x=120, y=480)
bt15.place(x=210, y=480)
bt16.place(x=300, y=480)
bt17.place(x=390, y=480)
bt18.place(x=30, y=590)
bt19.place(x=120, y=590)
bt20.place(x=210, y=590)
bt21.place(x=300, y=590)
bt22.place(x=390, y=590)
bt23.place(x=480, y=590)

l3=Label(rt, text="Tbl no.", font=(22))
l3.place(x=1200, y=550)

sc1=StringVar()
en1=Entry(rt, font=(22), width=5, textvariable=sc1)
en1.place(x=1300, y=550)

ch=Combobox(rt, font=(22))
ch['values']=("Cash", "Credit/Debit card", "Online Payment", "select anyone")
ch.current(3)
ch.place(x=1200, y=600)

ch1=Combobox(rt, font=(22))
ch1['values']=("Dine in", "Take away", "Delivery", "select anyone")
ch1.current(3)
ch1.place(x=1200, y=650)

def er():
    global total_price
    for i in price:
        total_price+=i
    # print(total_price)

    lbx2.insert(END, f"total amount = {total_price}")
    return total_price

btco=Button(rt, text="confirm items", command=er)
btco.place(x=1390, y=500)

def all():
    erp.execute(f"insert into res values('{total_price}', '{ch.get()}', '{ch1.get()}', '{date.today()}', '{datetime.now().strftime('%H:%M:%S')}')")
    mydb.commit()
    whole=f"{food_items}, {sc1.get()}, {ch1.get()}"
    clt.send(bytes(whole, "utf-8"))
    clt.close()
    lbx1.insert(0, END)
    lbx2.insert(0, END)
    sc1.set("")
    ch.grab_current()
    ch1.grab_current()

btcon=Button(rt, text="Confirm", command=all)
btcon.place(x=1300, y=700)

rt.mainloop()
