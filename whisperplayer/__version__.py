#
#     ____   ___                                 ___
#    / __ \ | _ \ ___ _  _  ___  _ _   __  ___  / __| _  _  _  _
#   / / _` ||  _/(_-<| || |/ -_)| ' \ / _|/ -_)| (_ || || || || |
#   \ \__,_||_|  /__/ \_, |\___||_||_|\__|\___| \___| \_,_| \_, |
#    \____/           |__/                                  |__/
#

#=========================================================================
#   VERSIONING (@today:05-21-2018):
#       Cool Kids use tuples I guess? So - tuple versioning:
#          VERSION = (version number, 0 or 1 (0=test, 1=release), always 0)
#=========================================================================
VERSION = (3, 0, 0)

__version__ = '.'.join(map(str, VERSION))
