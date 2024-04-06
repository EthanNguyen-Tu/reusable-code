summarize_num <- function(name, dataset, var) {
  # Summarizes a numerical variable by providing the mean, median, mode, mode count, range, and standard deviation of the variable.
  #
  # @param name String name of the summary
  # @param dataset Tibble of the entire data set
  # @param var Variable whose summary is of interest (numerical)
  mode = Mode(var)
  var_range = range(var)
  writeLines(sprintf("%s Summary:\n   Mean = %f \r\n   Median = %f\n   Mode = %f\n   Mode Count = %d of %d\n   Range = %f to %f\n   Standard Deviation = %f", name, mean(var), median(var), mode, sum(var==mode), nrows(datset), var_range[1], var_range[2], sd(var)))
}

summarize_cat <- function(name, dataset, var) {
  # Summarizes a categorical variable by providing the mode, mode count, and difference between the mode count and total number of data set rows.
  #
  # @param name String name of the summary
  # @param dataset Tibble of the entire data set
  # @param var Variable whose summary is of interest (categorical)
  mode = Mode(var)
  count = sum(var==mode)
  rows = nrows(datset)
  writeLines(sprintf("%s Summary:\n   Mode = %s\n   Mode Count = %d of %d\n   Difference = %d", name, mode, count, rows, rows-count))
}