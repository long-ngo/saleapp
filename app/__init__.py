from flask import Flask

app = Flask(__name__)

#os.urandom(16)
app.secret_key = "^\x86\xd9t\xe6hJ\xde\xc0a\xb5F\x978=\x1e"

# app.template_folder=templates -> default
# app.static_folder=static -> default