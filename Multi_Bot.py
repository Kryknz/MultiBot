"""==================================ใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใ==================================
แดแด แดสสแดษดแด ษช๊ฑ แดแดสแดษชแดแดแดแด แดแด ๐ฐ๐ผ๐ฝ๐ ๐ฎ๐ป๐ฑ ๐ฑ๐ถ๐๐๐ฟ๐ถ๐ฏ๐๐๐ฒ แด แดสสแดแดษชแด แดแดแดษชแด๊ฑ 
แด๊ฐ แดสษช๊ฑ สษชแดแดษด๊ฑแด แดแดแดแดแดแดษดแด, ๐ฏ๐๐ ๐ฐ๐ต๐ฎ๐ป๐ด๐ถ๐ป๐ด ๐ถ๐ ๐ถ๐ ๐ป๐ผ๐ ๐ฎ๐น๐น๐ผ๐๐ฒ๐ฑ.
ไธใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใไธ
สแด๊ฑ สแดแดษด สษชแดแดษด๊ฑแดแด แดษดแดแดส ษขษดแด ษขแดษดแดสแดส แดแดสสษชแด สษชแดแดษด๊ฑแด
๐๐จ๐ฉ๐ฒ๐ซ๐ข๐ ๐ก๐ญ (๐) ๐๐๐๐ ๐๐ฟ๐ฎ๐ธ๐ถ๐ป๐ | ๐๐ฟ๐ฎ๐ธ๐ถ๐ป๐๐๐ฎ๐ฏ
==================================ใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใ=================================="""
try:
    import os
    import sys
    import time
    import qrcode
    import pprint
    import random
    import logging
    import pyqrcode
    import platform
    from PIL import Image
    from termcolor import *
    from covid import Covid
    from playsound import *
    # from pygobject import*
    import youtube_dl as Krak
    from gtts import gTTS as speak
except ImportError:
    os.system("pip install -U pip")
    os.system("pip install qrcode")
    os.system("pip install pyqrcode")
    os.system("pip install termcolor")
    # os.system("install-pkg pygobject")
    os.system("pip install playsound")
    os.system("pip install youtube-dl")
    os.system("pip install termcolor")
    os.system("pip install pillow")
    os.system("pip install covid")
    os.system("pip install gtts")
    from gtts import gTTS as speak
    import youtube_dl as Krak
    # from pygobject import*
    from playsound import *
    from covid import Covid
    from termcolor import *
    from PIL import Image
    import platform
    import pyqrcode
    import logging
    import random
    import pprint
    import qrcode
    import time
    import sys
    import os
"""==================================ใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใ==================================
แดแด แดสสแดษดแด ษช๊ฑ แดแดสแดษชแดแดแดแด แดแด ๐ฐ๐ผ๐ฝ๐ ๐ฎ๐ป๐ฑ ๐ฑ๐ถ๐๐๐ฟ๐ถ๐ฏ๐๐๐ฒ แด แดสสแดแดษชแด แดแดแดษชแด๊ฑ 
แด๊ฐ แดสษช๊ฑ สษชแดแดษด๊ฑแด แดแดแดแดแดแดษดแด, ๐ฏ๐๐ ๐ฐ๐ต๐ฎ๐ป๐ด๐ถ๐ป๐ด ๐ถ๐ ๐ถ๐ ๐ป๐ผ๐ ๐ฎ๐น๐น๐ผ๐๐ฒ๐ฑ.
ไธใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใไธ
สแด๊ฑ สแดแดษด สษชแดแดษด๊ฑแดแด แดษดแดแดส ษขษดแด ษขแดษดแดสแดส แดแดสสษชแด สษชแดแดษด๊ฑแด
๐๐จ๐ฉ๐ฒ๐ซ๐ข๐ ๐ก๐ญ (๐) ๐๐๐๐ ๐๐ฟ๐ฎ๐ธ๐ถ๐ป๐ | ๐๐ฟ๐ฎ๐ธ๐ถ๐ป๐๐๐ฎ๐ฏ
==================================ใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใ=================================="""


class InterceptHandler(logging.Handler):
    LEVELS_MAP = {
        logging.CRITICAL:
        "CRITICAL",
        logging.ERROR:
        "ERROR",
        logging.WARNING:
        "WARNING",
        logging.INFO:
        "INFO",
        logging.DEBUG:
        "DEBUG"}

    def _get_level(
            self,
            record):
        return self.LEVELS_MAP.get(
            record.levelno,
            record.levelno)

    def emit(self, record):
        logger_opt = logger.opt(
            depth=6,
            exception=record.exc_info,
            ansi=True,
            lazy=True)
        logger_opt.log(self._get_level(record),
                       record.getMessage())


logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)
KrakinzLog = logging.getLogger(__name__)
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    KrakinzLog.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. KRAK quitting.")
    quit(1)
ำสวำษจีผส__สษึึวษขษ = cprint
"""==================================ใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใ==================================
แดแด แดสสแดษดแด ษช๊ฑ แดแดสแดษชแดแดแดแด แดแด ๐ฐ๐ผ๐ฝ๐ ๐ฎ๐ป๐ฑ ๐ฑ๐ถ๐๐๐ฟ๐ถ๐ฏ๐๐๐ฒ แด แดสสแดแดษชแด แดแดแดษชแด๊ฑ 
แด๊ฐ แดสษช๊ฑ สษชแดแดษด๊ฑแด แดแดแดแดแดแดษดแด, ๐ฏ๐๐ ๐ฐ๐ต๐ฎ๐ป๐ด๐ถ๐ป๐ด ๐ถ๐ ๐ถ๐ ๐ป๐ผ๐ ๐ฎ๐น๐น๐ผ๐๐ฒ๐ฑ.
ไธใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใไธ
สแด๊ฑ สแดแดษด สษชแดแดษด๊ฑแดแด แดษดแดแดส ษขษดแด ษขแดษดแดสแดส แดแดสสษชแด สษชแดแดษด๊ฑแด
๐๐จ๐ฉ๐ฒ๐ซ๐ข๐ ๐ก๐ญ (๐) ๐๐๐๐ ๐๐ฟ๐ฎ๐ธ๐ถ๐ป๐ | ๐๐ฟ๐ฎ๐ธ๐ถ๐ป๐๐๐ฎ๐ฏ
==================================ใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใ=================================="""
ำสวำษจีผส__ีฆสวสษจศถส__สษจึศถ = []
_ำสวำษจีผส_ = Krak.YoutubeDL()
ำสวำษจีผส__ึึศถษจึีผึ = {"format": "bestaudio", "outtmpl": "%(title)s - %(extractor)s-%(id)s.%(ext)s",
                    "no_warnings": True, "ignoreerrors": True, "writethumbnail": True}
ำสวำษจีผส__วสษษจึ = Krak.YoutubeDL(ำสวำษจีผส__ึึศถษจึีผึ)
ำสวำษจีผส__ึึศถษจึีผึ = {"format": "best", "outtmpl": "%(title)s - %(extractor)s-%(id)s.%(ext)s",
                    "no_warnings": True, "ignoreerrors": True, "writethumbnail": True}
ำสวำษจีผส__สษจษษึ = Krak.YoutubeDL(ำสวำษจีผส__ึึศถษจึีผึ)
"""==================================ใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใ==================================
แดแด แดสสแดษดแด ษช๊ฑ แดแดสแดษชแดแดแดแด แดแด ๐ฐ๐ผ๐ฝ๐ ๐ฎ๐ป๐ฑ ๐ฑ๐ถ๐๐๐ฟ๐ถ๐ฏ๐๐๐ฒ แด แดสสแดแดษชแด แดแดแดษชแด๊ฑ 
แด๊ฐ แดสษช๊ฑ สษชแดแดษด๊ฑแด แดแดแดแดแดแดษดแด, ๐ฏ๐๐ ๐ฐ๐ต๐ฎ๐ป๐ด๐ถ๐ป๐ด ๐ถ๐ ๐ถ๐ ๐ป๐ผ๐ ๐ฎ๐น๐น๐ผ๐๐ฒ๐ฑ.
ไธใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใไธ
สแด๊ฑ สแดแดษด สษชแดแดษด๊ฑแดแด แดษดแดแดส ษขษดแด ษขแดษดแดสแดส แดแดสสษชแด สษชแดแดษด๊ฑแด
๐๐จ๐ฉ๐ฒ๐ซ๐ข๐ ๐ก๐ญ (๐) ๐๐๐๐ ๐๐ฟ๐ฎ๐ธ๐ถ๐ป๐ | ๐๐ฟ๐ฎ๐ธ๐ถ๐ป๐๐๐ฎ๐ฏ
==================================ใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใ=================================="""


def ำสวำษจีผส__สษจีผำ__ษจีผสึ(yturl):
    with _ำสวำษจีผส_:
        _ำสวำีผส_ = _ำสวำษจีผส_.extract_info(yturl, download=False)
        for format in _ำสวำีผส_["formats"]:
            if not "dash" in str(format["format"]).lower():
                ำสวำษจีผส__ีฆสวสษจศถส__สษจึศถ.append({
                    "format": format["format"],
                    "filesize": format["filesize"],
                    "format_id": format["format_id"],
                    "yturl": yturl})
        return _ำสวำีผส_["title"], _ำสวำีผส_["thumbnail"], ำสวำษจีผส__ีฆสวสษจศถส__สษจึศถ


ำสวำษจีผส__สวษฎ__ีกึสำ = """
==================================ใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใ==================================
แดแด แดสสแดษดแด ษช๊ฑ แดแดสแดษชแดแดแดแด แดแด ๐ฐ๐ผ๐ฝ๐ ๐ฎ๐ป๐ฑ ๐ฑ๐ถ๐๐๐ฟ๐ถ๐ฏ๐๐๐ฒ แด แดสสแดแดษชแด แดแดแดษชแด๊ฑ 
แด๊ฐ แดสษช๊ฑ สษชแดแดษด๊ฑแด แดแดแดแดแดแดษดแด, ๐ฏ๐๐ ๐ฐ๐ต๐ฎ๐ป๐ด๐ถ๐ป๐ด ๐ถ๐ ๐ถ๐ ๐ป๐ผ๐ ๐ฎ๐น๐น๐ผ๐๐ฒ๐ฑ.
ไธใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใไธ
สแด๊ฑ สแดแดษด สษชแดแดษด๊ฑแดแด แดษดแดแดส ษขษดแด ษขแดษดแดสแดส แดแดสสษชแด สษชแดแดษด๊ฑแด
๐๐จ๐ฉ๐ฒ๐ซ๐ข๐ ๐ก๐ญ (๐) ๐๐๐๐ ๐๐ฟ๐ฎ๐ธ๐ถ๐ป๐ | ๐๐ฟ๐ฎ๐ธ๐ถ๐ป๐๐๐ฎ๐ฏ
==================================ใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใ=================================="""
ำสวำษจีผส__ษึีกีผสึวษษส = """
==================================ใ ๐๐จ๐ฎ๐๐ฎ๐๐โญ๏ธ๐๐จ๐ฐ๐ง๐ฅ๐จ๐๐๐๐ซ ใ==================================
ษขษดแด ษขแดษดแดสแดส แดแดสสษชแด สษชแดแดษด๊ฑแด   
Everyone is permitted to DISTRIBUTE verbatim copies     
of this license document, BUT CHANGING IS NOT ALLOWED  
_| ๐๐จ๐ฎ๐๐ฎ๐๐โญ๏ธ๐๐จ๐ฐ๐ง๐ฅ๐จ๐๐๐๐ซ |_
สแด๊ฑ สแดแดษด สษชแดแดษด๊ฑแดแด แดษดแดแดส ษขษดแด ษขแดษดแดสแดส แดแดสสษชแด สษชแดแดษด๊ฑแด 
๐๐จ๐ฉ๐ฒ๐ซ๐ข๐ ๐ก๐ญ (๐) ๐๐๐๐ ๐๐ฟ๐ฎ๐ธ๐ถ๐ป๐ | ๐๐ฟ๐ฎ๐ธ๐ถ๐ป๐๐๐ฎ๐ฏ 
==================================ใ ๐๐จ๐ฎ๐๐ฎ๐๐โญ๏ธ๐๐จ๐ฐ๐ง๐ฅ๐จ๐๐๐๐ซ ใ==================================
"""


def แดสแดแด__ษขสแดแดษด(text):
    return ำสวำษจีผส__สษึึวษขษ(text, "green")


def แดสแดแด__สแดแด(text):
    return ำสวำษจีผส__สษึึวษขษ(text, "red")


def แดสแดแด__สแดสสแดแดก(text):
    return ำสวำษจีผส__สษึึวษขษ(text, "yellow")


def แดสแดแด__สสแดแด(text):
    return ำสวำษจีผส__สษึึวษขษ(text, "blue")


def แดสแดแด__แดแดษขแดษดแดแด(text):
    return ำสวำษจีผส__สษึึวษขษ(text, "magenta")


def แดสแดแด__ษขสแดส(text):
    return ำสวำษจีผส__สษึึวษขษ(text, "grey")


def แดสแดแด__แดสแดษด(text):
    return ำสวำษจีผส__สษึึวษขษ(text, "cyan")


"""==================================ใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใ==================================
แดแด แดสสแดษดแด ษช๊ฑ แดแดสแดษชแดแดแดแด แดแด ๐ฐ๐ผ๐ฝ๐ ๐ฎ๐ป๐ฑ ๐ฑ๐ถ๐๐๐ฟ๐ถ๐ฏ๐๐๐ฒ แด แดสสแดแดษชแด แดแดแดษชแด๊ฑ 
แด๊ฐ แดสษช๊ฑ สษชแดแดษด๊ฑแด แดแดแดแดแดแดษดแด, ๐ฏ๐๐ ๐ฐ๐ต๐ฎ๐ป๐ด๐ถ๐ป๐ด ๐ถ๐ ๐ถ๐ ๐ป๐ผ๐ ๐ฎ๐น๐น๐ผ๐๐ฒ๐ฑ.
ไธใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใไธ
สแด๊ฑ สแดแดษด สษชแดแดษด๊ฑแดแด แดษดแดแดส ษขษดแด ษขแดษดแดสแดส แดแดสสษชแด สษชแดแดษด๊ฑแด
๐๐จ๐ฉ๐ฒ๐ซ๐ข๐ ๐ก๐ญ (๐) ๐๐๐๐ ๐๐ฟ๐ฎ๐ธ๐ถ๐ป๐ | ๐๐ฟ๐ฎ๐ธ๐ถ๐ป๐๐๐ฎ๐ฏ
==================================ใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใ=================================="""
p = "|--------------------ไธใ  " + platform.system() + "  ใไธ--------------------|\n"
ps = platform.system().lower()
pt = cprint(p.upper(), "green")
"""==================================ใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใ==================================
แดแด แดสสแดษดแด ษช๊ฑ แดแดสแดษชแดแดแดแด แดแด ๐ฐ๐ผ๐ฝ๐ ๐ฎ๐ป๐ฑ ๐ฑ๐ถ๐๐๐ฟ๐ถ๐ฏ๐๐๐ฒ แด แดสสแดแดษชแด แดแดแดษชแด๊ฑ 
แด๊ฐ แดสษช๊ฑ สษชแดแดษด๊ฑแด แดแดแดแดแดแดษดแด, ๐ฏ๐๐ ๐ฐ๐ต๐ฎ๐ป๐ด๐ถ๐ป๐ด ๐ถ๐ ๐ถ๐ ๐ป๐ผ๐ ๐ฎ๐น๐น๐ผ๐๐ฒ๐ฑ.
ไธใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใไธ
สแด๊ฑ สแดแดษด สษชแดแดษด๊ฑแดแด แดษดแดแดส ษขษดแด ษขแดษดแดสแดส แดแดสสษชแด สษชแดแดษด๊ฑแด
๐๐จ๐ฉ๐ฒ๐ซ๐ข๐ ๐ก๐ญ (๐) ๐๐๐๐ ๐๐ฟ๐ฎ๐ธ๐ถ๐ป๐ | ๐๐ฟ๐ฎ๐ธ๐ถ๐ป๐๐๐ฎ๐ฏ
==================================ใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใ=================================="""
try:
    while True:
        if ps.startswith("wi"):
            os.system("cls")
        elif ps.startswith("li"):
            os.system("clear")
        else:
            os.system("clear")
        แดสแดแด__ษขสแดแดษด(ำสวำษจีผส__สวษฎ__ีกึสำ)
        แดสแดแด__สแดสสแดแดก("""
        =====|ไธใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใไธ|=====

                แดสแดแด 1 ๊ฐแดส ษขแดแด๊ฑ
                แดสแดแด 2 ๊ฐแดส Qสแดแดแดแดส
                แดสแดแด 3 ๊ฐแดส สแดแดแดแดสแด แดแดแดกษดสแดแดแดแดส
                แดสแดแด 4 ๊ฐแดส แดแดแด ษชแด ษชษด๊ฐแด แดxแดสแดแดแดแดส
                แดสแดแด 0 แดแด แดxษชแด


        =====|ไธใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใไธ|=====
        """)
        Run = int(input(">  "))
        if Run == 0:
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
            แดสแดแด__สแดแด(ำสวำษจีผส__สวษฎ__ีกึสำ)
            quit(1)
        elif Run == 1:
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
            แดสแดแด__ษขสแดแดษด(ำสวำษจีผส__สวษฎ__ีกึสำ)
            ำสวำษจีผส__สษึึวษขษ("===========================| ๐๐ผ๐ผ๐ด๐น๐ฒ ๐ง๐ฒ๐๐ ๐ง๐ผ ๐ฆ๐ฝ๐ฒ๐ฒ๐ฐ๐ต |===========================",
                             "green", attrs=["bold"])
            แดสแดแด__ษขสแดแดษด("แดสแดแด แดสแด แดแดxแด สแดแด แดกแดษดแด แดแด ษขแดแด แด๊ฑ แด ๊ฑแดแดแดแดส")
            Tts = input(">   ")
            KRAK = speak(text=Tts, lang="en", slow=True)
            KRAK.save(f"{Tts}.mp3")
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
            แดสแดแด__ษขสแดแดษด(ำสวำษจีผส__สวษฎ__ีกึสำ)
            ำสวำษจีผส__สษึึวษขษ("===========================| ๐๐ผ๐ผ๐ด๐น๐ฒ ๐ง๐ฒ๐๐ ๐ง๐ผ ๐ฆ๐ฝ๐ฒ๐ฒ๐ฐ๐ต |===========================",
                             "green", attrs=["bold"])
            แดสแดแด__ษขสแดแดษด("แดแด สแดแด แดกแดษดแด แดแด สแดแดส แดสแด แดแดแดษชแด?")
            Listen = input("y/n >   ").lower()
            if Listen == "y":
                playsound(f"{Tts}.mp3")
                ำสวำษจีผส__สษึึวษขษ(
                    "===========================| ๐๐ผ๐ผ๐ด๐น๐ฒ ๐ง๐ฒ๐๐ ๐ง๐ผ ๐ฆ๐ฝ๐ฒ๐ฒ๐ฐ๐ต |===========================", "green", attrs=["bold"])
                แดสแดแด__ษขสแดแดษด("สแดแดก แดแดษดส แดษชแดแด๊ฑ ๊ฑสแดแดสแด ษช แดสแดส  [๐๐ฆ๐ด๐ด ๐ต๐ฉ๐ฆ๐ฏ 50 !]")
                Times = int(input(">   "))
                Count_Check = 0
                while Count_Check < Times and not Count_Check == 50:
                    print("แดสแด แดแดแดษดแด_แดสแดแดแด ษช๊ฑ:", Count_Check+1)
                    playsound(f"{Tts}.mp3")
                    Count_Check = Count_Check + 1
                    print("Done !!")
            elif Listen == "n":
                if ps.startswith("wi"):
                    os.system("cls")
                elif ps.startswith("li"):
                    os.system("clear")
                else:
                    os.system("clear")
                แดสแดแด__ษขสแดแดษด(ำสวำษจีผส__สวษฎ__ีกึสำ)
                ำสวำษจีผส__สษึึวษขษ(
                    "===========================| ๐๐ผ๐ผ๐ด๐น๐ฒ ๐ง๐ฒ๐๐ ๐ง๐ผ ๐ฆ๐ฝ๐ฒ๐ฒ๐ฐ๐ต |===========================", "green", attrs=["bold"])
                แดสแดแด__ษขสแดแดษด("แดแด สแดแด แดกแดษดแด แดแด แดแดแดแด แดสแด แดแดแดษชแด แดส แดแดสแดแดแด ษชแด?")
                Delete = input("y/n >   ").lower()
                if Delete == "y":
                    ำสวำษจีผส__สษึึวษขษ("แดแดสแดษชษดแดแดแดแด แดแดแดแดแดสแดแดษด แดแดแดแดแด!", "cyan")
                else:
                    os.remove(f"{Tts}.mp3")
            else:
                if ps.startswith("wi"):
                    os.system("cls")
                elif ps.startswith("li"):
                    os.system("clear")
                else:
                    os.system("clear")
                แดสแดแด__ษขสแดแดษด(ำสวำษจีผส__สวษฎ__ีกึสำ)
                ำสวำษจีผส__สษึึวษขษ(
                    "===========================| ๐๐ผ๐ผ๐ด๐น๐ฒ ๐ง๐ฒ๐๐ ๐ง๐ผ ๐ฆ๐ฝ๐ฒ๐ฒ๐ฐ๐ต |===========================", "green", attrs=["bold"])
                แดสแดแด__ษขสแดแดษด("แดแด สแดแด แดกแดษดแด แดแด แดแดแดแด แดสแด แดแดแดษชแด แดส แดแดสแดแดแด ษชแด?")
                Delete = input("y/n >   ").lower()
                if Delete == "y":
                    ำสวำษจีผส__สษึึวษขษ("แดแดสแดษชษดแดแดแดแด แดแดแดแดแดสแดแดษด แดแดแดแดแด!", "cyan")
                else:
                    os.remove(f"{Tts}.mp3")
        elif Run == 2:
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
            แดสแดแด__ษขสแดแดษด(ำสวำษจีผส__สวษฎ__ีกึสำ)
            ำสวำษจีผส__สษึึวษขษ("===========================| Qr Code generator |===========================",
                             "green", attrs=["bold"])
            แดสแดแด__สแดสสแดแดก(
                "แดสแดแด๊ฑแด แดแดแด แดสแด ษชษด๊ฐแดสแดแดแดษชแดษด สแดแด แดกแดษดแด ษชษด๊ฑษชแดแด แดสแด ๐ค๐ฅ๐๐ข๐๐")
            KB = input(">   ")
            Kustom_Bank = [
                "red", "black",
                "green", "yellow",
                "blue", "magenta",
                "cyan", "Brown",
                "white", "Teal",
                "Silver", "Purple",
                "Gray", "Orange",
                "Maroon", "Aquamarine",
                "Lime", "Crimson",
                "pink", "Golden",
                "Plum", "Olive"
            ]
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
            ำสวำษจีผส__สษึึวษขษ("===========================| Qr Code generator |===========================",
                             "green", attrs=["bold"])
            ำสวำษจีผส__สษึึวษขษ(
                "แดสแดแด๊ฑแด แดสแดแด๊ฑแด แดสแด แดแดสแดส แด๊ฐ แดสแด สแดแดแดษขสแดแดษดแด แด๊ฐ สแดแดส ๐ค๐ฅ๐๐ข๐๐", "green")
            Kolor_1 = "1 - red"
            แดสแดแด__สแดแด(Kolor_1)
            Kolor_2 = "2 - green"
            แดสแดแด__ษขสแดแดษด(Kolor_2,)
            Kolor_3 = "3 - yellow"
            แดสแดแด__สแดสสแดแดก(Kolor_3)
            Kolor_4 = "4 - blue"
            แดสแดแด__สสแดแด(Kolor_4,)
            Kolor_5 = "5 - magenta"
            แดสแดแด__แดแดษขแดษดแดแด(Kolor_5)
            Kolor_6 = "6 - cyan"
            แดสแดแด__แดสแดษด(Kolor_6)
            Kolor_7 = "7 - default white"
            ำสวำษจีผส__สษึึวษขษ(Kolor_7)
            print("8 - for a different color")
            print("9 - for a random color")
            ำสวำษจีผส__สษึึวษขษ("===========================| Qr Code generator |===========================",
                             "green", attrs=["bold"])
            แดสแดแด__แดแดษขแดษดแดแด("แดสแดแด๊ฑแด แดษดแดแดส แด แด แดสษชแด ษดแดแดสแดส ๊ฐสแดแด 1-9")
            Kolor_Finally = input(">   ")
            if Kolor_Finally == "1":
                Back_Kolor = "red"
            elif Kolor_Finally == "2":
                Back_Kolor = "green"
            elif Kolor_Finally == "3":
                Back_Kolor = "yellow"
            elif Kolor_Finally == "4":
                Back_Kolor = "blue"
            elif Kolor_Finally == "5":
                Back_Kolor = "magenta"
            elif Kolor_Finally == "6":
                Back_Kolor = "cyan"
            elif Kolor_Finally == "7":
                Back_Kolor = "white"
            elif Kolor_Finally == "8":
                Other_Kustom_Kolor = """
red    green   yellow
blue   magenta   cyan
Brown   white  Teal
Silver Purple   Gray
Orange   Maroon   Aquamarine
Lime   Crimson   pink
Golden   Plum   Olive
"""
                แดสแดแด__ษขสแดแดษด("แดสแดแด๊ฑแด ๊ฐสแดแด แดสแด๊ฑแด\n>  ")
                ำสวำษจีผส__สษึึวษขษ(Other_Kustom_Kolor)
                Kustom = input(">").lower()
                Back_Kolor = Kustom
            elif Kolor_Finally == "9":
                Back_Kolor = random.choice(Kustom_Bank)
                print(Back_Kolor)
            else:
                if ps.startswith("wi"):
                    os.system("cls")
                elif ps.startswith("li"):
                    os.system("clear")
                else:
                    os.system("clear")
                แดสแดแด__ษขสแดแดษด(ำสวำษจีผส__สวษฎ__ีกึสำ)
                ำสวำษจีผส__สษึึวษขษ(
                    "===========================| Qr Code generator |===========================", "green", attrs=["bold"])
                ำสวำษจีผส__สษึึวษขษ((colored("ษขษชแด แดษด แดกสแดษดษข ษชษดแดแดแด ๊ฑแด แดxษชแดษชษดษข",
                                          "red", attrs=["bold"])))
                quit(1)
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
            แดสแดแด__ษขสแดแดษด(ำสวำษจีผส__สวษฎ__ีกึสำ)
            ำสวำษจีผส__สษึึวษขษ("===========================| Qr Code generator |===========================",
                             "green", attrs=["bold"])
            แดสแดแด__แดสแดษด("""
            =====|ไธใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใไธ|=====

                    แดสแดแด๊ฑแด แดสแดแด 1 ๊ฐแดส แดษดษข
                    แดสแดแด๊ฑแด แดสแดแด 2 ๊ฐแดส ๊ฑแด ษข
                    แดสแดแด๊ฑแด แดสแดแด 3 ๊ฐแดส แดแดษข
                        
            =====|ไธใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใไธ|=====
            """)
            input_data = input(">  ")
            แดสแดแด__สแดสสแดแดก("Name of the QRCode file")
            SAVE = input(">   ")
            if input_data == "1":
                QRC = qrcode.QRCode(
                    version=1,
                    box_size=10,
                    border=5)
                QRC.add_data(input_data)
                QRC.make(fit=True)
                QC_IMG = QRC.make_image(fill="black", back_color=Back_Kolor)
                QC_IMG.save(f"{SAVE}.png")
                "Get Desired output as a .png file"
                แดสแดแด__ษขสแดแดษด(ำสวำษจีผส__สวษฎ__ีกึสำ)
            elif input_data == "2":
                QRC = qrcode.QRCode(
                    version=1,
                    box_size=10,
                    border=5)
                QRC.add_data(input_data)
                QRC.make(fit=True)
                QC_IMG = QRC.make_image(fill="black", back_color=Back_Kolor)
                QC_IMG.save(f"{SAVE}.svg")
                "Get Desired output as a .svg file"
                แดสแดแด__ษขสแดแดษด(ำสวำษจีผส__สวษฎ__ีกึสำ)
            elif input_data == "3":
                QRC = qrcode.QRCode(
                    version=1,
                    box_size=10,
                    border=5)
                QRC.add_data(input_data)
                QRC.make(fit=True)
                QC_IMG = QRC.make_image(fill="black", back_color=Back_Kolor)
                QC_IMG.save(f"{SAVE}.jpg")
                "Get Desired output as a .jpg file"
                แดสแดแด__ษขสแดแดษด(ำสวำษจีผส__สวษฎ__ีกึสำ)
            else:
                if ps.startswith("wi"):
                    os.system("cls")
                elif ps.startswith("li"):
                    os.system("clear")
                else:
                    os.system("clear")
                แดสแดแด__ษขสแดแดษด(ำสวำษจีผส__สวษฎ__ีกึสำ)
                ำสวำษจีผส__สษึึวษขษ(
                    "===========================| Qr Code generator |===========================", "green", attrs=["bold"])
                ำสวำษจีผส__สษึึวษขษ(
                    "แดแดแด สแดแด แดส แดแดแดแดส แดษดแดแดก แดสแดแด สแดแดแดษด๊ฑ แดกษชสส แดสส แดษดสแดสษชษดษข สแดแด 1 แดส 2", "cyan")
                แดสแดแด__สแดแด("๐ช๐ฅ๐ข๐ก๐ ๐๐ก๐ฃ๐จ๐ง \n ๐๐๐ข ๐ฐ๐๐๐๐!! ๐ฒ๐ข๐๐ ๐ฑ๐๐ข๐๐")
                แดสแดแด__ษขสแดแดษด(ำสวำษจีผส__สวษฎ__ีกึสำ)
                time.sleep(2)
        elif Run == 3:
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
            แดสแดแด__สแดสสแดแดก(ำสวำษจีผส__ษึีกีผสึวษษส)
            ำสวำษจีผส__สษึึวษขษ("===========================| ๐๐จ๐ฎ๐๐ฎ๐๐โญ๏ธ๐๐จ๐ฐ๐ง๐ฅ๐จ๐๐๐๐ซ |===========================",
                             "green", attrs=["bold"])
            แดสแดแด__ษขสแดแดษด("โญ๏ธ แดสแดแด๊ฑแด แดสแดแด แดแดแดษชแด แดส แด ษชแดแดแด")
            AudioVideoManager = input("       :").lower()
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
            if AudioVideoManager == "audio":
                if ps.startswith("wi"):
                    os.system("cls")
                elif ps.startswith("li"):
                    os.system("clear")
                else:
                    os.system("clear")
                แดสแดแด__สแดสสแดแดก(ำสวำษจีผส__ษึีกีผสึวษษส)
                ำสวำษจีผส__สษึึวษขษ(
                    "===========================| ๐๐จ๐ฎ๐๐ฎ๐๐โญ๏ธ๐๐จ๐ฐ๐ง๐ฅ๐จ๐๐๐๐ซ |===========================", "green", attrs=["bold"])
                แดสแดแด__สแดสสแดแดก(
                    "แดแดแดส & แดแด๊ฑแดแด แดสแด แดสส แด๊ฐ แดสแด สแดแดแดแดสแด แด ษชแดแดแด สแดแด แดกแดษดแด แดแด แดแดแดกษดสแดแดแด")
                Linked = input(":- ")
                title, thumbnail_url, formats = ำสวำษจีผส__สษจีผำ__ษจีผสึ(Linked)
                ำสวำษจีผส__สษึึวษขษ(title, "yellow")
                ำสวำษจีผส__สษึึวษขษ(formats, "yellow")
                zxt = Linked.strip()
                ำสวำษจีผส__วสษษจึ.download([zxt])
                แดสแดแด__แดแดษขแดษดแดแด(
                    "แดแดแดกษดสแดแดแดแดแด!\n\nแดสแดแด๊ฑแด แดสแดแดแด สแดแดแดส แดแดแดแด แดสแดแด แดแด ษขแดแด สแดแดส ๊ฐษชสแด....")
                time.sleep(8)
            elif AudioVideoManager == "video":
                if ps.startswith("wi"):
                    os.system("cls")
                elif ps.startswith("li"):
                    os.system("clear")
                else:
                    os.system("clear")
                แดสแดแด__สแดสสแดแดก(ำสวำษจีผส__ษึีกีผสึวษษส)
                ำสวำษจีผส__สษึึวษขษ(
                    "===========================| ๐๐จ๐ฎ๐๐ฎ๐๐โญ๏ธ๐๐จ๐ฐ๐ง๐ฅ๐จ๐๐๐๐ซ |===========================", "green", attrs=["bold"])
                แดสแดแด__สแดสสแดแดก(
                    "แดแดแดส & แดแด๊ฑแดแด แดสแด แดสส แด๊ฐ แดสแด สแดแดแดแดสแด แด ษชแดแดแด สแดแด แดกแดษดแด แดแด แดแดแดกษดสแดแดแด")
                Linked = input(":- ")
                title, thumbnail_url, formats = ำสวำษจีผส__สษจีผำ__ษจีผสึ(Linked)
                แดสแดแด__สแดสสแดแดก(title)
                แดสแดแด__แดสแดษด(formats)
                zxt = Linked.strip()
                ำสวำษจีผส__สษจษษึ.download([zxt])
                แดสแดแด__แดแดษขแดษดแดแด(
                    "แดแดแดกษดสแดแดแดแดแด!\n\nแดสแดแด๊ฑแด แดสแดแดแด สแดแดแดส แดแดแดแด แดสแดแด แดแด ษขแดแด สแดแดส ๊ฐษชสแด....")
                time.sleep(8)
            else:
                if ps.startswith("wi"):
                    os.system("cls")
                elif ps.startswith("li"):
                    os.system("clear")
                else:
                    os.system("clear")
                ำสวำษจีผส__สษึึวษขษ(
                    "===========================| ๐๐จ๐ฎ๐๐ฎ๐๐โญ๏ธ๐๐จ๐ฐ๐ง๐ฅ๐จ๐๐๐๐ซ |===========================", "green", attrs=["bold"])
                ำสวำษจีผส__สษึึวษขษ((colored("๐๐ถ๐๐ฒ๐ป ๐ช๐ฟ๐ผ๐ป๐ด ๐ถ๐ป๐ฝ๐๐ ๐๐ผ ๐ฒ๐๐ถ๐๐ถ๐ป๐ด",
                                          "red", attrs=["bold"])))
                quit(1)
        elif Run == 4:
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
            covid = Covid()
            แดสแดแด__สแดสสแดแดก(ำสวำษจีผส__สวษฎ__ีกึสำ)
            ำสวำษจีผส__สษึึวษขษ("===========================| Covid Info Extractor |===========================",
                             "green", attrs=["bold"])
            COUNT = ["US", "India", "Brazil", "United Kingdom", "Russia", "France", "Turkey", "Argentina", "Iran", "Colombia", "Spain",
                     "Italy", "Indonesia", "Germany", "Mexico", "Poland", "South Africa", "Ukraine", "Peru", "Philippines", "Netherlands", "Iraq", "Malaysia", "Czechia",
                     "Chile", "Japan", "Canada", "Bangladesh", "Thailand", "Belgium", "Pakistan", "Sweden", "Israel", "Romania", "Portugal", "Kazakhstan", "Morocco",
                     "Hungary", "Jordan", "Switzerland", "Serbia", "Nepal", "United Arab Emirates", "Cuba", "Austria", "Tunisia", "Lebanon", "Greece", "Georgia", "Vietnam",
                     "Saudi Arabia", "Ecuador", "Belarus", "Bolivia", "Guatemala", "Costa Rica", "Sri Lanka", "Bulgaria", "Panama", "Paraguay", "Azerbaijan", "Burma",
                     "Kuwait", "Slovakia", "Uruguay", "Croatia", "Ireland", "West Bank and Gaza", "Dominican Republic", "Denmark", "Honduras", "Venezuela", "Libya",
                     "Ethiopia", "Lithuania", "Oman", "Egypt", "Bahrain", "Moldova", "Slovenia", "Korea, South", "Armenia", "Mongolia", "Kenya", "Qatar", "Bosnia and Herzegovina",
                     "Zambia", "Algeria", "Nigeria", "North Macedonia", "Kyrgyzstan", "Norway", "Botswana", "Uzbekistan", "Afghanistan", "Kosovo", "Albania", "Mozambique",
                     "Latvia", "Estonia", "Finland", "Zimbabwe", "Namibia", "Ghana", "Uganda", "Montenegro", "Cyprus", "iChina", "Cambodia", "El Salvador", "Rwanda",
                     "Cameroon", "Maldives", "Luxembourg", "Senegal", "Jamaica", "Singapore", "Australia", "Malawi", "Cote d'Ivoire", "Congo (Kinshasa)", "Angola",
                     "Fiji", "Trinidad and Tobago", "Eswatini", "Madagascar", "Sudan", "Malta", "Cabo Verde", "Mauritania", "Suriname", "Guinea", "Syria", "Guyana",
                     "Gabon", "Togo", "Haiti", "Seychelles", "Bahamas", "Papua New Guinea", "Somalia", "Timor-Leste", "Tajikistan", "Belize", "Benin", "Laos", "Taiwan*",
                     "Andorra", "Mali", "Lesotho", "Burkina Faso", "Congo (Brazzaville)", "Mauritius", "Burundi", "Nicaragua", "Djibouti", "South Sudan", "Central African Republic",
                     "Iceland", "Equatorial Guinea", "Gambia", "Saint Lucia", "Yemen", "Eritrea", "Sierra Leone", "Guinea-Bissau", "Niger", "Liberia", "Barbados", "San Marino",
                     "Chad", "Comoros", "New Zealand", "Brunei", "Liechtenstein", "Monaco", "Sao Tome and Principe", "Bhutan", "Saint Vincent and the Grenadines", "Dominica",
                     "Antigua and Barbuda", "Grenada", "Tanzania", "Saint Kitts and Nevis", "Summer Olympics 2020", "Diamond Princess", "Holy See", "Solomon Islands",
                     "MS Zaandam", "Marshall Islands", "Vanuatu", "Samoa", "Kiribati", "Palau", "Micronesia"]
            แดสแดแด__ษขสแดแดษด("แดสแดแด๊ฑแด แดสแดแด แดแดแดษดแดสส ษดแดแดแด/แดแดแดแด")
            Country = input(">  ").capitalize()
            if Country in COUNT:
                pass
            else:
                แดสแดแด__สแดแด("ษชษดแด แดสษชแด ษดแดแดแด แดส ษดแดแด ๊ฑแดแดแดแดสแดแดแด สแดแด")
            Cases = covid.get_status_by_country_name(Country)
            pprint.pprint(Cases)
            แดสแดแด__แดแดษขแดษดแดแด("แดแดแดแด แดสแดแดษดษชษดษข ษชษด 20 ๊ฑแดแดแดษดแด๊ฑ !")
            time.sleep(20)
            if ps.startswith("wi"):
                os.system("cls")
            elif ps.startswith("li"):
                os.system("clear")
            else:
                os.system("clear")
        else:
            pass
except Exception as E:
    แดสแดแด__สแดแด("ERROR      :" + str(E))
"""==================================ใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใ==================================
แดแด แดสสแดษดแด ษช๊ฑ แดแดสแดษชแดแดแดแด แดแด ๐ฐ๐ผ๐ฝ๐ ๐ฎ๐ป๐ฑ ๐ฑ๐ถ๐๐๐ฟ๐ถ๐ฏ๐๐๐ฒ แด แดสสแดแดษชแด แดแดแดษชแด๊ฑ 
แด๊ฐ แดสษช๊ฑ สษชแดแดษด๊ฑแด แดแดแดแดแดแดษดแด, ๐ฏ๐๐ ๐ฐ๐ต๐ฎ๐ป๐ด๐ถ๐ป๐ด ๐ถ๐ ๐ถ๐ ๐ป๐ผ๐ ๐ฎ๐น๐น๐ผ๐๐ฒ๐ฑ.
ไธใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใไธ
สแด๊ฑ สแดแดษด สษชแดแดษด๊ฑแดแด แดษดแดแดส ษขษดแด ษขแดษดแดสแดส แดแดสสษชแด สษชแดแดษด๊ฑแด
๐๐จ๐ฉ๐ฒ๐ซ๐ข๐ ๐ก๐ญ (๐) ๐๐๐๐ ๐๐ฟ๐ฎ๐ธ๐ถ๐ป๐ | ๐๐ฟ๐ฎ๐ธ๐ถ๐ป๐๐๐ฎ๐ฏ
==================================ใ ๐๐ฅ KRAKINZ LฮB ๐ฅ๐ ใ=================================="""
