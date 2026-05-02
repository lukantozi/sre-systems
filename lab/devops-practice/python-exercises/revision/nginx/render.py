import yaml
from jinja2 import Template

with open("nginx.j2") as f:
    template = Template(f.read())

with open("data.yml") as data:
    vhosts = template.render(yaml.load(data, Loader=yaml.FullLoader))

#vhosts = template.render(config_data)
with open("vhosts.conf", "w") as f:
    f.write(vhosts)
