# you are not allowed to import any libraries for this question


def normalise_dict_scores_01(input_dict: dict) -> dict:
    '''
    Normalise the values of a dictionary scaled to a range of -100 to 100 and maintaining the 
    same shape distribution of the values
    
    Args:
        input_dict (dict): A dictionary with numeric values.
    
    Returns:
        dict: A new dictionary with the same keys, but values normalised to the range [-100, 100].
    '''
    # ----------------------- TODO: write your answer here -----------------------
    pass


if __name__ == "__main__":
    data = {
        'a': 10,
        'b': -10,
    }
    
    normalised_data = normalise_dict_scores_01(data)
    print(normalised_data)
