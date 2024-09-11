def test_nginx_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed

def test_https_redirect(host):
    cmd = host.run("curl -I http://localhost")
    assert "301 Moved Permanently" in cmd.stdout

def test_hello_world_page(host):
    cmd = host.run("curl -k https://localhost")
    assert "<h1>Hello World!</h1>" in cmd.stdout
