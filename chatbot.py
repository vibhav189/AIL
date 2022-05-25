import nltk
from nltk.chat.util import Chat, reflections

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"what is your name ?",
        ["you can call me chatter!", ]
    ],
    [
        r"how are you ?",
        ["I'm doing goodnHow about You ?", ]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind", ]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?", ]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "How can I help you?:)", ]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dudenSeriously you are asking me this?", ]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", ]
    ],
    [
        r"(.*) created ?",
        ["Nikhil created me using Python's NLTK library ", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Pune, Maharashtra', ]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot man here in %1",
            "Too cold man here in %1", "Never even heard about % 1"]
    ],
    [
        r"i work in (.*)?",
        ["% 1 is an Amazing company, I have heard about it. But they are in huge loss these days.", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2",
            "Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ", ]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Cricket", ]
    ],
    [
        r"who (.*) sportsperson ?",
        ["MS Dhoni", "Virat Kohli", "Rohit Sharma", ]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"quit",
        ["BBye take care. See you soon :) ",
            "It was nice talking to you. See you soon:)"]
    ],
]


def chat():
    print("Hi! I am a chatbot for your service")
    chat = Chat(pairs, reflections)
    chat.converse()


# initiate the conversation
if __name__ == "__main__":
    chat()


# OUTPUT :

"""
Hi! I am a chatbot for your service
>hii
Hello
>how are you
I'm doing goodnHow about You ?
>i am fine
Great to hear that, How can I help you?
>what is your name
you can call me chatter!
>what is your fav game
I'm a very big fan of Cricket
>quit
BBye take care. See you soon :) 
"""
