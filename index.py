import sys
import fresh_tomatoes

if len(sys.argv) > 1:
    port = sys.argv[1]
else:
    port = 8000

fresh_tomatoes.start(port)
