# -*- coding: utf-8 -*-
def confine(n, m, M):
    """
    Confines a value inside a range
    :param n: value
    :param m: min
    :param M: max
    """
    return max(min(M, n), m)


def dprint(*args, level=0):
    """
    Print helper
    """
    if DEBUG:
        print(datetime.now().strftime('%H:%M:%S.%f')[:-3], "|", "DEBUG", "|", "  " * level, *args)


def fourcc(dec):
    """
    Convert a 4 byte ASCII code into a string 
    """
    dec = int(dec)
    return chr((dec & 0XFF)) + chr((dec & 0XFF00) >> 8) + chr((dec & 0XFF0000) >> 16) + chr((dec & 0XFF000000) >> 24)


def parseMedia(path):
    """
    Parse media information of a file 
    """
    # Open file
    media = vlc.media_new(path)
    media.parse()

    # Get metadata
    _title = media.get_meta(0)
    _artist = media.get_meta(1)
    _album = media.get_meta(4)

    # Calculate duration
    m, s = divmod(int(media.get_duration() / 1000), 60)
    h, m = divmod(m, 60)
    _duration = ("%s:" if h else "") + "%02d:%02d" % (m, s)

    # Check for audio codec information
    _acodec = None
    tracks = list(filter(lambda track: track.type == Vlc.TrackType.audio, media.tracks_get()))

    if len(tracks) > 0:
        _acodec = fourcc(tracks[0].codec)
        _acodec2 = fourcc(tracks[0].original_fourcc)

    # Check for video codec information
    _vcodec = None
    tracks = list(filter(lambda track: track.type == Vlc.TrackType.video, media.tracks_get()))
    if len(tracks) > 0:
        _vcodec = fourcc(tracks[0].codec)
        _vcodec2 = fourcc(tracks[0].original_fourcc)

    return ("Title: %s\n" % _title if _title else "") + ("Artist: %s\n" % _artist if _artist else "") + (
        "Album: %s\n" % _album if _album else "") + ("Duration: %s\n" % _duration) + (
               "Audio Codec: %s%s\n" % (
                   _acodec, " (%s)" % _acodec2 if _acodec != _acodec2 else "") if _acodec else "") + (
               "Video Codec: %s%s\n" % (
                   _vcodec, " (%s)" % _vcodec2 if _vcodec != _vcodec2 else "") if _vcodec else "") + (
                                                                                                     "File Path: %s\n" % path)[
                                                                                                     :-1]


def identifyFileType(path):
    """
    Attempts to identify the file type of a given file 
    """

    # Is it a media? If it is it will have a duration
    media = vlc.media_new(path)
    media.parse()
    if media.get_duration() > 0:
        return "media"

    # Check against regex patterns
    matchPatterns = {
        'powerpoint': '^pp[ts]x?$',
    }

    extension = os.path.splitext(path)[1][1:]
    for type in matchPatterns:
        if re.match(matchPatterns[type], extension):
            return type
    return "unknown"

# Imports
DEBUG = True
from datetime import datetime
import sys, os, re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vlc as Vlc

try:
    vlc = Vlc.Instance()
except:
    parseMedia = lambda _: ""
    identifyFileType = lambda _: "unknown"
