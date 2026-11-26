dclm-1.0/counts/source.json: dclm-1.0/counts/*/*/source.json
	./etc/plan.py --sum $^ > $@;

starcoder-0.0.0/counts/source.json: starcoder-0.0.0/counts/*/source.json
	./etc/plan.py --sum $^ > $@;

dclm-1.0/counts/release.json: dclm-1.0/counts/*/*/release.json
	./etc/plan.py --sum $^ > $@;

starcoder-0.0.0/counts/release.json: starcoder-0.0.0/counts/*/release.json
	./etc/plan.py --sum $^ > $@;

clean:
	find . -name .\*.counts.json | xargs rm;
	find . -name .\*.md5 | xargs rm;

mix/stable.csv: mix/stable.txt etc/plan.py
	./flag/etc/plan.py --horizon $$(echo "8*10^12/0.976915" | bc) --budget --format , \
	  baby/mix/stable.txt | ( IFS= read -r head; echo $${head}; sort ) \
	> $@;

