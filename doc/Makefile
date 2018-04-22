EXE=learnCPlusPlus.pdf
SRC=learnCPlusPlus.tex
BIB=learnCPlusPlus.aux

$(EXE):$(SRC)
	xelatex $(SRC)

.PHONY.:look
look:
	evince learnCPlusPlus.pdf

.PHONY.:clean
clean:
	$(RM) learnCPlusPlus.aux learnCPlusPlus.log learnCPlusPlus.pdf learnCPlusPlus.dvi learnCPlusPlus.bbl learnCPlusPlus.blg learnCPlusPlus.toc learnCPlusPlus.out learnCPlusPlus.nav learnCPlusPlus.snm learnCPlusPlus.thm learnCPlusPlus.lot learnCPlusPlus.lof
