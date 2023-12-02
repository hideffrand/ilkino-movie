import sys
from .cinema import Il_Kino



if __name__ == '__main__':
    gifts = sys.argv[-1][7:]
    gifts = list(map(str, gifts.split(",")))
    ilkino = Il_Kino(gifts)
    ilkino.run()
