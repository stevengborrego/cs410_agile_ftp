import ftplib
import os
from unittest import mock
import unittest

from ftp import FTP_Client  

class FTPTestCase(unittest.TestCase):

    @mock.patch('ftplib.FTP')
    def test_log_off_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()
        
        ftp = FTP_Client(mockFtpObj)
        
        ftp.log_off()
        mockFtpObj.quit.assert_called()

    @mock.patch('ftplib.FTP')
    def test_get_file_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()
        
        ftp = FTP_Client(mockFtpObj)
        
        ftp._get_file("test")
        mockFtpObj.retrbinary.assert_called()

    @mock.patch('ftplib.FTP')
    def test_get_mul_file_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()

        ftp = FTP_Client(mockFtpObj)

        
        ftp._get_mul_files("test test1")
        ftp.ftp.close()
        mockFtpObj.retrbinary.assert_called()
    
    @mock.patch('ftplib.FTP')
    def test_upload_mul_file_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()

        ftp = FTP_Client(mockFtpObj)

        
        ftp._upload_multiple_files("test test1")
        ftp.ftp.close()
        mockFtpObj.storbinary.assert_called()

    @mock.patch('ftplib.FTP')
    @mock.patch('ftplib.open')
    def test_put_file_sucess(self, mockFtp, mOpen):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()

        mOpen.return_value = mock.Mock()

        ftp = FTP_Client(mockFtpObj) 
        
        ftp._put_file("test")
        mockFtpObj.storbinary.assert_called()

    @mock.patch('ftplib.FTP')
    def test_delete_file_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()

        ftp = FTP_Client(mockFtpObj) 
        
        ftp._delete_file("test")
        mockFtpObj.delete.assert_called()
    
    @mock.patch('ftplib.FTP')
    def test_list_directories_and_file_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()

        ftp = FTP_Client(mockFtpObj)

        ftp.list_directories_and_files()
        mockFtpObj.dir.assert_called()

    @mock.patch('ftplib.FTP')
    @mock.patch('os.listdir')
    def test_list_local_directories_and_file_sucess(self, mockFtp, mockOs):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()
    
        mockOs.return_value = mock.Mock()
        mockOsObj = mockOs()
        
        ftp = FTP_Client(mockFtpObj)
        ftp.passOS(mockOsObj)

        ftp._local_dir_and_files()

        mockOsObj.listdir.assert_called()

    @mock.patch('ftplib.FTP')
    def test_create_dir_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()

        ftp = FTP_Client(mockFtpObj)
        
        ftp._create_dir("test")

        assert mockFtpObj.mkd.called


    @mock.patch('ftplib.FTP')
    def test_delete_dir_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()

        ftp = FTP_Client(mockFtpObj)
        
        ftp._delete_dir("test")

        assert mockFtpObj.rmd.called

    @mock.patch('ftplib.FTP')
    def test_copy_directory_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()

        ftp = FTP_Client(mockFtpObj)
        
        ftp._copy_directories("test test1")

        assert mockFtpObj.copy_dir.called

    @mock.patch('ftplib.FTP')
    def test_rename_file_remote_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()
        
        ftp = FTP_Client(mockFtpObj)
        
        ftp._rename_file_remote("fromName", "toName")
        mockFtpObj.rename.assert_called()

    @mock.patch('ftplib.FTP')
    @mock.patch('os.rename')
    def test_rename_file_local_sucess(self, mockFtp, mockOs):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()
    
        mockOs.return_value = mock.Mock()
        mockOsObj = mockOs()
        
        ftp = FTP_Client(mockFtpObj)
        ftp.passOS(mockOsObj)
        
        ftp._rename_file_local("fromName", "toName")
        mockOsObj.rename.assert_called()

    @mock.patch('ftplib.FTP')
    def test_change_permission_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()
        
        ftp = FTP_Client(mockFtpObj)
        
        ftp._change_permission("test", "IDK")
        mockFtpObj.sendcmd.assert_called()

    @mock.patch('ftp.open')
    @mock.patch('ftplib.FTP')
    def test_save_info_sucess(self, mockFtp, mOpen):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()
        
        ftp = FTP_Client(mockFtpObj)

        mOpen.return_value = mock.Mock()
        
        #ftp.save_info("IDK")
        mOpen.assert_called

    @mock.patch('ftp.open')
    @mock.patch('ftplib.FTP')
    def test_load_info_sucess(self, mockFtp, mOpen):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()
        
        ftp = FTP_Client(mockFtpObj)

        mOpen.return_value = mock.Mock()
        
        #ftp.load_info()
        mOpen.assert_called

    @mock.patch('ftp.open')
    @mock.patch('ftplib.FTP')
    def test_diff_sucess(self, mockFtp, mOpen):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()
        
        ftp = FTP_Client(mockFtpObj)

        mOpen.return_value = mock.Mock()
        
        #ftp._diff("Test1", "Test2")
        mOpen.assert_called
    
    @mock.patch('ftp.open')
    @mock.patch('ftplib.FTP')
    def test_cat_sucess(self, mockFtp, mOpen):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()
        
        ftp = FTP_Client(mockFtpObj)

        mOpen.return_value = mock.Mock()
        
        ftp._cat("Test1")
        mOpen.assert_called()

    @mock.patch('ftp.open')
    @mock.patch('ftplib.FTP')
    def test_session_details_for_update_sucess(self, mockFtp, mOpen):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()
        
        ftp = FTP_Client(mockFtpObj)

        mOpen.return_value = mock.Mock()
        
        ftp._session_details_for_update()
        mOpen.assert_called




   





if __name__ == '__main__':
    unittest.main()