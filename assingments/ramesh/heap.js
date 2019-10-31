// parent_node = lambda i : int((i-1)/2)
// left_node   = lambda i : i*2 +1
// right_node  = lambda i : i*2 +2

function heapsort(sample){
    var sample_length = sample.length;
    for(var i in sample){
        if(!i){
            continue;
        }else if(sample[i] > sample[parseInt((i-1)/2)]){
            // var a = 1, b = 2;
            // b = [a, a = b][0];  // Swaps
            var j = i;
            while((j != 0) && (sample[j] > sample[parseInt((j-1)/2)])){
                sample[parseInt((j-1)/2)] = [sample[j], sample[j] = sample[parseInt((j-1)/2)]][0];
                j = parseInt((j-1)/2);
            }
        }
    }
    while(sample_length > 1){
        // swap with last item
        sample[sample_length - 1] = [sample[0], sample[0] = sample[sample_length - 1]][0];

        sample_length--;
        var j = 0;
        while(1){
            if((sample_length > (j*2+1)) && (sample[j] < sample[j*2+1])){
                if((sample_length > (j*2+2)) && (sample[j] < sample[j*2+2])){
                    if(sample[j*2+1] < sample[j*2+2]){
                        sample[j*2+2] = [sample[j], sample[j] = sample[j*2+2]][0];
                        j = j*2+2;
                        continue;
                    }
                }
                sample[j*2+1] = [sample[j], sample[j] = sample[j*2+1]][0];
                j = j*2+1;
                continue;
            }else{
                break;
            }
        }
    }
}



var array_length; 
function heap_root(input, i) {
    var left = 2 * i + 1;
    var right = 2 * i + 2;
    var max = i;
    if (left < array_length && input[left] > input[max]){
        max = left;
    }
    if (right < array_length && input[right] > input[max]){
        max = right;
    }
    if (max != i) {
        input[max] = [input[i], input[i] = input[max]][0];
        heap_root(input, max);
    }
}

function heap_sort(input) {
    array_length = input.length;
    for (var i = Math.floor(array_length / 2); i >= 0; i -= 1){
        heap_root(input, i);
    }
    for (i = input.length - 1; i > 0; i--) {
        input[i] = [input[0], input[0] = input[i]][0];
        array_length--;  
        heap_root(input, 0);
    }
}