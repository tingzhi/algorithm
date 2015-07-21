# CS325 - Summer 2015
# Project 2
# Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
# Date: 7/21/2015

data <- read.csv(file="results.csv",head=TRUE,sep=",")
groups <- split(data, list(data$algorithm, data$size))

# situation 1 plot 
x = data$size[data$algorithm=="changegreedy"]
y = data$coins[data$algorithm=="changegreedy"]

plot(x, y, main="Situation 1", type="b", col="blue", xlab="Amount of Change", ylab="Number of Coins")
#lines(x, fitted(lm(y~x+I(x^3))), col="red", type="l")
dev.copy(png, 'situation1.png')
dev.off()


