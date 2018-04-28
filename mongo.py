#!/usr/bin/env python
# coding: utf-8

# db.serverStatus().mem.[resident, virtual]
# db.serverStatus().connections.[current, available]
# db.serverStatus().opcounters.[insert, query, update, delete]

import commands
import sys


def get_status(arg1, arg2):
    _, result = commands.getstatusoutput('/usr/local/mongodb/bin/mongo '
                                         '--host "127.0.0.1" '
                                         '--port "27017" '
                                         '--username "admin" '
                                         '--password "password" '
                                         '--authenticationDatabase "admin" '
                                         '--eval "printjson(db.serverStatus().%s.%s)" | sed 1,2d' % (arg1, arg2))
    print result


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "ERROR: " + sys.argv[0] + " <arg1>" + " <arg2>"
        sys.exit(2)
    else:
        get_status(arg1=sys.argv[1], arg2=sys.argv[2])

