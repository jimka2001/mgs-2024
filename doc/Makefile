## Copyright (C) 2024 Jim Newton

all: pdf

SRC_DIR  := .
IMAGE_DIR := $(SRC_DIR)/img
LATEXMK = latexmk --pdf

pdf: mgs-2024-handout.pdf mgs-2024-slides.pdf galois.pdf

galois.pdf: ${SRC_DIR}/galois.ltx
	TEXINPUTS=$(TEXINPUTS):$(IMAGE_DIR) \
	${LATEXMK} ${SRC_DIR}/galois.ltx || true


mgs-2024-slides.pdf : ${SRC_DIR}/mgs-2024-slides.ltx
	TEXINPUTS=$(TEXINPUTS):$(IMAGE_DIR) \
	${LATEXMK} ${SRC_DIR}/mgs-2024-slides.ltx
	([ -d ~/Google\ Drive/MGS\ 2024/. ] && cp -fv $@ ~/Google\ Drive/MGS\ 2024/.) || true

mgs-2024-handout.pdf : ${SRC_DIR}/mgs-2024-handout.ltx
	TEXINPUTS=$(TEXINPUTS):$(IMAGE_DIR) \
	${LATEXMK} ${SRC_DIR}/mgs-2024-handout.ltx
	([ -d ~/Google\ Drive/MGS\ 2024/. ] && cp -fv $@ ~/Google\ Drive/MGS\ 2024/.) || true

pvc-handout:
	TEXINPUTS=$(TEXINPUTS):$(IMAGE_DIR) \
	${LATEXMK} -pvc ${SRC_DIR}/mgs-2024-handout.ltx

pvc-slides:
	TEXINPUTS=$(TEXINPUTS):$(IMAGE_DIR) \
	${LATEXMK} -pvc ${SRC_DIR}/mgs-2024-slides.ltx

WEBPAGE_REPO := git@gitlab.lre.epita.fr:lre/lre-web/members/jim-newton.git

webpage: mgs-2024-handout.pdf mgs-2024-slides.pdf galois.pdf
	tmp=$$(mktemp -d) && \
	git clone --depth 1 --quiet $(WEBPAGE_REPO) $$tmp && \
	cp mgs-2024-handout.pdf mgs-2024-slides.pdf $$tmp/ && \
	cp galois.pdf $$tmp/mgs-2024-galois.pdf && \
	cd $$tmp && \
	git add mgs-2024-handout.pdf mgs-2024-slides.pdf mgs-2024-galois.pdf && \
	(git diff --cached --quiet || git commit --quiet -m "Update mgs-2024-handout.pdf, mgs-2024-slides.pdf, mgs-2024-galois.pdf") && \
	git push --quiet ; \
	status=$$? ; rm -rf $$tmp ; exit $$status
