import numpy_financial as npf
import numpy as np

# 1. Set up the Bond details
# assume annual number, period as year
principal = 10000 # face value, or future value. The principal amount will be received in maturity of bond
coupon_rate = 0.05
annual_interest = 0.06 # also could be interpreted as required rate of return, or the opportunity cost. In this cal, assume the interests rate remain constant during the life of bond
period = 4 # years
coupon_payment = coupon_rate * principal

# 2. Cal the bond price, it is just the present value of discounted future cashflow
# the npf.pv result is default as negative to represent cash outflow to buy the bond, so times with -1 to represent the pv only
bond_price = (npf.pv(annual_interest, period, coupon_payment, principal))*-1
bond_price = bond_price.round(2)
print("The price of bond is : $" + str(bond_price))

# 3. Cal the estimated YTM (Yield to Maturity)
# todo it is an approximation only, To calculate the actual yield to maturity requires trial and error by putting rates into the present value of a bond formula until P, or Price, matches the actual price of the bond.
# todo it doesn show the value of a  bond if the market interests change
# an annual rate, so can compare the value of bonds with different payment structure or period
# the total expected return, not net, for holding the bond to maturity, while some bonds are designed for possible early redemption, so pay attention to the assumption here
# also the IRR of the bond investment
# this is also a way to cal IRR other than listing the array of entire cashflow during the period
# the result means the annualized return of this bond investment is 7.89%, higher than the coupon rate
# the excess return comes from the extra $1000 we will receive in the maturity
# so this bond is selling at discount, while holder is encouraged to hold till maturity to realize the IRR
market_price = 9000

ytm = ((coupon_payment + (principal-market_price)/ period)) / ((principal + market_price)/2)
print('Set Market Price as :$' + str(market_price))
print("The YTM for this bond is: " + str(ytm*100) + "%")

# Remarks: Bond's value depends on the spread between coupon rate and market interests rate
# Reference: Imagine the market interest rate is 3% today and you just purchased a bond paying a 5% coupon with a face value of $1,000. If interest rates go down by 1% from the time of your purchase, you will be able to sell the bond for a profit (or a premium). This is because the bond is now paying more than the market rate (because the coupon is 5%).
#
# The spread used to be 2% (5% - 3%), but it's now increased to 3% (5% - 2%). This is a simplified way of looking at a bond's price, as many other factors are involved; however, it does show the general relationship between bonds and interest rates.
#
# As for the attractiveness of the investment, you can't determine whether a bond is a good investment solely based on whether it is selling at a premium or a discount. Many other factors should affect this decision, such as the expectation of interest rates and the credit worthiness of the bond itself.


# 4. Make it as a function for further application in other file
def bond_price_yield_cal(principal,coupon_rate,annual_interest,period,market_price):
    coupon_payment = coupon_rate * principal
    bond_price = (npf.pv(annual_interest, period, coupon_payment, principal)) * -1
    bond_price = bond_price.round(2)
    print("The price of bond is : $" + str(bond_price))
    ytm = ((coupon_payment + (principal - market_price) / period)) / ((principal + market_price) / 2)
    print('Set Market Price as :$' + str(market_price))
    print("The YTM for this bond is: " + str(ytm * 100) + "%")

bond_price_yield_cal(100,.04915,.0245,15,100) #if sell at face value, yield = coupon rate
bond_price_yield_cal(100,.04915,.0245,15,79.943) #higher, yild, since the company has risk concern, market price goes low, selling at discount
bond_price_yield_cal(100,.04915,.0045,15,100) #if interests rate went down due to monetary policy, the bonds with yield of 4.915% becomes more worthy
bond_price_yield_cal(100,.04915,.0545,15,100) #if interests rate went up due to monetary policy, the bonds with yield of 4.915% becomes less worthy
