import jenkins
import json

server = jenkins.Jenkins('http://192.168.5.5:8080', username='admin', password='admin')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

print('Jenkins plugins:')
plugins = server.get_plugins_info()
#print(plugins)
json.dumps(plugins)
~
