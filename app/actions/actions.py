# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from re import X
from re import template
from tokenize import Name
from tkinter import Button
from turtle import title
from typing import Any, Text, Dict, List
from importlib_metadata import requires

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
import smtplib
import json
from getpass import getpass
from email.message import Message
from email.mime.text import MIMEText

class ActionService(Action):

    def name(self) -> Text:
        return "action_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/buyer{"property_type":"buyer"}', "title":"Buyer"},
            {"payload":'/seller{"property_type":"seller"}', "title":"Seller"},
        ]
        
        dispatcher.utter_message(text="How can I help you in Property?",buttons=buttons)

        return []

class ActionService1(Action):

    def name(self) -> Text:
        return "action_service1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/perfect_choices', "title": "Single-family home"},
            {"payload":'/perfect_choices', "title": "Condo"},
            {"payload":'/perfect_choices', "title": "Villa/Townhouse"},
            {"payload":'/perfect_choices', "title": "Manufactured Home"},
            {"payload":'/perfect_choices', "title": "Multi-Family"},
            {"payload":'/perfect_choices', "title": "Commercial"},
            {"payload":'/perfect_choices', "title": "Rental"},
            {"payload":'/perfect_choices', "title": "Commercial-lease"},
            {"payload":'/perfect_choices', "title": "Business opportunity"},

        ]
        dispatcher.utter_message(text="Well in that case, we have perfect home choices for you and your family. Can you elaborate what kind of property are you looking for? Should it be:",buttons=buttons)

        return []

class ActionService2(Action):

    def name(self) -> Text:
        return "action_service2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/details_property', "title": "House"},
            {"payload":'/details_property', "title": "Apartment"},
            {"payload":'/details_property', "title": "Plot"},

        ]
        dispatcher.utter_message(text="What type of property do you want for sell?",buttons=buttons)

        return []

class ActionService3(Action):

    def name(self) -> Text:
        return "action_service3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/affirm', "title": "YES"},
            {"payload":'/deny', "title": "NO"},

        ]
        dispatcher.utter_message(text="Yes of course! You have come at the right place for that. Do you have some time so that I can ask you about some information, regarding to your property?: ",buttons=buttons)

        return []

class ActionService4(Action):

    def name(self) -> Text:
        return "action_service4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/yes', "title": "YES"},
            {"payload":'/no', "title": "NO"},

        ]
            
        dispatcher.utter_message(text="Is your provieded information is correct? ",buttons=buttons)

        return []

class ActionService5(Action):

    def name(self) -> Text:
        return "action_service5"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/yess', "title": "YES"},
            {"payload":'/noo', "title": "NO"},

        ]

        dispatcher.utter_message(text="Is your provieded information is correct? ",buttons=buttons)

        return []

class ActionSendemail(Action):

    def name(self) -> Text:
        return "action_Sendemail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name=tracker.get_slot("name")
        pro=tracker.get_slot("property_type")
        num=tracker.get_slot("number")
        emi=tracker.get_slot("email")
        SendEmail(f"New Custmer, {name} . He is {pro}. his Number is {num} and Email is {emi}. Pleace contect him!!!")

        dispatcher.utter_message()

        return []

class ActionSend_email(Action):

    def name(self) -> Text:
        return "action_Send_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name=tracker.get_slot("name")
        pro=tracker.get_slot("property_type")
        num=tracker.get_slot("number")
        emi=tracker.get_slot("email")
        SendEmail(f"New Custmer, {name} . He is {pro}. his Number is {num} and Email is {emi}. Pleace contect him!!!")

        dispatcher.utter_message()

        return []

class ActionSaveConversation(Action):

    def name(self) -> Text:
        return "action_saveconversation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #print(tracker.events)
        conversation=tracker.events
        import os
        if not os.path.isfile('chats.txt'):
            with open('chats.txt','w') as file:
                file.write("New Client\n")
        chat_data=''
        for i in conversation:
            
            if i["event"]=="user":
                chat_data+='User: '+i['text']+'\n'

            elif i['event']=='bot':
                try:
                    chat_data+='Boot: '+i['text']+'\n'
                except KeyError:
                    pass
        else:
            with open('chats.txt', 'a', encoding="utf-8") as file:
                file.write(chat_data)

        dispatcher.utter_message()

        return []

# class vaildateforms(Action):
#     def name(self) -> Text:
#         return "user_detail_form"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#         ) -> List[Dict[Text, Any]]:
#         required_slots = ["name", "number", "email"]

#         for slot_name in required_slots:
#             if tracker.slots.get(slot_name) is None:
#                 return [SlotSet("requested_slot", slot_name)]

#         return [SlotSet("requested_slot", None)]

# class ActionSubmit(Action):
#     def name(self) -> Text:
#         return "action_submit"
    
#     def run(
#         self,
#         dispatcher,
#         tracker: Tracker,
#         domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_detail_thanks",
#                             name=tracker.get_sot("name"),
#                             number=tracker.get_sot("number"),
#                             email=tracker.get_sot("email"))

def SendEmail(txt):

    # define content
    recipients = ["enter your email"]
    sender = "enter your email"
    subject = "Bot Chat with customer"

    """
    This is example text for MIMEText function

    # body =
    # Dear Student,
    # Please send your report
    # Thank you for your attention
    # 
    """
    recipt="hello world"
    ## Convertinng reciept data to sring format
    JSON_recipt = json.dumps(txt)

    # Code for sending recipt through email
    msg = MIMEText(JSON_recipt)

    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)

    # sending
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    #print("Enter your password for email login : ")
    password ='enter you passwoed' #getpass()
    session.login(sender, password)
    send_it = session.sendmail(sender, recipients, msg.as_string())
    session.quit()
    #Note: go in that link and allow to bot send you email
    #https://myaccount.google.com/lesssecureapps?rapt=AEjHL4M19QDj7hRxzh8hudctoJA03PNJ_JOVHtTu-G0bEHgTtzNN1S8RAXe9PBhfLLw-6WISTU6fBZaMcQKlDnXNY4fQ0IYi5w
