## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
  
## default fallback
* bot_challenge
  - action_default_fallback

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

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
  - utter_ask_pincode
* deny
  - action_get_atm_location
* get_pincode{"pincode" : "411014"}
  - action_get_atm_location
* goodbye
  - utter_goodbye

## locate atm given location 
* get_atm_location{"location" : "Pune" }
  - utter_ask_pincode
* deny
  - action_get_atm_location
* get_pincode{"pincode" : "411014"}
  - action_get_atm_location
* goodbye
  - utter_goodbye

## locate atm given location + pincode
* get_atm_location{"location" : "Pune", "pincode" : "411014" }
  - action_get_atm_location
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
## interactive_story_1
* greet
    - utter_greet
* get_support{"support_type": "report problem shopping"}
    - action_get_support
    - utter_did_that_help
* affirm
    - utter_happy
    
## interactive_story_X
* greet
    - utter_greet
* get_support{"support_type": "report problem shopping"}
    - action_get_support
    - utter_did_that_help
* deny
    - action_default_fallback

## interactive_story_1
* greet
    - utter_greet
* get_atm_location{"location": "akola"}
    - slot{"location": "akola"}
    - utter_ask_pincode
* get_pincode{"pincode": "444002"}
    - action_get_atm_location
* thanks
    - utter_welcome
