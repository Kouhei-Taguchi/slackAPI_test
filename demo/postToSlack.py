#coding: UTF-8

import slackweb

slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
slack.notify(text="pythonからslackさんへ")
