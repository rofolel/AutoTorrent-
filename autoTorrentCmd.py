#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cmd
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
import motherShip.motherShip as motherShip

class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

        @classmethod
        def c(cls,s,color):
            return color + s + bcolors.ENDC



class autoTorrentCmd(cmd.Cmd):
    def emptyline(self):
        pass

    def preloop(self):
        banner =  u"""
 ▄▀▀█▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄
▐ ▄▀ ▀▄ █   █    █ █    █  ▐ █      █
  █▄▄▄█ ▐  █    █  ▐   █     █      █
 ▄▀   █   █    █      █      ▀▄    ▄▀
█   ▄▀     ▀▄▄▄▄▀   ▄▀         ▀▀▀▀
▐   ▐              █
                   ▐
 ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄▀▀▀▄   ▄▀▀█▄▄▄▄  ▄▀▀▄ ▀▄  ▄▀▀▀█▀▀▄
█    █  ▐ █      █ █   █   █  ▐  ▄▀   ▐ █  █ █ █ █    █  ▐
▐   █     █      █ ▐  █▀▀█▀     █▄▄▄▄▄  ▐  █  ▀█ ▐   █
   █      ▀▄    ▄▀  ▄▀    █     █    ▌    █   █     █
 ▄▀         ▀▀▀▀   █     █   R ▄▀▄▄▄▄   ▄▀   █    ▄▀
█                  ▐     ▐     █    ▐   █    ▐   █
▐                              ▐        ▐        ▐
        """
        banner = bcolors.c(banner,bcolors.FAIL)
        #print (banner)
        self.prompt = "[%s]> "%(bcolors.c("mothership",bcolors.WARNING))
        self.mothership = motherShip.motherShip()




    def do_exit(self,line):
        import tools.taskforce
        import sys
        for i in tools.taskforce.worker.taskforce:
            print( "stop")
            tools.taskforce.worker.todo('stopstop')
        sys.exit(0)

    def do_loadIMDB(self, line):
        self.mothership.loadFilmDB()


    def do_loadID(self,line):
        self.mothership.loadID(line)

    def do_list(self, line):
        self.mothership.loadData()
        print('film')
        for i in self.mothership.films:
            print(i.title)
        print('serie')
        for i in self.mothership.series:
            print(i.title)


cm = autoTorrentCmd()
cm.cmdloop()