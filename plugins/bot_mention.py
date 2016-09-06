# -*- coding: utf-8 -*-

from slackbot.bot import respond_to

import requests

url = 'http://vois3.cyberon.com.tw/cloud_tts/gen_tts_file.php'

data = {'outfmt': 'mp3', 'speed': 1.20, 'gain': 1.00, 'f0': 1.00, 'vbr_quality': 1,
        'punctuDuration': {"，": 0.5, '。': 1}, 'language': 'zh-TW', 'speaker': 'DaiYu',
        'esl_speaker': 'DaiYu', 'esl_prosody': 'Zero', 'esl_speed': 1.00, 'esl_gain': 1.00, 'esl_f0': 1.10}

headers = {'Content-Type': 'application/x-www-form-urlencoded',
           'Referer': 'http://vois3.cyberon.com.tw/cloud_tts/pc_tts.php'}


@respond_to('hi')
@respond_to('hello')
@respond_to('你好')
@respond_to('您好')
def hello(message):
    message.reply('有事嘛？')


@respond_to('give me (.*)')
def giveme(message, text):
    data['text'] = text
    r = requests.post(url, data=data, headers=headers)
    if r.status_code == requests.codes.ok:
        ret = r.json()
        message.reply(ret['note'])
