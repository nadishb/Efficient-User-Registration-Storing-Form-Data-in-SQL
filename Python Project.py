from tkinter import *
import tkinter.messagebox as box
import mysql.connector


window = Tk()
window.geometry("550x550")
window.title('Registration form')
conn = mysql.connector.connect(host='localhost', password='nadish2005', user='root', database="project")
cur = conn.cursor()
def sum():
    box.askyesno("Info","Want to Submit")

    A = enter_1.get()
    B = enter_3.get()
    C  = vars.get()
    D = vars1.get()
    X = vars2.get()
    M  = cv.get()

    while True:

            print(A)
            print(B)
            print(C)
            print(D)
            print(X)
            print(M)
            sql = '''INSERT INTO S(NAME,EMAIL,GENDER,COUNTRY,PROGRAM)
            VALUES(%s,%s,%s,%s,%s)'''
            Z = "Java"
            A1 = (""+A)
            B1 = (""+B)
            E1 = "Python"
            b1 = "Female"
            a1 = "Male"

            P = (A1,B1,a1,M,Z)
            L = (A1,B1,b1,M,E1)
            p = (A1,B1,a1,M,E1)
            l = (A1,B1,b1,M,Z)
            try:
                if C == 1 and D == 1:
                    cur.execute(sql,P)
                    conn.commit()
                elif C == 2 and X == 1:
                    cur.execute(sql,L)
                    conn.commit()
                elif C == 1 and X == 1:
                    cur.execute(sql,p)
                    conn.commit()
                else:
                    cur.execute(sql,l)
                    conn.commit()
            except:
                conn.rollback()
                if conn.is_connected():
                    print("Saved")
                    conn.close()
                else:
                    print("NOT")
            window.destroy()
            break







lbl_0 = Label(window, text="Registration form",  font=("bold", 20))
lbl_0.place(x=90, y=60)
lbl_1 = Label(window, text="FullName",  font=("bold", 10))
lbl_1.place(x=90, y=130)
enter_1 = Entry(window)
enter_1.place(x=240, y=130)
lbl_3 = Label(window, text="Email",  font=("bold", 10))
lbl_3.place(x=90, y=180)
enter_3 = Entry(window)
enter_3.insert(0,"@gmail.com")
enter_3.place(x=240, y=180)
lbl_4 = Label(window, text="Gender",  font=("bold", 10))
lbl_4.place(x=90, y=230)
vars = IntVar()
Radiobutton(window, text="Male", padx=5, variable=vars, value=1).place(x=235, y=230)
Radiobutton(window, text="Female", padx=20, variable=vars, value=2).place(x=290, y=230)
lbl_5 = Label(window, text="Country",  font=("bold", 11))
lbl_5.place(x=90, y=280)
list_of_cntry = ['India', 'Canada', 'US', 'Germany', 'UK']
cv = StringVar()
drplist = OptionMenu(window, cv, *list_of_cntry)
drplist.config(width=15)
cv.set('Select your Country')
drplist.place(x=240, y=280)
lbl_6 = Label(window, text="Programming",  font=('bold', 10))
lbl_6.place(x=90, y=330)
vars1 = IntVar()
Checkbutton(window, text="Java", variable=vars1).place(x=230, y=330)
vars2 = IntVar()
Checkbutton(window,text="Python", variable=vars2).place(x=290, y=330)
Button(window, text='Submit', width=20, bg="Red", fg='white',command=sum).place(x=120, y=380)


window.mainloop()
conn.close()
