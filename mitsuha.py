# -*- coding: utf-8 -*-
# Mitsuha 1.0B : Square Line Bot
# Creator : WyvernStudio
# Project : 2DTH[UBOT]
# https://line.2dth.club
# Thanks you [ https://github.com/crash-override404 ] for New lip linepy
# Not for sell. use for education only.

from linepy import *
import time

line = LINE() #Login Type: QRCode Link
#line = LINE('EMAIL', 'PASSWORD') #Login Type: Email and Password (like pc login)
#line = LINE('AUTHTOKEN') #Login Type: Token Code (use some one of two top option for get token)

line.log("Auth Token : " + str(line.authToken))
squareChatMid='(YOUR_SQUARE_MID)' 
#line.getJoinableSquareChats('YOUR_SQUARE_MID') #Get Mid from square chat

helpMessage = "╭───「 Helps 」" + "\n" + \
                    "├ME" + "\n" + \
                    "├CREATOR" + "\n" + \
                    "├MYMID" + "\n" + \
                    "├────────────" + "\n" + \
                    "├HELP [ช่วยเหลือ]" + "\n" + \
                    "├SPEED [ความเร็วบอท]" + "\n" + \
                    "╰────────────"

# Initialize OEPoll with LINE instance
oepoll = OEPoll(line)

while True:
    try:
        eventsSquareChat=oepoll.singleFetchSquareChat(squareChatMid=squareChatMid)
        for e in eventsSquareChat:
            if e.createdTime is not 0:
                ts_old = int(e.createdTime) / 1000
                ts_now = int(time.time())
                line.log('[FETCH_TIME] ' + str(int(e.createdTime)))
                if ts_old >= ts_now:
                    '''
                        This is sample for implement BOT in LINE square
                        BOT will noticed who leave square chat
                        Command availabe :
                        > hi
                        > /author
                    '''
                    # Receive messages
                    if e.payload.receiveMessage != None:
                        payload=e.payload.receiveMessage
                        line.log('[RECEIVE_MESSAGE]')
                        msg=payload.squareMessage.message
                        msg_id=msg.id
                        receiver_id=msg._from
                        sender_id=msg.to
                        if msg.contentType == 0:
                            text=msg.text
                            if text.lower() == 'hi':
                                line.log('%s' % text)
                                line.sendSquareMessage(squareChatMid, 'Hi too! How are you?')                            
                            elif text.lower() == 'help':
                                line.log('%s' % text)
                                line.sendSquareMessage(squareChatMid, helpMessage)
                            elif text.lower() == 'speed':
                                start = time.time()
                                line.sendSquareMessage(squareChatMid, 'speed starting...') 
                                elapsed_time = time.time() - start
                                line.sendSquareMessage(squareChatMid, '%s' % (elapsed_time))
                            elif text.lower() == 'creator':     
                                line.log('%s' % text) 
                                line.sendSquareContact(squareChatMid, 'u089eec140a9d80173cbf83a84913e9dc') 
                            elif text.lower() == 'mymid':
                                line.log('%s' % text)
                                line.sendSquareMessage(squareChatMid, receiver_id)
                            elif text.lower() == 'me':
                                line.log('%s' % text)
                                line.sendSquareContact(squareChatMid, receiver_id)         
                    # Notified leave Square Chat
                    elif e.payload.notifiedLeaveSquareChat != None:
                        payload=e.payload.notifiedLeaveSquareChat
                        line.log('[NOTIFIED_LEAVE_SQUARE_CHAT]')
                        squareMemberMid=payload.squareChatMid
                        squareMemberMid=payload.squareMemberMid
                        squareMember=payload.squareMember
                        line.sendSquareMessage(squareChatMid, 'ขอให้จากไปอย่างสงบนะเจ้าคะ')
                    else:
                        pass
            
    except Exception as e:
        line.log("[FETCH_SQUARE] ไม่สามารถดึงข้อมูลแชทได้: " + str(e))
