import sys

sys.dont_write_bytecode = True

from application import app
# imports from init file

if __name__ == "__main__":
    app.run(debug=True)