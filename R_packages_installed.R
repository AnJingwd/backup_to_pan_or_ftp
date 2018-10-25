
Args <- commandArgs()
output_file <- Args[6]

all_packages <-installed.packages()
num_installed <- dim(all_packages)[1]
packages_vector_installed <-vector()
for(i in 1:num_installed){
packages_vector_installed[i] <- all_packages[[i]]
}
#######################################################
source("https://bioconductor.org/biocLite.R")
AA <-"BiocInstaller" %in% rownames(installed.packages())
if (AA != "TRUE") {
	biocLite("BiocInstaller")
}

library(BiocInstaller)
Bio_packages <- available.packages(repos = biocinstallRepos()[1])
num_Bio <- dim(Bio_packages)[1]
Bio_packages_available <-vector()
for(i in 1:num_Bio){
Bio_packages_available[i] <- Bio_packages[[i]]
}
#######################################################
Bioconductor_packages <- ifelse(packages_vector_installed %in% Bio_packages_available,"Yes","No")
results<-data.frame(packages_vector_installed,Bioconductor_packages)
write.csv(results,output_file,row.names = FALSE)
