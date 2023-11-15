.PHONY: all codequality security ruff bandit safety

all: codequality security

codequality: ruff

security: bandit safety

ruff:
	@ ruff check . --show-source

bandit:
	@ bandit --recursive .

safety:
	@ printf -- '-r\0%s\0' main/requirements/*.txt | xargs -0 safety check --no-prompt --full-report
