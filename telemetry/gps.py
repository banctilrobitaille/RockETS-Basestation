class NMEASentence(object):
    def __init__(self):
        super(NMEASentence, self).__init__()
        self.__identifier = ""

    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier):
        self.__identifier = identifier


class GPGGASentence(NMEASentence):
    FIX = {
        0: "INVALID FIX",
        1: "GPS FIX",
        2: "DGPS FIX",
    }

    def __init__(self, data):
        super(GPGGASentence, self).__init__()

        try:
            sentence_elements = data.split(",")
            self.identifier = sentence_elements[0]
            self.__fixTime = sentence_elements[1]
            self.__latitude = sentence_elements[2]
            self.__longitude = sentence_elements[4]
            self.__fix = int(sentence_elements[6])
            self.__nbSatellite = int(sentence_elements[7])
            self.__altitude = float(sentence_elements[9])

        except Exception as e:
            pass

    @property
    def fix_time(self):
        return self.__fixTime

    @fix_time.setter
    def fix_time(self, fix_time):
        self.__fixTime = fix_time

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude):
        self.__latitude = latitude

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude):
        self.__longitude = longitude

    @property
    def fix(self):
        return GPGGASentence.FIX[self.__fix]

    @fix.setter
    def fix(self, fix):
        self.__fix = fix

    @property
    def number_of_satellites(self):
        return self.__nbSatellite

    @number_of_satellites.setter
    def number_of_satellites(self, number_of_satellites):
        self.__nbSatellite = number_of_satellites

    @property
    def altitude(self):
        return self.__altitude

    @altitude.setter
    def altitude(self, altitude):
        self.__altitude = altitude


class NMEASentenceFactory(object):
    SENTENCE_TYPE = {
        "GPGGA": "GPGGA",
        "GPGSA": "GPGSA",
        "GPGSV": "GPGSV",
        "GPMRC": "GPMRC",
    }

    @staticmethod
    def create(sentence_type, data):
        sentence = None
        if sentence_type is NMEASentenceFactory.SENTENCE_TYPE['GPGGA']:
            if NMEASentenceFactory.SENTENCE_TYPE['GPGGA'] in data:
                sentence = GPGGASentence(data)

        return sentence
