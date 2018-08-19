from bottle import route, run, static_file

@route('/')
def main():
    return static_file("index.html", root=".")

@route('/echo/<thing>')
def echo(thing):
    return "Say hello to my dear friend: {}!".format(thing)

run(host="localhost",port=9999, debug=True, reloader=True)
