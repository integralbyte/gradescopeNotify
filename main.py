import requests
from lxml import html
import time

def getElementXPath(id):
    return f'//*[@id="assignments-student-table"]/tbody/tr[{id}]/td[1]/div/text()'

def getElementText(id, signed_token, courseID):
    gradeScopeURL = f"https://www.gradescope.com/courses/{courseID}"
    gradeScopeCookies = cookies = {
        "signed_token": signed_token
        }

    gradescopeResponse = requests.get(gradeScopeURL, cookies=gradeScopeCookies)
    gradescopeHTML = html.fromstring(gradescopeResponse.content)
    
    elementXPath = getElementXPath(id)
    resultValue = gradescopeHTML.xpath(elementXPath)
    return "".join(resultValue)


id = input("Assignment Number: ") #The assignment number is sorted starting with 1 being the first (oldest) assignment
assignmentName = input("Assignment Name: ")
signed_token = input("GradeScope signed_token Cookie: ")
courseID = input("Course ID: ")

while ("/" not in getElementText(id, signed_token, courseID)):
    print("Results not released!")
    time.sleep(60)
       
print("Results released!")


webhookURL = "https://discord.com/api/webhooks/..." #Hard-coded as this is unlikely to change and only reqiures a one-time edit.
data = {"content": f"{assignmentName} marks released!"}

response = requests.post(webhookURL, data=data)
