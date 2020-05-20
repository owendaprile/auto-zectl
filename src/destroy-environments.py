import shutil
import subprocess
import configparser


def get_esp_usage(esp):
    esp_stat = shutil.disk_usage(esp)
    return esp_stat.used / esp_stat.total


def get_boot_environments(identifier):
    zectl_list = subprocess.run(
        ['/usr/bin/zectl', 'list'], capture_output=True, check=True).stdout.decode()

    boot_envs = list()

    for line in zectl_list.splitlines():
        if identifier in line:
            boot_envs.append(line.split(' ')[0])

    return sorted(boot_envs, reverse=True)


def destroy_boot_environment(boot_environment):
    subprocess.run(['/usr/bin/zectl', 'destroy', boot_environment], check=True)


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('/etc/auto-zectl.conf')

    boot_environment_identifier = config['auto-zectl']['BootEnvironmentIdentifier']
    esp = config['auto-zectl']['ESP']
    keep_environments = config['auto-zectl'].getint('KeepEnvironments')
    esp_disk_space = config['auto-zectl'].getfloat('ESPDiskSpace') / 100

    if get_esp_usage(esp) < esp_disk_space:
        exit(0)

    boot_environments = get_boot_environments(boot_environment_identifier)

    while get_esp_usage(esp) >= esp_disk_space and boot_environments and len(boot_environments) > keep_environments:
        destroy_boot_environment(boot_environments[-1])
        boot_environments.pop()
