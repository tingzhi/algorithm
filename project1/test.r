# CS325 - Summer 2015
# Project 1
# Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
# Date: 7/12/2015

data <- read.csv(file="project1.csv",head=TRUE,sep=",")
print(data)
plot(data$time, type="o", col="blue")

#y=c(12,15,28,17,18)
#x=c(22,39,50,25,18)
#print(mean(y))
#print(mean(x))
#plot(x,y)
