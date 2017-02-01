#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PW_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compiler(r"^[\S]+@[\S]+.[\S]+$")

def username_check(username):
    return username and USER_RE.match(username)

def pw_check(password):
    return password and PW_RE.match(password)

def email_check(email):
    return not email or EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)

    def get(self):
        header = "<h1>Signup</h1>"

        name_input = "<label>Username</label><input name= 'username' type= 'text' value='' required>"
        password= "<label>Password</label><input name='password' type= 'password' required>"
        verify_pw= "<label>Verify Password</label><input name='verify' type= 'password' required>"
        email= "<label>Email(Optional)</label><input name='email' type= 'email' value=''>"
        submit= "<input type='submit'>"
        form= "<form method='post'>" + name_input + "<br>" + password + "<br>" + verify_pw + "<br>" + email + '<br>' + submit + "</form>"

        self.response.write(header + form)


    def post(self):
        username= self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")
        message= "<h1>Welcome, " + username + "!</h1>"

        if not username_check(username):
            self.form("That was an invalid username", password, verify, email)
            have_Error = True

        if not pw_check(password):
            self.form("That was an invalid password", verify, email)
            have_Error = True
        elif: password!=verify:
            self.form(username, password, "Your passwords did not match.")

        if not email_check(email):
            self.write.form(username, password, verify, "That is not a valid email.")

        if have_Error:
            self.response.out.write(form)
        else:
            self.redirect(message)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
