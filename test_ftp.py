import ftplib
from unittest import mock
import unittest

from ftp import FTP_Client


class FTPTestCase(unittest.TestCase):
    ftp = ftplib.FTP

    @mock.patch('ftplib.open')
    @mock.patch('ftplib.FTP')
    def test_get_file_sucess(self, mockFtp, mOpen):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()

        mOpen.return_value = mock.Mock()

        mockFtpObj.get_file(self, "test")
        mockFtpObj.retrbinary.called
        mOpen.called


if __name__ == '__main__':
    unittest.main()