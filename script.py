import os
from pySym import ast_parse
from pySym.pyPath import Path
from pySym.pyPathGroup import PathGroup

test2 = os.getenv('TEST_TEXT')
b = ast_parse.parse(test2).body
p = Path(b,source=test2)
pg = PathGroup(p)
pg.explore()

print(len(pg.deadended))
print(len(pg.completed))