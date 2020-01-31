setwd("C:\\Users\\mczerwinski\\Documents\\BTIBudgetTool\\Repo\\BudgetPredict")

data <- read.csv('FY2019_070_Contracts_Full_20200110_1.csv', header = TRUE)

library(PerformanceAnalytics)

head(data)


lm_crime <- lm(federal_action_obligation
~.,data = data)


# row_ct <- dim(myData)[1]
# row_ct
# testrows <- sample(1:row_ct, size = round(row_ct/3), replace = FALSE, prob = rep(1/row_ct, row_ct))
# testrows
# 
# #define test data and train data
# train = myData[-testrows,]
# dim(train)


summary(data)

data['over_under'] = 
  
lm <- lm(over_under~., data = data)