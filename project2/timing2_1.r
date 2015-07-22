data <- read.csv(file="timing5_1.csv",head=TRUE,sep=",")

y1 = data$timing[data$algorithm=="changegreedy"]
y2 = data$timing[data$algorithm=="changedp"]

df <- data.frame(y1, y2, x = data$size[data$algorithm=="changedp"])

plot(y1 ~ x, data=df, type="p", pch=1, cex=0.5, col="blue", xlim=c(2000, 2200), ylim=c(0, 29), main=expression("Problem 5 Coin Change Timing Plot For V"[1]), xlab="Amount of Change", ylab="Running Time (ms)")

lines(y2 ~ x, data=df, type="p", pch=2, cex=0.8, col="red")

legend(1995, 29.6, c("Change Greedy", "Change DP"), pch=c(1,2), col=c("blue","red"))

dev.copy(png, 'time2_1.png')
dev.off()

plot(y1 ~ x, data=df, type="p", pch=1, cex=1, col="blue", xlim=c(2000, 2200), main=expression("Problem 5 Greedy Algorithm Timing Plot For V"[1]), xlab="Amount of Change", ylab="Running Time (ms)")
dev.copy(png, 'time2_1greedy.png')
dev.off()

plot(y2 ~ x, data=df, type="p", pch=2, cex=1, col="red", xlim=c(2000, 2200), main=expression("Problem 5 DP Algorithm Timing Plot For V"[1]), xlab="Amount of Change", ylab="Running Time (ms)")
dev.copy(png, 'time2_1dp.png')
dev.off()