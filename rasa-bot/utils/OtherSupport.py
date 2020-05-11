class OtherSupport:
    @classmethod
    def getResponse(cls, supportType):
        if supportType == "financial education":
            message = "For financial support, please check out following link:"
            link = "https://www.mastercard.us/en-us/personal/get-support/financial-education.html"
        elif supportType == "convert currency":
            message = "For converting currency, please check out following link:"
            link = "https://www.mastercard.us/en-us/personal/get-support/convert-currency.html"
        elif supportType == "reload a prepaid card":
            message = "For reloading a prepaid card, please check out following link:"
            link = "https://www.mastercard.us/en-us/personal/get-support/reload-a-prepaid-card.html"
        elif supportType == "pay tax":
            message = "For paying tax, please check out following link:"
            link = "https://www.mastercard.us/en-us/personal/get-support/pay-taxes.html"
        elif supportType == "report problem shopping":
            message = "For reporting problem, please check out following link:"
            link = "https://www.mastercard.us/en-us/personal/get-support/report-problem-shopping.html"
        elif supportType == "cash back store locator":
            message = "To get access to your cash at checkout, please check out following link:"
            link = "https://www.mastercard.us/en-us/personal/get-support/cash-back-store-locator.html"
        elif supportType == "support":
            message = "To get support, please check out following link:"
            link = "https://www.mastercard.us/en-us/personal/get-support.html"
        elif supportType == "find card":
            message = "To find a card, please check out following link:"
            link = "https://www.mastercard.us/en-us/personal/find-a-card.html"
        elif supportType == "ways to pay":
            message = "To pay, please check out following link:"
            link = "https://www.mastercard.us/en-us/personal/ways-to-pay.html"
        elif supportType == "business overview":
            message = "For business, please check out following link:"
            link = "https://www.mastercard.us/en-us/business/overview.html"
        elif supportType == "mastercard contactless":
            message = "To try mastercard contactless, please check out following link:"
            link = "https://www.mastercard.us/en-us/business/overview/grow-your-business/improve-checkout/mastercard-contactless.html"
        elif supportType == "bill payment service":
            message = "For bill payment services, please check out following link:"
            link = "https://www.mastercard.us/en-us/business/overview/grow-your-business/improve-checkout/bill-payment-services.html"
        elif supportType == "business cards":
            message = "To get a business card, please check out following link:"
            link = "https://www.mastercard.us/en-us/business/overview/cards.html"
        elif supportType == "start accepting":
            message = "For knowing more about accepting, please check out following link:"
            link = "https://www.mastercard.us/en-us/business/overview/start-accepting.html"
        elif supportType == "business support":
            message = "For business support, please check out following link:"
            link = "https://www.mastercard.us/en-us/business/overview/support.html"
        elif supportType == "merchant safety and security":
            message = "For knowing more about safety and security, please check out following link:"
            link = "https://www.mastercard.us/en-us/business/overview/safety-and-security.html"
        elif supportType == "grow your business":
            message = "For growing your business, please check out following link:"
            link = "https://www.mastercard.us/en-us/business/large-enterprise/grow-your-business.html"
        elif supportType == "manage employee expenses":
            message = "For managing employee expenses, please check out following link:"
            link = "https://www.mastercard.us/en-us/business/large-enterprise/manage-employee-expenses.html"
        elif supportType == "authentication services":
            message = "For knowing more about authentication services, please check out following link:"
            link = "https://www.mastercard.us/en-us/business/large-enterprise/safety-security/authentication-services.html"
        elif supportType == "manage customer needs":
            message = "For managing your customer needs, please check out following link:"
            link = "https://www.mastercard.us/en-us/business/issuers/manage-your-consumer-needs.html"
        elif supportType == "business payments":
            message = "For knowing more about business payments, please check out following link:"
            link = "https://www.mastercard.us/en-us/business/issuers/business-payments.html"
        elif supportType == "issuer safety and security":
            message = "For knowing more about business payments, please check out following link:"
            link = "https://www.mastercard.us/en-us/business/issuers/safety-security.html"
        elif supportType == "issuer support":
            message = "To explore our issuer support resources, please check out following link:"
            link = "https://www.mastercard.us/en-us/business/issuers/get-support.html"
        elif supportType == "government support":
            message = "To learn more about how Mastercard supports government, please check out following link:"
            link = "https://www.mastercard.us/en-us/business/governments/get-support.html"
        elif supportType == "global locations":
            message = "For knowing Mastercard global locations, please check out following link:"
            link = "https://www.mastercard.us/en-us/vision/who-we-are/global-locations.html"
        elif supportType == "career":
            message = "To know career opportunities in Mastercard, please check out following link:"
            link = "https://www.mastercard.us/en-us/vision/who-we-are/careers.html"
        elif supportType == "click to pay":
            message = "To know more about Mastercard click to pay, please check out following link:"
            link = "https://checkout.mastercard.com/clicktopay/en-us.html"
        else:
            message = "Sorry, didn't get that"
            link = None

        res = [message, link]
        return res