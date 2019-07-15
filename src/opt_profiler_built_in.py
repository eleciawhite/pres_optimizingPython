# Command line:
# python3 --help
# python3 --?
# python3 -m cProfile opt_profiler_built_in.py –o opt_profiler.conf
# Ugly, hard to deal with, bleah. Lots of 
# python3 -m cProfile -o so_DeepakKeshari100.cprof so_DeepakKeshari.py
# python3 -m cProfile -o so_DeepakKeshari1000.cprof so_DeepakKeshari.py

# lots we can do with that cprof file, it is a standard format lots of tools use…
# Let’s look at these cprof files in python
import pstats
p = pstats.Stats('so_DeepakKeshari100.cprof')
p.strip_dirs().sort_stats('cumulative').print_stats(20)
# still pretty confusing, input is a big one, lots of stuff here

# Let’s look at these cprof files in python
import pstats
p = pstats.Stats('so_DeepakKeshari1000.cprof')
p.strip_dirs().sort_stats('cumulative').print_stats(20)

# input is still on there, avoid that
# can run the same profiling from inside a python script or shell as well:
import cProfile
import so_DeepakKeshari
cProfile.run('so_DeepakKeshari.calcPi(100)', 'so_DeepakKeshari_function.cprof')
# another cprof file!
p = pstats.Stats('so_DeepakKeshari_function.cprof')
p.strip_dirs().sort_stats('cumulative').print_stats(20)
# look at cumulative time (where it spends its time including function calls) vs totaltime (doesn't include function calls)


# Look at the code that it points to or we could do this with areas of codes or functions
# Though there is a better way:
import cProfile, pstats, io
pr = cProfile.Profile()
pr.enable()
so_DeepakKeshari.calcPi(100)
pr.disable()
s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).strip_dirs().sort_stats(sortby)
ps.print_stats()
print(s.getvalue())

# Good info, much shorter
# let's just go nuts with these cprof files
import so_cdlane
cProfile.run('so_cdlane.calcPi(10000)', 'so_cdlane_function.cprof')
p = pstats.Stats('so_cdlane_function.cprof')
p.strip_dirs().sort_stats('cumulative').print_stats(20)
# I wonder if there is a library to implement arctan faster...

import w3_soln
cProfile.run('w3_soln.calcPi(5000)', 'w3_soln_function.cprof')
p = pstats.Stats('w3_soln_function.cprof')
p.strip_dirs().sort_stats('cumulative').print_stats(20)

import so_Martin_Thoma
cProfile.run('so_Martin_Thoma.calcPi(5000)', 'so_Martin_Thoma_function.cprof')
p = pstats.Stats('so_Martin_Thoma_function.cprof')
p.strip_dirs().sort_stats('cumulative').print_stats(20)



