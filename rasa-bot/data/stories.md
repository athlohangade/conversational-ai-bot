## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## support path
* get_support
  - action_get_support

## locate atm given no data happy
* greet
  - utter_greet
* get_atm_location
  - utter_ask_location
* get_location{"location" : "Pune"}
  - action_get_atm_location
  - utter_did_that_help
* affirm
  - utter_happy
* goodbye
  - utter_goodbye

## locate atm given no data sad 
* greet
  - utter_greet
* get_atm_location
  - utter_ask_location
* get_location{"location" : "Pune"}
  - action_get_atm_location
  - utter_did_that_help
* deny
  - utter_try_again
* goodbye
  - utter_goodbye

## locate atm given location happy
* greet
  - utter_greet
* get_atm_location{"location" : "Pune" }
  - action_get_atm_location
  - utter_did_that_help
* affirm
  - utter_happy
* goodbye
  - utter_goodbye

## locate atm given location sad
* greet
  - utter_greet
* get_atm_location{"location" : "Pune" }
  - action_get_atm_location
  - utter_did_that_help
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

## career_story_1
* greet
    - utter_greet
* get_support{"support_type": "career"}
    - action_get_support
    - utter_did_that_help
* affirm
    - utter_happy

## career_story_2
* greet
    - utter_greet
* get_support{"support_type": "career"}
    - action_get_support
    - utter_did_that_help
* deny
    - utter_submit_query

## tax_story_1
* greet
    - utter_greet
* get_support{"support_type": "tax"}
    - action_get_support
* thanks
    - utter_welcome

## reload_story_1
* greet
    - utter_greet
* get_support{"support_type": "reload"}
    - action_get_support
* thanks
    - utter_welcome

## convert_story_1
* greet
    - utter_greet
* get_support{"support_type": "convert"}
    - action_get_support
* thanks
    - utter_welcome

## convert_story_2
* greet
    - utter_greet
* get_support{"support_type": "convert"}
    - action_get_support
    - utter_did_that_help
* deny
    - utter_submit_query

## cashback_story_1
* greet
    - utter_greet
* get_support{"support_type": "cash"}
    - action_get_support
* thanks
    - utter_welcome

## bill_story_1
* greet
    - utter_greet
* get_support{"support_type": "bill"}
    - action_get_support
* thanks
    - utter_welcome

## location_story_1
* greet
    - utter_greet
* get_support{"support_type": "locations"}
    - action_get_support
    - utter_did_that_help
* thanks
    - utter_welcome

## support_story_1
* greet
    - utter_greet
* get_support{"support_type": "support"}
    - action_get_support
    - utter_did_that_help
* thanks
    - utter_welcome

## surcharge_story_1
* greet
    - utter_greet
* get_support{"support_type": "surcharge"}
    - action_get_support
    - utter_did_that_help
* thanks
    - utter_welcome

## report_story_1
* greet
    - utter_greet
* get_support{"support_type": "report"}
    - action_get_support
    - utter_ask_reporttype
    
## interactive_story_1
* greet
    - utter_greet
* get_atm_location{"location": "akola"}
    - action_get_atm_location
* thanks
    - utter_welcome
