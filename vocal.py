vocal = "aiueoAIUEO"
input = input("Masukkan Sebuah Kata : ")

for letter in vocal:
    if letter in vocal:
        input = input.replace(letter, "")

print(input)
