#CheerUpBot by Kier De Chavez
#Imports
from tkinter import *
from tkinter.font import names
import tkinter as tk
import random

root = tk.Tk()

#List of random advices
advices = [
    "Take time to know yourself. Know thyself said Aristotle. When you know who you are, you can be wise about your goals, your dreams, your standards, your convictions. Knowing who you are allows you to live your life with purpose and meaning.",
    "A narrow focus brings big results. The number one reason people give up so fast is because they tend to look at how far they still have to go instead of how far they have come. But it's a series of small wins that can give us the most significant success.",
    "Show up fully. Don't dwell on the past, and don't daydream about the future, but concentrate on showing up fully in the present moment.",
    "Don't make assumptions. If you don't know the situation fully, you can't offer an informed opinion.",
    "Be patient and persistent. Life is not so much what you accomplish as what you overcome."
]


#Getting user name
def send():
    
    #Receiving user choice
    send = "You:"+ e.get() + "\n"
    text.insert(tk.END,"\n" + send)

    if (e.get() == "1" ):
        text.insert(tk.END,"AnonKly: Oh, hello there! You know what? Each day in our life is an exam. Each day we'll lived we succeed. If we live for 75 years then we have almost 27,400 exams to give. Out of all exams emotional and practical exams of life are the most valuable and toughest (which grown ups can better understand) To pass in the test of life you need atleast 13,700 good days. ( 50% criteria is tough actually) In simple words you must compensate each bad day with a day well lived Which means you can afford 13,700 bad days! And you are mourning over 1 written paper? Not worth it! Keep fighting for the 50% target! I know you can do this! \n")
        
    elif (e.get() == "2" ):
        text.insert(tk.END,"AnonKly: You won't have to deal with this forever. Just push through it. Get a job and move out when you can. And just think about it, you're stronger for having to put up with this. if you're ever a parent, youll do a much better job of it. But until then, im here whenever you need me, anytime, in any way. \n ")

    elif (e.get() == "3" ): 
        text.insert(tk.END,"AnonKly: I am incredibly sorry to hear that you are unwell. While you recover, I hope you are surrounded by the warmth of those you love. Get well soon. Best wishes for a little progress and a little encouragement every day during your recuperation. Hoping you find strength with each new day. You are in our thoughts. Always remember that you will overcome this disease, you will also be healed just trust yourself you can fight this. \n")    
        
    elif (e.get() == "4" ): 
        text.insert(tk.END,"AnonKly: Oh, I am sorry to hear that but here some piece of Advice. People come and go to your life, either it's a blessing or it's a lesson. You deserve so much better than this. If someone dump you, there's absolutely nothing you can do about it. its their decision. Its hurt so much, but i promise it's not forever. Just, let yourself feel everything you need to feel. Also remember that TIME is the greatest healer. \n")

    elif (e.get() == "5" ):
        text.insert(tk.END, "Hey there bud! Life is indeed hard, we face problems in a daily basis, and there are times where we are unable to solve it, where we cannot find the right approach and end up failing. Do not worry, that's normal, everyone of us experience this, it is not the end, remember that. We should pick ourselves up again, and face the problem head on, with the learnings of not repeating the same mistakes. That's the beauty of failing, we learn and we improve ourselves. I am proud of where you are now, and you should be too! Slowly but surely, you can do this! Keep up the good work! Your past self is proud of where you are now, and you should be too! \n")

    elif (e.get() == "6" ):
        text.insert(tk.END, "AnonKly: Hi, fighter! How are you holding up? I see that the pandemic made gaining education harder than it was in regular  classes in school. I want you to know that it is totally okay and normal to feel burnout, plus a lot of people are surely willing to be present for you as you go on these seemingly rocky road— including me. Being tired is a sign of strength, a warrior's cooldown even. You've been so strong and I'm 101% proud! Please allow yourself to rest, productivity can also mean prioritizing one's self. Breathe for a moment, then fight again. \n")

    elif (e.get() == "7" ):
        text.insert(tk.END, "AnonKly: That's okay! Sometimes we have a hard time committing and completing a task. We can get back on track by listing a to-do tasks to complete for a day, the satisfaction of completing each task will surely boost you up. You can also challenge yourself to remove the distractions in your workplace area, listening to calming music while doing your task. Lastly, do not forget to reward yourself either with snacks, or playing games after completing your goals for the day. Keep grinding! You can do this. Don't forget to have fun doing each task! \n")

    elif (e.get() == "8" ):
        text.insert(tk.END, "AnonKly: hello there! doesn't your heart feel heavy from carrying all the burden of hate? I suggest that we take this slow— okay? okay. Breathe and calm yourself first, then allow your mind to have a deeper understanding, and lastly, think about what the trolls or candidates want for the country. We all want the best life for ourselves— a best country to be precise, it's just that sometimes, our beliefs can cloud our judgements. We will never know the complete intention and reason behind an action of a certain candidate or a soecific troll, but together as one, we can. This is not the time to foster anger deep within you, this should be the time we apply our well-known culture of 'bayanihan' and help each other create wiser choices this coming elections. So chill out, and bring others with you as you create a ripple of change or a small step towards a progressive country. Nananatiling matatag, palaging para sa Inang Bayan. \n")

    elif (e.get() == "9" ):
        text.insert(tk.END, "AnonKly:" + random.choice(advices) )

    elif (e.get() == "10" ): 
        text.insert(tk.END,"Anonkly: Thank you and stay safe :>")
        
    else:
        text.insert(tk.END,"The number you entered is invalid. Please pick from the number above.")

    
bg_image = tk.PhotoImage(file = "bg.png")
bgmenu = tk.Label (image = bg_image)
bgmenu.place(relheight=1, relwidth=1)
text = Text(bg='beige')
text.grid(row=0,column=0,columnspan=2)
text.place(x=150, y=110)
e = Entry(width=100)
send = Button(text='Send',bg='saddle brown',width=20,command=send)
send.place(x=645, y=498)
e.grid(row=1,column=0)
e.place(x=150, y=502)
    #Starting Conversations
text.insert(tk.END,"\nAnonKly: Hello there! \n")
text.insert(tk.END, "AnonKly: Come and sit and take a sip of coffee \n")
text.insert(tk.END, "\n" + "AnonKly: \x1B[3m Hands virtual coffee \x1B [0m ⅽ[ː̠̈ː̠̈ː̠̈] ͌  \n")
text.insert(tk.END, "\n" + "AnonKly: So what brings you here? \n")

    #Getting the users choice 
text.insert(tk.END, "AnonKly: Choose one of the following number so I can give an advice :> \n")
text.insert(tk.END, "1. Low Grades \n" + "2. Family Problems \n" + "3. Severe Illness \n" + "4. Heart Broken \n" + "5.Feeling like a Failure \n" + "6. Burnout in academic set-up \n" + "7. Unable to Concentrate \n" + "8. Anger this Political Season \n" + "9. Random Advice \n" + "10. That's all :> \n \n")
root.geometry("1280x720")
root.title('Cheer Up bot')
root.mainloop()