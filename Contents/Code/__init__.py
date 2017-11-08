import json
import re

NAME = "TVA"
PREFIX = "/video/tva"
ICON = "icon-default.jpg"

BASE_URL = "http://videos.tva.ca/page"
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38'

# /var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Logs/PMS Plugin Logs

####################################################################################################
def Start():

    ObjectContainer.title1 = NAME
    DirectoryObject.thumb = R(ICON)

####################################################################################################
@handler(PREFIX, NAME, thumb=ICON)
def MainMenu():

    oc = ObjectContainer()
    oc.add(DirectoryObject(
        key = Callback(
            AllContentMenu
        ),
        title = "Tous les contenus"
    ))

    # TODO add others

    return oc

####################################################################################################
@route(PREFIX + "/allcontent")
def AllContentMenu():

    oc = ObjectContainer(title2 = "Tous les contenus")

    # html = HTML.ElementFromURL("http://expressjs.com/", headers={"User-Agent": USER_AGENT})
    # Log("--------------------TEST------------------")
    # Log(str(html))

    # return ObjectContainer(title2 = "Tous les contenus", message="Il n'y a pas d'episode")

    # html = HTML.ElementFromURL(BASE_URL + "/touslescontenus", headers={"User-Agent": USER_AGENT})
    # state = json.loads(re.search("(?<=__INITIAL_STATE__ = ).*[^;\n]", html)) # Find the initial state of the page

    # for item in state["items"]:
    #     attributes = item["content"]["attributes"]

    #     oc.add(DirectoryObject(
    #         key = Callback(
    #             SectionMenu,
    #             title = attributes["title"],
    #             entry = attributes["entry"]
    #         ),
    #         title = attributes["title"],
    #         thumb = attributes["image-background"]
    #     ))

    oc.add(VideoClipObject(
        url="http://streamtvago.akamaized.net/media/v1/pmp4/static/clear/5481942443001/6e0d50f9-2a8a-4687-9acc-f9023697484c/high.mp4?akamai_token=exp=1512532988~acl=/media/v1/pmp4/static/clear/5481942443001/6e0d50f9-2a8a-4687-9acc-f9023697484c/high.mp4*~hmac=67957a7c627fdd7ed31087224c0f906d0ee3976292c6420ea9e1495d15dd02cb",
        title="TEST"
    ))

    return oc




####################################################################################################
@route(PREFIX + "/show")
def SectionMenu(title, url):
    
    oc = ObjectContainer(title2 = title)

    # TODO

    return oc