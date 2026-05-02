import jinja2

class ConfigGenerator:
    
    def __init__(self, template_file):
        self.template_file = template_file

    def render(self, server_name, port, docroot):
        try:
            with open(self.template_file) as t:
                read_template = t.read()
        except FileNotFoundError:
            raise ValueError("Template missing.")

        template = jinja2.Template(read_template)
        gen_conf =  template.render(server_name=server_name, port=port, docroot=docroot)
        return gen_conf

gen = ConfigGenerator("vhost.j2")
print(gen.render("web01.epam.com", 80, "/var/www"))
