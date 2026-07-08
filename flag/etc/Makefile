dclm-1.0/counts/source.json: dclm-1.0/counts/*/*/source.json
	./etc/plan.py --sum $^ > $@;

finephrase-0.0.0/counts/source.json: finephrase-0.0.0/counts/*/source.json
	./etc/plan.py --sum $^ > $@;

megamath-0.0.0/counts/source.json: megamath-0.0.0/counts/*/source.json megamath-0.0.0/counts/*/*/source.json
	./etc/plan.py --sum $^ > $@;

mixture-vitae-1.0/counts/source.json: mixture-vitae-1.0/counts/*/source.json
	./etc/plan.py --sum $^ > $@;

nemotron-mind-0.0/counts/source.json: nemotron-mind-0.0/counts/*/source.json
	./etc/plan.py --sum $^ > $@;

nemotron-pretraining-specialized-1.0/counts/source.json: nemotron-pretraining-specialized-1.0/counts/*/source.json
	./etc/plan.py --sum $^ > $@;

nemotron-pretraining-specialized-1.1/counts/source.json: nemotron-pretraining-specialized-1.1/counts/*/source.json
	./etc/plan.py --sum $^ > $@;

starcoder-0.0.0/counts/source.json: starcoder-0.0.0/counts/*/source.json
	./etc/plan.py --sum $^ > $@;

swallow-math-2.0/counts/source.json: swallow-math-2.0/counts/*/source.json swallow-math-2.0/counts/*/source.json
	./etc/plan.py --sum $^ > $@;

dclm-1.0/counts/release.json: dclm-1.0/counts/*/*/release.json
	./etc/plan.py --sum $^ > $@;

starcoder-0.0.0/counts/release.json: starcoder-0.0.0/counts/*/release.json
	./etc/plan.py --sum $^ > $@;

clean:
	find . -name .\*.counts.json | xargs rm;
	find . -name .\*.md5 | xargs rm;
