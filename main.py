import requests
import zeep

wsdl = 'http://www.dneonline.com/calculator.asmx?WSDL'
client = zeep.Client(wsdl=wsdl)

responseAdd = client.service.Add(100, 20)
print(responseAdd)  # result: 120

responseSubtract = client.service.Subtract(100, 20)
print(responseSubtract)  # result: 80

responseMultiply = client.service.Multiply(10, 2)
print(responseMultiply)  # result: 20

responseDivide = client.service.Divide(100, 20)
print(responseDivide)  # result: 5

# prints the response
# print(result)
