

data <- read.csv(file="denomination.csv",head=TRUE,sep=",")

y1 = data$timing[data$algorithm=="changegreedy"]
y2 = data$timing[data$algorithm=="changedp"]

df <- data.frame(y1, y2, x = data$n[data$algorithm=="changedp"])

plot(y1 ~ x, data=df, type="p", pch=1, cex=1, col="blue", main="Problem 8 Greedy Algorithm Plot", xlab="Number of Denominations", ylab="Running Time (ms)")


fit1 <- lm(y1 ~ df$x)
abline(fit1, col="blue")

dev.copy(png, 'den1.png')
dev.off()

plot(y2 ~ x, data=df, type="p", pch=2, cex=0.5, col="red", main="Problem 8 DP Algorithm Plot", xlab="Number of Denominations", ylab="Running Time (ms)")


fit2 <- lm(y2 ~ df$x)
abline(fit2, col="red")


dev.copy(png, 'den2.png')
dev.off()
