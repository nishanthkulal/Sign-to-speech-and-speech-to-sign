import cv2
import os
import tornado.ioloop
import tornado.web
import json

isl_database = {
    'A':'GestureImages/A1.jpg',
    'B':'GestureImages/B.jpg',
    'C':'GestureImages/C.jpg',
    'D':'GestureImages/D1.jpg',
    'E':'GestureImages/E1.jpg',
    'F':'GestureImages/F.jpg',
    'G':'GestureImages/G.jpg',
    'H':'GestureImages/H2.jpg',
    'I':'GestureImages/I1.jpg',
    'J':'GestureImages/J1.jpg',
    'K':'GestureImages/K1.jpg',
    'L':'GestureImages/L1.jpg',
    'M':'GestureImages/M1.jpg',
    'N':'GestureImages/N1.jpg',
    'O':'GestureImages/O1.jpg',
    'P':'GestureImages/P1.jpg',
    'Q':'GestureImages/Q1.jpg',
    'R':'GestureImages/R1.jpg',
    'S':'GestureImages/S1.jpg',
    'T':'GestureImages/T1.jpg',
    'U':'GestureImages/U1.jpg',
    'V':'GestureImages/V1.jpg',
    'W':'GestureImages/W1.jpg',
    'X':'GestureImages/X.jpg',
    'Y':'GestureImages/Y.jpg',
    'Z':'GestureImages/Z.jpg',
    '0':'GestureImages/0.jpg',
    '1':'GestureImages/1.jpg',
    '2':'GestureImages/2.jpg',
    '3':'GestureImages/3.jpg',
    '4':'GestureImages/4.jpg',
    '5':'GestureImages/5.jpg',
    '6':'GestureImages/6.jpg',
    '7':'GestureImages/7.jpg',
    '8':'GestureImages/8.jpg',
    '9':'GestureImages/9.jpg',
    'HELLO':'GestureImages/hello.jpg',
    'HAI':'GestureImages/hai.jpg',
    'HI':'GestureImages/hai.jpg',
    'GOOD':'GestureImages/good.jpeg',
    'MORNING':'GestureImages/morning.jpeg',
    'WHAT':'GestureImages/what3.jpg',
    'IS':'GestureImages/is.jpg',
    'YOUR':'GestureImages/your.jpg',
    'YOU':'GestureImages/your.jpg',
    'NAME':'GestureImages/name.jpg',
    'NAME?':'GestureImages/name.jpg',
    'MY':'GestureImages/my.jpg',
    'GOODBYE':'GestureImages/goodbye.jpg',
    'THANKS':'GestureImages/thanks.jpg',
    'THANKYOU':'GestureImages/thanks.jpg',
    'YES':'GestureImages/yes.jpg',
    'NO':'GestureImages/no.jpg',
    'PLEASE':'GestureImages/please.jpg',
    'WHEN':'GestureImages/when.png',
    'WHERE':'GestureImages/where.png',
    'WHO':'GestureImages/who.png',
    'FATHER':'GestureImages/father.jpg',
    'FRIEND':'GestureImages/friend.jpg',
    'ILOVEYOU':'GestureImages/ivu.jpg',
}

def translate_to_isl(input_text, isl_database):
    output_gestures = []
    for word in input_text.split():
        if word.upper() in isl_database:
            output_gestures.append(isl_database[word.upper()])
        else:
            for letter in word:
                if letter.upper() in isl_database:
                    output_gestures.append(isl_database[letter.upper()])
                else:
                    output_gestures.append("Gesture image not found for: " + letter)
    return output_gestures

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class TranslateHandler(tornado.web.RequestHandler):
    def post(self):
        input_text = self.get_body_argument("input_text")
        output_gestures = translate_to_isl(input_text, isl_database)
        self.write(json.dumps({"output_gestures": output_gestures}))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/translate", TranslateHandler),
        (r"/GestureImages/(.*)", tornado.web.StaticFileHandler, {"path":"GestureImages"}),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path":"static"}),
    ], 
    debug=True,
    reload=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8882)
    print("Server is Listening on port 8882")
    tornado.ioloop.IOLoop.current().start()
