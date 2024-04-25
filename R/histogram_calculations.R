calculate_histogramBinWidth <- function(var, num_bins, integer=TRUE) {
    # Calculates the bin width, rounding to the nearest integer unless specified 
    # otherwise.
    #
    # @param var Variable of numeric type to calculate the bin-width for
    # @param num_bins Integer of the number of bins the variable should be divided 
    #                 into
    # @param integer Boolean TRUE if the provided variable is an integer or FALSE if
    #                the provided variable is a float
    # @returns Integer or Float of the width of the Histogram bins dependiung on input parameter integer
    if (integer) {
    return(as.integer(round((max(var) - min(var)) / num_bins)))
    }
    return(as.numeric(((max(var) - min(var)) / num_bins)))
}


calculate_histogramNumBins <- function(data) {
    # Calculates the ideal number of histogram bins, where the ideal number of bins in a histogram
    # is defined as the square root of the number of datapoints rounded up to the nearest integer.
    #
    # @param data Dataframe of the data to calculate the number of histogram bins from
    # @returns Integer of the ideal number of histogram bins
    return(ceiling(sqrt(nrow(data))))
}