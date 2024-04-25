library(knitr)
library(kableExtra)


dataset_topX <- function(dataset, X=30, font_size=7){
  # Visualizes the top X datapoints of the given dataset in the form of a table.
  #
  # @param dataset Dataframe of the dataset to be visualized as a table
  # @param X Integer of the number of datapoints to print out, defaults to 30
  # @param font_size Integer of the size of the table's font, defaults to 7
  kable(head(dataset, X)) %>%
  kable_styling(full_width = TRUE, bootstrap_options = "striped", font_size=font_size)
}