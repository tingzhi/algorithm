# CS325 - Summer 2015
# Project 1
# Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
# Date: 7/12/2015

data <- read.csv(file="project1.csv",head=TRUE,sep=",")
groups <- split(data, list(data$algorithm, data$size))

# Enumeration algorithm plot
plot(data$size[data$algorithm=="enumeration"], data$timing[data$algorithm=="enumeration"], main="Enumeration", type="b", col="blue", xlab="input size (n)", ylab="running time (milliseconds)")
dev.copy(png, 'runtime_enumeration.png')
dev.off()

# Better Enumeration algorithm plot
plot(data$size[data$algorithm=="better_enumeration"], data$timing[data$algorithm=="better_enumeration"], main="Better Enumeration", type="b", col="red", xlab="input size (n)", ylab="running time (milliseconds)")
dev.copy(png, 'runtime_better_enumeration.png')
dev.off()

# Divide and Conquer algorithm plot
plot(data$size[data$algorithm=="divide_n_conquer"], data$timing[data$algorithm=="divide_n_conquer"], main="Divide and Conquer", type="b", col="green", xlab="input size (n)", ylab="running time (milliseconds)")
dev.copy(png, 'runtime_divide_n_conquer.png')
dev.off()

# Linear-time algorithm plot
plot(data$size[data$algorithm=="linear_time"], data$timing[data$algorithm=="linear_time"], main="Linear-time", type="b", col="orange", xlab="input size (n)", ylab="running time (milliseconds)")
dev.copy(png, 'runtime_linear_time.png')
dev.off()

# Note: The following commands adds lines to existing plot that is currently drawn to the screen. Not currently being used.

#lines(data$size[data$algorithm=="better_enumeration"], data$timing[data$algorithm=="better_enumeration"], col="red", type="l")

#lines(data$size[data$algorithm=="divide_n_conquer"], data$timing[data$algorithm=="divide_n_conquer"], col="green", type="l")

#lines(data$size[data$algorithm=="linear_time"], data$timing[data$algorithm=="linear_time"], col="orange", type="l")
