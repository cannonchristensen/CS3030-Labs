from datetime import date
import shutil

t = date.today()
date_str = t.isoformat()

shutil.make_archive("Section1_" + date_str, "zip", root_dir="../../section1")