# -*- coding: utf-8 -*-

from slackbot.bot import listen_to


@listen_to('hi')
@listen_to('hello')
@listen_to('你好')
@listen_to('您好')
def hello(message):
    message.reply('你好，我叫區塊鏈！')


# @listen_to('1')
# def reaction(message):
#     message.react('+1')
