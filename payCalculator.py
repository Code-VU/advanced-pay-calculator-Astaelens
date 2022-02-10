def calculatePay():
    
    # This first line is provided for you
    hrs = input("Enter Hours:")
    rate = input("Enter Rate: ")
    try: 
        fhrs = float(hrs)
        frate = float(rate)
        Pay = fhrs*frate
        if fhrs> 40:
            OT= fhrs - 40
            Pay = fhrs*frate + .5*OT*frate
        print(Pay)    
    except:
        print("Please enter a number")      

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()
