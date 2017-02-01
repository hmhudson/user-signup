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

import webapp2
import re

form=""" <!DOCTYPE html>

<html>
    <head>
        <title> User Signup </title>
        <style type= "text/css">
        .label {text-align: right}
        .error {color: red}
        </style>
    </head>

    <body>
        <h2>User Signup</h2>
        <form method= "post">
        <table>
            <tr>
                <td class="label">
                    username
                </td>
                <td>
                    <input type="text" name="username">
                </td>
                <td class="error">
                %(error_username)s
                </td>
            </tr>

            <tr>
                <td class="label">
                    password
                </td>

                <td>
                    <input type="password" name="password"
                </td>

                <td class="error">
                    %(error_password)s
                </td>
            </tr>

            <tr>
                <td class="label">
                    Verify password
                </td>
                <td>
                    <input type="password" name="verify">
                </td>
                <td class="error">
                    %(error_verify)s
                </td>
            </tr>

            <tr>
                <td class="label">
                    Email(Optional)
                </td>
                <td>
                    <input type="text" name="email">
                </td>

                <td class= "error">
                    %(error_email)s
                </td>
            </tr>
        </table>
        <input type="Submit">
        </form>
    </body>
</html>"""

welcome_form="""<!DOCTYPE html>

<html>
    <head>
        <title>Welcome Page</title>
    </head>

    <body>
        <h2>Welcome, %(username)s!<h2>
    </body>
</html>"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PW_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def username_check(username):
    return username and USER_RE.match(username)

def pw_check(password):
    return password and PW_RE.match(password)

def email_check(email):
    return not email or EMAIL_RE.match(email)

class signupForm(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form%{"error_username":'', "error_password":'', "error_verify":'', "error_email":''})

    def form_errors(self, username="", password="", verify="", email=""):
        self.response.out.write(form%{"error_username":username, "error_password":password, "error_verify":verify, "error_email":email})


    def post(self):
        username= self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")
        error = False

        username_error = ''
        pw_error = ''
        verify_error = ''
        email_error = ''

        if not username_check(username):
            username_error = "That was an invalid username"
            error = True

        if not pw_check(password):
            pw_error = "That was an invalid password"
            error = True
        elif password!=verify:
            verify_error = "Your passwords did not match."
            error = True

        if not email_check(email):
            email_error = "That is not a valid email."
            error = True

        if error:
            self.form_errors(username_error, pw_error, verify_error, email_error)
        else:
            self.redirect("/welcome?username=" + username)

class welcome_page(webapp2.RequestHandler):
    def get(self):
        username= self.request.get("username")
        if username_check(username):
            self.response.out.write(welcome_form%{"username":username})
        else:
            self.redirect("/")


app = webapp2.WSGIApplication([
    ('/', signupForm), ("/welcome", welcome_page)
], debug=True)
