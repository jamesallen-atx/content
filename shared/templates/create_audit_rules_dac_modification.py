#!/usr/bin/python2

#
# create_audit_rules_dac_modification.py
#        generate template-based checks for audit rules dac modifications


import re

from template_common import FilesGenerator, UnknownTargetError


class AuditRulesDacModificationGenerator(FilesGenerator):
    def __init__(self):
        super(AuditRulesDacModificationGenerator, self).__init__()
        self.delimiter = '&'

    def generate(self, target, audit_info):
        # the csv file contains lines that match the following layout:
        #    attr

        if target == "oval":
            # we are ready to create the check
            # open the template and perform the conversions
            attr = audit_info[0]

            self.file_from_template(
                "./template_OVAL_audit_rules_dac_modification",
                {
                    "%ATTR%":           attr,
                },
                "./oval/audit_rules_dac_modification_{0}.xml", attr
            )
        else:
            raise UnknownTargetError(target)

    def csv_format(self):
        return("CSV should contains lines of the format: "
               "attr")

if __name__ == "__main__":
    AuditRulesDacModificationGenerator().main()
