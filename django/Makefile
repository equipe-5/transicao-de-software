.PHONY: all codequality security prospector bandit safety

all: codequality security

codequality: prospector

security: bandit safety

prospector:
	@ prospector .

bandit:
	@ bandit --recursive .

safety:
	@ printf -- '-r\0%s\0' main/requirements/*.txt | xargs -0 safety check --no-prompt --full-report
