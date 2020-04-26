import logging
from wikigraph.model.validationArgz import Outcome
from wikigraph.config.Config import Config


class validateArgz():
    def __init__(self):
        log_level = Config().getLogLevel()
        self.log = logging.getLogger(__name__)
        self.log.setLevel(getattr(logging, log_level))

    def run(self, argzdict):
        if len(argzdict) != 1:
            self.log.error(
                "You need to post only phrases as argument. Found: {}".format(argzdict.values))
            return Outcome(
                "You need to post only phrases as argument. Found: {}".format(argzdict.values), False)

        if not argzdict['phrases']:
            self.log.error("Your request hasn't the required parameter phrases")
            return Outcome("Your request hasn't the required parameter phrases", False)

        return Outcome(argzdict, True)


    def single_run(self, argzdict):
        if len(argzdict) != 1:
            self.log.error(
                "You need to post only string as argument. Found: {}".format(argzdict.values))
            return Outcome(
                "You need to post only string as argument. Found: {}".format(argzdict.values), False)

        if not argzdict['string']:
            self.log.error("Your request hasn't the required parameter string")
            return Outcome("Your request hasn't the required parameter string", False)

        return Outcome(argzdict, True)