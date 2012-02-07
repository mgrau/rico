from __future__ import division
import tornado.ioloop
import tornado.web
from lobby import Lobby
import datetime


lobby = Lobby()

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/auth/login", AuthLoginHandler),
            (r"/", MainHandler),
            (r"/lobby", LobbyHandler),
            (r"/lobby_update", LobbyUpdateHandler),
            (r"/login_form", LoginForm),
            (r"/auth/logout", AuthLogoutHandler),
        ]
        tornado.web.Application.__init__(self, handlers)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        user_name = self.get_cookie('user_name', None)
        if user_name is None:
            self.redirect("/login_form")
        else:
            self.redirect("/lobby")

class LobbyHandler(tornado.web.RequestHandler):
    def get(self):
        user_name = self.get_cookie('user_name')
        player_list = self.render_string("lobby_update.html", user_names=lobby.player_list)
        self.render("lobby.html", user_name=user_name, player_list = player_list)

class LobbyUpdateHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        tornado.ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=1), self.send_update)

    def send_update(self):
        if self.request.connection.stream.closed(): #the client already disconnected
            return
        msg = dict(
            html=self.render_string("lobby_update.html", user_names=lobby.player_list))
        self.write(msg)
        self.finish()

class LoginForm(tornado.web.RequestHandler):
    def get(self):
        self.render("login_form.html")

class AuthLoginHandler(tornado.web.RequestHandler):
    def get(self):
        user_name = self.get_argument("user_name")
        self.set_cookie("user_name", user_name)
        lobby.add_player(user_name)
        self.redirect("/lobby")

class AuthLogoutHandler(tornado.web.RequestHandler):
    def get(self):
        user_name = self.get_cookie('user_name')
        lobby.remove_player(user_name)
        self.set_cookie('user_name', '')
        self.redirect('/login_form')

def run_server():
    app = Application()
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__=="__main__":
    run_server()
