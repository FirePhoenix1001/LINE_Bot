from linebot.models import (
    TextSendMessage, QuickReply, QuickReplyButton,
    MessageAction, URIAction, PostbackAction
)

def default_quick_reply():
    """建立一個 Quick Reply 選單"""
    quick_reply = QuickReply(items=[
        QuickReplyButton(action=MessageAction(label="會議記錄",
                                              text="還沒做好")),
        
        QuickReplyButton(action=MessageAction(label="活動回覆",
                                              text="還沒做好")),
        
        # QuickReplyButton(action=URIAction(label="會議記錄", 
        #                                   uri="")),
        
        # QuickReplyButton(action=URIAction(label="活動回覆", 
        #                                   uri="")),
        
        QuickReplyButton(action=URIAction(label="行事曆", 
                                          uri="https://calendar.google.com/calendar/embed?src=4b41db17cbc7f5ad83f855961d568cc2ed4e0fa6e2c61d3dd03ef2d4e0c8f63e%40group.calendar.google.com&ctz=Asia%2FTaipei")),
        
        QuickReplyButton(action=URIAction(label="添加行事曆", 
                                          uri="https://calendar.google.com/calendar/u/1?cid=NGI0MWRiMTdjYmM3ZjVhZDgzZjg1NTk2MWQ1NjhjYzJlZDRlMGZhNmUyYzYxZDNkZDAzZWYyZDRlMGM4ZjYzZUBncm91cC5jYWxlbmRhci5nb29nbGUuY29t")),
        
        
    ])

    return TextSendMessage(
        text="你好",
        quick_reply=quick_reply
    )