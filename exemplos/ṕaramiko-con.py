import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('172.28.12.170', username='kub-admin', password='admin')

# Executando o UPDATE

stdin, stdout, stderr = ssh.exec_command('ls -lah')

print(stdout.readlines())

# Executando o UPGRADE

stdin, stdout, stderr = ssh.exec_command('ls -lah')

stdin.write('y\n')

stdin.flush()

print(stdout.readlines())

ssh.close()
