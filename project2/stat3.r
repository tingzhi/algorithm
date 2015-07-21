data <- read.csv(file="situation3.csv",head=TRUE,sep=",")

y1 = data$coins[data$algorithm=="changegreedy"]
y2 = data$coins[data$algorithm=="changedp"]

df <- data.frame(y1, y2, x = data$size[data$algorithm=="changedp"])

plot(y1 ~ x, data=df, type="p", pch=0, cex=1.2, col="blue", xlim=c(1995, 2205), ylim=c(66,75), main="Problem 6 Coin Change Plot", xlab="Amount of Change", ylab="Number of Coins")
lines(y2 ~ x, data=df, type="p", pch=2, cex=0.5, col="red")

legend(1990, 75, c("Change Greedy", "Change DP"), pch=c(2,20), col=c("blue","red"))

dev.copy(png, 'situation3.png')
dev.off()