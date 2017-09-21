import sys
from Naked.toolshed.shell import muterun_js
var = 'bottry.js ' + sys.argv[1]
response = muterun_js(var)
if response.exitcode == 0:
  print(str(response.stdout))
else:
  sys.stderr.write(str(response.stderr))
