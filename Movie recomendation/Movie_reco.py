import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import pickle
import pandas as pd
def recommend_movie():
    user_movie = age_entry.get()
    recommend_movies=[]
    movies_dict = pickle.load(open("movie_dicts.pkl", 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open("similaritys.pkl", 'rb'))

    movie_index = movies[movies['title'] == user_movie].index[0]
    # print(user_movie)
    # print(movie_index)
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    movies_list = movies_list[1:5]
    # print(movies_list)
    for i in movies_list:
        # print(i)
        recommend_movies.append(movies.iloc[i[0]].title)
    movie0,movie1,movie2,movie3=recommend_movies
    recommend_movies.clear()
    suggest_movie = f'''Suggested Movies : 
{movie0}
{movie1}
{movie2}
{movie3}
    '''
    output.config(text=suggest_movie)
    
# Create main window
root = tk.Tk()
root.title("Movie Recommendation System")
root.geometry("1100x600")
# root.attributes('-fullscreen', True)

# background image:
img= Image.open("background.png").resize((1100,600))
bck_img = ImageTk.PhotoImage(img)
background_img_lbl = tk.Label(root,image=bck_img)
background_img_lbl.place(x=0,y=0)


# root.configure(bg="Pink")
# Age label and entry
age_label = tk.Label(root, text="Enter Movie name",font=("Comic Sans MS",18,"bold"),bg="#002D62",fg="white")
age_label.place(x= 230, y = 150)
age_var = tk.IntVar()
age_entry = tk.Entry(root,width=27,font=("Comic Sans MS",18,"italic"))
age_entry.place(x= 480 , y = 150)


# Button to recommend movie
recommend_button = tk.Button(root, text="Recommend Movie", width=43,bg = "#D10000",fg="white"
                             ,command=recommend_movie,font=("Broadway",15,"bold"))
recommend_button.place(x=230,y=200)

output = tk.Label(root,font=("Comic Sans MS",18,"bold"),fg="white",bg='#5072A7')
output.place(x= 350, y = 250)

# Run the GUI
root.mainloop()