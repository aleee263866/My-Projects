from tkinter import *
from tkinter import ttk
from customtkinter import *
from googletrans import Translator
from tkinter.messagebox import showerror

root = Tk()
root.title("PythonTrans")
root.configure(background="#14181f")
root.resizable(0,0)
root.iconbitmap("path")
translator = Translator()
window_width = 800
window_height = 500

#CENTRA LA FINESTRA
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.lift()
root.attributes('-topmost', True)


righe = 5
colonne = 8
for riga in range(righe):
    root.rowconfigure(riga, weight=1)
for colonna in range(colonne):
    root.columnconfigure(colonna, weight=1)

lingue_disponibili = {
    'af': 'afrikaans',
    'sq': 'albanese',
    'am': 'amarico',
    'ar': 'arabo',
    'hy': 'armeno',
    'az': 'azerbaigiano',
    'eu': 'basco',
    'bn': 'bengalese',
    'be': 'bielorusso',
    'my': 'birmano',
    'bs': 'bosniaco',
    'bg': 'bulgaro',
    'ca': 'catalano',
    'ceb': 'cebuano',
    'cs': 'ceco',
    'ny': 'chichewa',
    'zh-cn': 'cinese (semplificato)',
    'zh-tw': 'cinese (tradizionale)',
    'ko': 'coreano',
    'co': 'corso',
    'ht': 'creolo haitiano',
    'hr': 'croato',
    'ku': 'curdo (kurmanji)',
    'da': 'danese',
    'iw': 'ebraico',
    'he': 'ebraico',
    'eo': 'esperanto',
    'et': 'estone',
    'tl': 'filippino',
    'fi': 'finlandese',
    'fr': 'francese',
    'fy': 'frisone',
    'gd': 'gaelico scozzese',
    'gl': 'galiziano',
    'cy': 'gallese',
    'ka': 'georgiano',
    'ja': 'giapponese',
    'jw': 'giavanese',
    'el': 'greco',
    'gu': 'gujarati',
    'ha': 'hausa',
    'haw': 'hawaiano',
    'hi': 'hindi',
    'hmn': 'hmong',
    'ig': 'igbo',
    'id': 'indonesiano',
    'en': 'inglese',
    'ga': 'irlandese',
    'is': 'islandese',
    'it': 'italiano',
    'kn': 'kannada',
    'kk': 'kazako',
    'km': 'khmer',
    'ky': 'kirghiso',
    'lo': 'lao',
    'la': 'latino',
    'lv': 'lettone',
    'lt': 'lituano',
    'lb': 'lussemburghese',
    'mk': 'macedone',
    'ml': 'malayalam',
    'ms': 'malese',
    'mg': 'malgascio',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolo',
    'ne': 'nepalese',
    'no': 'norvegese',
    'or': 'odia',
    'nl': 'olandese',
    'ps': 'pashto',
    'fa': 'persiano',
    'pl': 'polacco',
    'pt': 'portoghese',
    'pa': 'punjabi',
    'ro': 'rumeno',
    'ru': 'russo',
    'sm': 'samoano',
    'sr': 'serbo',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'singalese',
    'sk': 'slovacco',
    'sl': 'sloveno',
    'so': 'somalo',
    'es': 'spagnolo',
    'su': 'sundanese',
    'sv': 'svedese',
    'sw': 'swahili',
    'tg': 'tagiko',
    'ta': 'tamil',
    'de': 'tedesco',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turco',
    'uk': 'ucraino',
    'ug': 'uiguro',
    'hu': 'ungherese',
    'ur': 'urdu',
    'uz': 'uzbeko',
    'vi': 'vietnamita',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu'
}


def processo_traduzione():
    try:
        testo = casella_testo.get("1.0",END)
        lingua_rilevata = translator.detect(testo) 
        traduzione = translator.translate(testo, src=f"{lingua_rilevata.lang}", dest=f"{lingua_scelta}") 
        casella_traduzione.delete(1.0, END)
        casella_traduzione.insert(1.0,f"{traduzione.text}")
    except Exception as t:
        errore = (f"Si è verificato un errore: {t}")
        showerror(title="Errore!", message=errore,)


    
    
def selezione_lingua (event):
    global lingua_scelta
    lingua_scelta = input.get()
    if lingua_scelta in lingue_disponibili.values():
        lingua_scelta = next((codice for codice, lingua_nome in lingue_disponibili.items() if lingua_nome == lingua_scelta), None)




# TITOLO DEL TRADUTTORE
titolo1 = CTkLabel(root, text="Python", bg_color="transparent", fg_color="transparent", text_color="white", font= ("Small Fonts", 45, "bold"), anchor= "e")
titolo1.grid(column=0, row=0, columnspan=4, sticky="e")
titolo2 = CTkLabel(root, text="Trans", bg_color="transparent", fg_color="transparent", text_color="#4d94ff", font= ("Small Fonts", 45, "bold"), anchor= "w")
titolo2.grid(column= 4, row=0, columnspan= 4, sticky= "w")

# CASELLA IN CUI INSERIRE IL TESTO NELLA LINGUA INIZIALE
casella_testo = CTkTextbox(root, corner_radius= 10, border_width= 5, border_color="white", bg_color= "transparent", fg_color= "#28303e", text_color="#d0d7e1",activate_scrollbars = True, font = ("Arial", 17))
casella_testo.grid(sticky = "news", column = 1, row = 1, rowspan= 3, columnspan= 2 )

# MENU A TENDINA PER SCEGLIERE LA LINGUA
input = StringVar()
lingue_combobox = ttk.Combobox(root, values=list(lingue_disponibili.values()), textvariable = input, font=("Arial", 9))
lingue_combobox["state"] = ["readonly"]
lingue_combobox.bind("<<ComboboxSelected>>", selezione_lingua)
lingue_combobox.grid(column= 3, row=1, columnspan= 2)

# SCRITTA "Scegli la lingua"
scegli_lingua_testo1 = CTkLabel(root, text= "Seleziona una", font=("Small Fonts", 13), bg_color="transparent", fg_color= "transparent", text_color="white", anchor = "ne")
scegli_lingua_testo1.grid(column = 3, row = 1, sticky = "ne")
scegli_lingua_testo2 = CTkLabel(root, text= " lingua", font=("Small Fonts", 13), bg_color="transparent", fg_color= "transparent", text_color="#4d94ff", anchor = "nw")
scegli_lingua_testo2.grid(column = 4, row = 1, sticky = "nw")

# CASELLA IN CUI APPARE LA TRADUZIONE
casella_traduzione = CTkTextbox(root, corner_radius= 10, border_width= 5, border_color="#4d94ff", bg_color= "transparent", fg_color= "#28303e", text_color="#d0d7e1", font= ("Arial", 17),
activate_scrollbars = True)
casella_traduzione.grid(sticky = "news", column = 5, row = 1, rowspan= 3, columnspan= 2 )
casella_traduzione.bind("<Key>", lambda n: "break")
casella_traduzione.bind("<Control-c>", lambda m:"continue")

# PULSANTE PER AVVIARE LA TRADUZIONE
pulsante_traduci = CTkButton(root, text= "Traduci", command = lambda:processo_traduzione(), bg_color="transparent", fg_color="#243042", corner_radius=100, border_width=2, border_color="white", font = ("Arial", 13, "bold"))
pulsante_traduci.grid(row = 3, rowspan = 2, column = 3, columnspan = 2)

root.mainloop()
