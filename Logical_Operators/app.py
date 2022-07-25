# if applicant has high income OR, AND good credit 
#   Eligible for loan
# and: both conditons
# or: at least one conditions should be true
# not: inverses any boolean value you give it, converts True to False
# if applicant has good credit AND doesn't have a criminal record 
#   then eligble for loan

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")