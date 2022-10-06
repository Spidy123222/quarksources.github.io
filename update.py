import logging
import os

from ipaUtil import get_github_release
from sourceUtil import (AltSourceManager, AltSourceParser, GithubParser,
                        Unc0verParser)

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# try:
#     g_token = os.environ["GITHUB_TOKEN"]
#     g_release = get_github_release(g_token, 321891219) # gets the github release by its API id
# except KeyError as err:
#     logging.error(f"Could not find GitHub Token.")
#     logging.error(f"{type(err).__name__}: {str(err)}")

sourcesData = [
    {
        "parser": AltSourceParser,
        "kwargs": {"filepath": "https://altstore.oatmealdome.me"},
        "ids": ["me.oatmealdome.dolphinios-njb", "me.oatmealdome.DolphiniOS-njb-patreon-beta"]
    },
    {
        "parser": AltSourceParser,
        "kwargs": {"filepath": "quarksource.json"},
        "ids": ["com.libretro.dist.ios.RetroArch", "com.louisanslow.record", "org.scummvm.scummvm", "com.dry05.filzaescaped11-12", "com.virtualapplications.play"]
    },
    {
        "parser": AltSourceParser,
        "kwargs": {"filepath": "https://provenance-emu.com/apps.json"},
        "ids": ["org.provenance-emu.provenance"]
    },
    {
        "parser": AltSourceParser,
        "kwargs": {"filepath": "https://theodyssey.dev/altstore/odysseysource.json"},
        "ids": ["org.coolstar.odyssey"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "Odyssey-Team", "repo_name": "Taurine"},
        #"kwargs": {"filepath": "https://taurine.app/altstore/taurinestore.json"},
        "ids": ["org.coolstar.taurine"]
    },
    {
        "parser": AltSourceParser,
        "kwargs": {"filepath": "https://alt.getutm.app"},
        "ids": ["com.utmapp.UTM", "com.utmapp.UTM-SE"]
    },
    {
        "parser": AltSourceParser,
        "kwargs": {"filepath": "https://demo.altstore.io"},
        "ids": ["com.rileytestut.GBA4iOS"]
    },
    {
        "parser": AltSourceParser,
        #"kwargs": {"repo_author": "flyinghead", "repo_name": "flycast"},
        "kwargs": {"filepath": "https://flyinghead.github.io/flycast-builds/altstore.json"},
        "ids": ["com.flyinghead.Flycast"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "iNDS-Team", "repo_name": "iNDS"},
        "ids": ["net.nerd.iNDS"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "yoshisuga", "repo_name": "MAME4iOS"},
        "ids": ["com.example.mame4ios"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "brandonplank", "repo_name": "flappybird"},
        "ids": ["org.brandonplank.flappybird"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "nspire-emus", "repo_name": "firebird"},
        "ids": ["com.firebird.firebird-emu"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "Wh0ba", "repo_name": "XPatcher"},
        "ids": ["com.wh0ba.xpatcher"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "litchie", "repo_name": "dospad"},
        "ids": ["com.litchie.idosgames"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "QuarkSources", "repo_name": "ppsspp-builder"},
        "ids": ["org.ppsspp.ppsspp"]
    },
    {
        "parser": Unc0verParser,
        "kwargs": {"url": "https://unc0ver.dev/releases.json"},
        "ids": ["science.xnu.undecimus"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "ianclawson", "repo_name": "Delta-iPac-Edition"},
        "ids": ["com.ianclawson.DeltaPacEdition"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "zydeco", "repo_name": "minivmac4ios"},
        ## This is the previous kwargs required when this application was distributed as a zipped .ipa file ##
        ## "kwargs": {"repo_author": "zydeco", "repo_name": "minivmac4ios", "asset_regex": r".*\.ipa\.zip", "extract_twice": True, "upload_ipa_repo": g_release},
        "ids": ["net.namedfork.minivmac"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "T-Pau", "repo_name": "Ready", "ver_parse": lambda x: x.replace("release-", "")},
        "ids": ["at.spiderlab.c64"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "yoshisuga", "repo_name": "activegs-ios"},
        "ids": ["com.yoshisuga.activeGS"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "zzanehip", "repo_name": "The-OldOS-Project"},
        "ids": ["com.zurac.OldOS"]
    },
    {
        "parser": GithubParser,
        "kwargs": {"repo_author": "n3d1117", "repo_name": "appdb", "prefer_date": True},
        "ids": ["it.ned.appdb-ios"]
    },
    {
        "parser": AltSourceParser,
        "kwargs": {"filepath": "https://pokemmo.eu/altstore/"},
        "ids": ["eu.pokemmo.client"]
    }
]
alternateAppData = {
    "eu.pokemmo.client": {
        "beta": False
    },
    "com.flyinghead.Flycast": {
      "localizedDescription": "Flycast is a multi-platform Sega Dreamcast, Naomi and Atomiswave emulator derived from reicast.\nInformation about configuration and supported features can be found on TheArcadeStriker's [flycast wiki](https://github.com/TheArcadeStriker/flycast-wiki/wiki).",
      "screenshotURLs": ["https://i.imgur.com/47KjD5a.png", "https://i.imgur.com/MfhD1h1.png", "https://i.imgur.com/wO88IVP.png"]
    },
    "org.ppsspp.ppsspp": {
        "tintColor": "#21486b",
        "subtitle": "PlayStation Portable games on iOS.",
        "screenshotURLs": [
            "https://i.imgur.com/CWl6GgH.png",
            "https://i.imgur.com/SxmN1M0.png",
            "https://i.imgur.com/sGWgR6z.png",
            "https://i.imgur.com/AFKTdmZ.png"
        ],
        "iconURL": "https://i.imgur.com/JP0Fncv.png"
    },
    "com.rileytestut.GBA4iOS": {
        "iconURL": "https://i.imgur.com/SBrqO9g.png",
        "screenshotURLs": [
            "https://i.imgur.com/L4H0yM3.png",
            "https://i.imgur.com/UPGYLVr.png",
            "https://i.imgur.com/sWpUAii.png",
            "https://i.imgur.com/UwnDXRc.png"
          ]
    },
    "org.provenance-emu.provenance": {
        "localizedDescription": "Provenance is a multi-system emulator frontend for a plethora of retro gaming systems. You can keep all your games in one place, display them with cover art, and play to your heart's content.\n\nSystems Supported:\n\n• Atari\n  - 2600\n  - 5200\n  - 7800\n  - Lynx\n  - Jaguar\n• Bandai\n  - WonderSwan / WonderSwan Color\n• NEC\n  - PC Engine / TurboGrafx-16 (PCE/TG16)\n  - PC Engine Super CD-ROM² System / TurboGrafx-CD\n  - PC Engine SuperGrafx\n  - PC-FX\n• Nintendo\n  - Nintendo Entertainment System / Famicom (NES/FC)\n  - Famicom Disk System\n  - Super Nintendo Entertainment System / Super Famicom (SNES/SFC)\n  - Game Boy / Game Boy Color (GB/GBC)\n  - Virtual Boy\n  - Game Boy Advance (GBA)\n  - Pokémon mini\n• Sega\n  - SG-1000\n  - Master System\n  - Genesis / Mega Drive\n  - Game Gear\n  - CD / MegaCD\n  - 32X\n• SNK\n  - Neo Geo Pocket / Neo Geo Pocket Color\n• Sony\n  - PlayStation (PSX/PS1)",
        "tintColor": "#1c7cf3",
        "permissions": [
            {
              "type": "camera",
              "usageDescription": "Used for album artwork."
            },
            {
              "type": "photos",
              "usageDescription": "Provenance can set custom artworks from your photos or save screenshots to your photos library."
            },
            {
              "type": "music",
              "usageDescription": "This will let you play your imported music on Spotify."
            },
            {
              "type": "bluetooth",
              "usageDescription": "Provenance uses Bluetooth to support game controllers."
            },
            {
              "type": "background-fetch",
              "usageDescription": "Provenance can continue running while in the background."
            },
            {
              "type": "background-audio",
              "usageDescription": "Provenance can continue playing game audio while in the background."
            }
        ]
    }
}

quantumsrc = AltSourceManager("quantumsource.json", sourcesData, alternateAppData, prettify=True) # if prettify is true, output will have indents and newlines
try:
    quantumsrc.update()
except Exception as err:
    logging.error(f"Unable to update {quantumsrc.src.name}.")
    logging.error(f"{type(err).__name__}: {str(err)}")
