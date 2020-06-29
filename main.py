from flask import Flask
from flask import request
import re 

app = Flask(__name__)

@app.route('/')
def mainPage():
    imsi_header = request.headers.get('imsi')
    if imsi_header:
        if 0 < len(imsi_header) < 16:
            # if re.match('^[0-9a-zA-Z_]*$', imsi_header):
            if re.match('^\w*$', imsi_header):
                return 'IMSI Header is OK', 200
            else:
                return 'IMSI header can contain only digits, letters and symbol _', 500
        else:
            return 'String lenght shotter than 1 or longer than 15', 500
    else:
        return 'There is no IMSI header', 500

if __name__ == '__main__':
    app.run()
