# -*- coding: utf-8 -*-

mystuff = {"apple": "I AM APPLES"
}
print mystuff['apple']

class me(object):
    """docstring for ."""
    def __init__(self):
        self.y = 'arg'
        print self.y

        self.printf()

    def printf(self):
        self.x = 'x'
        print self.x

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                  "I don't want to get sued",
                  "So I'll stop right there"])

happy_bday.sing_me_a_song()
