from telemetry.gps import NMEASentenceFactory


class AbstractDataProcessor(object):
    def process(self, data):
        raise NotImplementedError


class MainDataProcessor(AbstractDataProcessor):
    def process(self, data):
        pass


class GPSNMEADataProcessor(AbstractDataProcessor):
    def process(self, data):
        nmea_sentence = NMEASentenceFactory.create(NMEASentenceFactory.SENTENCE_TYPE['GPGGA'], data)
        if nmea_sentence is not None:
            return self.create_dict_from(nmea_sentence)
        else:
            return None

    def create_dict_from(self, data):
        return {'coords': str(data.latitude) + "," + str(data.longitude),
                'fix': data.fix,
                'altitude': data.altitude,
                'satellites': data.number_of_satellites}
