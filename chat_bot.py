"""This is a chatbot program"""
from nltk.chat.util import Chat, reflections


pairs = [
    ["my name is (.*)", ["hi %1"]],
    ["(hi|hello|hey|holla|hola)", ["hey there", "hi there", "haaayyy"]],
    ["(.*) in (.*) is fun", ["%1 in %2 is indeed fun"]],
    ["(.*)(location|city) ?", ["Malmö, Sweden"]],
    ["(.*) created you ?", ["Jwan did"]],
    ["how is the weather in (.*)", ["The weather is amazing in %1"]],
    ["(.*)help(.*)", ["I can help you"]],
    ["(.* your name ?)", ["My name is J.M"]]
]

my_refelctions = {
    "go": "gone",
    "hello": "hey there"
}
chat = Chat(pairs, reflections)
# chat._substitute("go hello")
chat.converse()
