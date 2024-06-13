import tkinter as tk
import pickle
import string
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from PIL import Image,ImageTk
from tkinter import messagebox


ps = PorterStemmer()
# Create your views here.
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

def analyze_text(input_sms):
    tfidf = pickle.load(open('vectorizer.pkl','rb'))
    model = pickle.load(open('model.pkl','rb'))

    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        return "Spam"
    else:
        return "Not Spam"

def analyze_and_display():
    input_text = text_entry.get("1.0", tk.END)
    result = analyze_text(input_text)
    messagebox.showinfo("Analysis Result", result)



# Create the main window
root = tk.Tk()
root.title("Spam Detector")
root.geometry("1200x600")
root.resizable(0,0)

# background image
img = Image.open("spam_background.jpeg")
bck_img = ImageTk.PhotoImage(img)
background_img_label = tk.Label(root,image=bck_img)
background_img_label.place(x=0,y=0)

# heading :
tk.Label(root,text=("SMS Spam Detector"),font=("ALGERIAN",40,"bold italic")).place(x=170,y=260)

# Text entry field
text_entry = tk.Text(root, height=12, width=21,font=("Bahnschrift",20,"italic"),fg="#002244")
text_entry.place(x=865,y=110)

# Button to analyze text
analyze_button = tk.Button(root, text="Analyze",font=("Lapture",15,"bold"), command=analyze_and_display)
analyze_button.place(x=975,y=515)

# Run the Tkinter event loop
root.mainloop()
