'use-strict';
var sam_arr = [101, 789, 39, 449, 008, 850, 457];
var max = sam_arr[0];
for(var len in sam_arr){
  if(max < sam_arr[len]){
    max = sam_arr[len];
  }
}
var max_itr = 0;
while((max/10) > 0){
  max_itr++;
  max = parseInt(max/10);
}
var place = 0;
if(max_itr > 0){
  radix_sort(sam_arr,place,max_itr);
}

function radix_sort(sam_arr,place,max_itr){
  if(place < max_itr){
    var temp_arr = [];
    for(var i=0; i < 10; i++){
      for(var j in sam_arr){
        if(parseInt(sam_arr[j]/(Math.pow(10,place)))%10 == i){
          temp_arr.push(sam_arr[j]);
        }
      }
    }
    place++;
    radix_sort(temp_arr,place,max_itr)
  }else{
    console.log('Sorted array is:',JSON.stringify(sam_arr));
  }
}