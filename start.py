from customtkinter import *
import tkinter as tkinter
from tkinter import font as tik
from shared import tables as tables
from shared import isDB as isDB
import re
import io
import tkinter
from contextlib import redirect_stdout
set_appearance_mode("dark")
import os
import shared
import sys

FONT_CANDIDATES = [
    "Rabar", "Rabar_004", "Rabar_005", "Unikurd", "Rudaw", "Hawar", "Kurdi", 
    "Noto Kufi Arabic", "Scheherazade New", "Amiri", "Lateef", "Noto Sans Arabic", "Noto Naskh Arabic",
    "Vazirmatn", "Vazir","Vazirmatn Black","Vazirmatn Medium", "IRANSansX", "IRANSans", "IranSans", "Yekan Bakh", "IranYekan", 
    "B Yekan+", "B Yekan", "Yekan", "Shabnam", "Sahel", "Samim", "Estedad", "Peyda", 
    "Peyda Black", "Dana", "Morabba", "Morabba Black", "Kalameh", "Kalameh Black", 
    "Doran", "Tanha", "Gandom", "Abar", "Changa", "Lalezar",
    "B Nazanin", "B Titr", "B Mitra", "B Lotus", "B Zar", "B Koodak", "B Roya",
    "B Homa", "B Naskh", "B Kamran", "B Traffic", "B Bardiya", "B Elham", 
    "B Mehr", "B Farnaz", "B Esfehan", "B Soroush", "B Shabnam",
    "Inter", "Roboto", "Open Sans", "Lato", "Montserrat", "Poppins", "Nunito", 
    "Ubuntu", "Raleway", "Oswald", "Fira Sans", "Proxima Nova", "Avenir", 
    "Century Gothic", "Gotham", "Futura", "Gilroy", "Manrope", "DM Sans", 
    "Work Sans", "Source Sans 3", "Source Sans", "Helvetica Neue", "Helvetica", "Calibri", "Noto Sans",
    "Times New Roman", "Georgia", "Garamond", "Baskerville", "Caslon", "Palatino", 
    "Cambria", "Merriweather", "Playfair Display", "Libre Baskerville", "Lora", 
    "Cormorant Garamond", "Crimson Text", "EB Garamond", "Noto Serif",
    "Bebas Neue", "Anton", "Impact", "Bangers", "Abril Fatface", "Archivo Black", 
    "Black Ops One", "League Spartan", "Russo One", "Audiowide", "Orbitron", 
    "Rajdhani", "Michroma", "Cinzel",
    "Pacifico", "Lobster", "Dancing Script", "Great Vibes", "Sacramento", "Allura",
    "Satisfy", "Caveat", "Permanent Marker", "Indie Flower","Arial"
]
MotaghayereBTN = {}
text = isDB()
selectDarss = {}
fontstylelist = {}
test = []
def find_all_fonts(system_fonts, font_list):
    for font in font_list:
        if font in system_fonts:
            test.append(font)
    if not test:
        test.append("Arial")
    return test[0]
class App(CTk):
    def __init__(self):
        super().__init__()
        font_family = find_all_fonts(set(tik.families()), FONT_CANDIDATES)
        if not (os.path.exists(f"{text}/marcodedb.txt") and os.path.exists(f"{text}/FontStyle/setting.txt")):
            self.createDataDB(test)
        self.current_lang = self.get_language()
        self.getFontSize()
        self.totalScore = shared.getMaxScore()
        if "Font" in fontstylelist:
            self.font_family = fontstylelist["Font"][0]
        else:
            self.font_family = font_family
        try:
            self.code = (self.font_family, int(fontstylelist["FontCodeSize"][0] or 15))
        except:
            self.code = (self.font_family, 15)
        try:
            self.code_x2 = (self.font_family, int(fontstylelist["FontCodeSizeX2"][0] or 17))
        except:
            self.code_x2 = (self.font_family,17)
        try:
            self.fontsmall = (self.font_family, int(fontstylelist["FontSmall"][0] or 13))
        except:
            self.fontsmall = (self.font_family,13)
        self.fontsmalluni = (self.font_family,13)
        self.geometry("1300x780")
        self.title("MarCode")
        self.minsize(1100, 650)
        self.configure(fg_color="#e9edf3")
        self.AyaInFixMishe = []
        self.ctkwindow = []
        
        if self.current_lang == "English":
            self.text_align = "left"
            self.text_anchor = "nw"
            self.grid_sticky = "w"
            self.pack_anchor = "nw"
        else:
            self.text_align = "right"
            self.text_anchor = "ne"
            self.grid_sticky = "e"
            self.pack_anchor = "ne"
            
        self.frame_aval = CTkFrame(self, height=64, corner_radius=0, fg_color="#e8823c")
        self.frame_aval.pack(side=TOP, fill="x")
        self.frame_aval.propagate(False)
        
        self.about_btn = CTkButton(master=self.frame_aval, text="?", width=32, height=32, corner_radius=16, fg_color="#242938", hover_color="#3a6ff0", text_color="white", font=self.code, command=self.show_about)
        self.about_btn.pack(side=RIGHT, anchor="center", padx=20)
        
        self.box = CTkComboBox(master=self.frame_aval, values=["English", "فارسی", "کوردی"], command=self.change_language, width=130, height=32, corner_radius=6, fg_color="#242938", border_width=0, border_color="dark_color", button_color="#1b1f2b", button_hover_color="#3a6ff0", text_color="white", dropdown_fg_color="#242938", dropdown_hover_color="#3a6ff0", dropdown_text_color="white", font=self.code, dropdown_font=self.code, justify=CENTER, state="readonly")
        self.box.set(self.current_lang)
        self.box.pack(side=RIGHT, anchor="center", padx=(0, 10))

        self.prograse = CTkFrame(self.frame_aval,width=200,fg_color="transparent")
        self.prograse.pack(side=RIGHT,fill="y", anchor="center",padx=100)
        self.prograse.propagate(False)

        self.emtiaz_label = CTkLabel(self.prograse, text=f"{tables['ui_texts']['YourScore'][self.current_lang]}: 0/{self.totalScore}", font=self.code)
        self.emtiaz_label.pack(side=TOP, anchor="center",pady=5)

        self.prograse_org = CTkProgressBar(self.prograse,120,progress_color="#3a6ff0")
        self.prograse_org.pack(side=BOTTOM, anchor="center",pady=8)
        self.prograse_org.set(0)
        self.marcode = CTkLabel(master=self.frame_aval, text="MarCode", font=self.code)
        self.marcode.place(relx=0.5, rely=0.5, anchor="center")
        
        self.frame_leftINI = CTkFrame(self,width=230,corner_radius=0,fg_color="#1b1f2b")
        self.frame_leftINI.pack(side=LEFT,fill="y")
        self.frame_leftINI.pack_propagate(False)
        
        self.jayecharkhdande = CTkFrame(self.frame_leftINI,height=50,corner_radius=0,fg_color="transparent")
        self.jayecharkhdande.pack(fill="x",anchor="s",side=BOTTOM)
        
        self.frame_chap = CTkScrollableFrame(master=self.frame_leftINI, fg_color="#1b1f2b", corner_radius=0)
        self.frame_chap.pack(side=TOP, fill="both",expand=True)

        self.btn_setting = CTkButton(self.jayecharkhdande,32,32,corner_radius=16,border_spacing=0,fg_color="transparent",hover_color="#1b1f2b",anchor="center",text="⚙️",font=self.code,command=self.setting)
        self.btn_setting.pack(side=LEFT,anchor="nw",pady=10)
        
        self.amozehi_text = CTkLabel(self.frame_chap, text=tables["ui_texts"]["LearningPaths"][self.current_lang], font=self.code_x2)
        self.amozehi_text.pack(side=TOP, anchor="center", pady=5)
        
        for name,value in tables["DarsHa"].items():
            button_text = value["name"][self.current_lang]
            self.button1 = CTkButton(self.frame_chap, height=44, text=button_text, fg_color="#242938", hover_color="#323a4f", font=self.code,command=lambda t=button_text:self.select_category(t))
            self.button1.pack(side=TOP, anchor="center", fill="x", padx=10, pady=4)
            MotaghayereBTN[button_text] = self.button1
            
        self.SamteRastSharh = CTkFrame(self, width=400, fg_color="transparent", corner_radius=0)
        self.SamteRastSharh.pack(side=RIGHT, fill="y")
        self.SamteRastSharh.propagate(False)
        
        self.framesharhedars = CTkScrollableFrame(master=self.SamteRastSharh, width=380, fg_color="#fff4e8", corner_radius=10)
        self.framesharhedars.pack(pady=10)
        self.framesharhedars.grid_columnconfigure(0, weight=1)
        
        self.labelsharehdars = CTkLabel(master=self.framesharhedars, text=tables["ui_texts"]["LessonDesc"][self.current_lang], font=self.code, text_color="black")
        self.labelsharehdars.grid(row=0, column=0, sticky=self.grid_sticky, padx=20, pady=10)
        
        self.labelsharehdars2 = CTkLabel(master=self.framesharhedars, text="",wraplength=350,justify=self.text_align,anchor=self.text_anchor,fg_color="transparent", font=self.code, text_color="black")
        self.labelsharehdars2.grid(row=1, column=0, sticky=self.grid_sticky, padx=20, pady=2)
        
        self.labelsharehdars3 = CTkLabel(master=self.framesharhedars, text="",wraplength=350,justify=self.text_align,anchor=self.text_anchor,fg_color="transparent", font=self.fontsmall, text_color="black")
        self.labelsharehdars3.grid(row=3, column=0, sticky=self.grid_sticky, padx=20, pady=70)
        
        self.editorcode = CTkFrame(master=self, fg_color="#181822", corner_radius=0)
        self.editorcode.pack(side=LEFT, expand=True, fill=BOTH)
        self.editorcode.propagate(False)
        
        self.mozobalaeditcode = CTkFrame(self.editorcode, height=50, corner_radius=0, fg_color="#323a4f")
        self.mozobalaeditcode.pack(side=TOP, fill="x")
        self.mozobalaeditcode.propagate(False)
        
        self.titletext = CTkLabel(master=self.mozobalaeditcode, text="", font=self.code)
        self.titletext.pack(side=RIGHT, padx=10)
        
        self.mozopaeineditcode = CTkFrame(self.editorcode, height=70, corner_radius=0, fg_color="#323a4f")
        self.mozopaeineditcode.pack(side=BOTTOM, fill="x")
        self.mozopaeineditcode.propagate(False)
        
        self.button_container = CTkFrame(self.mozopaeineditcode, fg_color="transparent")
        self.button_container.pack(expand=True)
        
        for i in range(0, 5):
            g = str(i)
            btn_text = tables["ConfigUi"]["TextBTNZirEdtcode"][self.current_lang][g]
            self.btnkar = CTkButton(self.button_container, width=130, font=self.code, fg_color=tables["ConfigUi"]["ColorBTNZirEdtcode"][g], hover_color=tables["ConfigUi"]["HoverColorBTNZirEdtcode"][g], text=btn_text,command=lambda m=btn_text,g=g:self.ClickKard(m,g))
            self.btnkar.pack(side=LEFT, padx=8)
            
        self.ouytput = CTkLabel(self.mozopaeineditcode,font=self.code,text_color="white",text="")
        self.ouytput.pack(side=RIGHT,padx=15)
        
        self.khorojizirBG = CTkFrame(master=self.SamteRastSharh, fg_color="#ffffff", corner_radius=10)
        self.khorojizirBG.propagate(False)
        self.khorojizirBG.pack(fill="both", expand=True, padx=15, pady=(8, 15))
        
        self.output_title_label = CTkLabel(self.khorojizirBG, text=tables["ui_texts"]["Output"][self.current_lang], text_color="black", font=self.code)
        self.output_title_label.pack(side=TOP, anchor=self.pack_anchor, padx=10, pady=3)
        
        self.khorojizirBG2 = CTkFrame(master=self.khorojizirBG, fg_color="#f2f2f2", corner_radius=10)
        self.khorojizirBG2.propagate(False)
        self.khorojizirBG2.pack(fill="both", expand=True, padx=15, pady=(8, 15))
        
        self.khorojizirBG3 = CTkLabel(self.khorojizirBG2, text="", wraplength=350, justify=self.text_align, font=self.code, text_color="black")
        self.khorojizirBG3.pack(side=TOP, anchor=self.pack_anchor, padx=10, pady=10)
        
        self.texteditor = CTkTextbox(self.editorcode,fg_color="#1e1e2e",font=self.code,corner_radius=0,wrap="none")
        self.texteditor.pack(fill="both",expand=True)
        
        self.select_category(tables["DarsHa"]["Dars1"]["name"][self.current_lang])
        
        for i in tables["ConfigUi"]["PyKeywordsColor"]:
            self.texteditor.tag_config(i,foreground=tables["ConfigUi"]["PyKeywordsColor"][i])
            
        self.texteditor.bind("<KeyRelease>",self.keyframe)
        self.UpdateLabeleScore()
    def get_language(self):
        try:
            with open(f"{text}marcodedb.txt", "r", encoding="utf-8") as file:
                for line in file:
                    if line.startswith("Language |"):
                        return line.split("|")[1].strip()
        except:
            pass
        return "English"

    def getFontSize(self):
        try:
            with open(f"{text}/FontStyle/setting.txt","r",encoding="utf-8") as file:
                for line in file:
                    fontstylelist[line.split("|")[0].strip()] = [line.split("|")[1].strip()]
        except:
            pass

    def set_language(self, lang):
        lines = []  
        try:
            with open(f"{text}marcodedb.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
        except:
            pass
        found = False
        with open(f"{text}marcodedb.txt", "w", encoding="utf-8") as file:
            for line in lines:
                if line.startswith("Language |"):
                    file.write(f"Language | {lang}\n")
                    found = True
                else:
                    file.write(line)
            if not found:
                file.write(f"Language | {lang}\n")

    def change_language(self, choice):
        self.set_language(choice)
        self.current_lang = choice
        
        if self.current_lang == "English":
            self.text_align = "left"
            self.text_anchor = "nw"
            self.grid_sticky = "w"
            self.pack_anchor = "nw"
        else:
            self.text_align = "right"
            self.text_anchor = "ne"
            self.grid_sticky = "e"
            self.pack_anchor = "ne"

        self.UpdateLabeleScore()
        self.amozehi_text.configure(text=tables["ui_texts"]["LearningPaths"][self.current_lang])
        self.labelsharehdars.configure(text=tables["ui_texts"]["LessonDesc"][self.current_lang])
        self.output_title_label.configure(text=tables["ui_texts"]["Output"][self.current_lang])
        
        self.labelsharehdars.grid(row=0, column=0, sticky=self.grid_sticky, padx=20, pady=10)
        self.labelsharehdars2.grid(row=1, column=0, sticky=self.grid_sticky, padx=20, pady=2)
        self.labelsharehdars3.grid(row=3, column=0, sticky=self.grid_sticky, padx=20, pady=70)
        self.output_title_label.pack(side=TOP, anchor=self.pack_anchor, padx=10, pady=3)
        self.khorojizirBG3.pack(side=TOP, anchor=self.pack_anchor, padx=10, pady=10)
        
        self.labelsharehdars2.configure(justify=self.text_align, anchor=self.text_anchor)
        self.labelsharehdars3.configure(justify=self.text_align, anchor=self.text_anchor)
        self.khorojizirBG3.configure(justify=self.text_align)

        for widget in self.frame_chap.winfo_children():
            if isinstance(widget, CTkButton):
                widget.destroy()
                
        MotaghayereBTN.clear()
        
        for name,value in tables["DarsHa"].items():
            button_text = value["name"][self.current_lang]
            btn = CTkButton(self.frame_chap, height=44, text=button_text, fg_color="#242938", hover_color="#323a4f", font=self.code,command=lambda t=button_text:self.select_category(t))
            btn.pack(side=TOP, anchor="center", fill="x", padx=10, pady=4)
            MotaghayereBTN[button_text] = btn
            
        for widget in self.button_container.winfo_children():
            widget.destroy()
            
        for i in range(0, 5):
            g = str(i)
            btn_text = tables["ConfigUi"]["TextBTNZirEdtcode"][self.current_lang][g]
            btnkar = CTkButton(self.button_container, width=130, font=self.code, fg_color=tables["ConfigUi"]["ColorBTNZirEdtcode"][g], hover_color=tables["ConfigUi"]["HoverColorBTNZirEdtcode"][g], text=btn_text,command=lambda m=btn_text,g=g:self.ClickKard(m,g))
            btnkar.pack(side=LEFT, padx=8)

        self.select_category(tables["DarsHa"]["Dars1"]["name"][self.current_lang])
        self.texteditor.delete("1.0", "end")
        self.titletext.configure(text="")
        self.labelsharehdars2.configure(text="")
        self.labelsharehdars3.configure(text="")
        self.ouytput.configure(text="")
        self.khorojizirBG3.configure(text="")
        
    def UpdateLabeleScore(self):
        score = 0 
        databasee = self.getDbAccept()
        for line in databasee:
            if "|" in line and not line.startswith("Language |"):
                partss = line.split("|")
                motaghayer = partss[1].strip()
                if motaghayer.isdigit():
                    score += int(motaghayer)
        if hasattr(self, 'emtiaz_label'):
            self.emtiaz_label.configure(text=f"{tables['ui_texts']['YourScore'][self.current_lang]}: {score}/{self.totalScore}")
            self.results = score / self.totalScore
            self.prograse_org.set(self.results)
    def setDbAccept(self, text2):
        with open(f"{text}marcodedb.txt","a", encoding="utf-8") as file:
            file.write(f"\n{text2} | 1")
        self.UpdateLabeleScore()

    def getDbAccept(self):
        try:
            with open(f"{text}marcodedb.txt","r", encoding="utf-8") as file:
                return file.readlines()
        except:
            return []

    def show_about(self):
        title = tables["ui_texts"]["AboutTitle"][self.current_lang]
        info = tables["ui_texts"]["AboutText"][self.current_lang]
        tkinter.messagebox.showinfo(title, info)

    def ClickKard(self,selfs,g):
        if g == "0":
            self.texteditor.delete("1.0","end")
            self.khorojizirBG3.configure(text="")
            self.ouytput.configure(text_color=tables["ConfigUi"]["ColorBTNZirEdtcode"][g],text=tables["ui_texts"]["Cleared"][self.current_lang])
        elif g == "1":
            self.excutes(self.texteditor.get('1.0','end-1c'))
        elif g == "2":
            usercode = self.texteditor.get("1.0","end-1c")
            output_ok = all(index in self.satlport for index in self.getbedechallenge)
            req = self.chaleng_active.get("must_include",[])
            code_ok = all(alamfix in usercode for alamfix in req)
            database = self.getDbAccept()
            miq = self.chaleng_active.get("output","")
            MotghayerAval = str(self.satlport).strip().lower()
            MotghayerDovom = str(miq).strip().lower()
            Mootaghayayare = False
            for i in database:
                if self.idDarsIn in i:
                    Mootaghayayare = True
                    break
            if output_ok and code_ok and MotghayerAval == MotghayerDovom:
                if Mootaghayayare:
                    self.ouytput.configure(text_color="#2fb350", text=tables["ui_texts"]["AlreadyCompleted"][self.current_lang])
                else:
                    self.ouytput.configure(text_color="#2fb350", text=tables["ui_texts"]["Passed"][self.current_lang])
                    self.setDbAccept(self.idDarsIn)
            elif output_ok and not code_ok:
                self.ouytput.configure(text_color="#e74c3c", text=tables["ui_texts"]["Cheat"][self.current_lang])
            else:
                self.ouytput.configure(text_color="#e74c3c", text=tables["ui_texts"]["WrongOutput"][self.current_lang])
        elif g == "3":
            tkinter.messagebox.showinfo(tables["ui_texts"]["HelpTitle"][self.current_lang], self.chaleng_active["question"][self.current_lang])
        elif g == "4":
            try:
                self.texteditor.delete("1.0","end")
                self.texteditor.insert("1.0",self.code_cntlz)
                self.ouytput.configure(text_color=tables["ConfigUi"]["ColorBTNZirEdtcode"][g],text=tables["ui_texts"]["Reverted"][self.current_lang])
            except:
                self.ouytput.configure(text_color=tables["ConfigUi"]["ColorBTNZirEdtcode"][g],text=tables["ui_texts"]["SelectLesson"][self.current_lang])

    def setting(self):
        for i in self.ctkwindow:
            i.destroy()
        self.ctkwindow.clear()
        self.settingBg = CTkToplevel(self)
        self.ctkwindow.append(self.settingBg)
        self.settingBg.geometry("400x400")
        self.settingBg.attributes("-topmost",True)
        self.settingBg.attributes("-alpha",0.99)
        self.settingBg.title("Setting")
        self.settingBg.maxsize(400,400)
        self.settingBg.minsize(400,400)
        self.setting_CtkFram1 = CTkFrame(self.settingBg,corner_radius=0,fg_color="transparent")
        self.setting_CtkFram1.pack(fill="both",expand=True)
        self.setting_CtkFram1.propagate(False)
        self.setting_BTNChange = CTkButton(self.setting_CtkFram1,fg_color="blue",text="Apply",font=self.fontsmalluni,command=self.update_font)
        self.setting_BTNChange.pack(side=BOTTOM,expand=True)
        self.setting_CtkFram2 = CTkScrollableFrame(self.setting_CtkFram1,height=130,corner_radius=0,fg_color="transparent")
        self.setting_CtkFram2.pack(fill="x",expand=True)
        self.ok = {}
        for i,y in fontstylelist.items():
            self.setting_frameone = CTkFrame(master=self.setting_CtkFram2,height=20,corner_radius=0,fg_color="transparent")
            self.setting_frameone.pack(fill="x",padx=5,pady=15)
            self.setting_textaval = CTkLabel(master=self.setting_frameone,text=f"{i}",font=self.fontsmalluni)
            self.setting_textaval.pack(side="left",anchor="w",padx=5)
            if i == "Font":
                self.settingCombo = CTkComboBox(master=self.setting_frameone,values=test)
                self.settingCombo.pack(side="right",anchor="e",padx=5)
                self.settingCombo.set(y[0])
                self.ok[i] = self.settingCombo
            else:
                self.setting_Textbox = CTkEntry(master=self.setting_frameone,width=50,height=20,corner_radius=5,justify="center",font=self.fontsmall,placeholder_text=f"{y[0]}")
                self.setting_Textbox.pack(side="right",anchor="e",padx=5)
                self.setting_Textbox.insert(0, f"{y[0]}")
                self.ok[i] = self.setting_Textbox
    def update_font(self):
        for key, textbox in self.ok.items():
            new_value = textbox.get()
            if key == "Font":
                fontstylelist[key] = [new_value]
                self.font_family = new_value
            else:
                if new_value.isdigit() and int(new_value) < 25:
                    fontstylelist[key] = [new_value]
        try:
            with open(f"{text}/FontStyle/setting.txt", "w", encoding="utf-8") as file:
                for key, val in fontstylelist.items():
                    file.write(f"{key} | {val[0]}\n")
                self.code = (self.font_family, int(fontstylelist["FontCodeSize"][0]))
                self.code_x2 = (self.font_family, int(fontstylelist["FontCodeSizex2"][0]))
                self.fontsmall = (self.font_family, int(fontstylelist["FontSmall"][0]))
                self.apply_fonts()
        except:
            pass
    def apply_fonts(self):
        self.texteditor.configure(font=self.code)
        self.titletext.configure(font=self.code)
        self.emtiaz_label.configure(font=self.code)
        self.marcode.configure(font=self.code)
        self.labelsharehdars.configure(font=self.code)
        self.labelsharehdars2.configure(font=self.code)
        self.labelsharehdars3.configure(font=self.fontsmall)
        self.ouytput.configure(font=self.code)
        self.khorojizirBG3.configure(font=self.code)
        self.amozehi_text.configure(font=self.code_x2)

    def excutes(self,text):
        self.satl = io.StringIO()
        try:
            with redirect_stdout(self.satl):
                exec(text)
        except:
            self.khorojizirBG3.configure(text=tables["ui_texts"]["Error"][self.current_lang])
        self.satlport = self.satl.getvalue()
        self.khorojizirBG3.configure(text=self.satlport)

    def keyframe(self,text=None):
        for i in tables["ConfigUi"]["PyKeywordsColor"]: 
            self.texteditor.tag_remove(i,"1.0","end")
            for wath in re.finditer(rf"\b{i}\b",self.texteditor.get("1.0","end-1c")):
                shoro = wath.start()
                endd = wath.end()
                self.texteditor.tag_add(i,f"1.0+{shoro}c",f"1.0+{endd}c")

    def select_category(self, text):
        for key,value in MotaghayereBTN.items():
            if key == text:
                value.configure(fg_color="#3a6ff0",hover_color="#285ee3")
            else:
                value.configure(fg_color="#242938")
        for i in self.AyaInFixMishe:
            i.destroy()
        for kelid,kigin in selectDarss.items():
            kigin.destroy()
        self.AyaInFixMishe.clear()
        selectDarss.clear()
        self.getbededarsaro = None 
        for darskey,valuekey in tables["DarsHa"].items():
            if valuekey["name"][self.current_lang] == text:
                self.getbededarsaro = valuekey
                break
        if self.getbededarsaro != None:
            if "Lessons" in self.getbededarsaro:
                for lsseon in self.getbededarsaro["Lessons"].values():
                    title_text = lsseon["Title"][self.current_lang]
                    self.sdas = CTkButton(self.frame_chap,width=200,height=20,fg_color="transparent",hover_color="#2c3448",text_color="#d6d9e0",font=self.fontsmall,text=title_text,command=lambda events=lsseon,btnname=title_text:self.SelectDars(events,btnname))
                    self.sdas.pack(anchor="center",pady=10)
                    self.AyaInFixMishe.append(self.sdas)
                    selectDarss[title_text] = self.sdas

    def SelectDars(self,text,btnname):
        for idish,key in selectDarss.items():
            if idish == btnname:
                key.configure(text_color="#3a6ff0")
            else:
                key.configure(text_color="#d6d9e0")
        self.chaleng_active = text["challenge"]
        self.idDarsIn = text["id"]
        self.titletext.configure(text=text["Title"][self.current_lang])
        self.code_cntlz = text["Code"][self.current_lang]
        self.getbedechallenge = text["challenge"]["expected"][self.current_lang]
        self.texteditor.delete("1.0","end")
        self.texteditor.insert("1.0",text["Code"][self.current_lang])
        self.keyframe()
        self.labelsharehdars2.configure(text=text["Tozihat"][self.current_lang])
        self.labelsharehdars3.configure(text=text["ZirTozihat"][self.current_lang])
        self.ouytput.configure(text="")
        self.khorojizirBG3.configure(text="")
        self.satlport = ""

    def createDataDB(self,vales):
            with open(f"{text}marcodedb.txt","w", encoding="utf-8") as file:
                file.write("Language | English\n")
            with open(f"{text}/FontStyle/setting.txt","w", encoding="utf-8") as file:
                file.write("FontCodeSize | 15\n")
                file.write("FontCodeSizex2 | 17\n")
                file.write("FontSmall | 13\n")
                file.write(f"Font | {vales[0]}\n")
if __name__ == "__main__":
    app = App()
    app.mainloop()
