import sqlite3
from tkinter import*
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import datetime

from source import DB
        
db = DB()


class Library :
    def __init__(self,root):
        self.root = root
        self.root.title("Sasiram Library Management System")
        #self.root.geometry("1350x750+0+0")

        width_value=self.root.winfo_screenwidth()
        height_value=self.root.winfo_screenheight()
        self.root.geometry('%dx%d+0+0'%(width_value,height_value))
        self.root.configure(background='powder blue')

#========================================page tab===================================================
        nb = ttk.Notebook(root.master)

        page1 = ttk.Frame(nb)
        page1.pack(fill="both")

        
        page2 = ttk.Frame(nb)
        page2.pack(fill="both")
        #text = ScrolledText(page2)
        #text.pack(expand=1, fill="both")

        page3 = ttk.Frame(nb)
        page3.pack(fill="both")

        nb.add(page1,  text='\tBook Management\t ')
        
        nb.add(page2, text='\tAll Data Records\t')

        nb.add(page3, text='\tAdd Books\t')

#===========================================page tab================================================  
#*******************************************************************************************************************************************************************
#==============================page 1 frame===============================================================================
        MainFrame = Frame(page1, bg='powder blue')
        MainFrame.pack(fill='both')

        TitleFrame = Frame(MainFrame, width=135,padx=20, bd=5, relief=RIDGE)#
        TitleFrame.pack(side=TOP,fill=X)
        self.lblTitle = Label(TitleFrame, width=35, font=('arial',40,'bold'),text="\tLibrary Management System\t", padx=12)
        self.lblTitle.pack()

        DataFrame = Frame(MainFrame, bd=5, width=130, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=TOP,fill=X)

        endFrame =Frame(MainFrame, bd=5,width=135,height=50,padx=20)#,relief=RIDGE
        endFrame.pack(side=BOTTOM,fill='both')# end frame cover last space

        ButtonFrame =Frame(MainFrame, bd=5,width=135,height=50,padx=20,pady=20,relief=RIDGE)#,relief=RIDGE
        ButtonFrame.pack(side=BOTTOM,fill=X)

        FrameDeatail = Frame(MainFrame, bd=5, width=1350, height=90, pady=20, padx=20, relief=RIDGE)#
        FrameDeatail.pack(side=BOTTOM,fill=X)
        


        DataFrameLEFT = LabelFrame(DataFrame,bd=10,width=800,height=300,padx=20,relief=RIDGE, font=('arial',12,'bold'),text="Library Membership Info:")
        DataFrameLEFT.pack(side=LEFT,fill=X)

        DataFrameRight = LabelFrame(DataFrame,bd=10,width=450,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'),text="Book Details:")
        DataFrameRight.pack(side=LEFT,fill=X)

#==============================page 1 frame===============================================================================
          

        def Issued_get_selected_row(event):
            global selected_tuple
            index= self.txtDisplayr.curselection()[0]
            selected_tuple = self.txtDisplayr.get(index)
            Issued_BookID.delete(0,END)
            Issued_BookID.insert(END, selected_tuple[1])
            Issued_BookTitle.delete(0,END)
            Issued_BookTitle.insert(END, selected_tuple[2])
            Issued_Author.delete(0,END)
            Issued_Author.insert(END, selected_tuple[3])
            Issued_BookSTD.delete(0,END)
            Issued_BookSTD.insert(END, selected_tuple[4])
            Issued_BookPrice.delete(0,END)
            Issued_BookPrice.insert(END, selected_tuple[5])

        def Return_get_selected_row(event):
            global selected_tuple
            index= student_record_display.curselection()[0]
            selected_tuple = student_record_display.get(index)
            Issued_MemberType.delete(0,END)
            Issued_MemberType.insert(END, selected_tuple[1])
            Issued_StudentID.delete(0,END)
            Issued_StudentID.insert(END, selected_tuple[2])
            Issued_Name.delete(0,END)
            Issued_Name.insert(END, selected_tuple[3])            
            Issued_Class.delete(0,END)
            Issued_Class.insert(END, selected_tuple[4])            
            Issued_Section.delete(0,END)
            Issued_Section.insert(END, selected_tuple[5])
            Issued_IssuedDate.delete(0,END)
            Issued_IssuedDate.insert(END, selected_tuple[6])
            Issued_ReturnDate.delete(0,END)
            Issued_ReturnDate.insert(END, selected_tuple[7])                      
            Issued_BookID.delete(0,END)
            Issued_BookID.insert(END, selected_tuple[8])
            Issued_BookTitle.delete(0,END)
            Issued_BookTitle.insert(END, selected_tuple[9])
            Issued_Author.delete(0,END)
            Issued_Author.insert(END, selected_tuple[10])
            Issued_BookSTD.delete(0,END)
            Issued_BookSTD.insert(END, selected_tuple[11])
            Issued_BookPrice.delete(0,END)
            Issued_BookPrice.insert(END, selected_tuple[12])
            Issued_Return.delete(0,END)
            Issued_Return.insert(END, selected_tuple[13])
            
#==============================WIDGE============Library Membership Info===================================================================
        MemberType_issued= StringVar()
        StudentID_issued= StringVar()
        Name_issued= StringVar()
        Class_issued= StringVar()
        Section_issued= StringVar()
        IssuedDate_issued= StringVar()
        ReturnDate_issued= StringVar()
        BookID_issued= StringVar()
        BookTitle_issued= StringVar()
        Author_issued= StringVar()
        BookSTD_issued= StringVar()
        BookPrice_issued= StringVar()
        Return_issued= StringVar()




        Issued_MemberType= Label(DataFrameLEFT,font=('arial',12,'bold'), text="member type", padx=2, pady=2)
        Issued_MemberType.grid(row=0, column=0, sticky=W)
        Issued_MemberType = ttk.Combobox(DataFrameLEFT, font=('arial', 12,'bold'),width=23, textvariable=MemberType_issued)#state='readonly',
        Issued_MemberType['value']=('student','Lecturer','Admin Staff')
        Issued_MemberType.current(0)
        Issued_MemberType.grid(row=0,column=1)

        Issued_StudentID = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Student ID", padx=2, pady=2)
        Issued_StudentID.grid(row=1, column=0, sticky=W)
        Issued_StudentID = Entry(DataFrameLEFT, font=('arial',12,'bold'),width=25, textvariable=StudentID_issued)
        Issued_StudentID.grid(row=1, column=1)

        Issued_Name = Label(DataFrameLEFT,font=('arial',12,'bold'), text="Name", padx=2, pady=2)
        Issued_Name.grid(row=2, column=0, sticky=W)
        Issued_Name = Entry(DataFrameLEFT, font=('arial',12,'bold'),width=25, textvariable=Name_issued)
        Issued_Name.grid(row=2, column=1)

        Issued_Class = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Class", padx=2, pady=2)
        Issued_Class.grid(row=3, column=0, sticky=W)
        Issued_Class = Entry(DataFrameLEFT, font=('arial',12,'bold'),width=25, textvariable=Class_issued)
        Issued_Class.grid(row=3, column=1)

        Issued_Section = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Section", padx=2, pady=2)
        Issued_Section.grid(row=4, column=0, sticky=W)
        Issued_Section = Entry(DataFrameLEFT, font=('arial',12,'bold'),width=25, textvariable=Section_issued)
        Issued_Section.grid(row=4, column=1)
        

        #date 
        date_now= datetime.datetime.now()
        date_seven=(datetime.datetime.now() + datetime.timedelta(days=7))

        Issued_IssuedDate = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Issued Date", padx=2, pady=2)
        Issued_IssuedDate.grid(row=5, column=0, sticky=W)
        Issued_IssuedDate = ttk.Combobox(DataFrameLEFT, font=('arial',12,'bold'),width=23, textvariable=IssuedDate_issued)
        Issued_IssuedDate['value']=(date_now,date_now)
        Issued_IssuedDate.current(0)
        Issued_IssuedDate.grid(row=5, column=1)


        Issued_ReturnDate = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Return Date", padx=2, pady=2)
        Issued_ReturnDate.grid(row=6, column=0, sticky=W)
        Issued_ReturnDate = ttk.Combobox(DataFrameLEFT, font=('arial',12,'bold'),width=23, textvariable=ReturnDate_issued)
        Issued_ReturnDate['value']=(date_seven,date_seven)
        Issued_ReturnDate.current(0)
        Issued_ReturnDate.grid(row=6, column=1)

        
        Issued_BookID = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Book ID", padx=2, pady=2)
        Issued_BookID.grid(row=0, column=2, sticky=W)
        Issued_BookID = Entry(DataFrameLEFT, font=('arial',12,'bold'),width=25, textvariable=BookID_issued)
        Issued_BookID.grid(row=0, column=3)

        Issued_BookTitle = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Book Title", padx=2, pady=2)
        Issued_BookTitle.grid(row=1, column=2, sticky=W)
        Issued_BookTitle = Entry(DataFrameLEFT, font=('arial',12,'bold'),width=25, textvariable=BookTitle_issued)
        Issued_BookTitle.grid(row=1, column=3)

        Issued_Author = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Author", padx=2, pady=2)
        Issued_Author.grid(row=2, column=2, sticky=W)
        Issued_Author = Entry(DataFrameLEFT, font=('arial',12,'bold'),width=25, textvariable=Author_issued)
        Issued_Author.grid(row=2, column=3)

        Issued_BookSTD = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Book std ", padx=2, pady=2)
        Issued_BookSTD.grid(row=3, column=2, sticky=W)
        Issued_BookSTD = Entry(DataFrameLEFT, font=('arial',12,'bold'),width=25, textvariable=BookSTD_issued)
        Issued_BookSTD.grid(row=3, column=3)

        Issued_BookPrice= Label(DataFrameLEFT, font=('arial',12,'bold'), text="Book price", padx=2, pady=2)
        Issued_BookPrice.grid(row=4, column=2, sticky=W)
        Issued_BookPrice = Entry(DataFrameLEFT, font=('arial',12,'bold'),width=25, textvariable=BookPrice_issued)
        Issued_BookPrice.grid(row=4, column=3)

        Issued_Return = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Return     ",bg="red", padx=2, pady=2)
        Issued_Return.grid(row=5, column=2, sticky=W)
        Issued_Return = ttk.Combobox(DataFrameLEFT, font=('arial',12,'bold'),width=23, textvariable=Return_issued)
        Issued_Return['value']=('NO','YES')
        Issued_Return.current(0)
        Issued_Return.grid(row=5, column=3)



       #==============================WIDGE============Library Membership Info===================================================================

        #==============================Right WIDGE============
         #==============================List box============
        self.txtDisplayr=Listbox(DataFrameRight,font=('arial',12,'bold'),width=50,height=11)#,padx=8,pady=20
        self.txtDisplayr.bind('<<ListboxSelect>>', Issued_get_selected_row)
        self.txtDisplayr.grid(row=0, column=0)
        
        scrollbar_10 = Scrollbar(DataFrameRight) #Scrollbar
        scrollbar_10.grid(row=0,column=1, sticky='ns')

        self.txtDisplayr.configure(yscrollcommand=scrollbar_10.set)
        scrollbar_10.configure(command=self.txtDisplayr.yview)

        scrollbar_11 = Scrollbar(DataFrameRight, orient=HORIZONTAL) #Scrollbar
        scrollbar_11.grid(row=1,column=0, sticky='ew')

        self.txtDisplayr.configure(xscrollcommand=scrollbar_11.set)
        scrollbar_11.configure(command=self.txtDisplayr.xview)


        for row in db.books():#disply books details
                self.txtDisplayr.insert(0, row)



                

        #==============================List box============
        #==============================Right WIDGE============

        

        #==============================list all details===================================================================
        student_record_display=Listbox(FrameDeatail,font=('arial',12,'bold'),width=141,height=7)
        student_record_display.bind('<<ListboxSelect>>', Return_get_selected_row)
        student_record_display.grid(row=1, column=0)

        scrollbar_12 = Scrollbar(FrameDeatail) #Scrollbar
        scrollbar_12.grid(row=1,column=1, sticky='ns')
        
        student_record_display.configure(yscrollcommand=scrollbar_12.set)
        scrollbar_12.configure(command=student_record_display.xview)
        #==============================list===================================================================
        def save_issued():
            add_issued_command()
            tkinter.messagebox.showinfo("Student Detail", "library Records Save Successfully")

                    
        def add_issued_command():
            db.insert2(MemberType_issued.get(),StudentID_issued.get(),Name_issued.get(),Class_issued.get(),Section_issued.get(),IssuedDate_issued.get(),ReturnDate_issued.get(),BookID_issued.get(),BookTitle_issued.get(),Author_issued.get(),BookSTD_issued.get(),BookPrice_issued.get(),Return_issued.get())
            student_record_display.delete(0,END)
            student_record_display.insert(END, (MemberType_issued.get(),StudentID_issued.get(),Name_issued.get(),Class_issued.get(),Section_issued.get(),IssuedDate_issued.get(),ReturnDate_issued.get(),BookID_issued.get(),BookTitle_issued.get(),Author_issued.get(),BookSTD_issued.get(),BookPrice_issued.get(),Return_issued.get()))            

        def non_return():
            student_record_display.delete(0,END)
            for row in db.STUDENT_RECORD():
                student_record_display.insert(0, row)

        def Reset_issued():
            MemberType_issued.set("")
            StudentID_issued.set("")
            Name_issued.set("")
            Class_issued.set("")
            Section_issued.set("")
            IssuedDate_issued.set("")
            ReturnDate_issued.set("")
            BookID_issued.set("")
            BookTitle_issued.set("")
            Author_issued.set("")
            BookSTD_issued.set("")
            BookPrice_issued.set("")
            Return_issued.set("")

        def Book_Returnd(): #update book
            db.update2(selected_tuple[0],Return_issued.get())
            tkinter.messagebox.showinfo("Student Detail", "Update Records Successfully")
            

        def search_command_issued():
            student_record_display.delete(0, END)
            for row in db.search2(Return_issued.get()):
                student_record_display.insert(END,row)


        #==============================Button===================================================================
        ButSave=Button(DataFrameLEFT, text='SAVE',font=('Roboto',11,'bold'), bg='powder blue',width=9,bd=6, padx=12,command=save_issued)
        ButSave.grid(row=6, column=3)
        

        
        self.btnDIsplayData=Button(ButtonFrame, text='display data',font=('arial',12,'bold'),width=30,bd=4,command=non_return)
        self.btnDIsplayData.grid(row=0,column=0)

        self.btnDelete=Button(ButtonFrame, text='Book Returnd',font=('arial',12,'bold'),width=30,bd=4,command=Book_Returnd)
        self.btnDelete.grid(row=0,column=1)

        self.btnReset=Button(ButtonFrame, text='Reset',font=('arial',12,'bold'),width=30,bd=4,command=Reset_issued)
        self.btnReset.grid(row=0,column=2)

        self.btnExit=Button(ButtonFrame, text='Exit',font=('arial',12,'bold'),width=30,bd=4, command=self.root.destroy)#search_command_issued
        self.btnExit.grid(row=0,column=3)
        #==============================Button===================================================================
#===========================================page 1 frame =====================================================
#*******************************************************************************************************************************************************************
        self.tree = ttk.Treeview(page2)
        self.tree["columns"]=("Member_type", "Student_ID", "Name", "Class", "Section", "Issue_Date","Return_Date","Book_ID","Book_Title","Author","Book_Std","Book_Price","Return")
        self.tree.column("Member_type", width=100 )
        self.tree.column("Student_ID", width=100)
        self.tree.column("Name", width=100)
        self.tree.column("Class", width=50)
        self.tree.column("Section", width=50)
        self.tree.column("Issue_Date", width=100)
        self.tree.column("Return_Date", width=100 )
        self.tree.column("Book_ID", width=50)
        self.tree.column("Book_Title", width=100)
        self.tree.column("Author", width=100)
        self.tree.column("Book_Std", width=50)
        self.tree.column("Book_Price", width=100)
        self.tree.column("Return", width=100)
        ###############################
        self.tree.heading("Member_type", text="Member type")
        self.tree.heading("Student_ID", text="Student ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Class", text="Class")
        self.tree.heading("Section", text="Section")
        self.tree.heading("Issue_Date", text="Issue Date")
        self.tree.heading("Return_Date", text="Return Date")
        self.tree.heading("Book_ID", text="Book ID")
        self.tree.heading("Book_Title", text="Book Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Book_Std", text="Book STD")
        self.tree.heading("Book_Price", text="Book Price")
        self.tree.heading("Return", text="Return")

        #################################


        

        for row in db.STUDENT_RECORD():
            self.tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]))

   
        self.tree.pack(fill='both')        
#*******************************************************************************************************************************************************************
#===========================================page 3 frame =====================================================
      
 #-------------------------------------------------- 
        MainFrame = Frame(page3, bg='powder blue')
        MainFrame.pack(fill='both')

        TitleFrame = Frame(MainFrame, width=135,padx=20,relief=RIDGE, bd=5)#
        TitleFrame.pack(side=TOP,fill=X)
        self.lblTitle = Label(TitleFrame, width=35, font=('arial',25,'bold'),text="\t Library Management System  \t", padx=12)
        self.lblTitle.pack()


        Frame_2 = Frame(page3, width=135,relief=RIDGE,bd=5)#,padx=5
        Frame_2.pack(side=TOP,fill='both')        
 #-------------------------------------------------- 

        DetailsFrame1 = Frame(Frame_2, width=350,height=750,padx=12, bg='powder blue', bd=2)
        DetailsFrame1.pack(side=LEFT, fill=Y)# fill=X,, expand=YES ,anchor=W,

        DetailsFrame1_title = Frame(DetailsFrame1, width=350,height=50,padx=12, bg='powder blue', bd=2)
        DetailsFrame1_title.pack(fill=X)
        

        DetailsFrame = Frame(DetailsFrame1, width=350,height=750,padx=12, bg='powder blue', bd=2)
        DetailsFrame.pack(side=LEFT, fill=Y)#, expand=YES, anchor=W,
        LblTitle = Label(DetailsFrame1_title, width=27, font=('Roboto',18,'bold'),text=" Book Details ", bg='cadet blue', padx=8)
        LblTitle.pack( fill=X)
        
        
        TitleFrame = Frame(Frame_2, width=100,padx=15, bg='green', bd=6)
        TitleFrame.pack(side=TOP, fill=X)
        LblTitle = Label(TitleFrame, width=72, font=('Roboto',16,'bold'),text=" Books Details ", bg='powder blue', padx=8)
        LblTitle.grid()

        MiddleFrame=Frame(Frame_2, width=1350,height=600, bd=6,bg='orange')
        MiddleFrame.pack(side=TOP, fill=X)#anchor=W, 
        

        ButtonFrame =Frame(Frame_2, bd=20,width=1350,height=50,padx=20)
        ButtonFrame.pack(side=TOP, fill=X)#, anchor=W,

 #--------------------------------------------------   

        
        def get_selected_row(event):
            global selected_tuple
            index= Display.curselection()[0]
            selected_tuple = Display.get(index)
            Name.delete(0,END)
            Name.insert(END, selected_tuple[1])
            FatherName.delete(0,END)
            FatherName.insert(END, selected_tuple[2])
            Occuption.delete(0,END)
            Occuption.insert(END, selected_tuple[3])
            Address1.delete(0,END)
            Address1.insert(END, selected_tuple[4])
            Address2.delete(0,END)
            Address2.insert(END, selected_tuple[5])
            PostCode.delete(0,END)
            PostCode.insert(END, selected_tuple[6])


            
#--------------------------------------------------------Middle frame List-------------------------------
        Display=Listbox(MiddleFrame, font=('Roboto',16,'bold'),width=70,height=15,background='#f0f0ff')#,padx=2,pady=4
        Display.bind('<<ListboxSelect>>', get_selected_row)
        Display.grid(row=0, column=0)
        

        scrollbar1 = Scrollbar(MiddleFrame) #Scrollbar #,bg="red"
        scrollbar1.grid(row=0,column=1, sticky='ns')

        Display.configure(yscrollcommand=scrollbar1.set)
        scrollbar1.configure(command=Display.yview)

        scrollbar2 = Scrollbar(MiddleFrame, orient=HORIZONTAL) #Scrollbar
        scrollbar2.grid(row=1,column=0, sticky='ew')

        Display.configure(xscrollcommand=scrollbar2.set)
        scrollbar2.configure(command=Display.xview)

#--------------------------------------------------------DeatialsFrame-------------------------------
        BookID_text= StringVar()
        BookTitle_text= StringVar()
        Author_text= StringVar()
        BookSTD_text= StringVar()
        BookPrice_text= StringVar()
        Date_text= StringVar()

        
        Name = Label(DetailsFrame, font=('Roboto',18,'bold'), text="Book ID", bg='powder blue', padx=2, pady=8)
        Name.grid(row=0, column=0, sticky=W)
        Name = Entry(DetailsFrame, font=('Roboto',16,'bold'),width=22, textvariable=BookID_text)
        Name.grid(row=0, column=1)
        
        FatherName = Label(DetailsFrame, font=('Roboto',18,'bold'), text="Book Title", bg='powder blue', padx=2, pady=8)
        FatherName.grid(row=1, column=0, sticky=W)
        FatherName = Entry(DetailsFrame, font=('Roboto',16,'bold'),width=22, textvariable=BookTitle_text)
        FatherName.grid(row=1, column=1)

        Occuption = Label(DetailsFrame, font=('Roboto',18,'bold'), text="Author", bg='powder blue', padx=2, pady=8)
        Occuption.grid(row=2, column=0, sticky=W)
        Occuption = Entry(DetailsFrame, font=('Roboto',16,'bold'),width=22, textvariable=Author_text)
        Occuption.grid(row=2, column=1)

        Address1 = Label(DetailsFrame, font=('Roboto',18,'bold'), text="Book STD", bg='powder blue', padx=2, pady=8)
        Address1.grid(row=3, column=0, sticky=W)

        Address1 = Entry(DetailsFrame, font=('Roboto',16,'bold'),width=22, textvariable=BookSTD_text)
        Address1.grid(row=3, column=1)
        
        #PlaceAss = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Placement Assistance:", padx=2, pady=2)
        #PlaceAss.grid(row=4, column=2, sticky=W)
        #Address1 = ttk.Combobox(DetailsFrame, font=('Roboto', 15,'bold'),width=23, textvariable=add1_text)#,state='readonly'
        #Address1['value']=('STD 1','STD 2 ','STD 3 ','STD 4 ','STD 5 ','STD 6 ','STD 7 ','STD 8 ','STD 9 ','STD 10 ','STD 11 ','STD 12 ','OTHER')
        #Address1.current(0)
        #Address1.grid(row=3,column=1)
        

        Address2 = Label(DetailsFrame, font=('Roboto',18,'bold'), text="Book Price", bg='powder blue', padx=2, pady=8)
        Address2.grid(row=4, column=0, sticky=W)
        Address2 = Entry(DetailsFrame, font=('Roboto',16,'bold'),width=22, textvariable=BookPrice_text)
        Address2.grid(row=4, column=1)

        PostCode = Label(DetailsFrame, font=('Roboto',18,'bold'), text="Date", bg='powder blue', padx=2, pady=8)
        PostCode.grid(row=5, column=0, sticky=W)
        PostCode = Entry(DetailsFrame, font=('Roboto',16,'bold'),width=22, textvariable=Date_text)
        PostCode.grid(row=5, column=1)
    
 


        
#-----------------------------------------

        def Reset():
            BookID_text.set("")
            BookTitle_text.set("")
            Author_text.set("")
            BookSTD_text.set("")
            BookPrice_text.set("")
            Date_text.set("")





        def view_command():
            Display.delete(0, END)
            for row in db.books():
                Display.insert(0, row)#END

        def search_command():
            Display.delete(0, END)
            for row in db.search1(BookSTD_text.get()):
                Display.insert(END,row)


        def add_command():
            db.insert1(BookID_text.get(), BookTitle_text.get(),Author_text.get(),BookSTD_text.get(),BookPrice_text.get(),Date_text.get())
            Display.delete(0,END)
            Display.insert(END, (BookID_text.get(), BookTitle_text.get(),Author_text.get(),BookSTD_text.get(),BookPrice_text.get(),Date_text.get()))

        def delete_command():
            db.delete1(selected_tuple[0])

        def update_command():
            db.update1(selected_tuple[0], BookID_text.get(), BookTitle_text.get(),Author_text.get(),BookSTD_text.get(),BookPrice_text.get(),Date_text.get())
     

#-------------------------------------------------------------Buttons-----------------------------------------------------------------------------------
        ButSave=Button(DetailsFrame, text='SAVE',font=('Roboto',11,'bold'), bg='powder blue',width=9,bd=6, padx=12,command=add_command)
        ButSave.grid(row=6, column=1)

     
        BtnDelete=Button(ButtonFrame, text='LIST',font=('Roboto',11,'bold'), bg='powder blue',width=9,bd=6, padx=12,command=view_command)
        BtnDelete.pack(side=LEFT)#grid(row=0,column=1)

        BtnDelete=Button(ButtonFrame, text='UPDATE',font=('Roboto',11,'bold'), bg='powder blue',width=9,bd=6, padx=12,command=update_command)
        BtnDelete.pack(side=LEFT)#grid(row=0,column=2)

        BtnSearch=Button(ButtonFrame, text='SEARCH STD',font=('Roboto',11,'bold'), bg='powder blue',width=9,bd=6, padx=12,command=search_command)
        BtnSearch.pack(side=LEFT)#grid(row=0,column=3)

        self.btnReset=Button(ButtonFrame, text='RESET',font=('Roboto',11,'bold'), bg='powder blue',width=9,bd=6, padx=12,command=Reset)
        self.btnReset.pack(side=LEFT)#grid(row=0,column=4)

        BtnDelete=Button(ButtonFrame, text='DELETE',font=('Roboto',11,'bold'), bg='powder blue',width=9,bd=6, padx=12,command=delete_command)
        BtnDelete.pack(side=LEFT)#grid(row=0,column=5)         

        self.btnExit=Button(ButtonFrame, text='EXIT',font=('Roboto',11,'bold'), bg='powder blue',width=9,bd=6, padx=12, command=self.root.destroy)
        self.btnExit.pack(side=LEFT)#grid(row=0,column=6)
 
#===========================================page 3 frame =====================================================
#******************************************************************************************************************************************************************
      
        nb.pack(expand=1, fill="both")
        
if __name__=='__main__':
    root=Tk()
    application = Library(root)
    root.mainloop()
