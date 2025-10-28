principal_amt = int(input("Enter the Principal amount => "))
rate = int(input("Enter the Rate of interest(in percentage) => "))
time = int(input("Enter the Time Period => "))

def si_calc(a,b,c):
  interest = (a*b*c)/100
  return interest

print(f"The Simple Interest on {principal_amt} at the rate of {rate} % for {time} years is => {si_calc(principal_amt,rate,time)}")

print(f"The amount at the end of {time} years is => {principal_amt + si_calc(principal_amt,rate,time)}")
  
  