#!/usr/bin/env python3

import argparse

from permasigner.__main__ import Main

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true',
                        help="shows some debug info, only useful for testing")
    parser.add_argument('-c', '--codesign', action='store_true',
                        help="uses codesign instead of ldid")
    parser.add_argument('-u', '--url', type=str,
                        help="the direct URL of the IPA to be signed")
    parser.add_argument('-p', '--path', type=str,
                        help="the direct local path of the IPA to be signed")
    parser.add_argument('-i', '--install', action='store_true',
                        help="installs the application to your device")
    parser.add_argument('-n', '--noinstall',
                        action='store_true', help="skips the install prompt")
    parser.add_argument('-o', '--output', type=str,
                        help="specify output file")
    parser.add_argument('-b', '--bundleid', type=str,
                        help="specify new bundle id")
    parser.add_argument('-N', '--name', type=str,
                        help="specify new app name")
    parser.add_argument('-m', '--minver', type=str,
                        help="specify new minimum app version (14.0 recommended)")
    parser.add_argument('-v', '--version', action='store_true',
                        help='show current version and exit',)
    parser.add_argument('-l', '--ldidfork', type=str,
                        help="specify a fork of ldid (eg. ProcursusTeam, itsnebulalol [default])")
    parser.add_argument('-f', '--folder', type=str,
                        help="sign multiple IPAs from a direct path to a folder")
    args = parser.parse_args()

    if args.version:
        from permasigner import __version__
        print(f"Permasigner v{__version__.__version__}")
        exit(0)

    main = Main(args)
    main.main()
