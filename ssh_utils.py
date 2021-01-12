import paramiko

class Ssh_utils:

    def test_connection_rsa(self):
        "test ssh to the remote server"
        result_flag = True
        self.target_ip = input("Enter an IP address to connect to: ") 
        self.target_user = input("Enter the user to connect with: ") 
        self.pkey = input("Enter full path to your RSA private-key: ")
        self.passphrase = input("Enter passphrase for this RSA private-key: ")


        self.pkey = paramiko.RSAKey.from_private_key_file(self.pkey)    

        self.client = paramiko.SSHClient()

        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            self.client.connect(hostname=self.target_ip,
                                username=self.target_user,
                                pkey=self.pkey)
                
        except paramiko.AuthenticationException:
            print("Authentication failed, please verify your credentials")
            result_flag = False
        except paramiko.SSHException as sshException:
            print("Could not establish SSH connection: %s" % sshException)
            result_flag = False
        except socket.timeout as e:
            print("Connection timed out")
            result_flag = False
        except Exception as e:
            print('Exception was raised:', e)
            result_flag = False
            self.client.close()

        return result_flag

    def execute_test(self): 
        if self.test_connection_rsa():
            self.client.close()
            print("connection via ssh was successful. Connection has just been closed")
        else:
            print("test failed with error.")



