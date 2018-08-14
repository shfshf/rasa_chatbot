## path greet->type
* greet
  - utter_greet
* fund_search_with_type{"fund_type": "股基"}
  - utter_working_on_it
  - action_fund_search_response
  - utter_response_fund

## path type
* fund_search_with_type{"fund_type": "债基"}
  - utter_working_on_it
  - action_fund_search_response
  - utter_response_fund

## path greet->company—>type 
* greet
  - utter_greet
* fund_search_with_type{"fund_type": "股基"}
  - utter_ask_company
* fund_search_with_company{"fund_company": "易方达"}
  - utter_working_on_it
  - action_fund_search_response
  - utter_response_fund

## path company—>type
* fund_search_with_type{"fund_type": "股基"}
  - utter_ask_company
* fund_search_with_company{"fund_company": "易方达"}
  - utter_working_on_it
  - action_fund_search_response
  - utter_response_fund

## path greet->topic->company—>type 
* greet
  - utter_greet
* fund_search_with_topic{"fund_topic": "2025规划"}
  - utter_ask_topic
* fund_search_with_type{"fund_type": "股基"}
  - utter_ask_company
* fund_search_with_company{"fund_company": "易方达"}
  - utter_working_on_it
  - action_fund_search_response
  - utter_response_fund

## path topic->company—>type
* fund_search_with_topic{"fund_topic": "2025规划"}
  - utter_ask_topic
* fund_search_with_type{"fund_type": "股基"}
  - utter_ask_company
* fund_search_with_company{"fund_company": "易方达"}
  - utter_working_on_it
  - action_fund_search_response
  - utter_response_fund

## path greet->achievement{fund_achievement_topk}
* greet
  - utter_greet
* fund_search_with_achievement{"fund_achievement_topk": "10"}
  - action_fund_search_with_achievement
  - slot{"fund_achievement_topk": "10"}
  - slot{"requested_slot": "fund_achievement_duration"}

## path greet->achievement{fund_achievement_duration}
* greet
  - utter_greet
* fund_search_with_achievement{"fund_achievement_duration": "1y"}
  - action_fund_search_with_achievement
  - slot{"fund_achievement_duration": "1y"}
  - slot{"requested_slot": "fund_achievement_topk"}
