import time
import logging.config

from vnfm.sdk.AbstractVnfmABC import AbstractVnfm, start_vnfm_instances

log = logging.getLogger("org.openbaton.python.vnfm.PythonVnfm")


class PythonVnfm(AbstractVnfm):
    def upgradeSoftware(self):
        pass

    def updateSoftware(self):
        pass

    def terminate(self, vnf_record):
        log.info("Executing TERMINATE for VNFR: %s" % vnf_record.get("name"))
        return vnf_record

    def stopVNFCInstance(self, vnf_record, vnfc_instance):
        pass

    def stop(self, vnf_record):
        pass

    def startVNFCInstance(self, vnf_record, vnfc_instance):
        pass

    def start_vnfr(self, vnf_record):
        log.info("Executing start for VNFR: %s" % vnf_record.get("name"))
        time.sleep(3)

        return vnf_record

    def scale(self, scale_out, vnf_record, vnf_component, scripts, dependency):
        pass

    def query(self):
        pass

    def notifyChange(self):
        pass

    def modify(self, vnf_record, dependency):
        log.info("Executing modify for VNFR: %s" % vnf_record.get("name"))

        log.debug("Dependencies are: \n%s" % dependency)
        time.sleep(3)

        return vnf_record

    def instantiate(self, vnf_record, scripts, vim_instances):
        log.info("Executing instantiate for VNFR: %s" % vnf_record.get("name"))
        log.info("Scripts are: ")
        if isinstance(scripts, (str, unicode)):
            log.info("Script link is: %s" % scripts)
        else:
            for script in scripts:
                log.debug("Script name: %s" % script.get("name"))
        time.sleep(3)
        return vnf_record

    def heal(self, vnf_record, vnf_instance, cause):
        pass

    def handleError(self, vnf_record):
        log.info("Executing ERROR for VNFR: %s" % vnf_record.get("name"))
        return vnf_record

    def checkInstantiationFeasibility(self):
        pass


if __name__ == "__main__":
    conf = "logging.conf"
    logging.config.fileConfig('logging.conf')
    log.info("Starting Python Vnfm")
    start_vnfm_instances(PythonVnfm, "python", 5)
