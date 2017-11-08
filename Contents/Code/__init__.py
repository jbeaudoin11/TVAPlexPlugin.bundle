import json
import re


NAME = "TVA"
PREFIX = "/video/tva"
ICON = "icon-default.jpg"

BASE_URL = "https://videos.tva.ca/page"

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
            AllContentMenu,
            title = "Tous les contenus"
        ),
        title = "Tous les contenus"
    ))

    # TODO add others

    return oc

####################################################################################################
@route(PREFIX + "/allcontent")
def AllContentMenu(title):

    oc = ObjectContainer(title2 = title)

    html = HTML.ElementFromUrl(BASE_URL + "/touslescontenus")
    state = json.loads(re.search("(?<=__INITIAL_STATE__ = ).*[^;\n]", html)) # Find the initial state of the page

    for item in state["items"]:
        attributes = item["content"]["attributes"]

        oc.add(DirectoryObject(
            key = Callback(
                SectionMenu,
                title = attributes["title"],
                entry = attributes["entry"]
            ),
            title = attributes["title"],
            thumb = attributes["image-background"]
        ))

    return oc




####################################################################################################
@route(PREFIX + "/section", entry=str)
def SectionMenu(title, entry):
    
    oc = ObjectContainer(title2 = title)

    # TODO

    return oc