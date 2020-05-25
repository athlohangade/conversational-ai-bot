## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- Hi bot
- Hey bot
- hello bot
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there
- greetings
- hello is anybody there
- hello robot
- hello hi
- hey dude
- hi can you speak?
- hi friend
- hola

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- bye bye
- Bye!
- catch you later
- bye for now
- Bye bot
- Goodbye friend
- gotta go
- See you
- goodnight
- have a nice day
- i'm off
- see you later alligator
- we'll speak soon
- bye was nice talking to you
- ok bye
- Yo bro

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- I agree
- I accept
- Cool
- Awesome
- Great
- I get it
- ok
- Nice
- ofcourse
- Oh yes
- Oh, ok
- okay
- okay!
- sure
- yea
- yup
- yeah
- yep
- fine
- good
- ok cool
- ok friend
- ok good
- ok great
- thats fine
- thats good
- thats great
- got it

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- I don't want to
- nah
- no thank you
- no, not really
- nope
- nah I'm good
- i'm not sure
- na
- n
- no sorry
- no thanks
- not yet
- oh no

## intent: chitchat/ask_whats_possible
- what can you do?
- How can you help me
- tell me what can you do

## intent: chitchat/mood_happy
- I am good
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good
- fantastic
- I am on cloud nine
- extremely happy

## intent: chitchat/mood_unhappy
- I am bored
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad
- angry

## intent: chitchat/ask_how_are_you
- How are you?
- How you doing
- tell me what can you do
- What's going on?
- wassup
- whats up
- howdy
- How do you do?
- How are you feeling?
- What’s sizzling?

## intent: chitchat/insult
- stupid bot
- you are stupid
- idiot
- you are waste of time
- useless bot
- you are dumb

## intent: chitchat/ask_weather
- how's weather?
- is it sunny where you are?

## intent: chitchat/bot_challenge
- what's your name
- who are you?
- what are you called?
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?
- are you a chat bot?
- are you a bot
- are you a human
- am I talking to a bot
- am I talking to a human
- are you a chat bot
- bot?
- you are chatbot
- i guess you are a chatbot
- who are you?

## intent:get_support
- I want to [reload](support_type) a prepaid card
- I want to [reload](support_type) my prepaid card
- Help me to [reload](support_type) a prepaid card
- Help me to [reload](support_type) my prepaid card
- [reload](support_type) a prepaid card

- How to [convert](support_type) currency
- [convert](support_type) currency
- I want to [convert](support_type) my currency
- Open mastercard currency [converter]{"entity": "support_type", "value": "convert"}
- Help me in [converting]{"entity": "support_type", "value": "convert"} my currency
- is currency [conversion]{"entity": "support_type", "value": "convert"} possible here?

- How to pay [taxes]{"entity": "support_type", "value": "tax"}
- How to pay [tax](support_type)
- How to pay [tax](support_type)?
- I want to pay [tax](support_type)
- pay [tax](support_type)

- [cash] back store locator(support_type)
- Get access to my [cash](support_type)
- I want to get access to my [cash](support_type)
- get [cash](support_type) when paying with Debit
- find the nearest [cash](support_type) back store
- find the nearest [cashback]{"entity": "support_type", "value": "cash"} store

- [report](support_type) problem [shopping]{"entity": "report_type", "value": "merchant"}
- [report](support_type) a problem
- I want to [report](support_type) a problem
- How to [report](support_type) a problem
- I want to [report](support_type) [merchant](report_type)
- I have a [problem]{"entity": "support_type", "value": "report"} with [merchant](report_type)
- [Merchant](report_type) refused to accept mastercard. What should I do?
- I am not able to [buy]{"entity": "report_type", "value": "merchant"} things using mastercard
- The [merchant](report_type) is not ready to accept mastercard for transactions
- I am facing a [problem]{"entity": "support_type", "value": "report"} while [buying]{"entity": "report_type", "value": "merchant"} using mastercard
- I want to [report](support_type) the [merchant](report_type) who is not accepting mastercard transactions
- Someone called to offer a lower rate on my Mastercard but it seems to be a [scam]{"entity": "report_type", "value": "fraud"}. What should I do?
- I believe [fraudulent]{"entity": "report_type", "value": "fraud"} purchases were made on my Mastercard. How do I [report](support_type) it?
- I know who committed [fraud](report_type) on my Mastercard credit or debit card. How do I [report](support_type) it?
- How do I [report](support_type) potential [fraud](report_type)?
- i [lost]{"entity": "report_type", "value": "theft"} my card
- someone has [stolen]{"entity": "report_type", "value": "theft"} my card
- I want to [report](support_type) [theft](report_type)

- [support](support_type)

- [contactless](support_type)
- How to accept mastercard [contactless](support_type)
- Which merchants use [contactless](support_type)
- How [tap & go]{"entity": "support_type", "value": "contactless"} payments work
- Why [cashless]{"entity": "support_type", "value": "contactless"} payment is safer than cash?

- [bill](support_type) payment service
- Which cards can I use to pay [bills]{"entity": "support_type", "value": "bill"}?
- pay [bills]{"entity": "support_type", "value": "bill"} using mastercard
- How do I pay a [bill](support_type) with a Mastercard?
- Can I pay my [billers]{"entity": "support_type", "value": "bill"} who accept Mastercard directly from this site?
- What are the benefits of [bill](support_type) payment using a Mastercard?
- I want to know about [bill](support_type) payment services at mastercard
- How [billers]{"entity": "support_type", "value": "bill"} are benefited if I pay using mastercard ?

- [authentication](support_type) services at mastercard
- how does mastercard [authenticate]{"entity": "support_type", "value": "authentication"}

- global [locations](support_type)
- where is mastercard [located]{"entity": "support_type", "value": "locations"}
- where is mastercard [situated]{"entity": "support_type", "value": "locations"}
- mastercard [office]{"entity": "support_type", "value": "locations"}
- [locations](support_type) of mastercard

- [career](support_type)
- [career](support_type) opportunities at mastercard
- I want to Apply for [job]{"entity": "support_type", "value": "career"}
- I want to [work]{"entity": "support_type", "value": "career"} in mastercard
- I want to relaunch my [career](support_type)
- how to [join]{"entity": "support_type", "value": "career"} mastercard
- how is [work]{"entity": "support_type", "value": "career"} at mastercard
- i am in search of [job]{"entity": "support_type", "value": "career"}
- i am searching for [job]{"entity": "support_type", "value": "career"}
- i am looking for [job]{"entity": "support_type", "value": "career"}
- help me to get [job]{"entity": "support_type", "value": "career"}
- help me to get [job]{"entity": "support_type", "value": "career"} opportunities at mastercard
- how to apply for [job]{"entity": "support_type", "value": "career"} in mastercard
- [job]{"entity": "support_type", "value": "career"} opportunities at mastercard
- [internship]{"entity": "support_type", "value": "career"} at mastercard
- what are the benefits of [internship]{"entity": "support_type", "value": "career"} at Mastercard

- i want to get [support](support_type)

- A merchant wanted to charge a [surcharge](support_type) or fee to use my Mastercard. What should I do?
- What should I do if the merchant [surcharge](support_type) was higher than I expected?
- What are the types of permissible [surcharges]{"entity": "support_type", "value": "surcharge"}?

- find [card]{"entity": "support_type", "value": "cards"}
- How many [cards](support_type) does Mastercard provide ?
- I am looking for a best suitable [card]{"entity": "support_type", "value": "cards"} for me
- find a [card]{"entity": "support_type", "value": "cards"} that's best for me
- I want [mastercard]{"entity": "support_type", "value": "cards"}
- I am looking for [business](card_type) [cards](support_type)
- I am looking for [debit](card_type) [cards](support_type)
- i am looking for a [card]{"entity": "support_type", "value": "cards"} for me
- i am looking for the perfect [mastercard]{"entity": "support_type", "value": "cards"} for me
- Show me all [credit](card_type) [cards](support_type) that Mastercard provide
- I am in search of a [card]{"entity": "support_type", "value": "cards"} that's best for me. Can you help me?
- Help me in choosing the best [card]{"entity": "support_type", "value": "cards"} for me
- Show me all types of [cards](support_type) that Mastercard provide
- Show me all [prepaid](card_type) [mastercard]{"entity": "support_type", "value": "cards"}
- Help me to get [mastercard]{"entity": "support_type", "value": "cards"}
- Help me to get a [debit](card_type) [mastercard]{"entity": "support_type", "value": "cards"}
- Apply for [mastercard]{"entity": "support_type", "value": "cards"}
- How do I apply for [mastercard]{"entity": "support_type", "value": "cards"}
- [debit](card_type) [cards](support_type)
- [credit](card_type) [cards](support_type)
- [prepaid](card_type) [cards](support_type)
- [business](card_type) [cards](support_type)

## intent:thanks
- thank you
- thanks
- that helped
- ty
- thankie
- Thanks

## intent:get_location
- [Pune](location)
- [Shivajinagar](location)
- It is [Kanpur](location)
- [Hadapsar](location)
- My location is [Shillong](location)
- I live in [Bhubaneshwar](location)
- [Pimpri](location)
- [Katraj](location)
- It is [Kanpur](location)
- [Viman Nagar](location)
- Location is [Kharagpur](location)
- [Akurdi](location)
- My location is [Wardha](location)
- [Chandigarh](location) it is
- I live in [Miami](location)
- [Ajmer](location)
- [Sydney](location)
- My location is [London](location)
- It is [Colombo](location)
- The location is [Yerwada](location)

## intent:get_atm_location
- atm location
- atm locations
- ATM location
- ATM locations
- Any atm locations
- I need an atm
- I need an ATM
- ATMs please
- ATM locations please
- Need some atm locations
- Would like to know atm locations
- Get some atm locations
- Find atms
- I am looking for an atm
- atm locations in [Kalyan](location)
- Any atm locations in [Vasai](location)
- Get the atm locations near [Pune](location)
- Get me some atm locations near [Katraj](location)
- Find the atms in [Sangvi](location)
- atms in [Kolkata](location)
- Will you please get the atms in [Solapur](location)
- Tell me some places near [Hampi](location) that have atms
- I need some atm locations near [Pimpri](location)
- Get some atm locations near [Viman Nagar](location)
- Show me some atm locations near [Shivajinagar](location)
- I want atm locators in [Pune](location)
- Would like know some ATMs near [Jodhpur](location)
- I am looking for some atms in [Dapodi](location)
- Need some information of atms in [Kothrud](location)
- I require some places in [Mysore](location) that have atms
- Please find atms nearest to [Shahapur](location)
- Get me the list of atm locations near [Jalgaon](location)
- Want to know ATMs in [Baroda](location)
- Find me some atms in [Shivajinagar](location)
- Get some ATM locations near [Viman Nagar](location)
- Show the atm locations in [Satara](location)
- I would like to know some atms near [Gandhi Nagar](location)
- atms in [Akola](location)
- Please find me atms in [Rajkot](location)
- Will you do me a favour of finding atm locations near [Gurgaon](location)
- I require locations of ATMs near [Bangalore](location)
- ATMs in [Dhule](location) please
- Is there any atm [Lonavala](location)
- Find atms in [Jaipur](location)
- I want to know locations of atm in [Beijing](location)

## synonym:business cards
- business debit
- business prepaid
- Mastercard business prepaid card
- card for business
- debit mastercard business card
- business credit cards
- world elite business
- world elite mastercard for business
- business card
- payment solution for business
- payment solutions for business
## synonym:authentication
- authenticate
- biometric
- biometrics

## synonym:report
- problem
- reported
- reporting

## synonym:fraud
- fraudulent
- scam

## synonym:surcharge
- surcharges

## synonym:theft
- stolen
- lost

## synonym:contactless
- cashless
- tap & go

## synonym:locations
- located
- situated
- office

## synonym:career
- join
- joining
- joins
- job
- work
- works
- jobs
- working
- life
- lifes
- hire
- hiring
- hires
- career
- careers
- internship
- opportunities
- opportunity

## synonym:bill
- bills
- billers

## synonym:cash
- money
- cashback

## synonym:convert
- convert
- currency
- converter
- converting
- converted
- conversion

## synonym:cards
- mastercard
- card

## synonym:tax
- taxes
- GST

## synonym:reload
- reloading
- topup
- recharge

## synonym:support
- help

## synonym:merchant
- buy
- shopping
- buy
- buying

## synonym:ways to pay
- payment methods
- pay your way
- pay
- pay MTA

## lookup:support_type
lookup-files/search-lookup.txt

## lookup:location
lookup-files/citynames.txt
