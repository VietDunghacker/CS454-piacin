import pandas as pd
import sys
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, NullLocator, FormatStrFormatter

def process_default_runs(log_prefix):
	index = pd.Series(range(20), name="index")
	df = pd.DataFrame(columns=["index", "time"])
	for i in range(20):
		input_file = "%s_%02d.txt" % (log_prefix, i)
		times = pd.read_csv(input_file, names=["time"], comment="#")
		# print times
		_new = pd.DataFrame({"index":index, "time":times["time"]})
		df = df.append(_new)
	df.to_csv("%s_concat.csv" % (log_prefix), sep=",", index=False)

def process_piacin_runs(log_prefix):
	index = pd.Series(range(100), name="index")
	df = pd.DataFrame(columns=["index", "time"])
	for i in range(20):
		input_file = "%s_%02d.txt" % (log_prefix, i)
		times = pd.read_csv(input_file, names=["time"], comment="#")
		# print times
		_new = pd.DataFrame({"index":index, "time":times["time"]})
		df = df.append(_new)
	df.to_csv("%s_concat.csv" % (log_prefix), sep=",", index=False)


if __name__ == '__main__':
	process_default_runs("log_bm_spambayes.py_n_20_bm_50_pypy_piacin_0_run")
	process_piacin_runs("log_bm_spambayes.py_n_100_bm_50_pypy_piacin_1_run")

	process_default_runs("log_bm_spitfire.py_n_20_bm_50_pypy_piacin_0_run")
	process_piacin_runs("log_bm_spitfire.py_n_100_bm_50_pypy_piacin_1_run")

	process_default_runs("log_bm_regex_v8.py_n_20_bm_50_pypy_piacin_0_run")
	process_piacin_runs("log_bm_regex_v8.py_n_100_bm_50_pypy_piacin_1_run")

	process_default_runs("log_bm_regex_compile.py_n_20_bm_50_pypy_piacin_0_run")
	process_piacin_runs("log_bm_regex_compile.py_n_100_bm_50_pypy_piacin_1_run")

	process_default_runs("log_bm_django.py_n_20_bm_50_pypy_piacin_0_run")
	process_piacin_runs("log_bm_django.py_n_100_bm_50_pypy_piacin_1_run")

	process_default_runs("log_bm_call_method.py_n_20_bm_50_pypy_piacin_0_run")
	process_piacin_runs("log_bm_call_method.py_n_100_bm_50_pypy_piacin_1_run")