## default fallback
* out_of_scope
  - utter_default

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## support path
* get_support
  - action_get_support

## locate atm given no data
* get_atm_location
  - utter_ask_location
* get_location{"location" : "Pune"}
  - action_get_atm_location
  - utter_did_that_help
* affirm
  - utter_happy
* deny
  - utter_try_again
* goodbye
  - utter_goodbye

## locate atm given location 
* get_atm_location{"location" : "Pune" }
  - action_get_atm_location
  - utter_did_that_help
* affirm
  - utter_happy
* deny
  - utter_try_again
* goodbye
  - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* get_support{"support_type": "support"}
    - action_get_support
* thanks
    - utter_did_that_help
* stop
    - utter_goodbye

## business_overview_story
* greet
    - utter_greet
* get_support{"support_type":"business overview"}
    - action_get_support
    - utter_did_that_help
* thanks
    - utter_welcome
## report_story_1
* greet
    - utter_greet
* get_support{"support_type": "report", "report_type": "theft"}
    - action_get_support
    - utter_did_that_help
* affirm
    - utter_happy

## report_story_4
* greet
    - utter_greet
* get_support{"support_type": "report", "report_type": "merchant"}
    - action_get_support
    - utter_did_that_help
* affirm
    - utter_happy

## report_story_3
* greet
    - utter_greet
* get_support{"support_type": "report"}
    - utter_ask_reporttype
* get_support{"report_type": "theft"}
    - action_get_support
* thanks
    - utter_welcome
    
## report_story_2
* greet
    - utter_greet
* get_support{"support_type": "report", "report_type": "fraud"}
    - action_get_support
    - utter_did_that_help
* deny
    - action_default_fallback