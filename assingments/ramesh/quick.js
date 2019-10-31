function quick_sort(sample) {
	if (sample.length <= 1)  
		return sample;
    var lesser = [];
    var greater = [];
    var final_array = [];
    var length = sample.length;
    var last = sample[length - 1];
    length = length - 1;
    for (var i = 0; i < length; i++) {
        if (sample[i] <= last) {
            lesser.push(sample[i]);
        } else {
            greater.push(sample[i]);
        }
    }
    return final_array.concat(quick_Sort(lesser), last, quick_Sort(greater));
}