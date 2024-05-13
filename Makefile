.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: setup
setup: ## Setup local environment
	@pdm sync

.PHONY: lint
lint:  ## Lint and fix code
	@PIPENV_VERBOSITY=-1
	@pdm run black --target-version=py312 .
	@pdm run pylint --recursive=y ./src ./tests

.PHONY: test
test:  ## Locally run unit tests
	@pdm run pytest
