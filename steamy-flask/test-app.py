# On this example we are going to show how to send a file
# to the browser for the user to "Download" it, instead
# of just outputing text.
# To ilustrate this, the default route will print a CSV file
# while the download route will open a "Save as..." dialog
# Browse the /download route to see it in action

from flask import Flask, make_response

# Initialize the Flask application
app = Flask(__name__)

# This route will just print some csv lines
@app.route('/')
def index():
    csv = """"REVIEW_DATE","AUTHOR","ISBN","DISCOUNTED_PRICE"
"1985/01/21","Douglas Adams",0345391802,5.95
"1990/01/12","Douglas Hofstadter",0465026567,9.95
"1998/07/15","Timothy ""The Parser"" Campbell",0968411304,18.99
"1999/12/03","Richard Friedman",0060630353,5.95
"2004/10/04","Randel Helms",0879755725,4.50"""
    return csv

# This route will prompt a file download with the csv lines
@app.route('/download')
def download():
    csv = """"REVIEW_DATE","AUTHOR","ISBN","DISCOUNTED_PRICE"
"1985/01/21","Douglas Adams",0345391802,5.95
"1990/01/12","Douglas Hofstadter",0465026567,9.95
"1998/07/15","Timothy ""The Parser"" Campbell",0968411304,18.99
"1999/12/03","Richard Friedman",0060630353,5.95
"2004/10/04","Randel Helms",0879755725,4.50"""
    # We need to modify the response, so the first thing we 
    # need to do is create a response out of the CSV string
    response = make_response(csv)
    # This is the key: Set the right header for the response
    # to be downloaded, instead of just printed on the browser
    response.headers["Content-Disposition"] = "attachment; filename=books.csv"
    return response

if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=int("80"),
        debug=True
    )