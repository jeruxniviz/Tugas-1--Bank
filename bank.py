# 220535601751 - Muhammad Abdul Aziz - S1 TI B 

greeting = input("Greeting : ").strip().lower()

if greeting=="hello" or greeting[0:5]=="hello":
    print("output = $0")
elif "hello" in greeting : #cek apakah ada hello dalam kalimat
    print("output = $0")
elif greeting[0]=="h" : 
    print("output = $20")
else : 
    print("output = $100")