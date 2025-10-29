from linebot.v3.messaging import (
    TextMessage,
    QuickReply,
    QuickReplyItem,
    MessageAction,
    URIAction
)

def default_quick_reply():
    """建立一個 Quick Reply 選單（v3 版）"""
    quick_reply = QuickReply(items=[
        QuickReplyItem(action=MessageAction(label="會議記錄", text="還沒做好")),
        QuickReplyItem(action=MessageAction(label="活動回覆", text="還沒做好")),
        QuickReplyItem(action=URIAction(
            label="行事曆",
            uri="https://calendar.google.com/calendar/embed?src=4b41db17cbc7f5ad83f855961d568cc2ed4e0fa6e2c61d3dd03ef2d4e0c8f63e%40group.calendar.google.com&ctz=Asia%2FTaipei")),
        QuickReplyItem(action=URIAction(
            label="添加行事曆",
            uri="https://calendar.google.com/calendar/u/1?cid=NGI0MWRiMTdjYmM3ZjVhZDgzZjg1NTk2MWQ1NjhjYzJlZDRlMGZhNmUyYzYxZDNkZDAzZWYyZDRlMGM4ZjYzZUBncm91cC5jYWxlbmRhci5nb29nbGUuY29t"))
    ])

    return TextMessage(
        text="你好​",  # 使用零寬空白，避免出現文字
        quick_reply=quick_reply
    )
