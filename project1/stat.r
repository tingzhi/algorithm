# CS325 - Summer 2015
# Project 1
# Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
# Date: 7/12/2015

data <- read.csv(file="project1.csv",head=TRUE,sep=",")
groups <- split(data, list(data$algorithm, data$size))

# Enumeration algorithm plot
x = data$size[data$algorithm=="enumeration"]
y = data$timing[data$algorithm=="enumeration"]

plot(x, y, main="Enumeration", type="b", col="blue", xlab="input size (n)", ylab="running time (milliseconds)")
lines(x, fitted(lm(y~x+I(x^3))), col="red", type="l")
dev.copy(png, 'enumeration.png')
dev.off()

plot(x, y, log="xy", main="Log-Log Plot: Enumeration")
dev.copy(png, 'loglog_enumeration.png')
dev.off()

# Better Enumeration algorithm plot
x = data$size[data$algorithm=="better_enumeration"]
y = data$timing[data$algorithm=="better_enumeration"]

plot(x, y, main="Better Enumeration", type="b", col="blue", xlab="input size (n)", ylab="running time (milliseconds)")
lines(x, fitted(lm(y~x+I(x^2))), col="red", type="l")
dev.copy(png, 'better_enumeration.png')
dev.off()

plot(x, y, log="xy", main="Log-Log Plot: Better Enumeration")
dev.copy(png, 'loglog_better_enumeration.png')
dev.off()

# Divide and Conquer algorithm plot
x = data$size[data$algorithm=="divide_n_conquer"]
y = data$timing[data$algorithm=="divide_n_conquer"]

plot(x, y, main="Divide and Conquer", type="b", col="blue", xlab="input size (n)", ylab="running time (milliseconds)")
lines(x, fitted(lm(y~x+I(x**log(x)))), col="red", type="l")
dev.copy(png, 'divide_n_conquer.png')
dev.off()

plot(x, y, log="xy", main="Log-Log Plot: Divide and Conquer")
dev.copy(png, 'loglog_divide_n_conquer.png')
dev.off()

# Linear-time algorithm plot
x = data$size[data$algorithm=="linear_time"]
y = data$timing[data$algorithm=="linear_time"]

plot(x, y, main="Linear-time", type="b", col="blue", xlab="input size (n)", ylab="running time (milliseconds)")
lines(x, fitted(lm(y~x+I(x))), col="red", type="l")
dev.copy(png, 'linear_time.png')
dev.off()

plot(x, y, log="xy", main="Log-Log Plot: Linear-time")
dev.copy(png, 'loglog_linear_time.png')
dev.off()
