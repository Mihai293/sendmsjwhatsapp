import pywhatkit

phone_number = ["+40725015306", "+40724013049"]
# phone_number = input("Numar telefon: ")
for n in phone_number:
    pywhatkit.sendwhatmsg(n, "test", 21, 40,)
# pywhatkit.sendwhatmsg(phone_number, "test", 21, 35)