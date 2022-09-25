from argparse import Action
from ast import List
from typing import Text, Any, Dict

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionSetResult(Action):

    def number(self) -> Text:
        return "action_set_result"
    
    def run(
        self,
        dispacher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text,Any]]:
        input_numbers = {}

        input_numbers['num1'] = tracker.get_slot("first_number")
        input_numbers['num2'] = tracker.get_slot("second_number")
       
        Result = sum(input_numbers.values())

        # print(Result)

        return [
            SlotSet("result", Result)
        ]