import pytest
from pytest_mock import mocker
from unittest.mock import patch
import ftp


def get_file_sucess(self, mock_ftp_constructor):
  ftp_constructor_mock = mocker.patch('cs410_agile_ftp.ftp.FTP_Client')
  ftp_mock = ftp_constructor_mock.return_value
  ftp_mock.get_file('test.txt')
  #ftp_constructor_mock.assert_called_with('ftp.server.local')
  ftp_mock.cwd.assert_called_with('test.txt')
