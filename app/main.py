# main.py 

import sys
if sys.version_info<(3,6):
    print("Requires Python 3.6 or later, halting.")
    raise Requires36

from flask import Flask, request, session
app = Flask(__name__)

#---------------------------------------------------------------------

@app.route("/")
def hello():
    return "Hello World!"

#---------------------------------------------------------------------

def main():
    HOST="127.0.0.1"
    PORT="9033"
    app.run(host=HOST, port=PORT)

if __name__ == '__main__':
    print("Starting web app...")
    main()
    
#end
