# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import sys
import os
import json
import urllib.request as urllib
import contextlib

def send_request(settings, url, request_data):
    # 送信先URL設定
    request = urllib.Request(url % settings.get('team'))

    # リクエストヘッダ設定
    request.add_header('Authorization', 'Bearer ' + settings.get('token'))
    request.add_header('Content-Type', 'application/json')

    # リクエストパラメータ設定
    request.add_data(request_data.encode('utf-8'))

    # APIリクエスト送信
    try:
        with contextlib.closing(urllib.urlopen(request)) as response:
            print('--- success ---')
            success = json.loads(response.read().decode('utf8', 'ignore'))
            success['code'] = response.getcode()
            return success

    except urllib.HTTPError as err:
        print('--- err ---')
        errors = {}
        errors['code'] = err.code
        errors['reason'] = err.reason
        return errors


def create_document(settings, title, region_data, wip):
    param = {}
    param['name'] = title
    param['body_md'] = region_data[0]

    if not wip:
        param['wip'] = False

    request_url = 'https://api.esa.io/v1/teams/%s/posts'

    # パラメータをセットする
    request_data = json.dumps(param)

    return send_request(settings, request_url, request_data)


class EsaIoCommand(sublime_plugin.TextCommand):
    wip = True

    def mode(self):
        return '[WIP]' if self.wip else ''

    def run(self, edit):
        # プラグインの設定ファイル読み込み
        settings = sublime.load_settings('Chick.sublime-settings')

        if not settings.get('token') or not settings.get('team'):
            sublime.status_message('CAUTION: You must enter your access token and joining team.')
            return

        # 全文取得
        # 1. 0文字目〜ファイル内の文字数までのregionオブジェクトを取得
        # 2. 1で取得した範囲の文字を取得する(リスト形式なのは複数範囲選択出来るため？)
        regions = [sublime.Region(0, self.view.size())]
        region_data = [self.view.substr(region) for region in regions]

        # windowオブジェクトを取得
        window = self.view.window()

        # タイトルを受け取ってPublish
        def on_create_document(title):
            # todo: titleが未入力であれば終了
            if not title:
                sublime.status_message('Title is required.')
                return

            request_result = create_document(settings, title, region_data, self.wip)
            print(request_result)

            # エラーが返ってきていればステータスバーに表示
            if request_result['code'] == 500 or request_result['code'] == 400:
                sublime.status_message('Error: ' + request_result['reason'])

            document_url = request_result['url']
            sublime.set_clipboard(document_url)
            sublime.status_message('Document published' + self.mode() + '. url: ' + document_url)

        # Esa.ioに登録するドキュメントタイトルを入力させる
        window.show_input_panel('Document Title(on Esa.io) (Required):', '', on_create_document, None, None)


class EsaIoShipCommand(EsaIoCommand):
    wip = False
