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
- wassup
- whats up
- Hello

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

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
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

## intent:bot_challenge
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
- How to pay [taxes]{"entity": "support_type", "value": "tax"}
- How to pay [tax](support_type)
- I want to pay [tax](support_type)
- pay [tax](support_type)
- [cash] back store locator(support_type)
- Get access to my [cash](support_type)
- I want to get access to my [cash](support_type)
- get [cash](support_type) when paying with Debit
- find the nearest [cash](support_type) back store
- find the nearest [cashback]{"entity": "support_type", "value": "cash"} store
- [report](support_type) problem shopping
- [report](support_type) a problem
- I want to [report](support_type) a problem
- How to [report](support_type) a problem
- I want to [report](support_type) merchant
- I have a [problem](support_type) with merchant
- [support](support_type)
- [find card](support_type)
- I want [mastercard]{"entity": "support_type", "value": "find card"}
- [ways to pay](support_type)
- [payment methods]{"entity": "support_type", "value": "ways to pay"}
- [business overview](support_type)
- [start accepting]{"entity": "support_type", "value": "business overview"}
- [bill] payment service(support_type)
- pay [bills] using mastercard
- [business cards](support_type)
- [authentication](support_type) services at mastercard
- how does mastercard [authenticate]{"entity": "support_type", "value": "authentication"}
- global [locations](support_type)
- where is mastercard [located]{"entity": "support_type", "value": "locations"}
- where is mastercard [situated]{"entity": "support_type", "value": "locations"}
- mastercard [office]{"entity": "support_type", "value": "locations"}
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
- i [lost]{"entity": "support_type", "value": "support"} my card
- someone has [stolen]{"entity": "support_type", "value": "support"} my card

## lookup:support_type
lookup-files/search-lookup.txt

## synonym:authentication
- authenticate
- biometric
- biometrics

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

## synonym:cash
- money
- cashback

## synonym:convert
- convert
- currency
- converter

## synonym:find card
- get mastercard
- get card
- personal card
- standard mastercard
- world mastercard
- world elite mastercard
- standard credit card
- debit mastercard
- prepaid travel card
- prepaid gift card
- mastercard prepaid
- world debit mastercard
- enhanced debit mastercard
- credit card
- debit card
- prepaid card
- all cards

## synonym:tax
- taxes

## synonym:reload
- reloading

## synonym:report
- problem
- reported
- reporting

## synonym:support
- help
- lost
- stolen
- theft

## synonym:ways to pay
- payment methods
- pay your way
- pay
- pay MTA

## intent:thanks
- thank you
- thanks
- that helped
- ty
- thankie
- Thanks

## intent:get_pincode
- [411014](pincode)
- [510011](pincode)
- [411009](pincode)
- [411044](pincode)
- [411035](pincode)
- [510987](pincode)
- [787182](pincode)
- [444002](pincode)

## intent:get_location
- [Pune](location)
- [Shivajinagar](location)
- [Hadapsar](location)
- [Pimpri](location)
- [Katraj](location)
- [Viman Nagar](location)
- [Akurdi](location)

## intent:get_atm_location
- atm location
- atm locations
- ATM location
- ATM locations
- Any atm locations
- I need an atm
- I need an ATM
- I am looking for an atm
- atm locations in [Kalyan](location)
- Any atm locations in [Vasai](location)
- Get the atm locations near [Pune](location)
- Get me some atm locations near [Katraj](location)
- Find the atms in [Sangvi](location)
- Will you please get the atms in [Solarpur](location)
- I need some atm location near [Pimpri](location)
- Get some atm locations near [Viman Nagar](location)
- Show me some atm locations near [Shivajinagar](location)
- I want atm locators in [Pune](location)
- I am looking for some atms in [Dapodi](location)
- Need some information of atms in [Kothrud](location)
- Find me some atms in [Shivajinagar](location)
- Get some ATM locations near [Viman Nagar](location)
- Show the atm locations in [Satara](location)
- atms in [pune](location)
- atms in [Kolkata](location)
- atms in [akola](location)
