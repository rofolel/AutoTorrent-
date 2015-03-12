#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cmd

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


    def do_loadFilmdb(self,line):
        self.mothership.loadFilmDB()

    def do_number(self,l):
        print( len(self.mothership.films))

    def do_load(self,line):
        self.mothership.loadFilm(line)


    def do_exit(self,line):
        import tools.taskforce
        import sys
        for i in tools.taskforce.worker.taskforce:
            print( "stop")
            tools.taskforce.worker.todo('stopstop')
        sys.exit(0)
    def do_search(self,line):
        print ("lol")
    def complete_search(self, text, line, begidx, endidx):
        _line = line.replace("search ","").lower()
        filmnames = []

        for i in self.mothership.films:
            filmnames.append(i.lower())
        return [i for i in filmnames if i.startswith(_line)]

    def do_loadID(self,line):
        self.mothership.loadID(line)

cm = autoTorrentCmd()
cm.cmdloop()