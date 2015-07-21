# CS325 - Summer 2015
# Project 2
# Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
# Date: 7/21/2015

data <- read.csv(file="situation1.csv",head=TRUE,sep=",")

y1 = data$coins[data$algorithm=="changegreedy"]
y2 = data$coins[data$algorithm=="changedp"]

df <- data.frame(y1, y2, x = data$size[data$algorithm=="changedp"])

plot(y1 ~ x, data=df, type="p", pch=3, cex=1.2, col="blue", xlim=c(1995, 2205), main="Problem 4 Coin Change Plot", xlab="Amount of Change", ylab="Number of Coins")
lines(y2 ~ x, data=df, type="p", pch=2, cex=1.6, col="red")

legend(1995, 46, c("Change Greedy", "Change DP"), pch=c(3,2), col=c("blue","red"))

dev.copy(png, 'situation1.png')
dev.off()