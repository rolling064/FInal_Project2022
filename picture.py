from transitions.extensions import GraphMachine
import pygraphviz as pgv
from Leefsm import TocMachine

machine = TocMachine(
    states=['user','1st_level_folder','password','secret','ncku_folder','math','csie','nckuedu','entertainment_folder','facebook','youtube','twich','google_folder','translation','drive','gmail','end'],
    transitions=[{'trigger': 'advance', 'source': 'user', 'dest':'1st_level_folder', 'conditions':'is_going_to_1st_level_folder'},
                 {'trigger': 'advance', 'source': 'user', 'dest':'password', 'conditions':'is_going_to_password'},
                 {'trigger': 'advance', 'source': 'password', 'dest':'secret', 'conditions':'is_going_to_secret'},

                 {'trigger': 'advance', 'source': '1st_level_folder', 'dest':'ncku_folder', 'conditions':'is_going_to_ncku_folder'},
                 
                 {'trigger': 'advance', 'source': '1st_level_folder', 'dest':'ncku_folder', 'conditions':'is_going_to_ncku_folder'},
                 {'trigger': 'advance', 'source': 'ncku_folder', 'dest':'1st_level_folder', 'conditions':'back_to_1st_level_folder'},
                 {'trigger': 'advance', 'source': '1st_level_folder', 'dest':'entertainment_folder', 'conditions':'is_going_to_entertainment_folder'},
                 {'trigger': 'advance', 'source': 'entertainment_folder', 'dest':'1st_level_folder', 'conditions':'back_to_1st_level_folder'},
                 {'trigger': 'advance', 'source': '1st_level_folder', 'dest':'google_folder', 'conditions':'is_going_to_google_folder'},
                 {'trigger': 'advance', 'source': 'google_folder', 'dest':'1st_level_folder', 'conditions':'back_to_1st_level_folder'},
                 {'trigger': 'advance', 'source': '1st_level_folder', 'dest':'end', 'conditions':'is_going_to_end'},

                 {'trigger': 'advance', 'source': 'ncku_folder', 'dest':'math', 'conditions':'is_going_to_math'},
                 {'trigger': 'advance', 'source': 'math', 'dest':'ncku_folder', 'conditions':'back_to_ncku_folder'},
                 {'trigger': 'advance', 'source': 'ncku_folder', 'dest':'csie', 'conditions':'is_going_to_csie'},
                 {'trigger': 'advance', 'source': 'csie', 'dest':'ncku_folder', 'conditions':'back_to_ncku_folder'},
                 {'trigger': 'advance', 'source': 'ncku_folder', 'dest':'nckuedu', 'conditions':'is_going_to_nckuedu'},
                 {'trigger': 'advance', 'source': 'nckuedu', 'dest':'ncku_folder', 'conditions':'back_to_ncku_folder'},

                 {'trigger': 'advance', 'source': 'entertainment_folder', 'dest':'facebook', 'conditions':'is_going_to_facebook'},
                 {'trigger': 'advance', 'source': 'facebook', 'dest':'entertainment_folder', 'conditions':'back_to_entertainment_folder'},
                 {'trigger': 'advance', 'source': 'entertainment_folder', 'dest':'youtube', 'conditions':'is_going_to_youtube'},
                 {'trigger': 'advance', 'source': 'youtube', 'dest':'entertainment_folder', 'conditions':'back_to_entertainment_folder'},
                 {'trigger': 'advance', 'source': 'entertainment_folder', 'dest':'twich', 'conditions':'is_going_to_twich'},
                 {'trigger': 'advance', 'source': 'twich', 'dest':'entertainment_folder', 'conditions':'back_to_entertainment_folder'},

                 {'trigger': 'advance', 'source': 'google_folder', 'dest':'translation', 'conditions':'is_going_to_translation'},
                 {'trigger': 'advance', 'source': 'translation', 'dest':'google_folder', 'conditions':'back_to_google_folder'},
                 {'trigger': 'advance', 'source': 'google_folder', 'dest':'drive', 'conditions':'is_going_to_drive'},
                 {'trigger': 'advance', 'source': 'drive', 'dest':'google_folder', 'conditions':'back_to_google_folder'},
                 {'trigger': 'advance', 'source': 'google_folder', 'dest':'gmail', 'conditions':'is_going_to_gmail'},
                 {'trigger': 'advance', 'source': 'gmail', 'dest':'google_folder', 'conditions':'back_to_google_folder'},

                 {'trigger': 'go_back', 'source': ['math','csie','nckuedu','facebook','youtube','twich','translation','drive','gmail','end','secret',], 'dest':'user',},
                
                 {'trigger': 'advance', 'source': '1st_level_folder', 'dest':'1st_level_folder'},
                 {'trigger': 'advance', 'source': 'ncku_folder', 'dest':'ncku_folder'},
                 {'trigger': 'advance', 'source': 'entertainment_folder', 'dest':'entertainment_folder'},
                 {'trigger': 'advance', 'source': 'google_folder', 'dest':'google_folder'},
                ],
)

 
machine.get_graph().draw('fsm.png', prog='dot')