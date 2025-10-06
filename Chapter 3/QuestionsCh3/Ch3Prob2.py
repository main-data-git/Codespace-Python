name = input("Enter Your Name : ")
date = input("Enter Date in DD/MM/YYYY format : ")

letter = '''Dear <|Name|>,
You are selected!
Date : <|DATE|>'''
            
            
print(letter.replace("<|Name|>",name).replace("<|DATE|>",date))