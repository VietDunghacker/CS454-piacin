decimals = 4
fmp <- function(x){
	if(x < 0.05)
	{
		formatted = format(round(x, decimals), nsmall=decimals)
		if(formatted == "0.0000"){
			return("\\textbf{< 1e-4}")
		}
		else{
			paste("\\textbf(", format(round(x, decimals), nsmall=decimals), ")", sep="")
		}
	} 
	else format(round(x, decimals), nsmall=decimals)
}

fm <- function(x){
	format(round(x, decimals), nsmall=decimals)
}

setwd("/Users/ntrolls/Projects/piacin/test")

benchmarks = c("bm_spambayes.py", "bm_spitfire.py", "bm_regex_v8.py", "bm_django.py", "bm_regex_compile.py", "bm_call_method.py")

for(bm in benchmarks)
{
	f0 = paste("log_", bm, "_n_20_bm_50_pypy_piacin_0_run_concat.csv", sep="")
	f1 = paste("log_", bm, "_n_100_bm_50_pypy_piacin_1_run_concat.csv", sep="")
	
	df0 = read.csv(f0, sep=",")
	df1 = read.csv(f1, sep=",")
	
	min_y = min(min(df0$time), min(df1$time))
	max_y = max(max(df0$time), max(df1$time))
	
	p = paste("boxplot_", bm, ".pdf", sep="")
	pdf(p, width=10, height=5)

	l = rep(c(""), 100)
	for(x in seq(0, 100, by=10)){l[x] = x}
	m <- matrix(c(1, 2), nrow=1, ncol=2)
	layout(m, widths=c(1, 3))
	boxplot(time ~ index, df0, ylim=c(min_y, max_y), at=seq(0, 19), xaxt="n", main=paste("Default:", bm), cex.main=0.8)
	axis(side=1, at=seq(0, 99, by=5), cex.axis=0.8)
	axis(side=2)
	boxplot(time ~ index, df1, ylim=c(min_y, max_y), at=seq(0, 99), xaxt="n", main=paste("Amortised Optimisation:", bm), cex.main=0.8)
	abline(v=79)
	axis(side=1, at=seq(0, 99, by=5), cex.axis=0.8)
	dev.off()
	
	default_time = df0$time
	optimised_time = subset(df1, df1$index >= 80)$time
	print(paste(bm, "default", "shapiro-wilk", shapiro.test(default_time)$p.value))
	print(paste(bm, "default", "mean", fm(mean(default_time)), "st.dev", fm(sd(default_time))))
	print(paste(bm, "optimised", "shapiro-wilk", shapiro.test(optimised_time)$p.value))
	print(paste(bm, "optimised", "mean", fm(mean(optimised_time)), "st.dev", fm(sd(optimised_time))))
	print(paste(bm, "t.test", "p.value", t.test(default_time, optimised_time, alternative="greater")$p.value))
	print(" ")
}