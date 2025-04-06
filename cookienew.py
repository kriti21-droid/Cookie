import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from googletrans import Translator

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

def quiz(question, answer, answer_type):
    global score, total_questions
    total_questions += 1
    speak(question)
    print(question)

    if answer_type == 'type':
        user_answer = input().lower()
    elif answer_type == 'speak':
        user_answer = takeCommand().lower()
    else:
        speak("Invalid answer type. Please choose 'type' or 'speak'.")
        return

    if user_answer == 'quit':
        speak("Quitting the quiz...")
        print("Quitting the quiz...")
        raise SystemExit

    elif user_answer == answer.lower():
        speak("Correct!")
        print("Correct!")
        score += 1
    else:
        speak("Incorrect!")
        print("Incorrect!")

jokes = [
    "What did the light bulb say to the switch? You know how to turn me on",
    "What do you call a bee that can’t make up its mind? A maybee",
    "Knock-Knock. Whose there? Amish. Amish who? Amish you too",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "What did the big flower say to the little flower? 'Hi, bud!'",
    "Why did the math book look sad? Because it had too many problems!",
    "What did the ocean say to the beach? Nothing, it just waved",
    "What did one wall say to the other wall? Lets meet at the corner!",
    "How do you organize a space party? You 'planet'",
    "Why was 6 afraid of 7? Because 7 8 9",
    "What do you give a sick lemon? A lemon aid",
    "Why did the school kids eat their homework? Because their teacher told them it was a piece of cake",
    "Why did the painting go to jail?  It was framed.",
    "What does a house wear? Address!",
    "What’s the best smelling insect? A deodor-ant.",
    "Why did the mushroom go to the party? Cause he was a fungi",
    "What’s orange and sounds like a parrot? A carrot!"
]

def get_random_riddle():
    riddles = [
        {
            'riddle': "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
            'answer': "Echo"
        },
        {
            'riddle': "What has keys but can't open locks?",
            'answer': "Piano"
        },
        {
            'riddle':" David's father has three sons: Snap, Crackle, and who?",
            'answer': "David"
        },
        {
            'riddle': "Can you name three consecutive days without using the words Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?",
            'answer': "Yesterday, Today, and Tomorrow."
        },
        {
            'riddle': "What belongs to you, but other people use it more than you?",
            'answer': "My name."
        },
        {
            'riddle': "I make two people out of one. What am I?",
            'answer': "A mirror."
        },
        {
            'riddle': "What is more useful when it is broken?",
            'answer': "An egg"
        },
        {
            'riddle': "I am white when I am dirty, and black when I am clean. What am I?",
            'answer': " A blackboard."
        },
        {
            'riddle': "A doctor and a bus driver are both in love with the same woman, an attractive girl named Sarah. The bus driver had to go on a long bus trip that would last a week. Before he left, he gave Sarah seven apples. Why?",
            'answer': "An apple a day keeps the doctor away!"
        },
        {
            'riddle': "You have me today, Tomorrow you'll have more; As your time passes, I'm not easy to store; I don't take up space, But I'm only in one place; I am what you saw, But not what you see. What am I?",
            'answer': " Memories."
        },
    ]
    random_riddle = random.choice(riddles)
    return random_riddle

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def TranslationToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You: {data}.")
    return data

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Cookie Maam. Please tell me. how may i help you?")

def takeCommand():
    # it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        speak("Sorry, I did not catch that. Could you please repeat?")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speak("Sorry, I am having trouble connecting to the speech recognition service.")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    stop_listening = False
    answer_type = None
    while not stop_listening:
        query = takeCommand().lower()
        if query == "None":
            continue

        if 'stop listening to me' in query:
            speak("Sure")
            stop_listening = True
            break

        # logic for executing tasks based on query
        elif 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'open spotify' in query:
            speak("Opening Spotify")
            webbrowser.open('spotify.com')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open visual studio' in query:
            speak("Opening Visual Studio")
            codepath = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'google' in query:
            speak("Searching on google")
            search_query = query.replace('search on google', '').strip()
            search_url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
            webbrowser.open(search_url)

        elif 'youtube' in query:
            speak("Searching on youtube")
            search_query = query.replace('search on youtube', '').strip()
            search_url = f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}"
            webbrowser.open(search_url)

        elif 'your name' in query:
            speak("My name is Cookie!")

        elif 'how are you' in query:
            speak("I am good, i hope you are good too, please let me know how may i help you?")

        elif 'quiz' in query:
            if answer_type is None:
                speak("Do you want to type your answers or speak your answers?")
                answer_choice = takeCommand().lower()
                if 'type' in answer_choice:
                    answer_type = 'type'
                elif 'speak' in answer_choice:
                    answer_type = 'speak'
                else:
                    speak("Invalid choice. Please choose 'type' or 'speak'.")
                    continue

            speak("Sure! Let's start the quiz.")
            total_questions = 0
            score = 0
            try:
                quiz("What is the capital of France?", "Paris", answer_type)
                quiz("Who painted the Mona Lisa?", "Leonardo da Vinci", answer_type)
                quiz("What is the largest continent in the world?", "Asia", answer_type)
                quiz("What is the chemical symbol for water?", "H2O", answer_type)
                quiz("Which country is known for its famous pyramids?", "Egypt", answer_type)
                quiz("Which country is famous for the Taj Mahal?", "India", answer_type)
                quiz("Who wrote the play Romeo and Juliet?", "William Shakespeare", answer_type)
                quiz("How many members are there in the famous band One Direction?", "five", answer_type)
                quiz("What is the largest organ in the human body?", "Skin", answer_type)
                quiz("Who is the famous scientist who developed the theory of gravity?", "Isaac Newton", answer_type)
            except SystemExit:
                break

            speak(f"Quiz ended. Your score is {score} out of {total_questions}.")
            print(f"Quiz ended. Your score is {score} out of {total_questions}.")

            if score == total_questions:
                print("Congratulations!! You slayed the Quiz")
                speak("Congratulations!! You slayed the Quiz")
            else:
                print("Oh! Come on you can do better and get a full score!")
                speak("Oh! Come on you can do better and get a full score!")

        elif 'joke' in query:
            joke = random.choice(jokes)
            speak(joke)
            print(joke)

        elif 'translate' in query:
            text_to_translate = query.replace('translate', '').strip()
            translated_text = TranslationToEng(text_to_translate)
            speak(translated_text)

        elif 'riddle' in query:
            speak("Sure! Here's a riddle for you:")
            riddle = get_random_riddle()
            speak(riddle['riddle'])
            print(riddle['riddle'])
            speak("Take a guess!")

            user_answer = takeCommand().lower()
            if user_answer.lower() == riddle['answer'].lower():
                speak("WOW! You got it right! Good job")
            else:
                speak(f"Sorry, the correct answer is {riddle['answer']}. Try better next time")
