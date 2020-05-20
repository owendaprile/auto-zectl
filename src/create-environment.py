import configparser
import subprocess
import datetime

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('/etc/auto-zectl.conf')

    boot_environment_name = config['auto-zectl']['BootEnvironmentIdentifier'] + \
        '_' + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    subprocess.run(['/usr/bin/zectl', 'create', boot_environment_name])
