## say goodbye
* goodbye
  - utter_goodbye

## chitchat
* greet
  - utter_greet
* chitchat
   - respond_chitchat

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

## locate atm given location happy
* greet
  - utter_greet
* get_atm_location{"location" : "Pune" }
  - action_get_atm_location
* thanks
  - utter_welcome

## card_story_1
* greet
    - utter_greet
* get_support{"support_type": "cards"}
    - action_get_support
    - utter_ask_cardtype

## career_story_1
* greet
    - utter_greet
* get_support{"support_type": "career"}
    - action_get_support
* thanks
  - utter_welcome

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

## support_story_1
* greet
    - utter_greet
* get_support{"support_type": "support"}
    - action_get_support
* thanks
    - utter_welcome

## surcharge_story_1
* greet
    - utter_greet
* get_support{"support_type": "surcharge"}
    - action_get_support
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