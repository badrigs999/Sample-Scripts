#!/usr/bin/python
"""
Created: 22nd Jun 2022

This module is used for internal notications.
we can use this module for any software which supports python.

"""

# default module
import re
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import binascii
import logging
logging.basicConfig(level=logging.DEBUG)


__author__ = ["Badri Gs"]
__email__ = "badri.gs999@gmail.com"


class CreateMail(object):
    """
    CreateMail SMTP instance.

    InternalMail is the class to send a notification to 
    given user.

    internal mail IP address: xx.xx.xx.xx:xx

    Note: we are restricted the BCC mail.
    """

    def __init__(self, *args, **kwargs):
        self._host = kwargs.get("host", None)
        self._port = kwargs.get("port", None)
        self._username = kwargs.get("username", None)
        self._password = kwargs.get("password", None)
        self.org_domain = kwargs.get("org_domain", None)
        self._subject = None
        self._to_addresses = []
        self._to_cc = []
        self.body = MIMEMultipart('alternative')

        # logging 
        self.logger = logging.getLogger("com.org.send-internal-mail")

        _checks =  [
          self.org_domain is not None,
          self._host is not None,
          self._port is not None,
          self._username is not None,
          self._password is not None
        ]

        if not all(_checks):
            raise ValueError("missing org_domain | host | port | username | password.")
    
    def __str__(self):
        return """
        To: {}
        CC: {}
        Subject: {}
        Body: {}
        """.format(
          self.to_address, self.cc_address, 
          self.subject_name, self.body
        )
      
    @static_method
    def check_and_correct_email_addresses(mail_address):
        if isinstance(mail_address, str):
            # this will return only the name
            if mail_address.find("@{0}".format(self.org_domain)) < -1:
                return "{0}@{1}".format(mail_address, self.org_domain)
        elif isinstance(mail_address, list):
            _results = []
            for each in mail_addresses:
                if each.find("@{0}".format(self.org_domain)) < -1:
                    _results.append("{0}@{1}".format(each, self.org_domain))
                else:
                    _results.append(each)
            return _results
        else:
            self.logger.error("Please give the valid mail ID.")
            raise ValueError("expected `str` or `list` found: `{0}`".format(type(mail_address)))
    
    @property
    def subject(self):
        return self._subject
    
    @property.setter
    def subject(self, _subject):
        if isinstance(_subject, str):
            self._subject = _subject
            self.logger.debug("subject: {}".format(subject_name))
        else:
            self.logger.error("Excepted `str` but given {}".format(type(subject_name)))
            raise TypeError("Excepted `str` but given {}".format(type(subject_name)))

    @property
    def to_address(self):
        return self._to_addresses
    
    @property.setter
    def to_address(self, _data):
        if isinstance(_data, str):
            self._to_addresses.append(self.check_and_correct_email_addresses(_data))
            self.logger.debug("Added {}".format(_data))
        else if isinstance(_data, list):
            self._to_addresses.extend(self.check_and_correct_email_addresses(_data))
            self.logger.debug("Added {}".format(_data))
        else:
            self.logger.error("Invalid To Address, required `str` or `list`.")
            raise TypeError("Invalid To Address, required `str` or `list`.")
    
    @property
    def cc_address(self):
        return self._to_cc
    
    @property.setter
    def cc_address(self, _data):
        if isinstance(_data, str):
            self._to_cc.append(self.check_and_correct_email_addresses(_data))
            self.logger.debug("Added {}".format(_data))
        else if isinstance(_data, list):
            self._to_cc.extend(_data)
            self.logger.debug("Added {}".format(self.check_and_correct_email_addresses(_data)))
        else:
            self.logger.error("Invalid CC Address, required `str` or `list`.")
            raise TypeError("Invalid CC Address, required `str` or `list`.")
  
            
    def append_body(self, _body):
        if not isinstance(_body, str):
            raise ValueError("Please Give the `str` data.")
        # check if content is html
        if bool(re.search("<\/?[a-z][\s\S]*>", _body)):
            self.body.attach(MIMEText(html_template, "html"))
        else:
            self.body.attach(MIMEText(_body, "plain"))
        
        self.logger.debug("body: {}".format(_body))
          
    def send_mail(self):

        """
        SMTP Mail sender
        """
        
        _checks = [
          self.subject is not None,
          len(self.to_addresses),
          len(self.cc_addresses)
        ]
        
        if not all(_checks):
            self.logger.error("missing data: provide all the data like (to_address, subject, body).")
            raise ValueError("missing data: provide all the data like (to_address, subject, body).")
        try:
          self.body['Subject'] = self.subject
          self.body['From'] = self.username
          self.body['To'] = ", ".join(self.to_address)
          self.body['Cc'] = ", ".join(self.cc_address)
          self.body['Bcc'] = ""

          server = SMTP(self.mail_host, self.mail_port)
          server.ehlo()
          server.login(
              self.username.replace(self.org_domain, ""), 
              binascii.unhexlify(self.password)
          )
          server.sendmail(
              self.username, 
              self.to_address+self.cc_address, 
              self.body.as_string()
          )
          server.quit()
        except Exception as _error:
          raise _error

if __name__ == '__main__':

    # create the mail instance.
    in_mail = InternalMail(
        host=os.environ.get("ORG_DOMAIN", None),
        host=os.environ.get("MAIL_HOST", None),
        port=os.environ.get("MAIL_PORT", None),
        username=os.environ.get("MAIL_USERNAME", None),
        password=os.environ.get("MAIL_pas", None),
    )
    in_mail.append_to_address(["abc_name"])
    in_mail.append_cc_address(["xyz_name"])
    in_mail.set_subject("test mail")
    in_mail.append_text_body("Hi, \ntesting mail")
    
    # preview the mail template
    logging.info("mail preview: {}".format(in_mail))
    
    in_mail.send_mail()

    logging.info("sending mail")
