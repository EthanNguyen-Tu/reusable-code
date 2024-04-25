Mode <- function(var) {
  # Calculates the mode of the passed in variable.
  #
  # @param var Variable to calculate the mode of
  # @returns the mode of variable var
  unique_var <- unique(var)
  return(unique_var[which.max(tabulate(match(var, unique_var)))])
}


summarize_num <- function(name, dataset, var, print=TRUE) {
  # Summarizes the provided numerical variable, providing a print statement and
  # dataframe of the variable mean, median, mode, mode count, range, and standard
  # deviation.
  #
  # @param name String of the passed in variable's name  
  # @param dataset Tibble of the entire data set
  # @param var Variable of numerical type to be summarized
  # @param print Boolean of TRUE if the summary should be printed out, else FALSE
  # @returns DataFrame of the summary variables
  mode = Mode(var)
  mean = mean(var)
  median = median(var)
  rows = nrow(dataset)
  var_range = range(var)
  count = sum(var==mode)
  std = sd(var)
  if (print) {
    writeLines(sprintf("%s Summary:\n   Mean = %f \r\n   Median = %f\n   Mode = %f\n   Mode Count = %d of %d\n   Range = %f to %f\n   Standard Deviation = %f", name, mean, median, mode, count, rows, var_range[1], var_range[2], std))
  }
  return(data.frame(Name = c(name), Mean = c(mean), Median = c(median), Mode = c(mode), Mode_Count = c(count), Total_Rows = c(rows), Range_From = c(var_range[1]), Range_To = c(var_range[2]), Range = c(var_range[2] - var_range[1]), Standard_Deviation = c(std)))
}


summarize_cat <- function(name, dataset, var, print=TRUE) {
  # Summarizes the provided categorical variable, providing a print statement of
  # the variable mode, mode count, and the difference between the total number of
  # rows and the mode count.
  #
  # @param name String of the passed in variable's name
  # @param dataset Tibble of the entire data set
  # @param var Variable of categorical type to be summarized
  # @param print Boolean of TRUE if the summary should be printed out, else FALSE
  # @returns DataFrame of the summary variables
  mode = Mode(var)
  count = sum(var==mode)
  rows = nrow(dataset)
  difference = rows - count
  if (print) {
    writeLines(sprintf("%s Summary:\n   Mode = %s\n   Mode Count = %d of %d\n   Difference = %d", name, mode, count, rows, difference))
  }
  return(data.frame(Name = c(name), Mode = c(mode), Mode_Count = c(count), Difference = c(difference), Total_Rows = c(rows)))
}
