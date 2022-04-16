def tuple_to_dict(tuple_list, fields):
    data_array = []

    for item in tuple_list:
        data = {}
        for i in range(len(fields)):
            data[fields[i]] = item[i]
        data_array.append(data)

    return data_array
