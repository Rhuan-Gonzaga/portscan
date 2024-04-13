from pip._vendor import requests


portas = {21,22,23,25,139,445,443,80,8000,3306,5432,8080,888,8443,3389,9000}

for port in portas:
    print("Testando porta ["+str(port)+"]:")
    r=requests.get("url:"+str(port))
    print(len(r.text))
    print(r.text)