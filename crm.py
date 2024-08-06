import sqlite3
from tkinter import ttk
import mysql.connector as con
print("Customer Receipt Management")
from tkinter import *
mywin=Tk()
mywin.title("Dreamer Infotech CRM")
mywin.iconbitmap("D logo.ico")
#mywin.attributes("-fullscreen",True)
mywin.geometry("1340x500")
mywin.resizable(1,1)

def search_records_by_date():
    lookup_record=search_entry.get()
    print(lookup_record)
    search.destroy()
    for record in t_tree.get_children():
        t_tree.delete(record)

    conn=sqlite3.connect("crm.db")
    c=conn.cursor()
    c.execute("SELECT rowid,* FROM CUSTOMER WHERE LAST_DATE = ?",(lookup_record,))
    records=c.fetchall()
    for i in records:
        *j,=i
        print(j)
    global count
    count=0
    for record in records:
        if count%2==0:
            t_tree.insert(parent="",index='end',iid=count,text='',
                        values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]),tags=("even_row",))
        else:
            t_tree.insert(parent="", index='end', iid=count, text='',
                        values=(record[0], record[1], record[2], record[3], record[4],record[5],record[6],record[7]), tags=("odd_row",))

        count+=1

def search_record_by_name():
    lookup_record=name_entry.get()
    print(lookup_record)
    name.destroy()
    for record in t_tree.get_children():
        t_tree.delete(record)

    conn=sqlite3.connect("crm.db")
    c=conn.cursor()
    c.execute("SELECT rowid,* FROM CUSTOMER WHERE FIRST_NAME = ?",(lookup_record,))
    records=c.fetchall()
    for i in records:
        *j,=i
        print(j)
    global count
    count=0
    for record in records:
        if count%2==0:
            t_tree.insert(parent="",index='end',iid=count,text='',
                        values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]),tags=("even_row",))
        else:
            t_tree.insert(parent="", index='end', iid=count, text='',
                        values=(record[0], record[1], record[2], record[3], record[4],record[5],record[6],record[7]), tags=("odd_row",))

        count+=1

def lookup_records():
    global search_entry,search
    search=Toplevel(mywin)
    search.title("DREAMER INFOTECH")
    search.geometry("300x200")
    search.iconbitmap("D logo.ico")

    search_frame=LabelFrame(search,text="SEARECH BY DATE ")
    search_frame.pack(padx=10,pady=20)

    search_entry=Entry(search_frame,font=("calibri",18))
    search_entry.pack(padx=20,pady=20)

    search_button=Button(search,text="SEARCH",bg="red",fg="white",command=search_records_by_date)
    search_button.pack(padx=20,pady=20 )

def lookup_record_by_name():
    global name_entry,name
    name=Toplevel(mywin)
    name.title("DREAMER INFOTECH")
    name.geometry("300x200")
    name.iconbitmap("D logo.ico")

    name_frame=LabelFrame(name,text="SEARECH BY NAME ")
    name_frame.pack(padx=10,pady=20)

    name_entry=Entry(name_frame,font=("calibri",18))
    name_entry.pack(padx=20,pady=20)

    name_button=Button(name,text="SEARCH  NAME",bg="red",fg="white",command=search_record_by_name)
    name_button.pack(padx=20,pady=20 )


# DATABASE KA KAM
conn=sqlite3.connect("crm.db")
curr=conn.cursor()
curr.execute("""
CREATE TABLE if not exists CUSTOMER(
FIRST_NAME TEXT,
LAST_NAME TEXT,
ADDRESS TEXT,
MOBILE TEXT,
FIRST_DATE TEXT,
LAST_DATE TEXT,
STATUS TEXT
)
""")
conn.commit()



# data=[
#     [1,"dev","a","b","c","d","e","f"],
#     [2,"dev","a","b","c","d","e","f"],
#     [4,"dev","a","b","c","d","e","f"],
# ]

# for record in data:
#     curr.execute("INSERT INTO CUSTOMER VALUES(:ID, :FIRST_NAME, :LAST_NAME, :ADDRESS, :MOBILE, :FIRST_DATE, :LAST_DATE, :STATUS)",
#     {
#         "ID":record[0],
#         "FIRST_NAME": record[1],
#         "LAST_NAME": record[2],
#         "ADDRESS": record[3],
#         "MOBILE":record[4],
#         "FIRST_DATE": record[5],
#         "LAST_DATE": record[6],
#         "STATUS": record[7]
#     }
#     )
# conn.commit()
# conn.close() 


def query_database():
    conn=sqlite3.connect("crm.db")
    c=conn.cursor()
    c.execute("SELECT rowid,* FROM CUSTOMER")
    records=c.fetchall()
    for i in records:
        *j,=i
        print(j)
    global count
    count=0
    for record in records:
        if count%2==0:
            t_tree.insert(parent="",index='end',iid=count,text='',
                        values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7]),tags=("even_row",))
        else:
            t_tree.insert(parent="", index='end', iid=count, text='',
                        values=(record[0], record[1], record[2], record[3], record[4],record[5],record[6],record[7]), tags=("odd_row",))

        count+=1
    conn.commit()
    conn.close()

# styling

mystyle=ttk.Style()
mystyle.theme_use('clam')
mystyle.configure("Treeview",
                  background="teal",
                  foreground="black",
                  rowhieght=100,
                  font=("calibri",13),
                  fieldbackground="black")


t_frame=Frame(mywin)
t_frame.pack(pady=10)



t_tree=ttk.Treeview(t_frame)
t_tree.pack()

t_tree['columns']=("ID","FIRST NAME","LAST NAME","ADDRESS","MOBILE","VISIT DATE","FOLLOWUP DATE","STATUS" )
t_tree.column("#0",width=0,stretch=NO)
t_tree.column("ID",anchor=CENTER,width=50)
t_tree.column("FIRST NAME",anchor=CENTER,width=200)
t_tree.column("LAST NAME",anchor=CENTER,width=200)
t_tree.column("ADDRESS",anchor=CENTER,width=200)
t_tree.column("MOBILE",anchor=CENTER,width=200,)
t_tree.column("VISIT DATE",anchor=CENTER,width=150)
t_tree.column("FOLLOWUP DATE",anchor=CENTER,width=150,)
t_tree.column("STATUS",anchor=CENTER,width=50)


# HEADINGS
t_tree.heading("#0",text="",anchor=CENTER)
t_tree.heading("ID",text="ID",anchor=CENTER )
t_tree.heading("FIRST NAME",text="FIRST NAME",anchor=CENTER )
t_tree.heading("LAST NAME",text="LAST NAME",anchor=CENTER)
t_tree.heading("ADDRESS",text="ADDRESS",anchor=CENTER)
t_tree.heading("MOBILE",text="MOBILE",anchor=CENTER)
t_tree.heading("VISIT DATE",text="VISIT DATE",anchor=CENTER)
t_tree.heading("FOLLOWUP DATE",text="FOLLOWUP DATE",anchor=CENTER)
t_tree.heading("STATUS",text="STATUS",anchor=CENTER)


# DUMMY DATA





t_tree.tag_configure("even_row",background="",foreground="white")
t_tree.tag_configure("odd_row",background="white")




data_frame=LabelFrame(mywin,text="MyRecords")
data_frame.pack(fill="x",expand="yes",padx=20)

id_label=Label(data_frame,text="ID:",font=(15))
id_label.grid(row=0,column=0,padx=10,pady=10)
id_entry=Entry(data_frame,font=(15))
id_entry.grid(row=0,column=1,padx=10,pady=10)

fn_label=Label(data_frame,text="First Name:",font=(15))
fn_label.grid(row=0,column=0,padx=10,pady=10)
fn_entry=Entry(data_frame,font=(15))
fn_entry.grid(row=0,column=1,padx=10,pady=10)

ln_label=Label(data_frame,text="Last Name:",font=(15))
ln_label.grid(row=0,column=2,padx=10,pady=10)
ln_entry=Entry(data_frame,font=(15))
ln_entry.grid(row=0,column=3,padx=10,pady=10)

add_label=Label(data_frame,text="ADDRESS:",font=(15))
add_label.grid(row=1,column=0,padx=10,pady=10)
add_entry=Entry(data_frame,font=(15))
add_entry.grid(row=1,column=1,padx=10,pady=10)

mob_label=Label(data_frame,text="MOB:",font=(15))
mob_label.grid(row=1,column=2,padx=10,pady=10)
mob_entry=Entry(data_frame,font=(15))
mob_entry.grid(row=1,column=3,padx=10,pady=10)

first_date_label=Label(data_frame,text="VISIT DATE",font=(15))
first_date_label.grid(row=1,column=4,padx=10,pady=10)
first_date_entry=Entry(data_frame,font=(15))
first_date_entry.grid(row=1,column=5,padx=10,pady=10)

last_date_label=Label(data_frame,text="FOLLOWUP DATE:",font=(15))
last_date_label.grid(row=1,column=6,padx=10,pady=10)
last_date_entry=Entry(data_frame,font=(15))
last_date_entry.grid(row=1,column=7,padx=10,pady=10)


status_label=Label(data_frame,text="STATUS",font=(15))
status_label.grid(row=0,column=4,padx=10,pady=10)
status_entry=Entry(data_frame,font=(15))
status_entry.grid(row=0,column=5,padx=10,pady=10)
# functions
# clear
def clear_entry():
    id_entry.delete(0, END)
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    add_entry.delete(0, END)
    mob_entry.delete(0, END)
    first_date_entry.delete(0, END)
    last_date_entry.delete(0, END)
    status_entry.delete(0, END)

def select_record(e):
    id_entry.delete(0,END)
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    add_entry.delete(0, END)
    mob_entry.delete(0, END)
    first_date_entry.delete(0,END)
    last_date_entry.delete(0, END)
    status_entry.delete(0,END)

    selected=t_tree.focus()
    values=t_tree.item(selected,"values")

    id_entry.insert(0, values[0])
    fn_entry.insert(0, values[1])
    ln_entry.insert(0, values[2])
    add_entry.insert(0, values[3])
    mob_entry.insert(0, values[4])
    first_date_entry.insert(0, values[5])
    last_date_entry.insert(0, values[6])
    status_entry.insert(0, values[7])

def update_record():
    selected=t_tree.focus()
    t_tree.item(selected,text="",values=(id_entry.get(),fn_entry.get(),ln_entry.get(),add_entry.get(),mob_entry.get(),first_date_entry.get(),last_date_entry.get(),status_entry.get()))
    conn=sqlite3.connect("crm.db")
    c=conn.cursor()
    c.execute("""UPDATE CUSTOMER SET 
    FIRST_NAME=:fname,
    LAST_NAME=:lname,
    ADDRESS=:address,
    MOBILE=:mob,
    FIRST_DATE=:first_date,
    LAST_DATE=:last_date,
    STATUS=:status

    WHERE oid = :oid """,

    {
        "oid":id_entry.get(),
        "fname":fn_entry.get(),
        "lname":ln_entry.get(),
        "address":add_entry.get(),
        "mob":mob_entry.get(),
        "first_date":first_date_entry.get(),
        "last_date":last_date_entry.get(),
        "status":status_entry.get(),
    })

    conn.commit()
    conn.close()

    id_entry.delete(0,END)
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    add_entry.delete(0, END)
    mob_entry.delete(0, END)
    first_date_entry.delete(0,END)
    last_date_entry.delete(0, END)
    status_entry.delete(0,END)

    # selected=t_tree.focus()
    # values=t_tree.item(selected,"values")

    # id_entry.insert(0, values[0])
    # fn_entry.insert(0, values[1])
    # ln_entry.insert(0, values[2])
    # add_entry.insert(0, values[3])
    # mob_entry.insert(0, values[4])
    # first_date_entry.insert(0, values[5])
    # last_date_entry.insert(0, values[6])
    # status_entry.insert(0, values[7])


def add_record():
    conn=sqlite3.connect("crm.db")
    c=conn.cursor()
    c.execute("INSERT INTO  CUSTOMER VALUES(:FIRST_NAME,:LAST_NAME,:ADDRESS,:MOBILE,:FIRST_DATE,:LAST_DATE,:STATUS)",
            {
                # 'ID':id_entry.get(),
                'FIRST_NAME':fn_entry.get(),
                'LAST_NAME':ln_entry.get(),
                'ADDRESS':add_entry.get(),
                'MOBILE':mob_entry.get(),
                'FIRST_DATE':first_date_entry.get(),
                'LAST_DATE':last_date_entry.get(),
                'STATUS':status_entry.get(),
            } ) 
    conn.commit()
    conn.close()

    id_entry.delete(0,END)
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    add_entry.delete(0, END)
    mob_entry.delete(0, END)
    first_date_entry.delete(0,END)
    last_date_entry.delete(0, END)
    status_entry.delete(0,END)

    t_tree.delete(*t_tree.get_children())
    query_database()

    


def delete_one():
    d=t_tree.selection()[0]
    t_tree.delete(d)
    conn=sqlite3.connect("crm.db")
    c=conn.cursor()
    c.execute("DELETE FROM CUSTOMER WHERE oid="+ id_entry.get() ) 
    conn.commit()
    conn.close()
    
# buttons
button_frame=LabelFrame(mywin,text="Operations")
button_frame.pack(fill="x",expand="yes",pady=20,padx=10)

all_button=Button(button_frame,text="RESET", command=query_database,bg="green" ,fg="white",font=(7))
all_button.grid(row=0,column=1,padx=10,pady=10)

add_button=Button(button_frame,text="ADD RECORD",command=add_record,bg="green" ,fg="white",font=(7))
add_button.grid(row=0,column=2,padx=10,pady=10)

update_button=Button(button_frame,text="UPDATE RECORD",command=update_record,bg="orange" ,fg="white",font=(7))
update_button.grid(row=0,column=3,padx=10,pady=10)

delete_button=Button(button_frame,text="DELETE RECORD",command=delete_one,bg="red" ,fg="white",font=(7))
delete_button.grid(row=0,column=4,padx=10,pady=10)



search_by_name_button=Button(button_frame,text="SEARCH BY NAME",command=lookup_record_by_name,bg="MAGENTA" ,fg="white",font=(7))
search_by_name_button.grid(row=0,column=5,padx=10,pady=10)

search_by_date_button=Button(button_frame,text="SEARCH BY DATE",command=lookup_records,bg="BLUE" ,fg="white",font=(7))
search_by_date_button.grid(row=0,column=6,padx=10,pady=10)

select_button=Button(button_frame,text="CLEAR",command=clear_entry,bg="red" ,fg="white",font=(7))
select_button.grid(row=0,column=7,padx=10,pady=10)

t_tree.bind("<ButtonRelease-1>",select_record)


query_database()











mywin.mainloop()