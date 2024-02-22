import os

current_file_path = os.path.abspath(__file__)


class Constants:
    SPEED = 0.07
    AUTHORIZATION_PAGE_URL = 'https://www.adjarabet.am/hy/Promo/volcanicwinnings'
    AKCIA_PAGE_URL = 'https://www.adjarabet.am/hy/Promo/astrocash'
    DB_PATH = os.path.join(os.path.dirname(current_file_path), 'app_db.db')
    REQUEST_URL = "https://promos.www.adjarabet.am/astrocash/WebServices/handler.php"
    PAYLOAD = {
                "userID": "",
                "hour": 2,
                "curLang": "hy",
                "gameID": 1,
                "gameLevel": 0,
                "boxNum": 16,
                "autoSpin": 0,
                "pMultiplier": 1,
                "wsfilename": "Ajax-Game.php",
                "env": "production",
                "domain": "am",
                "promoCorePath": "/var/www/html/promo.v.5",
                "handlerHash": "a718cbda40712cc3adea089ac6a1d571082767efde80a381f179aa98bc2846b7"
            }
    PRIZE_PAYLOAD = {
                'userID': '',
                'curLang': 'hy',
                'wsfilename': 'Ajax-Live.php',
                'env': 'production',
                'domain': 'am',
                'promoCorePath': '/var/www/html/promo.v.5',
                'handlerHash': 'a718cbda40712cc3adea089ac6a1d571082767efde80a381f179aa98bc2846b7'
                    }
    REFRESH_PAYLOAD = {
                "userID": "",
                "gameID": "1",
                "curLang": "hy",
                "wsfilename": "Ajax-Cashout.php",
                "env": "production",
                "domain": "am",
                "promoCorePath": "/var/www/html/promo.v.5",
                "handlerHash": "a718cbda40712cc3adea089ac6a1d571082767efde80a381f179aa98bc2846b7"
                    }
    REQUEST_HEADERS = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7,hy;q=0.6",
                "Content-Length": "261",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie": "video__drow=0; onboard=1; GameId=2; curLang=hy; BIAB_LANGUAGE=hy_am; viplivechat=false; bmscookie=f28cd409-ba7a-43dd-8ef6-b12e3bb7ac28; _gid=GA1.2.834597041.1686254050; _fbp=fb.1.1686254050342.1189349928; currencyId=8; userOtpStatus=false; hideRegistrationButton=true; showCashier=false; _hjSessionUser_417641=eyJpZCI6ImNkZTJmZGQ2LTA0NWMtNTcxMS04OGFiLWNkMGQ0YjM2N2E4YSIsImNyZWF0ZWQiOjE2ODYyNTQwNTA1NzksImV4aXN0aW5nIjp0cnVlfQ==; SportsWidgets=true; slotNavigationSeeMore=hide; game_bar_casino_image_size=big; windowWidth=5; userTelCode=13836721; _ga=GA1.4.465086964.1686254050; hideQuickDeposit=true; _hjAbsoluteSessionInProgress=0; ZLD381859000000265001avuid=c24f0232-6ad4-463d-8ebc-b8dd7c261659; ZLD7d1f4041dbbc7c1576a9819af65132501f5de2dcab19d0c694ce1253193ac0f2avuid=c24f0232-6ad4-463d-8ebc-b8dd7c261659; _hjIncludedInSessionSample_417641=0; _hjSession_417641=eyJpZCI6IjI2ODQxODBhLTQwODQtNGJlNC04ZTdhLWRjNGI2ODQyNTQxNyIsImNyZWF0ZWQiOjE2ODgxNjA0Mjk4NjIsImluU2FtcGxlIjpmYWxzZX0=; JSESSIONID=eyJ0cyI6NDMxMDQ5MTIxMTQ4LCJkdCI6ImV5SjFhV1FpT2pJMk16SXpOalVzSW5OemFXUWlPaUppWlRsaU5ETTNZUzB4WldRMUxUUXdOMkV0WVdSaFpDMDJZakJoTmpJNU5EQTJPVGtpZlE9PSIsInNnIjoiY2UxODY2NjlmMGY5NDM5OWVkOGUyMWUyMjRlYjBmY2I1MzU4ZGJmZTlkOTY2NzNjODNjOTkwNjMyMTQ4MDBhNCJ9; BIAB_CUSTOMER=MjYzMjM2NS02YzNiNDRjOTJkMzQyMGUwNmVmZjIyYTQxZmZkNDkxNDQ4ZWE4ZjEwN2I4NmM5NzVkYjMzMjhmNGIxNmI1M2E4; userId=2632365; userName=davit.noreyan; currencyName=AMD; userBirthDate=1985-07-21; isUserVerified=2; widgetOrder=28,19,27,25,23,32,7,13; _gid=GA1.4.834597041.1686254050; ZLD1bb280db8e04640d673bbf8938b575e578f1a1d978879c4btabowner=undefined; adjarabet-_zldp=Qfc3LxuXok56%252FsV3fw%252BdpORtRrAItiYgamX29F2FmcvyKwOqG9LBRbX7LYdvCK5ymKwM1K1ctjo%253D; _ga=GA1.2.465086964.1686254050; _gat_UA-36161265-7=1; _ga_2R90203ZSM=GS1.1.1688160428.130.1.1688160979.0.0.0; zohoJWT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfaWQiOiIyNjMyMzY1IiwibmFtZSI6IkRBVklUIiwiZW1haWwiOiIyNjMyMzY1QGNoYXQuY29tIiwiaWF0IjoxNjg4MTYwOTc5LCJleHAiOjE2ODgxNjE4Nzl9.MxrqwagWt5_1ydzfWioCyRdLXfrr_JsvTIztVcBLSaw; _ga_E0WQB62ERL=GS1.2.1688160429.2.1.1688160980.60.0.0; _ga_E0WQB62ERL=GS1.4.1688160429.2.1.1688160982.58.0.0",
                "Origin": "https://promos.www.adjarabet.am",
                "Referer": "https://promos.www.adjarabet.am/slotlantis/?lang=hy&token=46f69054-f852-4a46-8475-8ef3c26f98e9&device=desktop&",
                "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "\"macOS\"",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest"
                    }
    star_box_payload = {
                "userID": "",
                "curLang": "hy",
                "boxNum": "1",
                "wsfilename": "Ajax-StarGame.php",
                "env": "production",
                "domain": "am",
                "promoCorePath": "/var/www/html/promo.v.5",
                "handlerHash": "a718cbda40712cc3adea089ac6a1d571082767efde80a381f179aa98bc2846b7"
                        }
    VALID_PRIZE = ['206', '205', '1', '204', '2', '3', '35', '36', '33', '34']
    pyramid_payload = {
                "userID": "",
                "hour": "14",
                "curLang": "hy",
                "boxNum": '4',
                "gameID": '2',
                "gameLevel": '1',
                "pMultiplier": '1',
                "wsfilename": "Ajax-Game.php",
                "env": "production",
                "domain": "am",
                "promoCorePath": "/var/www/html/promo.v.5",
                "handlerHash": "a718cbda40712cc3adea089ac6a1d571082767efde80a381f179aa98bc2846b7"
            }
    WHEEL_PAYLOAD = {
                "userID": "",
                "hour": "14",
                "curLang": "hy",
                "boxNum": '0',
                "gameID": '3',
                "gameLevel": '0',
                "pMultiplier": '1',
                "autoSpin": 0,
                "wsfilename": "Ajax-Game.php",
                "env": "production",
                "domain": "am",
                "promoCorePath": "/var/www/html/promo.v.5",
                "handlerHash": "a718cbda40712cc3adea089ac6a1d571082767efde80a381f179aa98bc2846b7"
            }
    SLOT_PAYLOAD = {
                "userID": "",
                "hour": "14",
                "curLang": "hy",
                "boxNum": '0',
                "gameID": '4',
                "gameLevel": '0',
                "pMultiplier": '1',
                "autoSpin": 0,
                "wsfilename": "Ajax-Game.php",
                "env": "production",
                "domain": "am",
                "promoCorePath": "/var/www/html/promo.v.5",
                "handlerHash": "a718cbda40712cc3adea089ac6a1d571082767efde80a381f179aa98bc2846b7"
            }
    DATA_HISTORY = {
        "userID": '',
        "userHash": '',
        "curLang": 'hy',
        "PeriodCurr": '13',
        "wsfilename": 'Ajax-History.php',
        "env": 'production',
        "domain": 'am',
        "promoCorePath": '/var/www/html/promo.v.5',
        "handlerHash": 'a718cbda40712cc3adea089ac6a1d571082767efde80a381f179aa98bc2846b7',
    }

