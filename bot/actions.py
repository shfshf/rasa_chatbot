from rasa_core.actions.action import Action
from rasa_core.actions.forms import FormAction, EntityFormField
from rasa_core.events import SlotSet

from api.fund import FundSearch

class ActionFundSearchResponse(Action):
    def name(self):
        return 'action_fund_search_response'

    def run(self, dispatcher, tracker, domain):
        results = FundSearch().search({
            'fund_type':tracker.get_slot('fund_type'),
            'fund_company':tracker.get_slot('fund_company'),
            'fund_topic':tracker.get_slot('fund_topic'),
            'fund_achievement_duration':tracker.get_slot('fund_achievement_duration'),
            'fund_achievement_topk':tracker.get_slot('fund_achievement_topk'),
        })
        dispatcher.utter_message(results.__str__())
        return [SlotSet("search_results", results)]

# FormAction:
# Collecting Information to Complete a Request (Slot Filling)

class ActionFundSearchWithAchievement(FormAction):
    
    RANDOMIZE = False

    @staticmethod
    def required_fields():
        return [
            EntityFormField("duration", "fund_achievement_duration"), # entity_name, slot_name
            EntityFormField("topk", "fund_achievement_topk"),
        ]

    def name(self):
        return 'action_fund_search_with_achievement'

    def submit(self, dispatcher, tracker, domain):
        results = FundSearch().search({
            'fund_achievement_durationation':tracker.get_slot("fund_achievement_duration"),
            'fund_achievement_topk':tracker.get_slot("fund_achievement_topk")
        })
        dispatcher.utter_message(results.__str__())
        return [SlotSet("search_results", results)]