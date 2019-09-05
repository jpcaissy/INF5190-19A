define HTML_HEADER
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>INF5190 - Automne 2019</title>
</head>

<body>
endef

.PHONY: index.html docker vendor

index.html:
	$(file > $@,$(HTML_HEADER))
	python3 -m markdown2 README.md >> $@
	@echo "</body></html>" >> $@

docker: index.html vendor
	sudo docker build -t jpcaissy/inf5190 .
	sudo docker push jpcaissy/inf5190

vendor: index.html
	git submodule update --init --recursive
	cd vendor/reveal.js ; npm install
