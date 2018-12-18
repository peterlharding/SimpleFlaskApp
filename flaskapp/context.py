
import sys

from datetime import datetime

from flask import session

from .trace import Trace

#-------------------------------------------------------------------------------

class Context:

    Authenticated = None
    Today         = None

    #----------------------------------------------------------------------

    def __init__(self, title, authenticated=False):

        self.Title   = title
        self.Menu    = title

        # self.DBName  = DBName

        self.Now     = datetime.now()
        self.Today   = self.Now.strftime("%Y-%m-%d")
        self.Year    = self.Now.strftime("%Y")

        self.Session = session

        if 'profile' in session:

            # We have successfully authenticated...
            # ...but are we in the database? (i.e. have just registered)

            # Trace.Write("[Context::__init__]  >>>>> profile in session - Authenticated.")

            self.Authenticated = True

            self.Profile       = session['profile']
            self.Email         = self.Profile['email']

            # Trace.Write("[Context::__init__]  >>>>> Profile [%s]" % self.Profile)
            # Trace.Write("[Context::__init__]  >>>>>   Email [%s]" % self.Email)

        else:

            self.Authenticated = True
            self.Profile       = None
            self.Email         = None

    #----------------------------------------------------------------------

#-------------------------------------------------------------------------------


