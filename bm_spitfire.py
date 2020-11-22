import argparse
import os, sys
import time

# Spitfire imports
import spitfire
import spitfire.compiler.analyzer
import spitfire.compiler.util

SPITFIRE_SRC = """<table xmlns:py="http://spitfire/">
#for $row in $table
<tr>
#for $column in $row
<td>$column</td>
#end for
</tr>
#end for
</table>
"""

def test_spitfire(count):
    # Activate the most aggressive Spitfire optimizations. While it might
    # conceivably be interesting to stress Spitfire's lower optimization
    # levels, we assume no-one will be running a production system with those
    # settings.
    spitfire_tmpl_o4 = spitfire.compiler.util.load_template(
        SPITFIRE_SRC,
        "spitfire_tmpl_o4",
        spitfire.compiler.analyzer.o4_options,
        {"enable_filters": False})

    table = [xrange(1000) for _ in xrange(1000)]

    # Warm up Spitfire.
    spitfire_tmpl_o4(search_list=[{"table": table}]).main()
    spitfire_tmpl_o4(search_list=[{"table": table}]).main()

    times = []
    for _ in xrange(count):
        t0 = time.time()
        data = spitfire_tmpl_o4(search_list=[{"table": table}]).main()
        t1 = time.time()
        times.append(t1 - t0)
    return sum(times)

class FakePsyco(object):
    def bind(self, *args, **kwargs):
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--piacin', dest='piacin', action='store_const', const=True, default=False, help='Use piacin')
    parser.add_argument('--clear', dest='clear', action='store_const', const=True, default=False, help='Clear piacin bag')
    parser.add_argument("-k", "--bmnumber", type=int, default=100, help="Number of time to repeat benchmark within run (default: 100)")
    args = parser.parse_args()

    sys.modules["psyco"] = FakePsyco()

    if args.piacin:    
        import piacin.hc

    print test_spitfire(args.bmnumber)