#! ~/softwares/R-3.4/packages/R-3.4.4/bin/Rscript
Args <- commandArgs()
input_file <- Args[6]

# ipak function: install and load multiple R packages.
# check to see if packages are installed. Install them if they are not, then load them into the R session.

ipak <- function(pkg){
    new.pkg <- pkg[!(pkg %in% installed.packages()[, "Package"])]
    if (length(new.pkg)) 
        install.packages(new.pkg, dependencies = TRUE)
    sapply(pkg, require, character.only = TRUE)
}

# usage

packages_info <-read.csv(input_file,header = TRUE)
packages_CRAN <-subset(packages_info,Bioconductor_packages=="No")
packages_BIO <-subset(packages_info,Bioconductor_packages=="Yes")

packages_CRAN_name <-as.vector(packages_CRAN[,1])
packages_BIO_name <-as.vector(packages_BIO[,1])

## install CRAN packages
ipak(packages_CRAN_name)

## install bioconductor packages
source("http://bioconductor.org/biocLite.R")
biocLite(packages_BIO_name)