data <- read.csv(file="situation2_2.csv",head=TRUE,sep=",")

y1 = data$coins[data$algorithm=="changegreedy"]
y2 = data$coins[data$algorithm=="changedp"]

df <- data.frame(y1, y2, x = data$size[data$algorithm=="changedp"])

plot(y1 ~ x, data=df, type="o", pch=20, cex=1.1, lty=2, col="blue", xlim=c(1995, 2205), ylim=c(14,24), main=expression("Problem 5 Coin Change Plot for V"[2]), xlab="Amount of Change", ylab="Number of Coins")
lines(y2 ~ x, data=df, type="o", pch=20, cex=0.8, lty=2, col="red")

legend(1990, 24, c("Change Greedy", "Change DP"), pch=c(20,20), lty=c(2,2),col=c("blue","red"))

dev.copy(png, 'situation2_2.png')
dev.off()