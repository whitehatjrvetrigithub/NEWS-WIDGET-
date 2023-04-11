from tkinter import *
import requests
import json

root = Tk()
root.title("BBC News Update")
root.geometry("900x600")
root.config(bg = "white")

news_title1_lbl = Label(root, font = "arial 15 bold", fg = "blue", bg = "white", wraplength = 900, justify = LEFT)
news_title1_lbl.place(relx = 0.5, rely = 0.05, anchor = CENTER)
news_description1_lbl = Label(root, font = "arial 15 bold", fg = "red", bg = "white", wraplength = 900, justify = LEFT)
news_description1_lbl.place(relx = 0.5, rely = 0.15, anchor = CENTER)

news_title2_lbl = Label(root, font = "arial 15 bold", fg = "blue", bg = "white", wraplength = 900, justify = LEFT)
news_title2_lbl.place(relx = 0.5, rely = 0.25, anchor = CENTER)
news_description2_lbl = Label(root, font = "arial 15 bold", fg = "red", bg = "white", wraplength = 900, justify = LEFT)
news_description2_lbl.place(relx = 0.5, rely = 0.35, anchor = CENTER)

news_title3_lbl = Label(root, font = "arial 15 bold", fg = "blue", bg = "white", wraplength = 900, justify = LEFT)
news_title3_lbl.place(relx = 0.5, rely = 0.45, anchor = CENTER)
news_description3_lbl = Label(root, font = "arial 15 bold", fg = "red", bg = "white", wraplength = 900, justify = LEFT)
news_description3_lbl.place(relx = 0.5, rely = 0.55, anchor = CENTER)

news_title4_lbl = Label(root, font = "arial 15 bold", fg = "blue", bg = "white", wraplength = 900, justify = LEFT)
news_title4_lbl.place(relx = 0.5, rely = 0.65, anchor = CENTER)
news_description4_lbl = Label(root, font = "arial 15 bold", fg = "red", bg = "white", wraplength = 900, justify = LEFT)
news_description4_lbl.place(relx = 0.5, rely = 0.75, anchor = CENTER)

news_title5_lbl = Label(root, font = "arial 15 bold", fg = "blue", bg = "white", wraplength = 900, justify = LEFT)
news_title5_lbl.place(relx = 0.5, rely = 0.85, anchor = CENTER)
news_description5_lbl = Label(root, font = "arial 15 bold", fg = "red", bg = "white", wraplength = 900, justify = LEFT)
news_description5_lbl.place(relx = 0.5, rely = 0.95, anchor = CENTER)

def getNews():
    api_request = requests.get("https://newsapi.org/v1/articles?sourc...")
    api_output_json = json.loads(api_request.content)
    
    news_title1 = api_output_json["articles"][1]["title"]
    news_description1 = api_output_json["articles"][1]["description"]
    
    news_title2 = api_output_json["articles"][3]["title"]
    news_description2 = api_output_json["articles"][3]["description"]
    
    news_title3 = api_output_json["articles"][5]["title"]
    news_description3 = api_output_json["articles"][5]["description"]
    
    news_title4 = api_output_json["articles"][7]["title"]
    news_description4 = api_output_json["articles"][7]["description"]
    
    news_title5 = api_output_json["articles"][9]["title"]
    news_description5 = api_output_json["articles"][9]["description"]
    
    
    news_title1_lbl["text"] = "Title : " + news_title1
    news_description1_lbl["text"] = "Description : " + news_description1
    
    news_title2_lbl["text"] = "Title : " + news_title2
    news_description2_lbl["text"] = "Description : " + news_description2
    
    news_title3_lbl["text"] = "Title : " + news_title3
    news_description3_lbl["text"] = "Description : " + news_description3
    
    news_title4_lbl["text"] = "Title : " + news_title4
    news_description4_lbl["text"] = "Description : " + news_description4
    
    news_title5_lbl["text"] = "Title : " + news_title5
    news_description5_lbl["text"] = "Description : " + news_description5
    
getNews()

root.mainloop()