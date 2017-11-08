#!/bin/bash

PLUGIN_FOLDER_NAME="TVAPlexPlugin.bundle"
PLEX_PLUGIN_FOLDER_PATH="/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins"

echo "===> Installing the plugin <==="

rm -rf "$PLEX_PLUGIN_FOLDER_PATH/$PLUGIN_FOLDER_NAME"
cp -r "../$PLUGIN_FOLDER_NAME" "$PLEX_PLUGIN_FOLDER_PATH/$PLUGIN_FOLDER_NAME"


echo "===> DONE <==="