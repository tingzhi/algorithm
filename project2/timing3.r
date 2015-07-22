data <- read.csv(file="timing6.csv",head=TRUE,sep=",")

y1 = data$timing[data$algorithm=="changegreedy"]
y2 = data$timing[data$algorithm=="changedp"]

df <- data.frame(y1, y2, x = data$size[data$algorithm=="changedp"])

plot(y1 ~ x, data=df, type="p", pch=1, cex=0.5, col="blue", xlim=c(2000, 2200), ylim=c(0, 55), main="Problem 6 Coin Change Timing Plot", xlab="Amount of Change", ylab="Running Time (ms)")

lines(y2 ~ x, data=df, type="p", pch=2, cex=0.8, col="red")

legend(1995, 55.8, c("Change Greedy", "Change DP"), pch=c(1,2), col=c("blue","red"))

fit1 <- lm(y1 ~ df$x)
abline(fit1, col="blue")

fit2 <- lm(y2 ~ df$x)
abline(fit2, col="red")

dev.copy(png, 'time3.png')
dev.off()

plot(y1 ~ x, data=df, type="p", pch=1, cex=1, col="blue", xlim=c(2000, 2200), main="Problem 6 Greedy Algorithm Timing Plot", xlab="Amount of Change", ylab="Running Time (ms)")
dev.copy(png, 'time3greedy.png')
dev.off()

plot(y2 ~ x, data=df, type="p", pch=2, cex=1, col="red", xlim=c(2000, 2200), main="Problem 6 DP Algorithm Timing Plot", xlab="Amount of Change", ylab="Running Time (ms)")
dev.copy(png, 'time3dp.png')
dev.off()