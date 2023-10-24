import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class Employee:
    def __init__(self,root):
      self.root=root 
      self.root.geometry("1530x790+0+0")
      self.root.title('Employee mangaement System')
      #variable
      self.var_dep=StringVar()
      self.var_name=StringVar()
      self.var_designition=StringVar()
      self.var_email=StringVar()
      self.var_address=StringVar()
      self.var_married=StringVar()
      self.var_dob=StringVar()
      self.var_doj=StringVar()
      self.var_idproofcomb=StringVar()
      self.var_idproof=StringVar()
      self.var_gender=StringVar()
      self.var_phone=StringVar()
      self.var_country=StringVar()
      self.var_salary=StringVar()






      lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('time new roman',37,'bold'),fg='darkblue',bg='white')
      lbl_title.place(x=0,y=0,width=1530,height=50)

      img_logo=Image.open(r"C:\Users\DELL\OneDrive\Desktop\employee management\emp image\emplogo2.jpg")
      img_logo=img_logo.resize((50,50),Image.Resampling.LANCZOS)
      self.photo_logo=ImageTk.PhotoImage(img_logo)

      self.logo=Label(self.root,image=self.photo_logo)
      self.logo.place(x=270,y=0,width=60,height=60)

      #Image frame

      img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
      img_frame.place(x=0,y=50,width=1530,height=160)

      #1st image
      img1=Image.open(r"C:\Users\DELL\OneDrive\Desktop\employee management\emp image\emp1.jpg")
      img1=img1.resize((540,160),Image.Resampling.LANCZOS)
      self.photo1=ImageTk.PhotoImage(img1)
      
      self.log1=Label(img_frame,image=self.photo1)
      self.log1.place(x=0,y=0,width=540,height=160)

      


      #2nd image

      img2=Image.open(r"C:\Users\DELL\OneDrive\Desktop\employee management\emp image\emp2.jpg")
      img2=img2.resize((540,160),Image.Resampling.LANCZOS)
      self.photo2=ImageTk.PhotoImage(img2)
      
      self.log2=Label(img_frame,image=self.photo2)
      self.log2.place(x=420,y=0,width=540,height=160)

      #3rd image
      img3=Image.open(r"C:\Users\DELL\OneDrive\Desktop\employee management\emp image\emp3.jpg")
      img3=img3.resize((540,160),Image.Resampling.LANCZOS)
      self.photo3=ImageTk.PhotoImage(img3)
    
      self.log3=Label(img_frame,image=self.photo3)
      self.log3.place(x=960,y=0,width=540,height=160)

      #main frame
       
      Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
      Main_frame.place(x=10,y=220,width=1500,height=560)      

      #upper frame

      upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Employee Information',font=('time new roman',11,'bold'),fg='red',bg='white')
      upper_frame.place(x=10,y=10,width=1480,height=270)      

      #Lables and Entry fields

      #department
      lbl_dep=Label(upper_frame,text='Department:',font=('arial',11,'bold'),bg='white')
      lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
      combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',11,'bold'),width=17,state='readonly')
      combo_dep['value']=('Select Department','HR','software Engineer','Manager')
      combo_dep.current(0)
      combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
     
      #Name

      lbl_Name=Label(upper_frame,text='Name:',font=('arial',12,'bold'),bg='white')
      lbl_Name.grid(row=0,column=2,padx=2,pady=7,sticky=W)

      txt_Name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("arial",11,"bold"))
      txt_Name.grid(row=0,column=3,padx=2,pady=7)

      #Designition
      
      lbl_Designition=Label(upper_frame,text='Designition:',font=('arial',12,'bold'),bg='white')
      lbl_Designition.grid(row=1,column=0,padx=2,pady=7,sticky=W)

      txt_Designition=ttk.Entry(upper_frame,textvariable=self.var_designition,width=22,font=("arial",11,"bold"))
      txt_Designition.grid(row=1,column=1,padx=2,pady=7,sticky=W)

      #Email
      lbl_email=Label(upper_frame,text='Email:',font=('arial',12,'bold'),bg='white')
      lbl_email.grid(row=1,column=2,padx=2,pady=7,sticky=W)

      txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=("arial",11,"bold"))
      txt_email.grid(row=1,column=3,padx=2,pady=7,sticky=W)
      
      #Address
      lbl_address=Label(upper_frame,text='Address:',font=('arial',12,'bold'),bg='white')
      lbl_address.grid(row=2,column=0,padx=2,pady=7,sticky=W)

      txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=("arial",11,"bold"))
      txt_address.grid(row=2,column=1,padx=2,pady=7,sticky=W)

      #Married
      lbl_married=Label(upper_frame,text='Married Status:',font=('arial',12,'bold'),bg='white')
      lbl_married.grid(row=2,column=2,padx=2,pady=7,sticky=W)


      com_txt_married=ttk.Combobox(upper_frame,font=('arial',12,'bold'),width=17,state='readonly')
      com_txt_married['value']=("Select","Married","Unmarried")
      com_txt_married.current(0)
      com_txt_married.grid(row=2,column=3,sticky=W,padx=2,pady=7)  

      #Dob
      lbl_dob=Label(upper_frame,text='Date Of Brith:',font=('arial',12,'bold'),bg='white')
      lbl_dob.grid(row=3,column=0,padx=2,pady=7,sticky=W)

      txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=("arial",11,"bold"))
      txt_dob.grid(row=3,column=1,padx=2,pady=7,sticky=W)

      #Doj
      lbl_doj=Label(upper_frame,text='Date Of Joining:',font=('arial',12,'bold'),bg='white')
      lbl_doj.grid(row=3,column=2,padx=2,pady=7,sticky=W)

      txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=("arial",11,"bold"))
      txt_doj.grid(row=3,column=3,padx=2,pady=7,sticky=W)
      #Id Proof
      com_txt_proof=ttk.Combobox(upper_frame,textvariable= self.var_idproofcomb,font=('arial',12,'bold'),width=17,state='readonly')
      com_txt_proof['value']=("Select ID Proof","PAN CARD","ADHAR CARD","DRIVING LICENCE")
      com_txt_proof.current(0)
      com_txt_proof.grid(row=4,column=0,sticky=W,padx=2,pady=7)  
     
      txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=("arial",11,"bold"))
      txt_proof.grid(row=4,column=1,padx=2,pady=7,sticky=W)
      #Gender
      lbl_gender=Label(upper_frame,text='Gender:',font=('arial',12,'bold'),bg='white')
      lbl_gender.grid(row=4,column=2,padx=2,pady=7,sticky=W)

      com_txt_Gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('arial',12,'bold'),width=17,state='readonly')
      com_txt_Gender['value']=("Select","Male","Female","Other")
      com_txt_Gender.current(0)
      com_txt_Gender.grid(row=4,column=3,sticky=W,padx=2,pady=7)  
      
      #Phone
      lbl_phone=Label(upper_frame,text='Contact Detail:',font=('arial',12,'bold'),bg='white')
      lbl_phone.grid(row=0,column=4,padx=2,pady=7,sticky=W)

      txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=("arial",11,"bold"))
      txt_phone.grid(row=0,column=5,padx=2,pady=7,sticky=W)


      #Country

      lbl_country=Label(upper_frame,text='Country:',font=('arial',12,'bold'),bg='white')
      lbl_country.grid(row=1,column=4,padx=2,pady=7,sticky=W)

      txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=("arial",11,"bold"))
      txt_country.grid(row=1,column=5,padx=2,pady=7,sticky=W)

      #CTC
      lbl_CTC=Label(upper_frame,text='Salary(CTC):',font=('arial',12,'bold'),bg='white')
      lbl_CTC.grid(row=2,column=4,padx=2,pady=7,sticky=W)

      txt_CTC=ttk.Entry(upper_frame,textvariable= self.var_salary,width=22,font=("arial",11,"bold"))
      txt_CTC.grid(row=2,column=5,padx=2,pady=7,sticky=W)

      #Image mask

      img_mask=Image.open(r"C:\Users\DELL\OneDrive\Desktop\employee management\emp image\empmask.png")
      img_mask=img_mask.resize((220,220),Image.Resampling.LANCZOS)
      self.photo_mask=ImageTk.PhotoImage(img_mask)
      
      self.log_mask=Label(upper_frame,image=self.photo_mask)
      self.log_mask.place(x=993,y=0,width=210,height=220)

      #Button frame
       
      Button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
      Button_frame.place(x=1168,y=10,width=150,height=175)

      #save
      btn_add=Button(Button_frame,command=self.add_data,text="Save",font=("arial",12,"bold"),width=13,bg="blue",fg="white")
      btn_add.grid(row=0,column=0,padx=1,pady=5)   

      #update 
      btn_Update=Button(Button_frame,command=self.update_data,text="Update",font=("arial",12,"bold"),width=13,bg="blue",fg="white")
      btn_Update.grid(row=1,column=0,padx=1,pady=5)  

      #delete
      btn_Delete=Button(Button_frame,text="Delete",command=self.delete_data,font=("arial",12,"bold"),width=13,bg="blue",fg="white")
      btn_Delete.grid(row=2,column=0,padx=1,pady=5)  

      #clear
      btn_Clear=Button(Button_frame,text="Clear",command=self.reset_data,font=("arial",12,"bold"),width=13,bg="blue",fg="white")
      btn_Clear.grid(row=3,column=0,padx=1,pady=5)  
      
      #down frame
      down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Employee Information Table',font=('time new roman',11,'bold'),fg='red',bg='white')
      down_frame.place(x=10,y=280,width=1480,height=270)   

      #search frame
      search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Employee Information',font=('time new roman',11,'bold'),fg='red',bg='white')
      search_frame.place(x=0,y=0,width=1470,height=60)  

      search_by=Label(search_frame,text="Search By:",font=("arial",12,"bold"),width=13,bg="red",fg="white")
      search_by.grid(row=0,column=0,padx=2,sticky=W)  

      #search
      self.var_com_search=StringVar()
      com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('arial',12,'bold'),width=17,state='readonly')
      com_txt_search['value']=("Select Option","Contact Detail","Name","ID Proof")
      com_txt_search.current(0)
      com_txt_search.grid(row=0,column=1,sticky=W,padx=5)  
      
      self.var_search=StringVar()
      txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
      txt_search.grid(row=0,column=2,padx=5)

      #search button
      btn_search=Button(search_frame,text="Search",command=self.search_data,font=("arial",12,"bold"),width=13,bg="blue",fg="white")
      btn_search.grid(row=0,column=3,padx=5) 
      txt_phone.grid(row=0,column=5,padx=2,pady=7,sticky=W)

      #ShowAll button
      btn_ShowAll=Button(search_frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),width=13,bg="blue",fg="white")
      btn_ShowAll.grid(row=0,column=4,padx=5)  

      #Stay Home button
      stayhome=Label(search_frame,text='Wear a Mask',font=('times new roman',30,'bold'),bg='white')
      stayhome.place(x=920,y=1,width=300,height=30)
      
      #mask logo 2
      img5=Image.open(r"C:\Users\DELL\OneDrive\Desktop\employee management\emp image\empmask.png")
      img5=img5.resize((50,50),Image.Resampling.LANCZOS)
      self.photo5=ImageTk.PhotoImage(img5)

      self.logo=Label(search_frame,image=self.photo5)
      self.logo.place(x=900,y=0,width=50,height=30)

      

      ######################Employee tablee######################################################

      #Table Frame
      table_frame=Frame(down_frame,bd=3,relief=RIDGE,bg='white')
      table_frame.place(x=0,y=60,width=1470,height=170)  

      #scroll bar

      scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
      scroll_y=Scrollbar(table_frame,orient=VERTICAL)

      self.employee_table=ttk.Treeview(table_frame,columns=("dep","name","degi","email","add","married","dob","doj","idproofcomb","idproof","gender","phone","country","salary",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=BOTTOM,fill=Y)

      scroll_x.config(command=self.employee_table.xview)
      scroll_y.config(command=self.employee_table.yview)

      self.employee_table.heading('dep',text='Department')
      self.employee_table.heading('name',text='Name')
      self.employee_table.heading('degi',text='Degignition')
      self.employee_table.heading('email',text='Email')
      self.employee_table.heading('add',text='Address')
      self.employee_table.heading('married',text='Married')
      self.employee_table.heading('dob',text='Date Of Birth')
      self.employee_table.heading('doj',text='Date Of Joining')
      self.employee_table.heading('idproofcomb',text='ID Type')
      self.employee_table.heading('idproof',text='ID Proof')
      self.employee_table.heading('gender',text='Gender')
      self.employee_table.heading('phone',text='Phone')
      self.employee_table.heading('country',text='Country')
      self.employee_table.heading('salary',text='Salary')

      self.employee_table['show']='headings'

      self.employee_table.column('dep',width=80)
      self.employee_table.column('name',width=80) 
      self.employee_table.column('degi',width=80)
      self.employee_table.column('email',width=80) 
      self.employee_table.column('add',width=80)
      self.employee_table.column('married',width=80) 
      self.employee_table.column('dep',width=80)
      self.employee_table.column('dob',width=80)
      self.employee_table.column('doj',width=80)
      self.employee_table.column('idproofcomb',width=80)
      self.employee_table.column('idproof',width=80) 
      self.employee_table.column('gender',width=80)
      self.employee_table.column('phone',width=80)
      self.employee_table.column('country',width=80)
      self.employee_table.column('salary',width=80) 
 
 


      self.employee_table.pack(fill=BOTH,expand=1)
      self.employee_table.bind("<ButtonRelease>",self.get_cursor)
      self.fetch_data()

      #**************Fuction Declartion*************
    def add_data(self):
      if self.var_dep.get()=="" or self.var_email.get()=="":
        messagebox.showerror('Error','All Fields are required' )
      else:
           try:

             conn=mysql.connector.connect(host='localhost',username="root",password='J@yesh1209',database='mydata')
             my_cursor=conn.cursor()
             my_cursor.execute('insert into emp1 value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                 self.var_dep.get(),
                                                 self.var_name.get(),
                                                 self.var_designition.get(),
                                                 self.var_email.get(),
                                                 self.var_address.get(),
                                                 self.var_married.get(),
                                                 self.var_dob.get(),
                                                 self.var_doj.get(),
                                                 self.var_idproofcomb.get(),
                                                 self.var_idproof.get(),
                                                 self.var_gender.get(),
                                                 self.var_phone.get(),
                                                 self.var_country.get(),
                                                 self.var_salary.get()  ))
             conn.commit()
             self.fetch_data()
             conn.close()
             messagebox.showinfo('Success','Employee has been added!',parent=self.root)
           except Exception as es :
            messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
    #fetch Data
    def fetch_data(self):
       conn=mysql.connector.connect(host='localhost',username="root",password='J@yesh1209',database='mydata')
       my_cursor=conn.cursor()
       my_cursor.execute('select * from emp1')
       data=my_cursor.fetchall()
       if len(data)!=0:
        self.employee_table.delete(*self.employee_table.get_children())
        for i in data:
            self.employee_table.insert("",END,values=i) 
        conn.commit()  
       conn.close()

    #Get cursor

    def get_cursor(self,event=""):
      cursor_row=self.employee_table.focus()
      content=self.employee_table.item(cursor_row)
      data=content['values'] 


      self.var_dep.set(data[0])
      self.var_name.set(data[1])
      self.var_designition.set(data[2])
      self.var_email.set(data[3])
      self.var_address.set(data[4])
      self.var_married.set(data[5])  
      self.var_dob.set(data[6])
      self.var_doj.set(data[7])
      self.var_idproofcomb.set(data[8])
      self.var_idproof.set(data[9])
      self.var_gender.set(data[10])
      self.var_phone.set(data[11])
      self.var_country.set(data[12])
      self.var_salary.set(data[13])
      

    def update_data(self):
      if self.var_dep.get()=="" or self.var_email.get()=="":
        messagebox.showerror('Error','All Fields are required' )
      else:
           try:

            update=messagebox.askyesno('Update','Are you sure update this employee data')
            if update>0:
              conn=mysql.connector.connect(host='localhost',username="root",password='J@yesh1209',database='mydata')
              my_cursor=conn.cursor()
              my_cursor.execute('UPDATE emp1 SET Department=%s,Name=%s,Designition=%s,Email=%s,Address=%s,Married=%s,Date Of Brith=%s,Date Of Joining=%s,id_proof_type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where id_proof=%s',(
                                                            
                                                 self.var_dep.get(),
                                                 self.var_name.get(),
                                                 self.var_designition.get(),
                                                 self.var_email.get(),
                                                 self.var_address.get(),
                                                 self.var_married.get(),
                                                 self.var_dob.get(),
                                                 self.var_doj.get(),
                                                 self.var_idproofcomb.get(),
                                                 self.var_gender.get(),
                                                 self.var_phone.get(),
                                                 self.var_country.get(),
                                                 self.var_salary.get(),
                                                 self.var_idproof.get()
                                                  ))   
            else:
              if not update:
                return
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo('Success','Employee Sucessfully updated',parent=self.root)
           except Exception as es:
            messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
     
     #Delete
    def delete_data(self):
      if self.var_idproof.get()=="":
        messagebox.showerror('Error','All Fields are required' )
      else:
        try:
          Delete=messagebox.askyesno('Delete','Are you sure delete this employee',parent=self.root)
          if Delete>0:
             conn=mysql.connector.connect(host='localhost',username="root",password='J@yesh1209',database='mydata')
             my_cursor=conn.cursor()
             sql='delete from emp1 where id_proof=%s'
             value=(self.var_idproof.get(),)
             my_cursor.execute(sql,value)
          else:
            if not Delete:
              return
          conn.commit()
          self.fetch_data()
          conn.close() 
          messagebox.showinfo('Success','Employee Sucessfully Delete',parent=self.root)
        except Exception as es:
            messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
        
      #clear
    def reset_data(self):
      self.var_dep.set("Select Department")
      self.var_name.set("")
      self.var_designition.set("")
      self.var_email.set("")
      self.var_address.set("")
      self.var_married.set("Select")  
      self.var_dob.set("")
      self.var_doj.set("")
      self.var_idproofcomb.set("Select ID Proof")
      self.var_idproof.set("")
      self.var_gender.set("Select")
      self.var_phone.set("")
      self.var_country.set("")
      self.var_salary.set("")

    #search
    def search_data(self):
          if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error','Please select option')
          else:
            try: 
             conn=mysql.connector.connect(host='localhost',username="root",password='J@yesh1209',database='mydata')
             my_cursor=conn.cursor()    
             my_cursor.execute('select * from emp where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
             rows=my_cursor.fetchall()
             if len(rows)!=0:
               self.employee_table.delete(*self.employee_table.get_children())
               for i in rows:
                 self.emplooyee_table.insert("",END,values=i)
             conn.commit
             conn.close()
            except Exception as es:
              messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()



















































