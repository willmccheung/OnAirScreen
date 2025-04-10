import json
import PyQt5.QtNetwork as QtNetwork
import mainscreen
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui


class RoomTemperatures():
    
    def __init__(self, parent = None):
        super(RoomTemperatures, self).__init__(parent)
        self.roomTempEnabled = True
        self.podcastBox = True
        self.studioBox = False
        self.nam = None

        self.updateTemperature()

        # background timer every 15 minutes
        self.updateTimer = QtCore.QTimer()
        self.updateTimer.timeout.connect(self.updateTemperature)
        self.updateTimer.start(15 * 60 * 1000)
        
    def updateTemperature(self):
        if(self.isEnabled and (self.podcastBox or self.studioBox)):
            print("updating room temperatures")
            self.makeAPICall()

    def makeAPICall(self):
        url = "https://fusefm-temp.bungeefield.io/api/current/"
        if(self.PodcastBox):
            print("Calling Podcast Room Temperature")
            url += "1"
        elif(self.StudioBox):
            print("Calling Studio Room Temperature")
            url += "2"

        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.finished.connect(self.handleAPIresponse)
        self.nam.get(req)


    def handleAPIresponse(self, reply):
        er = reply.error()
        if(er == QtNetwork.QNetworkReply.NoError):
            bytes_string = reply.readAll()
            reply_string = str(bytes_string, 'utf-8')
            try:
                temperature_json = json.loads(reply_string)
            except:
                error_string = "Room Temperature JSON Response: {}".format(reply_string)
                print(error_string)
                return
            room_name = temperature_json["roomName"]
            room_colour = temperature_json["roomColour"]
            temperature = "{:.1f}{}".format(temperature_json["temperature"], "°C")
        else:
            error_string = "Error occurred: {}, {}".format(er, reply.errorString())
            print(error_string)

    def setData(self,room_name, room_colour, temperature):
        pass
    