from tkinter import *
root = Tk()
frame = Frame(root, bg='skyblue')
frame.pack()
scrollbar = Scrollbar(frame)
scrollbar.pack( side = RIGHT, fill = Y )
mylist = Listbox(frame, yscrollcommand = scrollbar.set )
dict={"1":9815869325,"2":9807611250,"3":7310675568,"4":7060874227,"5":7060874229,"6":9807832757,"7":6098765432,"8":9817878597,"9":9844162099,\
      "10":6744541181 }
for item in dict:
    mylist.insert(END,"Key Is : " + str(item))
    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )
mainloop()