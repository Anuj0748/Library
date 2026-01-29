from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime


class librarymanagement:
    def __init__(self,root):
        self.root=root
        self.root.title("library")
        self.root.geometry("1550x800+0+0")

        #variable
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue=StringVar()
        self.finallprice=StringVar ()


        lbtitle=Label(self.root,text="LIBRARY MANAGEMENT",bg="light blue", fg="green",bd=20, relief=RIDGE, font=("times new roman",50,"bold"),padx=2,pady=6)
        lbtitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue") 
        frame.place(x=0,y=110, width=1530, height=400)
        
        #leftframe
        DataFrameLeft=LabelFrame(frame,text="Library member information",bg="light blue", fg="black",bd=12,relief=RIDGE, font=("times new roman",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblmember=Label(DataFrameLeft,bg="light blue",fg="black",text="member type",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblmember.grid(row=0,column=0,sticky=W)

        commember=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),width=27,textvariable=self.member_var,state="readonly")
        commember["value"]=("Admin Staf", "Student", "Lecturer")
        commember.grid(row=0,column=1)

        lblprnnum=Label(DataFrameLeft,bg="light blue",fg="black",text="prn number",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblprnnum.grid(row=1,column=0,sticky=W)
        txtprn=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.prn_var,width=29)
        txtprn.grid(row=1,column=1)

        lblprnnum=Label(DataFrameLeft,bg="light blue",fg="black",text="id no.",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblprnnum.grid(row=2,column=0,sticky=W)
        txtprn=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.id_var,width=29)
        txtprn.grid(row=2,column=1)

        lblprnnum=Label(DataFrameLeft,bg="light blue",fg="black",text="first name",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblprnnum.grid(row=3,column=0,sticky=W)
        txtprn=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.firstname_var,width=29)
        txtprn.grid(row=3,column=1)

        lblprnnum=Label(DataFrameLeft,bg="light blue",fg="black",text="last name",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblprnnum.grid(row=4,column=0,sticky=W)
        txtprn=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.lastname_var,width=29)
        txtprn.grid(row=4,column=1)

        lblprnnum=Label(DataFrameLeft,bg="light blue",fg="black",text="address 1",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblprnnum.grid(row=5,column=0,sticky=W)
        txtprn=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.address1_var,width=29)
        txtprn.grid(row=5,column=1)

        lblprnnum=Label(DataFrameLeft,bg="light blue",fg="black",text="address 2",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblprnnum.grid(row=6,column=0,sticky=W)
        txtprn=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.address2_var,width=29)
        txtprn.grid(row=6,column=1)

        lblprnnum=Label(DataFrameLeft,bg="light blue",fg="black",text="post code",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblprnnum.grid(row=7,column=0,sticky=W)
        txtprn=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.postcode_var,width=29)
        txtprn.grid(row=7,column=1)

        lblprnnum=Label(DataFrameLeft,bg="light blue",fg="black",text="mobile",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblprnnum.grid(row=8,column=0,sticky=W)
        txtprn=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.mobile_var,width=29)
        txtprn.grid(row=8,column=1)

        lblprnnum=Label(DataFrameLeft,bg="light blue",fg="black",text="book id",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblprnnum.grid(row=0,column=5,sticky=W)
        txtprn=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.bookid_var,width=29)
        txtprn.grid(row=0,column=6)

        lblprnnum=Label(DataFrameLeft,bg="light blue",fg="black",text="book title",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblprnnum.grid(row=1,column=5,sticky=W)
        txtprn=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.booktitle_var,width=29)
        txtprn.grid(row=1,column=6)

        lblprnnum=Label(DataFrameLeft,bg="light blue",fg="black",text="auther name",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblprnnum.grid(row=2,column=5,sticky=W)
        txtprn=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.auther_var,width=29)
        txtprn.grid(row=2,column=6)

        lblprnnum=Label(DataFrameLeft,bg="light blue",fg="black",text="date borrowed",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblprnnum.grid(row=3,column=5,sticky=W)
        txtprn=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtprn.grid(row=3,column=6)

        lblprnnum=Label(DataFrameLeft,bg="light blue",fg="black",text="date due",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblprnnum.grid(row=4,column=5,sticky=W)
        txtprn=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.dateoverdue,width=29)
        txtprn.grid(row=4,column=6)

        lblprnnum=Label(DataFrameLeft,bg="light blue",fg="black",text="days on book",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblprnnum.grid(row=5,column=5,sticky=W)
        txtprn=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.daysonbook,width=29)
        txtprn.grid(row=5,column=6)


        lblprnnum=Label(DataFrameLeft,bg="light blue",fg="black",text="last return fine",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblprnnum.grid(row=6,column=5,sticky=W)
        txtprn=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.lateratefine_var,width=29)
        txtprn.grid(row=6,column=6)

        lblprnnum=Label(DataFrameLeft,bg="light blue",fg="black",text="date overdue",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblprnnum.grid(row=7,column=5,sticky=W)
        txtprn=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.dateoverdue,width=29)
        txtprn.grid(row=7,column=6)

        lblprnnum=Label(DataFrameLeft,bg="light blue",fg="black",text="actual price",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblprnnum.grid(row=8,column=5,sticky=W)
        txtprn=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.finallprice,width=29)
        txtprn.grid(row=8,column=6)



        #rightframe
        DataFrameRight=LabelFrame(frame,text="book details",bg="light blue", fg="black",bd=12,relief=RIDGE, font=("times new roman",15,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text (DataFrameRight,font=("arial",12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listscrollbar=Scrollbar(DataFrameRight)
        listscrollbar.grid(row=0,column=1,sticky="ns")

        Listbooks=['Head Firt Book','Learn Python The Hard Way',"Python Programming","Secrete Rahshy", "Python CookBook", "Into to Machine Learning, Fluent Pyt",
        'Machine tecno', 'My Python','Joss Ellif guru',' Elite Jungle python',' Jungli Python', 'Mumbai Python', 'Pune Pytho',
        'Machine python", "Advance Python", "Inton Python", RedChilli Python', 'Ishq Python','ddd','fgg','ddd','ddd']

        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Head Firt Book"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set( "Paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self. daysonbook.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("Rs.788")

        listBox=Listbox(DataFrameRight,font=("arial",12, "bold"), width=20, height=16, yscrollcommand=listscrollbar.set)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listscrollbar.config(command=listBox.yview)

        for item in Listbooks:
            listBox.insert(END,item)

        #butoons 
        framebutton=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue") 
        framebutton.place(x=0,y=500, width=1530, height=100)

        butadddata=Button(framebutton,command=self.add_data,text="Add Data",font=("arial",12, "bold"),width=23,bg="blue", fg="white")
        butadddata.grid(row=0,column=0)
        
        butadddata=Button(framebutton,command=self.showData,text="Show Data",font=("arial",12, "bold"),width=23,bg="blue", fg="white")
        butadddata.grid(row=0,column=1)

        butadddata=Button(framebutton,command=self.update,text="Update",font=("arial",12, "bold"),width=23,bg="blue", fg="white")
        butadddata.grid(row=0,column=2)

        butadddata=Button(framebutton,command=self.delete,text="Delete",font=("arial",12, "bold"),width=23,bg="blue", fg="white")
        butadddata.grid(row=0,column=3)

        butadddata=Button(framebutton,command=self.reset,text="Reset",font=("arial",12, "bold"),width=23,bg="blue", fg="white")
        butadddata.grid(row=0,column=4)

        butadddata=Button(framebutton,command=self.iexit,text="Exit",font=("arial",12, "bold"),width=23,bg="blue", fg="white")
        butadddata.grid(row=0,column=5)



        #database
        framedatabase=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue") 
        framedatabase.place(x=0,y=600, width=1530, height=195)

        tableframe=Frame(framedatabase,bd=6,relief=RIDGE,bg="powder blue")
        tableframe.place(x=0,y=2, width=1460, height=170)

        xscroll=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(tableframe,orient=VERTICAL)


        self.library_table=ttk.Treeview(tableframe,column=("memebertype", "prnno", "title", "firtname", "lastname", "adress1","adress2", "postid", "mobile", "bookid", "booktitle", "auther", "dateborrowed",
        "datedue", "days", "latereturnfine", "dateoverdue", "finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("memebertype", text="Member Type" )
        self.library_table.heading("prnno", text="Prn no.")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("firtname", text="First Name") 
        self.library_table.heading("lastname", text="Last Name") 
        self.library_table.heading("adress1", text="Address1") 
        self.library_table.heading("adress2", text="Address2") 
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("mobile", text="Mobile Number")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("auther", text="Auther")
        self.library_table.heading("dateborrowed", text="Date Of Borrowed")
        self.library_table.heading("datedue", text="Date Due") 
        self. library_table.heading("days", text="DaysOnBook")
        self.library_table.heading("latereturnfine", text="LateReturnFine")
        self.library_table.heading("dateoverdue", text="DateOverDue") 
        self.library_table.heading("finalprice", text="Final Price")


        self.library_table["show"]= "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self. library_table. column("memebertype", width=100)
        self. library_table.column("prnno", width=100) 
        self.library_table.column("title", width=100) 
        self.library_table.column("firtname", width=100)
        self.library_table.column("lastname", width=100) 
        self.library_table.column("adress1", width=100) 
        self.library_table.column("adress2", width=100) 
        self.library_table. column("postid", width=100) 
        self.library_table.column("mobile", width=100) 
        self.library_table. column("bookid", width=100) 
        self.library_table.column("booktitle", width=100)
        self.library_table. column("auther", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100) 
        self. library_table. column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table. column("dateoverdue", width=100) 
        self.library_table.column("finalprice", width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="anuj0748",database="data")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into libray values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.member_var.get(),
                                                                                                            self.prn_var.get(),
                                                                                                            self.id_var.get(),
                                                                                                            self.firstname_var.get(),
                                                                                                            self.lastname_var.get(),
                                                                                                            self.address1_var.get(),
                                                                                                            self.address2_var.get(),
                                                                                                            self.postcode_var.get(),
                                                                                                            self.mobile_var.get(),
                                                                                                            self.bookid_var.get(),
                                                                                                            self.booktitle_var.get(),
                                                                                                            self.auther_var.get(),
                                                                                                            self.dateborrowed_var.get(),
                                                                                                            self.datedue_var.get(),
                                                                                                            self.daysonbook.get(),
                                                                                                            self.lateratefine_var.get(),
                                                                                                            self.dateoverdue.get(),
                                                                                                            self.finallprice.get()
                                                                                                            ))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Success","Member has been inserted sccessfully")

    def fetch_data(self):    
        conn=mysql.connector.connect( host="localhost", user="root",password="anuj0748",database="data")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM libray")
        rows = my_cursor.fetchall()

  
        self.library_table.delete(*self.library_table.get_children())

   
        for i in rows:
           self.library_table.insert("", END, values=i)

        conn.close()  

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue.set(row[16]),
        self.finallprice.set(row[17])
    
    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get()+"\n")
        self.txtBox. insert(END,"PRN No: \t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END, "ID No: \t\t"+ self.id_var. get() + "\n")
        self.txtBox.insert(END, "FirstName: \t\t"+ self. firstname_var.get() + "\n")
        self.txtBox.insert(END, "LastName: \t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END, "Address1: \t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END, "Address2: \t\t"+ self. address2_var.get() + "\n")
        self.txtBox.insert(END, "Post Code: \t\t"+ self. postcode_var.get() + "\n") 
        self.txtBox.insert(END, "Mobile No: \t\t"+ self. mobile_var.get() + "\n") 
        self.txtBox.insert(END, "Book ID: \t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Book Title: \t\t"+ self.booktitle_var.get() + "\n") 
        self.txtBox.insert(END, "Auther: \t\t"+ self.auther_var.get() + "\n")
        self.txtBox.insert(END, "DateBorrowed: \t\t"+ self.dateborrowed_var.get()+ "\n") 
        self.txtBox.insert(END, "DateDue: \t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "DaysOnBook: \t\t"+ self.daysonbook.get() + "\n")
        self.txtBox.insert(END, "LateRateFine: \t\t"+ self. lateratefine_var.get() + "\n")
        self.txtBox.insert(END, "DateOverDue: \t\t"+ self.dateoverdue.get() + "\n")
        self.txtBox.insert(END, "FinallPrice: \t\t"+ self.finallprice.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set("'"),
        self.address2_var.set(""), 
        self.postcode_var.set(""),
        self.mobile_var.set(""), 
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set("'"),
        self.daysonbook.set(""),
        self.lateratefine_var.set(""),
        self.dateoverdue.set(""),
        self.finallprice.set("")
        self.txtBox.delete("1.0", END) 


    def iexit(self):
        iexit=tkinter.messagebox.askyesno("library mangement system","do you want to exit")
        if iexit>0:
            self.root.destroy()
            return
    
    def update(self):
        conn=mysql.connector.connect( host="localhost",user="root",password="anuj0748",database="data")
        my_cursor=conn.cursor()
        my_cursor.execute("update libray set Member=%s,prn_no=%s,id=%s,firstName=%s,last_name=%s,address_1=%s,address_2=%s,post_id=%s,mobile_no=%s,book_id=%s,book_title=%s,author=%s,date_borrowed=%s,date_due=%s,days=%s,last_return_fine=%s,date_overdue=%s,final_price=%s where prn_no=%s",(
                                                                                                                                        self.member_var.get(),
                                                                                                                                        self.id_var.get(),
                                                                                                                                        self.firstname_var.get(),
                                                                                                                                        self.lastname_var.get(),
                                                                                                                                        self.address1_var.get(),
                                                                                                                                        self.address2_var.get(),
                                                                                                                                        self.postcode_var.get(),
                                                                                                                                        self.mobile_var.get(),
                                                                                                                                        self.bookid_var.get(),
                                                                                                                                        self.booktitle_var.get(),
                                                                                                                                        self.auther_var.get(),
                                                                                                                                        self.dateborrowed_var.get(),
                                                                                                                                        self.datedue_var.get(),
                                                                                                                                        self.daysonbook.get(),
                                                                                                                                        self.lateratefine_var.get(),
                                                                                                                                        self.dateoverdue.get(),
                                                                                                                                        self.finallprice.get(),
                                                                                                                                        self.prn_var.get(),
                                                                                                         ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("sucess","memeber has been updated")

    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the member") 

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="anuj0748",database="data")
            my_cursor=conn.cursor()
            query="delete from libray where prn_no=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been deleted")



if __name__ == "__main__":
     root=Tk()
     obj=librarymanagement(root)
     root.mainloop()
