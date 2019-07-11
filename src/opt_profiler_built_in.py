# Command line:
# python3 -m cProfile opt_profiler_built_in.py
# Ugly, hard to deal with, bleah

# python3 --help
# python3 -m cProfile -o so_DeepakKeshari.cprof so_DeepakKeshari.py
# lots we can do with that cprof file, it is a standard format lots of tools use…

# Let’s look at these cprof files in python
import pstats
p = pstats.Stats('so_DeepakKeshari.cprof')
p.strip_dirs().sort_stats(-1).print_stats()
p.sort_stats('cumulative').print_stats(10)

# can run the same profiling from inside a python script or shell as well:
import cProfile
import so_DeepakKeshari
cProfile.run('so_DeepakKeshari.calcPi(100)', 'so_DeepakKeshari_function.cprof')
# another cprof file!

# let's just go nuts with these cprof files
import w3_soln
cProfile.run('w3_soln.calcPi(1000)', 'w3_soln_function.cprof')
import so_cdlane
cProfile.run('so_cdlane.calcPi(10000)', 'so_cdlane_function.cprof')
import so_Martin_Thoma
cProfile.run('so_Martin_Thoma.calcPi(1000)', 'so_Martin_Thoma_function.cprof')


# Not going to look at it but we could… or we could do this with areas of codes or functions
# Though there is a better way:

import cProfile, pstats, io
pr = cProfile.Profile()
pr.enable()
so_DeepakKeshari.calcPi(100)
pr.disable()
s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())



