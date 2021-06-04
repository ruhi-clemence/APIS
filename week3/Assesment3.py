## For the customer

detect_complain = {}


def register():
    if detect_complain:

        name = input('Enter your name: ')
        submit_complain = input('Kindly submit your complain: ')

        if submit_complain in detect_complain.keys() or name in detect_complain.values():
            print('Data already exist, please try again!')

        else:
            for record in detect_complain.values():
                if name in detect_complain.values():
                    print('Data already exists, please try again!')
                else:
                    detect_complain[submit_complain] = {'Name':name,'Complain':submit_complain}
                    print('Your complain has been submitted!')
                    print(detect_complain.values())
                    print('===================================')
                    break       
    else:
        name = input('Enter your name: ')
        submit_complain = input('Kindly submit your complain: ')
        detect_complain[submit_complain] = {'Name':name,'Complain':submit_complain}
        print(detect_complain)


def main():
    runtime = 1
    print('Welcome!')
    while runtime:
        checker = int(input('Enter 0 to submit your name, 1 for submit a complain, 2 to quit:'))
             

        if checker == 0:
            register()
        elif checker == 1:
            complain = input('Kindly submit your complain:')
        elif checker == 2:
               break 
        else:
            print('invalid value, try again')
            main()

main()
## For the team
import requests

complaints = [
    "This items does not function",
    "We were not taught that unit",
    "That ice-cream wasn't frosty",
    "My bread is not from jupiter",
    "I don't want to live forever"
]

print("\n\tComplaints from users.")
print("===============================")

for index, complaint in enumerate(complaints):
    print(str(index + 1) + ". " + complaint)

print("===============================\n")

prompt = f"Pick a complaint by inputting the number next to the complaint\n" \
         f"(It should be an integer ranging from 1 - {len(complaints)}):\n"
complaint_index = int(input(prompt))


complaint_choice = complaints[complaint_index]
print(complaint_choice)



url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

query = complaint_choice.replace(" ", "%20")

payload = f"q={query}"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

import json
data = json.loads(response.text)

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

query = complaint_choice.replace(" ", "%20")

payload = "q=Hello%2C%20world!&target=es&source=en"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
data = json.loads(response.text)



